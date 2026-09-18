#!/usr/bin/env python3
"""Prepare a Client release from component versions public at the cutoff."""
import argparse,json,re,urllib.request
from datetime import date,datetime,timezone
from pathlib import Path
COMPONENTS=(
 ("ragnavik-compat","Ragnavik_Compatibility","LostKode-Ragnavik_Compatibility","package/manifest.json"),
 ("ragnavik-ui","Ragnavik_UI","LostKode-Ragnavik_UI","package/manifest.json"),
 ("ragnavik-server-bridge","Ragnavik_Server_Bridge","LostKode-Ragnavik_Server_Bridge","package/manifest.json"),
 ("ragnavik-server-pack","Ragnavik_Server","LostKode-Ragnavik_Server","manifest.json"),)
ROW=re.compile(r"^\|\s*(\d+\.\d+\.\d+)\s*\|\s*(.*?)\s*\|\s*$")
def fail(message): raise SystemExit(message)
def public_version(package):
 url=f"https://valheim.hexium.gg/mods/LostKode/{package}"
 with urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Ragnavik release coordinator"}),timeout=30) as response: page=response.read().decode()
 for payload in re.findall(r'<script type="application/ld\+json">(.*?)</script>',page,re.S):
  metadata=json.loads(payload)
  if metadata.get("@type")=="SoftwareApplication" and metadata.get("softwareVersion"): return metadata["softwareVersion"]
 return None
def change_for(path,version):
 for line in path.read_text().splitlines():
  match=ROW.match(line)
  if match and match.group(1)==version:return re.sub(r"<br\s*/?>"," ",match.group(2)).strip()
 fail(f"{path} has no row for public version {version}")
def pin(manifest,key,version):
 prefix=key+"-"
 for index,value in enumerate(manifest["dependencies"]):
  if value.startswith(prefix):
   previous=value[len(prefix):]; manifest["dependencies"][index]=prefix+version; return previous,previous!=version
 fail(f"client manifest is missing {key}")
def update_client(path,version,changes):
 lines=path.read_text().splitlines(); combined=" ".join(changes)
 for index,line in enumerate(lines):
  match=ROW.match(line)
  if match and match.group(1)==version:
   if combined not in match.group(2):lines[index]=f"| {version}  | {match.group(2).strip()} {combined} |"
   path.write_text("\n".join(lines)+"\n");return
 separator=next(i for i,line in enumerate(lines) if line.startswith("|-"));lines.insert(separator+1,f"| {version}  | {combined} |");path.write_text("\n".join(lines)+"\n")
def update_site(root,version,published,changes):
 changelog=root/"src/data/changelog.ts";text=changelog.read_text();values=",\n        ".join(json.dumps(x) for x in changes)
 entry="    {\n      version: "+json.dumps(version)+",\n      publishedAt: "+json.dumps(published)+",\n      title: \"Coordinated client release\",\n      changes: [\n        "+values+",\n      ],\n    },\n"
 if f'version: "{version}"' not in text:text=text.replace("  entries: [\n","  entries: [\n"+entry,1)
 stamp=datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00","Z");text=re.sub(r'updatedAt: "[^"]+"',f'updatedAt: "{stamp}"',text,1);changelog.write_text(text)
 slug=f"ragnavik-client-{version.replace('.', '-')}";post=root/"src/app/blog"/slug/"page.mdx";post.parent.mkdir(parents=True,exist_ok=True);bullets="\n".join("- "+x for x in changes)
 post.write_text(f'''export const article = {{
  author: "Ragnavik Team",
  date: "{published}",
  title: "Ragnavik Client {version}",
  description: "The coordinated Ragnavik Client Pack release for {published}.",
}};

# Ragnavik Client {version}

{bullets}

Review the [current Known Issues page](/known-issues) before updating.
''')
 return f"https://ragnavik.vercel.app/blog/{slug}"
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--sources",type=Path,required=True);ap.add_argument("--website",type=Path,required=True);ap.add_argument("--output",type=Path,required=True);ap.add_argument("--date",default=date.today().isoformat());args=ap.parse_args()
 path=Path("manifest.json");manifest=json.loads(path.read_text());version=manifest["version_number"];changes=[];versions={}
 for directory,package,key,manifest_name in COMPONENTS:
  source=args.sources/directory;public=public_version(package);main=json.loads((source/manifest_name).read_text())["version_number"]
  if public is None:
   print(f"{package}: no public release at cutoff; ignoring {main}");continue
  if public!=main:print(f"{package}: main is {main}; using public cutoff {public}")
  previous,changed=pin(manifest,key,public);versions[package]=public
  if changed:changes.append(f"Updated {package.replace('_',' ')} from {previous} to {public}. {change_for(source/'CHANGELOG.md',public)}")
 if not changes:changes.append("Published the prepared Client Pack changes with the component versions public at the cutoff.")
 path.write_text(json.dumps(manifest,indent=2)+"\n");update_client(Path("CHANGELOG.md"),version,changes);blog=update_site(args.website,version,args.date,changes);args.output.write_text(json.dumps({"client_version":version,"blog_url":blog,"component_versions":versions,"changes":changes},indent=2)+"\n")
if __name__=="__main__":main()
