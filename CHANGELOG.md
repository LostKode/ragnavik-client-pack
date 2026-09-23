# Changelog

| Version  | Changes                                                                                              |
|----------|------------------------------------------------------------------------------------------------------|
| 1.1.52  | Require Ragnavik Shared 1.0.20 with Compatibility 1.0.12 so ItemDrawers preserves cooked food, magic reagents, upgrades, and other custom item data during automatic storage and pickup. |
| 1.1.51  | Require Ragnavik Shared 1.0.19. Remove the ZenRaids light perimeter hum, reduce WardIsLove audio, move the Explorer pin toggle to Alt+L, move Store All to Alt+S, and move Pause Auto Store to Alt+Shift+S. |
| 1.1.50  | Require Ragnavik Shared 1.0.18 with Compatibility 1.0.11 so Afterdeath spirits can use permitted doors, resurrect at their assigned bed, and restore recovered items to their original quick slots. |
| 1.1.49  | Require Ragnavik UI 1.2.14 with refreshed Production connection metadata. |
| 1.1.48  | Allow ores, metals, and other normally restricted items through TargetPortal portals. |
| 1.1.47  | Require Ragnavik Shared 1.0.16 with the dedicated Ragnavik Gameplay package icon. |
| 1.1.46  | Update WardIsLove to 4.0.4, Warfare to 1.9.4, Zen ModLib to 1.14.9, ZenRaids to 1.2.2, Resurrection to 1.0.15, and PlantEasily to 2.2.1. Require Gameplay 1.0.3 with stronger starter chest protection and Compatibility 1.0.9 with durable Take All coverage. |
| 1.1.45  | Require Ragnavik Shared 1.0.13 with Compatibility 1.0.8, the current performance profiler, seed bag configuration, and the available Startup Accelerator 1.0.3 release. |
| 1.1.44  | Require Ragnavik Shared 1.0.10 with Gameplay 1.0.2 to restore starter chest interaction and current Valheim API compatibility. |
| 1.1.43  | Require Ragnavik Shared 1.0.9 with Valheim Performance Profiler 0.1.0 for client and dedicated-server diagnostics. |
| 1.1.42  | Require Ragnavik Shared 1.0.8 with Jotunn 2.30.2 and EpicLoot 0.14.11. |
| 1.1.41  | Require Ragnavik Shared 1.0.7 with Gameplay 1.0.1, Jotunn 2.30.2, OdinBanners 1.1.14, OdinHorse 1.7.3, and KillMeForMyPower 2.5.0. Update Unshamed to 1.0.7. |
| 1.1.40  | Require Ragnavik Shared 1.0.6, adding Ragnavik Gameplay 1.0.0 and the personalized starter chest at the StartTemple. |
| 1.1.39  | Require Ragnavik Shared 1.0.5 with Ragnavik Compatibility 1.0.7 so Afterdeath wisps can cross dungeon transitions and use existing portals during corpse recovery. |
| 1.1.38  | Require Ragnavik Shared 1.0.4, which removes GhostBuild and HearthBelow after isolated testing confirmed client frame-rate and terrain-rendering regressions. |
| 1.1.37  | Require Ragnavik Shared 1.0.3, which removes DedicatedServer 1.0.3 to restore normal simulation ownership and reduce performance issues. |
| 1.1.36  | Require Ragnavik Shared 1.0.2 so Gale installs Ragnavik Compatibility 1.0.6 with the current MagicPlugin and EpicMMO compatibility fixes. |
| 1.1.35  | Depend on Ragnavik Shared for client-and-server gameplay mods, including a controlled DedicatedServer 1.0.3 simulation test. Keep client-only interface and convenience mods here, and stop installing server-only Network and Server Bridge code on players. |
| 1.1.34  | Move all loading tips into Ragnavik UI as their sole owner and require Ragnavik UI 1.2.13. Update Ragnavik Compatibility to 1.0.3, Odin's Kingdom to 1.6.1, and Zen ModLib to 1.14.8. Retain FineWoodPieces 1.6.6 until its newer release is available on Hexium. |
| 1.1.33  | Replace outdated loading tips with current player guidance for the installed mod set. Remove references to retired mods and document the current profession rules, hotkeys, progression systems, building tools, storage, travel, combat, companions, and food systems. |
| 1.1.32  | Allow each player to pursue two professions. Permit profession changes once every 24 hours and reset an abandoned profession's level. Resolve confirmed hotkey conflicts across Professions, Passive Powers, HearthBelow, HUDCompass, SeidrChest, PerfectPlacement, ComfortTweaks, LootParticlePlus, and Farming. |
| 1.1.31  | Update CookingAdditions to 1.3.3, FloraCollector to 1.1.4, MagicPlugin to 2.2.1, and OdinsFoodBarrels to 1.2.9. Retain FineWoodPieces 1.6.6 because it is already the latest Hexium release. Update Ragnavik UI to 1.2.10 so connection guidance no longer overlaps its action button. Configure Farming to retain profession progression while PlantEasily owns planting grids and bulk harvesting, and PlantEverything owns growth display and biome restrictions. |
| 1.1.30  | Correct BoardersBumperBlurbs, GhostBuild, HildirsQuest, and SmartSkills to their available Hexium 1.0.3 releases so Gale installs the complete required shared mod set. |
| 1.1.29  | Update Afterdeath to 1.0.10 and restore the packaged Epic Loot startup configuration so its welcome and core-config prompts remain disabled. |
| 1.1.28  | Align five shared dependencies with the server: BoardersBumperBlurbs 1.0.4, GhostBuild 1.0.4, HildirsQuest 1.0.4, SmartSkills 1.0.4, and StartupAccelerator 1.0.4. |
| 1.1.27  | Add OreMines 1.2.1 as a shared client and server dependency so the fresh Ragnavik world includes progression-gated mining dungeons across its biomes. |
| 1.1.26  | Add World Advancement Progression 1.0.0 for per-player progression, nearby participant credit, day-gated boss altars, private raids, and area-host-based spawn progression. Retain Afterdeath 1.0.9 because it is already current. |
| 1.1.25  | Update Smoothbrain Blacksmithing to 1.3.6, Ranching to 1.1.9, and MoreGatesExtended to 1.0.5. Declare the shared OdinMounts, The Fisher, and MoreGatesExtended packages directly now that the Client Pack no longer depends on the server-only Server Pack. |
| 1.1.24  | Remove the server-only Ragnavik Server dependency from the Client Pack so Server Bridge and other server-only package contents are not installed on players. |
| 1.1.23  | Require Ragnavik Server 1.1.4 with Server Bridge 1.0.2 notification routing and Ragnavik UI 1.2.9 with clearer connection failure handling. |
| 1.1.22  | Require Ragnavik UI 1.2.8 with player-facing store details and release history kept in its standalone changelog. |
| 1.1.21  | Require Ragnavik UI 1.2.7 to restore isolated character selection, preserve player names, and recover interrupted Ragnavik character registrations. |
| 1.1.20  | Update 16 dependencies: Epic Loot 0.14.10, BoardersBumperBlurbs 1.0.3, BottledNeck 0.3.3, HedgeWalls 1.0.16, OdinBear 1.4.9, OdinCampsite 1.6.5, OdinHorse 1.7.2, OdinsFoodBarrels 1.2.8, OdinsHorsePen 1.1.2, OdinsKingdom 1.6.0, OdinsTraps 1.1.23, OdinsUndercroft 1.3.5, PotionPlus 4.3.4, Ranching 1.1.8, WackyEpicMMOSystem 1.9.68, and Zen ModLib 1.14.7. |
| 1.1.19  | Remove FastLink and CustomMainMenu now that Ragnavik UI owns direct server entry, the main menu, and loading presentation. Remove their obsolete configuration, artwork, release secret rendering, and FastLink anti-cheat entry from the Client Pack. |
| 1.1.18  | Require Ragnavik Server 1.1.2, Ragnavik Compatibility 1.0.1, and Ragnavik UI 1.2.6. Keep AzuClock on the verified Hexium 1.1.1 release. |
| 1.1.17  | Update Epic Loot, FastLink, First Person Mode, Haulers Helper, Max Player Count, Ship Stats and OdinShip, and Jotunn for local compatibility testing. Remove Marketplace for now after its prerelease could not be represented safely in the pack manifest. Restore CustomMainMenu with its incompatible intro-skip feature disabled so players still see the vanilla intro. Keep Ragnavik UI for its compass and clock behavior while retiring its inventory positioning behavior. |
| 1.1.16  | Rebuild the complete Gale dependency set with Hexium as the primary source and Thunderstore fallback. Replace MagicRevamp with MagicPlugin 2.2.0 and the retired custom sleep components with Azumatt SleepSkip. Restore the approved client packages and preserve FastLink plus the existing loading artwork. |
| 1.1.15  | Mark Ragnavik as being in private testing and replace the public access invitation with a link to the current request page. |
| 1.1.14  | Simplify the Thunderstore Details page to explain what the pack is, how to install and use it, and how to join Ragnavik. |
| 1.1.13  | Require Ragnavik Server 1.0.13 with seven reviewed mod updates. Disable the Vapok startup splash and anonymous telemetry. |
| 1.1.12  | Require Ragnavik Server 1.0.12 with Odin's Kingdom 1.5.7.<br>Require Ragnavik UI 1.0.2 for aligned inventory rows and a corrected trash drop target. |
| 1.1.11  | Require Ragnavik Server 1.0.11 with OdinHorse 1.7.0 and its scoped sound patch.<br>Require Ragnavik UI 1.0.1 for the clock and inventory layout fix. |
| 1.1.10  | Require Ragnavik Server 1.0.10 and remove the mistaken Ragnavik Progress client requirement. Retain the tested ProperPortals dependency version. |
| 1.1.9   | Require Ragnavik Server 1.0.9 with the EpicMMO reload guard and compatible ShieldMeBruh 2.0.2 and XPortalNetworks 2.0.1. |
| 1.1.8   | Install Ragnavik UI as its own mod dependency instead of bundling its files in the client pack. |
| 1.1.7   | Place the clock display below the compass and the trash button below the gold row. |
| 1.1.6   | Add a visible SleepSkip warning countdown, and require the server pack with the one-sleeper vote and anti-cheat allowlist update. |
| 1.1.5   | Correct FastLink toggle values to hide the server address and port from both the menu and tooltip while retaining the working server shortcut. |
| 1.1.4   | Remove Groups 1.2.10 after confirming that its Valheim 1.0 interface creates a blocking placeholder overlay over the intro and main menu. |
| 1.1.3   | Suppress both Epic Loot's welcome panel and its separate core-config update prompt, preserving the normal Valheim intro and main menu. Hide FastLink addresses and ports from its panel and tooltip, and never display a saved password. |
| 1.1.2   | Restore FastLink as a client-only server menu. Add CatosAntiCheat 1.0.4 to the shared core with the complete client quality-of-life allowlist, exact version checks, fail-closed enforcement, and private Discord rejection reporting. |
| 1.1.1   | Require a fresh character for first enrollment. Previously played characters can no longer be imported into Ragnavik. The server remains authoritative after enrollment and permits multiple fresh characters per platform account for restarts and testing. |
| 1.1.0   | Split gameplay and synchronized configuration into Ragnavik Server. Added tested Groups support and a conservative Epic MMO progression profile. Reduced recycling to 50 percent, doubled portal costs, protected portals from removal, disabled ground and leviathan resets, and retained 30 day dungeon resets. Current Guilds and Professions releases failed Valheim 1.0.12 testing and were not shipped. |
| 1.0.11  | Selected Epic Loot's Balanced preset and disabled its startup welcome panel so it does not cover the intro video. |
| 1.0.10  | Rebuilt the pack with the compatible requested mods plus current BepInEx and Jotunn pins. Uses XPortalNetworks instead of conflicting XPortal and the current SleepSkip fork. Uses Smoothbrain Backpacks with the Valheim 1.0 compatibility patch required by MagicRevamp. Includes RunicCharacterVault and the original Intermission artwork. Runtime testing excluded AzuAntiCheat and PlanBuild for confirmed Valheim 1.0 failures. |
| 1.0.9   | Removed MultiUserChest and ItemHopper together. InventorySlots 1.4.15 remains enabled as the pack's inventory and shared-container implementation. |
| 1.0.8   | Removed Exploration and PlanBuild after Valheim 1.0 startup compatibility failures. Removed HookGenPatcher because it was only required by PlanBuild. Retained InventorySlots 1.4.15. |
| 1.0.7   | Replaced all previous Intermission artwork with eight original 21:9 Nordic loading screens. Important subjects remain inside a centered 16:9 safe area for standard and ultrawide displays. |
| 1.0.6   | Updated all 14 available dependencies. Updated Runic Character Vault to 1.0.2 and removed Passive Powers 1.1.5 because it references a PlayerProfile field removed in Valheim 1.0, preventing new character creation. Replaced the deprecated XPortal Patched package with the official XPortal 1.2.25 Valheim 1.0 release. Added Warm Torches 1.0.0 and KillMeForMyPower 2.4.0. |
| 1.0.5   | Added Valheim 1.0 replacements for Crafty Boxes, Backpacks, extended inventory, and server authoritative characters. Replaced Quick Stack with InventorySlots. Retained MultiUserChest because ItemHopper requires it. Crafty Carts remains disabled because no compatible Valheim 1.0 replacement is available. Removed client-unneeded server utilities MaxPlayerCount, SmoothSave, and Max Dungeon Rooms from the published pack. |
| 1.0.0   | Refreshed 83 retained dependencies to their current Thunderstore versions for Valheim 1.0. Removed eight deprecated packages: BetterWards, ItemDrawers, Marketplace And Server NPCs Revamped, Warfare, RRRCore, RRRNpcs, RRRMonsters, and RRRBetterRaids. Retained AzuAntiCheat as a required part of the pack. |
| 0.5.1   | Updated blacks7ar-MagicPlugin from 2.0.4 to 2.0.5, Updated ishid4-BetterArchery from 1.9.6 to 1.9.7, Updated Digitalroot-Max_Dungeon_Rooms from 2.0.32 to 2.0.34, Added VentureValheim-Venture_Floating_Items v0.2.2, Added Smoothbrain-Exploration v1.0.3, Removed castix-FloatingItems |
| 0.5.0   | Updated ishid4-BetterArchery from 1.9.5 to 1.9.6, Added Azumatt-AzuExtendedPlayerInventory v1.4.3, Removed RandyKnapp-EquipmentAndQuickSlots (previously v2.1.13) |
| v0.4.29 | Upgrade Marketplace_And_Server_NPCs_Revamped to v9.3.3, WackyEpicMMOSystem to v1.9.14, TargetPortal to v1.1.20, MagicPlugin to v2.0.4, PlantEverything to v1.18.1, SearsCatalog to v1.5.1, AzuAutoStore to v3.0.1, FirstPersonMode to v1.3.5, Venture_Location_Reset to v0.9.1. |
| v0.4.27 | Upgrade AAA Crafting to v1.4.5, AzuAutoStore to v3.0.0, PlantEasily to v1.8.1 CraftyBoxes to v1.4.3, MagicPlugin to v2.0.3, MarketPlace to v9.3.2, Backpack to v1.3.4, Blacksmithing to v2.3.0 and Warfare to v1.7.5.
| v0.4.25 | Upgrade AAA Crafting to v1.4.4. Add AzuAutoStore v2.1.12, Recycle N Reclaim v1.3.4, HildirsQuest v1.0.2, plumga clutter v0.1.7, and venture location reset v0.9.0. Fixed loadscreens to fit 16:9. Add new tooltip.  |
| v0.4.24 | Upgrade OdinShip to v0.4.5, AirAnimals to v0.2.0, SeaAnimals to v0.2.6, and OdinsFoodBarrels to v1.0.25. |
| v0.4.23  | Upgrade cooking to v1.1.16, jotunn to v1.20.1, wackyepicmmosystem to v1.9.13, and planbuild to v0.16.0. |
| v0.4.22  | Upgrade aaa_crafting to v1.4.3, craftyboxes to v1.4.0, planteverything to v1.18.0, airanimals to v1.9.0, and seaanimals to v0.2.5. |
| v0.4.21  | Upgrade warefare to v1.7.4, odinsfoodbarrels to v1.0.24, magicplugin to v1.9.7, servercharacters to v1.4.12, and dragooncapes to v1.3.3. |
| v0.4.20  | Correct mistake with version 0.4.19.                                                                 |
| v0.4.19  | Downgrade Warfare to v1.7.1. Issues with the latest version.                                          |
| v0.4.18  | Update Warfare to v1.7.3.                                                                             |
| v0.4.17  | Improve intermission screens.                                                                         |
| v0.4.16  | Update BetterWards to v1.9.2, and CraftyCartsRemake to v3.1.2. Add Intermission v1.5.0.               |
| v0.4.15  | Update OdinPlus-OdinsFoodBarrels to v1.0.21.                                                          |
| v0.4.14  | Add Mods: **Azumatt-SleepSkip v1.1.1**: Enhances night-time gameplay by allowing players to skip sleeping periods.<br>**Smoothbrain-Guilds v1.1.8**: Introduces a guild system with enhanced player interaction and community features.<br>**Searica-SafetyStatus v1.1.0**: Adds a safety status indicator for players, improving awareness and safety in hostile environments.<br>**Azumatt-AzuHoverStats v1.1.6**: Provides detailed stats when hovering over items, improving gameplay information accessibility.<br>**Azumatt-MaxPlayerCount v1.2.3**: Increases the maximum number of players allowed on the server, enhancing the multiplayer experience.<br>**Smoothbrain-DarwinAwards v1.0.6**: Adds humorous awards for unusual player deaths, increasing entertainment value.<br>**Azumatt-FastLink v1.4.2**: Facilitates quick and easy server connection setups through a streamlined interface. |
| v0.4.13  | Repeated update: Add ItemDrawers v1.0.8.                                                              |
| v0.4.12  | Update ComfortTweaks to v3.3.1, Marketplace_And_Server_NPCs_Revamped to v9.3.1, and AzuAntiCheat to v4.3.7 for improved gameplay balance and security enhancements. |
| v0.4.11  | Update ComfortTweaks to v3.3.0, and OdinShip to v0.4.4. Removed Clutter due to it being deprecated.    |
| v0.4.10  | Update PlantEverything to v1.17.3, PassivePowers to v1.1.2, MagicPlugin to v1.9.5, and AzuAntiCheat to v4.3.5: Enhanced gameplay mechanics and security features. |
| v0.4.9   | Update PlantEverything to v1.17.2, ComfortTweaks to v3.3.0. Added DragonCapes v1.3.2 and CustomBanners v1.0.7: New aesthetic options and gameplay improvements. |
| v0.4.8   | Update Readme to include link to Ragnavik website for better access to server information.            |
| v0.4.7   | Update EpicLoot to v0.10.1: Enhanced loot system for better player rewards.                           |
| v0.4.6   | Update OdinsFoodBarrels to v1.0.20, and Foraging to v1.0.8. Added ItemHopper v1.5.0: Improved food and resource gathering mechanics. |
| v0.4.5   | Update Warfare to v1.7.1: Enhanced combat mechanics for a more engaging player experience.            |
| v0.4.4   | Update Groups to v1.2.8 and Valharvest to v3.1.2: Improved group management and harvesting mechanics. |
| v0.4.3   | Updated EpicLoot to v0.10.0: Further enhancements to the loot system.                                 |
| v0.4.2   | Remove mods that are not working with the current version of Valheim to ensure stability and compatibility. |
| v0.4.0   | Update mods for Ashlands: Adjustments to ensure mod compatibility and enhancement in new game areas.  |
| v0.3.0   | Remove or replace mods that did not work together starting out. More testing needed to ensure compatibility. |
| v0.2.0   | Remove or replace outdated mods to maintain server performance and stability.                         |
| v0.1.0   | Initial Release: Establishing the foundational mod set for the Ragnavik server.                       |
