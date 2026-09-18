# FastLink history sanitization

The private FastLink address entered tracked history in commit
fe78dd2d4859e4b8a076896a3ca5acef8f32c650. The affected path is
config/Azumatt.FastLink_servers.yml. The all-ref audit found no other path, but
the value remains present in 18 reachable commit snapshots:

- 2a72b67c56107deeb4e2cbc18f5e63a7a2adbc0c
- 9b39271400c1a0627f72dd0913c7fcec69df9e41
- ba6491cc99d63e77699243feac5e1c84e6ed0f76
- 9a2bd7255d709b519e65d54721e5e0c0d084d7ed
- 251afbfc5ab88e6ee1e12363336a4558266cd96c
- 26ccd62337767a2f5c684f5c7cf943e2a4982081
- f36a3638429e30ddd84677b5178f18fdbe62246e
- edbfa3ab8ca472e3af248250c56c64cbef2b20d1
- fd82355e473f2d31f726ca1b9d85a54b9d08e78b
- bba9990ba799c87ec18dbfa87a62c082da41fdf4
- e9f1139c1de3afe5a5f2ff1a16cf98661d344856
- 79041ac54e849cdf1cd24c3d0883abfdc616e5c4
- 31eb7fe0bc0519f972c8b67b4abca2560e989731
- b542405d120fa56d005214cbc3ba8fad50db8dd8
- 1d3d14ed5d8a19bb1a63d01daaaaa2fc41e1c907
- 51799d1ffef9a3baa6c8809eedb0fc059f6896aa
- 802e1a0fdadf7fec1bd8d4c60beb0799afb78919
- fe78dd2d4859e4b8a076896a3ca5acef8f32c650

Do not rewrite or force-push while release work is active. Coordinate a
maintenance window, preserve backup refs outside the remote, and notify every
contributor that existing clones must be replaced afterward.

During that maintenance window, put the exposed value in a private replacement
file that is never committed, then run:

    git filter-repo --force --replace-text /private/path/fastlink-replacements.txt
    git for-each-ref --format='delete %(refname)' refs/original | git update-ref --stdin
    git reflog expire --expire=now --all
    git gc --prune=now
    git push --force --mirror origin

The replacement file format is:

    EXPOSED_VALUE==>__RAGNAVIK_SERVER_ADDRESS__

After the rewrite, clone the repository into a new directory and confirm that
an all-ref search finds no exposed address before resuming release work. Rotate
or change the address separately if operationally possible. History rewriting
does not invalidate a network address that has already been disclosed.
