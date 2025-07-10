import typing
from enum import Enum

from BaseClasses import MultiWorld, Region, Entrance, Location
from .Options import SRB2Options
from .Locations import SRB2Location, location_table, GFZ_table,THZ_table,DSZ_table,CEZ_table,ACZ_table,\
    RVZ_table,ERZ_table,BCZ_table


class SRB2Zones(int, Enum):
    GREENFLOWER = 1
    TECHNO_HILL = 2
    DEEP_SEA = 3
    CASTLE_EGGMAN = 4
    ARID_CANYON = 5
    RED_VOLCANO = 6
    EGG_ROCK = 7
    BLACK_CORE = 8
# TODO ADD the rest of the zones/ special stages


class SRB2Region(Region):
    subregions: typing.List[Region] = []


# sm64paintings is a dict of entrances, format LEVEL | AREA


def create_regions(world: MultiWorld, options: SRB2Options, player: int):
    regMM = Region("Menu", player, world, "Level Select")
    #create_default_locs(regMM, locSS_table)#TODO this might break something
    world.regions.append(regMM)
    regCredits = create_region("Credits", player, world)
    create_locs(regCredits,"Good Ending")

    regATZC = create_region("Azure Temple Club", player, world)
    create_locs(regATZC, "Azure Temple Club Emblem")
    if options.oneup_sanity:
        create_locs(regATZC,"Azure Temple Monitor - x:-4192 y:21344",
        "Azure Temple Monitor - x:-4192 y:21280",
        "Azure Temple Monitor - x:-4192 y:21408")

    if options.oneup_sanity:
        regDSFD = create_region("Deep Sea Fast Door", player, world)
        create_locs(regDSFD, "Deep Sea (Act 1) Monitor - x:3104 y:15520","Deep Sea (Act 1) Monitor - x:3296 y:15520")


    if options.match_maps:
        regMPJVZ = create_region("Jade Valley Zone", player, world)
        create_locs(regMPJVZ,"Jade Valley Ring Emblem")
        regMPNFZ = create_region("Noxious Factory Zone", player, world)
        create_locs(regMPNFZ, "Noxious Factory Ring Emblem")
        regMPTPZ = create_region("Tidal Palace Zone", player, world)
        create_locs(regMPTPZ, "Tidal Palace Ring Emblem")
        regMPTCZ = create_region("Thunder Citadel Zone", player, world)
        create_locs(regMPTCZ, "Thunder Citadel Ring Emblem")
        regMPDTZ = create_region("Desolate Twilight Zone", player, world)
        create_locs(regMPDTZ, "Desolate Twilight Ring Emblem")
        regMPFMZ = create_region("Frigid Mountain Zone", player, world)
        create_locs(regMPFMZ, "Frigid Mountain Ring Emblem")
        regMPOHZ = create_region("Orbital Hangar Zone", player, world)
        create_locs(regMPOHZ, "Orbital Hangar Ring Emblem")
        regMPSFZ = create_region("Sapphire Falls Zone", player, world)
        create_locs(regMPSFZ, "Sapphire Falls Ring Emblem")
        regMPDBZ = create_region("Diamond Blizzard Zone", player, world)
        create_locs(regMPDBZ, "Diamond Blizzard Ring Emblem")
        regMPCSZ = create_region("Celestial Sanctuary Zone", player, world)
        create_locs(regMPCSZ, "Celestial Sanctuary Ring Emblem")
        regMPFCZ = create_region("Frost Columns Zone", player, world)
        create_locs(regMPFCZ, "Frost Columns Ring Emblem")
        regMPMMZ = create_region("Meadow Match Zone", player, world)
        create_locs(regMPMMZ, "Meadow Match Ring Emblem")
        regMPGLZ = create_region("Granite Lake Zone", player, world)
        create_locs(regMPGLZ, "Granite Lake Ring Emblem")
        regMPSSZ = create_region("Summit Showdown Zone", player, world)
        create_locs(regMPSSZ, "Summit Showdown Ring Emblem")
        regMPSShZ = create_region("Silver Shiver Zone", player, world)
        create_locs(regMPSShZ, "Silver Shiver Ring Emblem")
        regMPUBZ = create_region("Uncharted Badlands Zone", player, world)
        create_locs(regMPUBZ, "Uncharted Badlands Ring Emblem")
        regMPPSZ = create_region("Pristine Shores Zone", player, world)
        create_locs(regMPPSZ, "Pristine Shores Ring Emblem")
        regMPCHZ = create_region("Crystalline Heights Zone", player, world)
        create_locs(regMPCHZ, "Crystalline Heights Ring Emblem")
        regMPSWZ = create_region("Starlit Warehouse Zone", player, world)
        create_locs(regMPSWZ, "Starlit Warehouse Ring Emblem")
        regMPMAZ = create_region("Midnight Abyss Zone", player, world)
        create_locs(regMPMAZ, "Midnight Abyss Ring Emblem")
        regMPATZ = create_region("Airborne Temple Zone", player, world)
        create_locs(regMPATZ, "Airborne Temple Ring Emblem")



    regGFZ = create_region("Greenflower Zone", player, world)
    create_locs(regGFZ, "Greenflower (Act 1) Star Emblem", "Greenflower (Act 1) Spade Emblem","Greenflower (Act 1) Heart Emblem", "Greenflower (Act 1) Diamond Emblem",
                        "Greenflower (Act 1) Club Emblem","Greenflower (Act 2) Star Emblem", "Greenflower (Act 2) Spade Emblem","Greenflower (Act 2) Heart Emblem", "Greenflower (Act 2) Diamond Emblem",
                        "Greenflower (Act 2) Club Emblem","Greenflower (Act 1) Clear","Greenflower (Act 2) Clear","Greenflower (Act 3) Clear","Greenflower (Act 1) Emerald Token - Breakable Wall Near Bridge",
                "Greenflower (Act 1) Emerald Token - Midair Top Path","Greenflower (Act 2) Emerald Token - Main Path Cave","Greenflower (Act 2) Emerald Token - Under Bridge Near End",
                "Greenflower (Act 2) Emerald Token - No Spin High on Ledge")
    if options.time_emblems:
        create_locs(regGFZ, "Greenflower (Act 1) Time Emblem","Greenflower (Act 2) Time Emblem","Greenflower (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regGFZ, "Greenflower (Act 1) Ring Emblem","Greenflower (Act 2) Ring Emblem")
    if options.score_emblems:
        create_locs(regGFZ, "Greenflower (Act 3) Score Emblem")
    if options.oneup_sanity:
        create_locs(regGFZ,"Greenflower (Act 1) Monitor - Upper Spin Path in Cave","Greenflower (Act 1) Monitor - Single Pillar Near End","Greenflower (Act 1) Monitor - Highest Ledge","Greenflower (Act 2) Monitor - Breakable Floor Near Springs 1",
        "Greenflower (Act 2) Monitor - Open Area Behind Checkered Pillar","Greenflower (Act 2) Monitor - Skylight in 2nd Cave","Greenflower (Act 2) Monitor - Fenced Flower Ledge","Greenflower (Act 2) Monitor - Near Star Emblem 1",
        "Greenflower (Act 2) Monitor - Waterfall Top Near Start","Greenflower (Act 2) Monitor - Pillar Next to End","Greenflower (Act 2) Monitor - High Ledge After Final Cave","Greenflower (Act 2) Monitor - Inside Fence Above Start")
    if options.superring_sanity:
        create_locs(regGFZ,"Greenflower (Act 1) Monitor - Lake Side Path on Ledge","Greenflower (Act 1) Monitor - Spin Path Entrance","Greenflower (Act 1) Monitor - Alcove Near Bridges 2",
        "Greenflower (Act 1) Monitor - First Pillar","Greenflower (Act 1) Monitor - Across High Bridge in Flowers","Greenflower (Act 1) Monitor - High Ledge After Cave","Greenflower (Act 1) Monitor - Alcove Near Bridges 1",
        "Greenflower (Act 1) Monitor - Lake Alcove Near End","Greenflower (Act 1) Monitor - Spring Pillar Near End 1","Greenflower (Act 1) Monitor - Behind Bars in Cave","Greenflower (Act 1) Monitor - Behind Bushes Upper Path",
        "Greenflower (Act 1) Monitor - Spring Pillar Near End 2","Greenflower (Act 2) Monitor - Main Path Springs","Greenflower (Act 2) Monitor - Very High Alcove 1","Greenflower (Act 2) Monitor - Very High Alcove 2",
        "Greenflower (Act 2) Monitor - Very High Alcove 3","Greenflower (Act 2) Monitor - Very High Alcove 4","Greenflower (Act 2) Monitor - Very High Alcove 5","Greenflower (Act 2) Monitor - Very High Alcove 6",
        "Greenflower (Act 2) Monitor - Very High Alcove 7","Greenflower (Act 2) Monitor - Very High Alcove 8","Greenflower (Act 2) Monitor - Spade Emblem Cave 1","Greenflower (Act 2) Monitor - Spade Emblem Cave 2",
        "Greenflower (Act 2) Monitor - Spade Emblem Cave 3","Greenflower (Act 2) Monitor - In Fences Near Picnic","Greenflower (Act 2) Monitor - Log on Final Path","Greenflower (Act 2) Monitor - Near Springs Before End",
        "Greenflower (Act 2) Monitor - Square Pillar Before Big Ramp","Greenflower (Act 2) Monitor - Behind Bush Near Start","Greenflower (Act 2) Monitor - Wall Under High Alcove","Greenflower (Act 2) Monitor - No Spin Inside Spikes",
        "Greenflower (Act 2) Monitor - Open Area on Ledge","Greenflower (Act 2) Monitor - High Path River","Greenflower (Act 2) Monitor - Spin Path Red Springs")


    regTHZ = create_region("Techno Hill Zone", player, world)
    create_locs(regTHZ, "Techno Hill (Act 1) Star Emblem", "Techno Hill (Act 1) Spade Emblem","Techno Hill (Act 1) Heart Emblem", "Techno Hill (Act 1) Diamond Emblem",
                        "Techno Hill (Act 1) Club Emblem","Techno Hill (Act 2) Star Emblem", "Techno Hill (Act 2) Spade Emblem","Techno Hill (Act 2) Heart Emblem", "Techno Hill (Act 2) Diamond Emblem",
                        "Techno Hill (Act 2) Club Emblem","Techno Hill (Act 1) Clear","Techno Hill (Act 2) Clear","Techno Hill (Act 3) Clear","Techno Hill (Act 1) Emerald Token - On Pipes",
                "Techno Hill (Act 1) Emerald Token - Alt Path Under Slime","Techno Hill (Act 2) Emerald Token - Deep in Slime","Techno Hill (Act 2) Emerald Token - Knuckles Path Backtrack")
    if options.time_emblems:
        create_locs(regTHZ, "Techno Hill (Act 1) Time Emblem","Techno Hill (Act 2) Time Emblem","Techno Hill (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regTHZ, "Techno Hill (Act 1) Ring Emblem","Techno Hill (Act 2) Ring Emblem")
    if options.score_emblems:
        create_locs(regTHZ, "Techno Hill (Act 3) Score Emblem")
    if options.oneup_sanity:
        create_locs(regTHZ,
        "Techno Hill (Act 1) Monitor - Spin Under Conveyor Belt Door","Techno Hill (Act 1) Monitor - Knuckles Path Highest Ledge","Techno Hill (Act 1) Monitor - In Slime Above Spade Emblem",
        "Techno Hill (Act 1) Monitor - Spring Shell Pipe Challenge","Techno Hill (Act 1) Monitor - Pipe Room High Corner","Techno Hill (Act 1) Monitor - Top of Elevator Shaft","Techno Hill (Act 1) Monitor - Deep in Slime Near 2nd Checkpoint",
        "Techno Hill (Act 1) Monitor - Outside Pipe Room High Ledge","Techno Hill (Act 1) Monitor - High Ledge in Hole Near Start","Techno Hill (Act 2) Monitor - Under Slime Before 2nd Checkpoint",
        "Techno Hill (Act 2) Monitor - High Ledge Outside 1","Techno Hill (Act 2) Monitor - Near Spade Emblem","Techno Hill (Act 2) Monitor - Large Jump Into Slime C",
        "Techno Hill (Act 2) Monitor - Near Detons on Pillar","Techno Hill (Act 2) Monitor - Behind Glass Piston Path","Techno Hill (Act 2) Monitor - Knuckles Path Under Spiked Hallway",
        "Techno Hill (Act 2) Monitor - Egg Corp Cavity Under Slime","Techno Hill (Act 2) Monitor - Pillar Before End","Techno Hill (Act 2) Monitor - Egg Corp Deep in Slime",
        "Techno Hill (Act 2) Monitor - Near Amy Emerald Token","Techno Hill (Act 2) Monitor - Tall Pillar Outside Glass")
    if options.superring_sanity:
        create_locs(regTHZ,"Techno Hill (Act 1) Monitor - Crate on Large Slime Lake",
        "Techno Hill (Act 1) Monitor - Upper Path in Alcove","Techno Hill (Act 1) Monitor - On Pipe Outside Pipe Room","Techno Hill (Act 1) Monitor - Alt Path on Ledge 1","Techno Hill (Act 1) Monitor - Low Ledge Before Pipe Room",
        "Techno Hill (Act 1) Monitor - Pipe Room on Ground","Techno Hill (Act 1) Monitor - Knuckles Path Behind Pipe","Techno Hill (Act 1) Monitor - Deep in Slime Towards Factory","Techno Hill (Act 1) Monitor - Knuckles Path on Ledge",
        "Techno Hill (Act 1) Monitor - Knuckles Path High Ledge","Techno Hill (Act 1) Monitor - First Factory Back Ledge","Techno Hill (Act 1) Monitor - End of Knuckles Path in Flowers","Techno Hill (Act 1) Monitor - Knuckles Path on Pipes",
        "Techno Hill (Act 1) Monitor - On Top of Piston Near End","Techno Hill (Act 1) Monitor - Before End on Crates","Techno Hill (Act 1) Monitor - Knuckles Path in Slime","Techno Hill (Act 1) Monitor - In Slime Near 2nd Checkpoint",
        "Techno Hill (Act 1) Monitor - Factory Deep in Slime","Techno Hill (Act 1) Monitor - Ledge Above Start","Techno Hill (Act 1) Monitor - Alt Path on Machine","Techno Hill (Act 1) Monitor - High Above Slime Lake 1",
        "Techno Hill (Act 1) Monitor - Breakable Wall Ledge","Techno Hill (Act 1) Monitor - High Above Slime Lake 2","Techno Hill (Act 1) Monitor - Yellow Springs Near Start","Techno Hill (Act 1) Monitor - Upper Path on Ledge",
        "Techno Hill (Act 1) Monitor - Upper Path Spring Corner","Techno Hill (Act 1) Monitor - First Factory in Slime","Techno Hill (Act 1) Monitor - Alt Path on Ledge 2","Techno Hill (Act 1) Monitor - In First Slime River",
        "Techno Hill (Act 1) Monitor - Deep in 2nd Slime River","Techno Hill (Act 1) Monitor - Upper Path Around Corner","Techno Hill (Act 1) Monitor - Highest Ledge Above Slime Lake","Techno Hill (Act 1) Monitor - Alt Path on Pillar",
        "Techno Hill (Act 2) Monitor - Knuckles Path Exit 1","Techno Hill (Act 2) Monitor - Knuckles Path Exit 2","Techno Hill (Act 2) Monitor - Barricade Path Under 1st Conveyor",
        "Techno Hill (Act 2) Monitor - Barricade Path End Ledge 1","Techno Hill (Act 2) Monitor - Barricade Path Cavity 1st Checkpoint","Techno Hill (Act 2) Monitor - Knuckles Path Metal Pillar",
        "Techno Hill (Act 2) Monitor - High Ledge Outside 2","Techno Hill (Act 2) Monitor - High Ledge Outside 3","Techno Hill (Act 2) Monitor - Piston Room High Ledge 1",
        "Techno Hill (Act 2) Monitor - Piston Room High Ledge 2","Techno Hill (Act 2) Monitor - Large Jump Into Slime S", "Techno Hill (Act 2) Monitor - Barricade Path End Ledge 2",
        "Techno Hill (Act 2) Monitor - Large Jump Into Slime W","Techno Hill (Act 2) Monitor - Outside Heart Emblem Door","Techno Hill (Act 2) Monitor - Large Jump Into Slime N",
        "Techno Hill (Act 2) Monitor - Knuckles Path Before Diagonal Conveyors","Techno Hill (Act 2) Monitor - Behind Crates After 3rd Checkpoint","Techno Hill (Act 2) Monitor - Final Room Cavity in Pillar",
        "Techno Hill (Act 2) Monitor - Before Detons Behind Crates","Techno Hill (Act 2) Monitor - Near Heart Emblem 1","Techno Hill (Act 2) Monitor - Deton Room Behind Crate",
        "Techno Hill (Act 2) Monitor - Near Heart Emblem 2","Techno Hill (Act 2) Monitor - Behind Breakable Wall Near Start","Techno Hill (Act 2) Monitor - Egg Corp High Glass Platform",
        "Techno Hill (Act 2) Monitor - Egg Corp Upper Cavity Around Corner","Techno Hill (Act 2) Monitor - Egg Corp Under Slime W","Techno Hill (Act 2) Monitor - Egg Corp Under Slime E",
        "Techno Hill (Act 2) Monitor - Egg Corp Under Slime N","Techno Hill (Act 2) Monitor - Egg Corp Under Slime S","Techno Hill (Act 2) Monitor - After Turret Room Under Slime",
        "Techno Hill (Act 2) Monitor - Large Jump Into Slime E","Techno Hill (Act 2) Monitor - Near Club Emblem 1","Techno Hill (Act 2) Monitor - Near Club Emblem 2",
        "Techno Hill (Act 2) Monitor - Final Room Under Slime","Techno Hill (Act 2) Monitor - Before 2nd Checkpoint Breakable Wall L","Techno Hill (Act 2) Monitor - Before 2nd Checkpoint Breakable Wall R",
        "Techno Hill (Act 2) Monitor - Barricade Path on Crate","Techno Hill (Act 2) Monitor - Near Heart Emblem 3","Techno Hill (Act 2) Monitor - Final Room Behind Pipe",
        "Techno Hill (Act 2) Monitor - Near Diamond Emblem 1","Techno Hill (Act 2) Monitor - Near Diamond Emblem 2")

    regDSZ = create_region("Deep Sea Zone", player, world)
    create_locs(regDSZ, "Deep Sea (Act 1) Star Emblem", "Deep Sea (Act 1) Spade Emblem","Deep Sea (Act 1) Heart Emblem", "Deep Sea (Act 1) Diamond Emblem",
                        "Deep Sea (Act 1) Club Emblem","Deep Sea (Act 2) Star Emblem", "Deep Sea (Act 2) Spade Emblem","Deep Sea (Act 2) Heart Emblem", "Deep Sea (Act 2) Diamond Emblem",
                        "Deep Sea (Act 2) Club Emblem","Deep Sea (Act 1) Clear","Deep Sea (Act 2) Clear","Deep Sea (Act 3) Clear","Deep Sea (Act 1) Emerald Token - V on Right Path",
                "Deep Sea (Act 1) Emerald Token - Underwater Air Pocket on Right Path","Deep Sea (Act 1) Emerald Token - Yellow Doors",
    "Deep Sea (Act 1) Emerald Token - Large Underwater Curve", "Deep Sea (Act 1) Emerald Token - Waterslide Gargoyles", "Deep Sea (Act 2) Emerald Token - Near Heart Emblem",
    "Deep Sea (Act 2) Emerald Token - Red and Yellow Springs", "Deep Sea (Act 2) Emerald Token - Down Right From Goal", "Deep Sea (Act 2) Emerald Token - No Spin Spring Turnaround")
    if options.time_emblems:
        create_locs(regDSZ, "Deep Sea (Act 1) Time Emblem","Deep Sea (Act 2) Time Emblem","Deep Sea (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regDSZ, "Deep Sea (Act 1) Ring Emblem","Deep Sea (Act 2) Ring Emblem")
    if options.score_emblems:
        create_locs(regDSZ, "Deep Sea (Act 3) Score Emblem")
    if options.oneup_sanity:
        create_locs(regDSZ,"Deep Sea (Act 1) Monitor - x:3008 y:3392","Deep Sea (Act 1) Monitor - x:2944 y:5248","Deep Sea (Act 1) Monitor - x:11008 y:5696","Deep Sea (Act 1) Monitor - x:8640 y:3168","Deep Sea (Act 1) Monitor - x:9920 y:896",
    "Deep Sea (Act 1) Monitor - x:2048 y:720","Deep Sea (Act 1) Monitor - x:15616 y:896","Deep Sea (Act 1) Monitor - x:-3296 y:6784","Deep Sea (Act 1) Monitor - x:5088 y:11872","Deep Sea (Act 1) Monitor - x:10880 y:5568","Deep Sea (Act 1) Monitor - x:20000 y:15136","Deep Sea (Act 1) Monitor - x:320 y:4544",
    "Deep Sea (Act 1) Monitor - x:17584 y:-5544","Deep Sea (Act 1) Monitor - x:17792 y:12160","Deep Sea (Act 1) Monitor - x:64 y:12224","Deep Sea (Act 1) Monitor - x:13952 y:-2112","Deep Sea (Act 1) Monitor - x:10304 y:-736",
    "Deep Sea (Act 2) Monitor - x:15104 y:6128","Deep Sea (Act 2) Monitor - x:26848 y:11584","Deep Sea (Act 2) Monitor - x:15104 y:6032","Deep Sea (Act 2) Monitor - x:19264 y:-5888","Deep Sea (Act 2) Monitor - x:19072 y:-10816","Deep Sea (Act 2) Monitor - x:9696 y:-3328",
    "Deep Sea (Act 2) Monitor - x:8672 y:12960","Deep Sea (Act 2) Monitor - x:15808 y:2816","Deep Sea (Act 2) Monitor - x:25856 y:256","Deep Sea (Act 2) Monitor - x:19008 y:9344","Deep Sea (Act 2) Monitor - x:5776 y:10304","Deep Sea (Act 2) Monitor - x:9568 y:16992",
    "Deep Sea (Act 2) Monitor - x:1952 y:-2192","Deep Sea (Act 2) Monitor - x:1696 y:2592","Deep Sea (Act 2) Monitor - x:15104 y:6080")

    if options.superring_sanity:
        create_locs(regDSZ,"Deep Sea (Act 1) Monitor - x:15616 y:2944","Deep Sea (Act 1) Monitor - x:-3136 y:5696","Deep Sea (Act 1) Monitor - x:8704 y:3168",
        "Deep Sea (Act 1) Monitor - x:3904 y:-2048","Deep Sea (Act 1) Monitor - x:3648 y:-2048","Deep Sea (Act 1) Monitor - x:8576 y:3168","Deep Sea (Act 1) Monitor - x:3136 y:5216",
        "Deep Sea (Act 1) Monitor - x:12224 y:12352","Deep Sea (Act 1) Monitor - x:1536 y:3680","Deep Sea (Act 1) Monitor - x:-1952 y:7456","Deep Sea (Act 1) Monitor - x:-2016 y:7456",
        "Deep Sea (Act 1) Monitor - x:3136 y:1152","Deep Sea (Act 1) Monitor - x:2144 y:14176","Deep Sea (Act 1) Monitor - x:2144 y:13728","Deep Sea (Act 1) Monitor - x:5152 y:-2208",
        "Deep Sea (Act 1) Monitor - x:-96 y:6400","Deep Sea (Act 1) Monitor - x:15520 y:1184", "Deep Sea (Act 1) Monitor - x:19712 y:13184", "Deep Sea (Act 1) Monitor - x:15344 y:10656",
        "Deep Sea (Act 1) Monitor - x:2800 y:8368","Deep Sea (Act 1) Monitor - x:10848 y:8352","Deep Sea (Act 1) Monitor - x:10432 y:2176","Deep Sea (Act 1) Monitor - x:16192 y:16640",
        "Deep Sea (Act 1) Monitor - x:-1664 y:2496","Deep Sea (Act 1) Monitor - x:15072 y:8672","Deep Sea (Act 1) Monitor - x:12368 y:13248","Deep Sea (Act 1) Monitor - x:18256 y:16272",
        "Deep Sea (Act 1) Monitor - x:704 y:12224","Deep Sea (Act 1) Monitor - x:384 y:12224","Deep Sea (Act 1) Monitor - x:12800 y:3456","Deep Sea (Act 1) Monitor - x:15136 y:2656",
        "Deep Sea (Act 1) Monitor - x:16448 y:1696","Deep Sea (Act 1) Monitor - x:1728 y:4384","Deep Sea (Act 1) Monitor - x:160 y:14240","Deep Sea (Act 2) Monitor - x:128 y:-7264",
        "Deep Sea (Act 2) Monitor - x:17408 y:-16640","Deep Sea (Act 2) Monitor - x:16576 y:7552","Deep Sea (Act 2) Monitor - x:7840 y:96","Deep Sea (Act 2) Monitor - x:18016 y:-2592",
        "Deep Sea (Act 2) Monitor - x:15040 y:-1792","Deep Sea (Act 2) Monitor - x:16176 y:-10240","Deep Sea (Act 2) Monitor - x:10528 y:5232","Deep Sea (Act 2) Monitor - x:15424 y:6080",
        "Deep Sea (Act 2) Monitor - x:4128 y:6880","Deep Sea (Act 2) Monitor - x:19872 y:-8672","Deep Sea (Act 2) Monitor - x:20736 y:-10816","Deep Sea (Act 2) Monitor - x:10792 y:-7616",
        "Deep Sea (Act 2) Monitor - x:21632 y:-6144","Deep Sea (Act 2) Monitor - x:12608 y:-9248","Deep Sea (Act 2) Monitor - x:12608 y:-9184","Deep Sea (Act 2) Monitor - x:5408 y:10048",
        "Deep Sea (Act 2) Monitor - x:-16 y:-3968","Deep Sea (Act 2) Monitor - x:-16 y:-4224","Deep Sea (Act 2) Monitor - x:26144 y:12960","Deep Sea (Act 2) Monitor - x:19712 y:-672",
        "Deep Sea (Act 2) Monitor - x:5600 y:-3344","Deep Sea (Act 2) Monitor - x:8064 y:-4928","Deep Sea (Act 2) Monitor - x:8064 y:-6080","Deep Sea (Act 2) Monitor - x:15104 y:3776",
        "Deep Sea (Act 2) Monitor - x:15360 y:3776","Deep Sea (Act 2) Monitor - x:10784 y:-8512","Deep Sea (Act 2) Monitor - x:7680 y:3456","Deep Sea (Act 2) Monitor - x:7680 y:3328",
        "Deep Sea (Act 2) Monitor - x:9120 y:3680","Deep Sea (Act 2) Monitor - x:7776 y:3744","Deep Sea (Act 2) Monitor - x:14384 y:12131","Deep Sea (Act 2) Monitor - x:14512 y:13315",
        "Deep Sea (Act 2) Monitor - x:7776 y:3680","Deep Sea (Act 2) Monitor - x:8384 y:16752","Deep Sea (Act 2) Monitor - x:11904 y:14016","Deep Sea (Act 2) Monitor - x:9120 y:3744",
        "Deep Sea (Act 2) Monitor - x:23488 y:4736")


    regCEZ = create_region("Castle Eggman Zone", player, world)
    create_locs(regCEZ, "Castle Eggman (Act 1) Star Emblem", "Castle Eggman (Act 1) Spade Emblem", "Castle Eggman (Act 1) Heart Emblem", "Castle Eggman (Act 1) Diamond Emblem",
                "Castle Eggman (Act 1) Club Emblem", "Castle Eggman (Act 2) Star Emblem", "Castle Eggman (Act 2) Spade Emblem", "Castle Eggman (Act 2) Heart Emblem", "Castle Eggman (Act 2) Diamond Emblem",
                "Castle Eggman (Act 2) Club Emblem","Castle Eggman (Act 1) Clear","Castle Eggman (Act 2) Clear","Castle Eggman (Act 3) Clear","Castle Eggman (Act 1) Emerald Token - Behind Fence Near Start",
    "Castle Eggman (Act 1) Emerald Token - Spring Side Path","Castle Eggman (Act 1) Emerald Token - Inside Castle","Castle Eggman (Act 2) Emerald Token - First Outside Area","Castle Eggman (Act 2) Emerald Token - Corner of Right Courtyard",
    "Castle Eggman (Act 2) Emerald Token - Window of Back Left Courtyard","Castle Eggman (Act 2) Emerald Token - Spring Near Club Emblem","Castle Eggman (Act 2) Emerald Token - High Ledge Before Final Tower")
    if options.time_emblems:
        create_locs(regCEZ, "Castle Eggman (Act 1) Time Emblem", "Castle Eggman (Act 2) Time Emblem", "Castle Eggman (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regCEZ, "Castle Eggman (Act 1) Ring Emblem", "Castle Eggman (Act 2) Ring Emblem")
    if options.score_emblems:
        create_locs(regCEZ, "Castle Eggman (Act 3) Score Emblem")
    if options.oneup_sanity:
        create_locs(regCEZ,"Castle Eggman (Act 1) Monitor - x:-8096 y:-8608","Castle Eggman (Act 1) Monitor - x:-136 y:-9856","Castle Eggman (Act 1) Monitor - x:1120 y:-6464","Castle Eggman (Act 1) Monitor - x:10336 y:6080","Castle Eggman (Act 1) Monitor - x:-4032 y:-11136",
        "Castle Eggman (Act 1) Monitor - x:5120 y:192","Castle Eggman (Act 1) Monitor - x:-1872 y:-6160","Castle Eggman (Act 1) Monitor - x:2944 y:6816","Castle Eggman (Act 1) Monitor - x:7584 y:-2592","Castle Eggman (Act 1) Monitor - x:3328 y:4288","Castle Eggman (Act 2) Monitor - x:0 y:-21760",
        "Castle Eggman (Act 2) Monitor - x:-3584 y:-14720","Castle Eggman (Act 2) Monitor - x:2112 y:-320","Castle Eggman (Act 2) Monitor - x:0 y:-6784","Castle Eggman (Act 2) Monitor - x:3072 y:-16128","Castle Eggman (Act 2) Monitor - x:-4608 y:1856","Castle Eggman (Act 2) Monitor - x:-6816 y:-16768",
        "Castle Eggman (Act 2) Monitor - x:-3072 y:-20864","Castle Eggman (Act 2) Monitor - x:8320 y:6656","Castle Eggman (Act 2) Monitor - x:8672 y:-14880","Castle Eggman (Act 2) Monitor - x:-13184 y:832","Castle Eggman (Act 2) Monitor - x:-4864 y:-13568","Castle Eggman (Act 2) Monitor - x:-6912 y:1920",
        "Castle Eggman (Act 2) Monitor - x:12416 y:768")

    if options.superring_sanity:
        create_locs(regCEZ,"Castle Eggman (Act 1) Monitor - x:4224 y:-1600","Castle Eggman (Act 1) Monitor - x:10336 y:6144","Castle Eggman (Act 1) Monitor - x:10336 y:6016",
        "Castle Eggman (Act 1) Monitor - x:2464 y:-17536","Castle Eggman (Act 1) Monitor - x:-3968 y:-11072","Castle Eggman (Act 1) Monitor - x:-4096 y:-11200","Castle Eggman (Act 1) Monitor - x:7392 y:1472",
        "Castle Eggman (Act 1) Monitor - x:5056 y:192","Castle Eggman (Act 1) Monitor - x:5184 y:192","Castle Eggman (Act 1) Monitor - x:1760 y:-5760","Castle Eggman (Act 1) Monitor - x:-2080 y:-15008",
        "Castle Eggman (Act 1) Monitor - x:6016 y:7936","Castle Eggman (Act 1) Monitor - x:7392 y:1536","Castle Eggman (Act 1) Monitor - x:-3104 y:-11616","Castle Eggman (Act 1) Monitor - x:6784 y:9024",
        "Castle Eggman (Act 1) Monitor - x:5504 y:9024","Castle Eggman (Act 1) Monitor - x:4704 y:32","Castle Eggman (Act 1) Monitor - x:5280 y:-6496","Castle Eggman (Act 1) Monitor - x:5472 y:-6496",
        "Castle Eggman (Act 1) Monitor - x:-6880 y:-12736","Castle Eggman (Act 1) Monitor - x:-6880 y:-12800","Castle Eggman (Act 1) Monitor - x:8512 y:-512","Castle Eggman (Act 1) Monitor - x:6048 y:-5920",
        "Castle Eggman (Act 1) Monitor - x:-3104 y:-11488","Castle Eggman (Act 1) Monitor - x:13424 y:4640","Castle Eggman (Act 1) Monitor - x:6304 y:-5856","Castle Eggman (Act 1) Monitor - x:3024 y:-5424",
        "Castle Eggman (Act 1) Monitor - x:-4736 y:-12096","Castle Eggman (Act 1) Monitor - x:-6720 y:-10304","Castle Eggman (Act 1) Monitor - x:-6752 y:-10272","Castle Eggman (Act 1) Monitor - x:1792 y:-2528",
        "Castle Eggman (Act 1) Monitor - x:1824 y:-2560","Castle Eggman (Act 1) Monitor - x:2960 y:2160","Castle Eggman (Act 1) Monitor - x:5280 y:4704","Castle Eggman (Act 1) Monitor - x:2464 y:-17664",
        "Castle Eggman (Act 2) Monitor - x:-6848 y:-20096","Castle Eggman (Act 2) Monitor - x:-7392 y:-20768","Castle Eggman (Act 2) Monitor - x:0 y:-21056","Castle Eggman (Act 2) Monitor - x:-8472 y:-18480",
        "Castle Eggman (Act 2) Monitor - x:-2256 y:-18912","Castle Eggman (Act 2) Monitor - x:-8604 y:-8704","Castle Eggman (Act 2) Monitor - x:0 y:-11296","Castle Eggman (Act 2) Monitor - x:6976 y:320",
        "Castle Eggman (Act 2) Monitor - x:6144 y:-11136","Castle Eggman (Act 2) Monitor - x:7392 y:1696","Castle Eggman (Act 2) Monitor - x:3456 y:992","Castle Eggman (Act 2) Monitor - x:-6352 y:5120",
        "Castle Eggman (Act 2) Monitor - x:-8472 y:-18384","Castle Eggman (Act 2) Monitor - x:-12288 y:-1664","Castle Eggman (Act 2) Monitor - x:-3072 y:-16224","Castle Eggman (Act 2) Monitor - x:4288 y:-17216",
        "Castle Eggman (Act 2) Monitor - x:1728 y:-14784","Castle Eggman (Act 2) Monitor - x:-5184 y:-19776","Castle Eggman (Act 2) Monitor - x:-5376 y:-15904","Castle Eggman (Act 2) Monitor - x:2112 y:-18432",
        "Castle Eggman (Act 2) Monitor - x:-7616 y:-10368","Castle Eggman (Act 2) Monitor - x:-6784 y:-14592","Castle Eggman (Act 2) Monitor - x:4608 y:-7808","Castle Eggman (Act 2) Monitor - x:-4224 y:-17024",
        "Castle Eggman (Act 2) Monitor - x:-9664 y:64","Castle Eggman (Act 2) Monitor - x:4064 y:-1120","Castle Eggman (Act 2) Monitor - x:-544 y:-1328","Castle Eggman (Act 2) Monitor - x:-6448 y:5120",
        "Castle Eggman (Act 2) Monitor - x:-1984 y:-9984","Castle Eggman (Act 2) Monitor - x:-832 y:-1280","Castle Eggman (Act 2) Monitor - x:-9472 y:-1888","Castle Eggman (Act 2) Monitor - x:7712 y:-8288",
        "Castle Eggman (Act 2) Monitor - x:-5632 y:-7200","Castle Eggman (Act 2) Monitor - x:-32 y:-2720","Castle Eggman (Act 2) Monitor - x:32 y:-2656","Castle Eggman (Act 2) Monitor - x:-544 y:-1232",
        "Castle Eggman (Act 2) Monitor - x:9760 y:1824","Castle Eggman (Act 2) Monitor - x:8800 y:736","Castle Eggman (Act 2) Monitor - x:8800 y:-736","Castle Eggman (Act 2) Monitor - x:5312 y:-1984",
        "Castle Eggman (Act 2) Monitor - x:-8064 y:3584","Castle Eggman (Act 2) Monitor - x:-8064 y:4608","Castle Eggman (Act 2) Monitor - x:7424 y:-12416","Castle Eggman (Act 2) Monitor - x:5600 y:-9184",
        "Castle Eggman (Act 2) Monitor - x:2112 y:-16736","Castle Eggman (Act 2) Monitor - x:5664 y:-9184","Castle Eggman (Act 2) Monitor - x:-14464 y:-1152","Castle Eggman (Act 2) Monitor - x:1984 y:-9984",
        "Castle Eggman (Act 2) Monitor - x:6656 y:-14336")

    regACZ = create_region("Arid Canyon Zone", player, world)
    create_locs(regACZ, "Arid Canyon (Act 1) Star Emblem", "Arid Canyon (Act 1) Spade Emblem", "Arid Canyon (Act 1) Heart Emblem", "Arid Canyon (Act 1) Diamond Emblem",
                "Arid Canyon (Act 1) Club Emblem", "Arid Canyon (Act 2) Star Emblem", "Arid Canyon (Act 2) Spade Emblem", "Arid Canyon (Act 2) Heart Emblem", "Arid Canyon (Act 2) Diamond Emblem",
                "Arid Canyon (Act 2) Club Emblem","Arid Canyon (Act 1) Clear","Arid Canyon (Act 2) Clear","Arid Canyon (Act 3) Clear","Arid Canyon (Act 1) Emerald Token - Speed Shoes Central Pillar",
    "Arid Canyon (Act 1) Emerald Token - Behind Pillar Before Exploding Ramp","Arid Canyon (Act 1) Emerald Token - Behind Wall and Spikes","Arid Canyon (Act 2) Emerald Token - Left No Spin Path Minecarts",
    "Arid Canyon (Act 2) Emerald Token - Large Arch Cave Right Ledge","Arid Canyon (Act 2) Emerald Token - Knuckles Dark Path Around Wall")
    if options.time_emblems:
        create_locs(regACZ, "Arid Canyon (Act 1) Time Emblem", "Arid Canyon (Act 2) Time Emblem", "Arid Canyon (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regACZ, "Arid Canyon (Act 1) Ring Emblem", "Arid Canyon (Act 2) Ring Emblem")
    if options.score_emblems:
        create_locs(regACZ, "Arid Canyon (Act 3) Score Emblem")
    if options.oneup_sanity:
        create_locs(regACZ,"Arid Canyon (Act 1) Monitor - x:-896 y:96","Arid Canyon (Act 1) Monitor - x:-2624 y:-15680","Arid Canyon (Act 1) Monitor - x:5312 y:-5472","Arid Canyon (Act 1) Monitor - x:1984 y:-704","Arid Canyon (Act 1) Monitor - x:-6592 y:-2896",
        "Arid Canyon (Act 1) Monitor - x:5184 y:-4416","Arid Canyon (Act 1) Monitor - x:2816 y:-992","Arid Canyon (Act 1) Monitor - x:2720 y:-15648","Arid Canyon (Act 1) Monitor - x:-5184 y:14912","Arid Canyon (Act 1) Monitor - x:-11200 y:992","Arid Canyon (Act 2) Monitor - x:-10144 y:-4640",
        "Arid Canyon (Act 2) Monitor - x:4928 y:-21312","Arid Canyon (Act 2) Monitor - x:-3488 y:-20704","Arid Canyon (Act 2) Monitor - x:7312 y:-6432","Arid Canyon (Act 2) Monitor - x:6720 y:-22816","Arid Canyon (Act 2) Monitor - x:3888 y:-16448","Arid Canyon (Act 2) Monitor - x:-2176 y:-11904",
        "Arid Canyon (Act 2) Monitor - x:160 y:-10784","Arid Canyon (Act 2) Monitor - x:2240 y:-15456","Arid Canyon (Act 2) Monitor - x:128 y:-15712","Arid Canyon (Act 2) Monitor - x:-7317 y:-12433","Arid Canyon (Act 2) Monitor - x:-14240 y:-6336","Arid Canyon (Act 2) Monitor - x:-7088 y:-13824",
        "Arid Canyon (Act 2) Monitor - x:2752 y:-9776","Arid Canyon (Act 2) Monitor - x:-3536 y:3360","Arid Canyon (Act 2) Monitor - x:-4992 y:-7744","Arid Canyon (Act 2) Monitor - x:-1408 y:-14976")

    if options.superring_sanity:
        create_locs(regACZ,"Arid Canyon (Act 1) Monitor - x:-2368 y:-15680","Arid Canyon (Act 1) Monitor - x:3568 y:-1824","Arid Canyon (Act 1) Monitor - x:3856 y:-9648",
        "Arid Canyon (Act 1) Monitor - x:3952 y:-9616","Arid Canyon (Act 1) Monitor - x:4895 y:-8222","Arid Canyon (Act 1) Monitor - x:-352 y:-2688","Arid Canyon (Act 1) Monitor - x:-6208 y:-2304",
        "Arid Canyon (Act 1) Monitor - x:2336 y:-14304","Arid Canyon (Act 1) Monitor - x:-1872 y:-12080","Arid Canyon (Act 1) Monitor - x:928 y:-10784","Arid Canyon (Act 1) Monitor - x:1632 y:1696",
        "Arid Canyon (Act 1) Monitor - x:-11680 y:672","Arid Canyon (Act 1) Monitor - x:3904 y:544","Arid Canyon (Act 1) Monitor - x:-7360 y:-2240","Arid Canyon (Act 1) Monitor - x:3568 y:-1696",
        "Arid Canyon (Act 1) Monitor - x:-7360 y:-2368","Arid Canyon (Act 1) Monitor - x:704 y:-12224","Arid Canyon (Act 1) Monitor - x:992 y:-10784","Arid Canyon (Act 1) Monitor - x:-10400 y:-4544",
        "Arid Canyon (Act 1) Monitor - x:864 y:-16064","Arid Canyon (Act 1) Monitor - x:6368 y:-17376","Arid Canyon (Act 1) Monitor - x:320 y:-8640","Arid Canyon (Act 1) Monitor - x:224 y:-8640",
        "Arid Canyon (Act 1) Monitor - x:416 y:-8640","Arid Canyon (Act 1) Monitor - x:2032 y:-13120","Arid Canyon (Act 1) Monitor - x:2816 y:-4800","Arid Canyon (Act 1) Monitor - x:4336 y:-12176",
        "Arid Canyon (Act 1) Monitor - x:-3669 y:1024","Arid Canyon (Act 1) Monitor - x:-7456 y:-1184","Arid Canyon (Act 2) Monitor - x:-3488 y:-23200","Arid Canyon (Act 2) Monitor - x:-2240 y:-23648",
        "Arid Canyon (Act 2) Monitor - x:4672 y:-10912","Arid Canyon (Act 2) Monitor - x:4416 y:-22144","Arid Canyon (Act 2) Monitor - x:-1120 y:-9280","Arid Canyon (Act 2) Monitor - x:3072 y:-9216",
        "Arid Canyon (Act 2) Monitor - x:5440 y:-9664","Arid Canyon (Act 2) Monitor - x:3888 y:-16096","Arid Canyon (Act 2) Monitor - x:3888 y:-16800","Arid Canyon (Act 2) Monitor - x:3232 y:-17440",
        "Arid Canyon (Act 2) Monitor - x:-768 y:-16512","Arid Canyon (Act 2) Monitor - x:-3840 y:-15968","Arid Canyon (Act 2) Monitor - x:-3904 y:-15968","Arid Canyon (Act 2) Monitor - x:-1776 y:-23296",
        "Arid Canyon (Act 2) Monitor - x:2216 y:-16960","Arid Canyon (Act 2) Monitor - x:2264 y:-16960","Arid Canyon (Act 2) Monitor - x:4576 y:-7904","Arid Canyon (Act 2) Monitor - x:-7648 y:-13824",
        "Arid Canyon (Act 2) Monitor - x:2176 y:-15456","Arid Canyon (Act 2) Monitor - x:-7088 y:-13760","Arid Canyon (Act 2) Monitor - x:-7088 y:-13888","Arid Canyon (Act 2) Monitor - x:2304 y:-15456",
        "Arid Canyon (Act 2) Monitor - x:6976 y:-22208","Arid Canyon (Act 2) Monitor - x:6976 y:-22144","Arid Canyon (Act 2) Monitor - x:4928 y:-15488","Arid Canyon (Act 2) Monitor - x:-4720 y:-17344",
        "Arid Canyon (Act 2) Monitor - x:-3360 y:-14208","Arid Canyon (Act 2) Monitor - x:7776 y:-6528","Arid Canyon (Act 2) Monitor - x:7776 y:-6592","Arid Canyon (Act 2) Monitor - x:896 y:-20992",
        "Arid Canyon (Act 2) Monitor - x:-3136 y:-17376","Arid Canyon (Act 2) Monitor - x:-14240 y:-5376","Arid Canyon (Act 2) Monitor - x:-14176 y:-5376","Arid Canyon (Act 2) Monitor - x:-15424 y:-5312",
        "Arid Canyon (Act 2) Monitor - x:-12960 y:-2400","Arid Canyon (Act 2) Monitor - x:-5008 y:-17344","Arid Canyon (Act 2) Monitor - x:-6624 y:-13888","Arid Canyon (Act 2) Monitor - x:-6816 y:-19616",
        "Arid Canyon (Act 2) Monitor - x:-5632 y:-10528","Arid Canyon (Act 2) Monitor - x:7360 y:-9280","Arid Canyon (Act 2) Monitor - x:-5144 y:-616")

    regRVZ = create_region("Red Volcano Zone", player, world)
    create_locs(regRVZ, "Red Volcano (Act 1) Star Emblem", "Red Volcano (Act 1) Spade Emblem", "Red Volcano (Act 1) Heart Emblem", "Red Volcano (Act 1) Diamond Emblem",
                "Red Volcano (Act 1) Club Emblem","Red Volcano (Act 1) Clear","Red Volcano (Act 1) Emerald Token - First Outside Area","Red Volcano (Act 1) Emerald Token - Hidden Ledge Near 4th Checkpoint",
    "Red Volcano (Act 1) Emerald Token - Rollout Rock Lavafall","Red Volcano (Act 1) Emerald Token - Behind Ending Rocket")
    if options.time_emblems:
        create_locs(regRVZ, "Red Volcano (Act 1) Time Emblem")
    if options.ring_emblems:
        create_locs(regRVZ, "Red Volcano (Act 1) Ring Emblem")
    if options.oneup_sanity:
        create_locs(regRVZ,"Red Volcano (Act 1) Monitor - Lava Waves Pillar","Red Volcano (Act 1) Monitor - Thin Ledge First Outside Area","Red Volcano (Act 1) Monitor - First Outside Cave",
        "Red Volcano (Act 1) Monitor - Whirlwind Path Cave Around Corner","Red Volcano (Act 1) Monitor - Right Path Rising Lava Room Ledge","Red Volcano (Act 1) Monitor - Flame Jets Room Ledge",
        "Red Volcano (Act 1) Monitor - Behind Pillar Near End","Red Volcano (Act 1) Monitor - Near Heart Emblem","Red Volcano (Act 1) Monitor - Thin Ledge Second Outside Area")
    if options.superring_sanity:
        create_locs(regRVZ,"Red Volcano (Act 1) Monitor - x:-4096 y:-8864","Red Volcano (Act 1) Monitor - x:23136 y:6304","Red Volcano (Act 1) Monitor - x:22304 y:8192",
        "Red Volcano (Act 1) Monitor - x:25792 y:8480","Red Volcano (Act 1) Monitor - x:3488 y:-7888","Red Volcano (Act 1) Monitor - x:7952 y:-4112","Red Volcano (Act 1) Monitor - x:3520 y:-7920",
        "Red Volcano (Act 1) Monitor - x:10784 y:-6912","Red Volcano (Act 1) Monitor - x:-768 y:1600","Red Volcano (Act 1) Monitor - x:15840 y:12692","Red Volcano (Act 1) Monitor - x:4128 y:17504",
        "Red Volcano (Act 1) Monitor - x:4064 y:17568","Red Volcano (Act 1) Monitor - x:15904 y:12704")

    regERZ = create_region("Egg Rock Zone", player, world)
    create_locs(regERZ, "Egg Rock (Act 1) Star Emblem", "Egg Rock (Act 1) Spade Emblem", "Egg Rock (Act 1) Heart Emblem", "Egg Rock (Act 1) Diamond Emblem",
                "Egg Rock (Act 1) Club Emblem", "Egg Rock (Act 2) Star Emblem", "Egg Rock (Act 2) Spade Emblem", "Egg Rock (Act 2) Heart Emblem", "Egg Rock (Act 2) Diamond Emblem",
                "Egg Rock (Act 2) Club Emblem","Egg Rock (Act 1) Clear","Egg Rock (Act 2) Clear","Egg Rock (Act 1) Emerald Token - Gravity Conveyor Belts",
    "Egg Rock (Act 1) Emerald Token - Moving Platforms","Egg Rock (Act 2) Emerald Token - Outside on Metal Beam","Egg Rock (Act 2) Emerald Token - Skip Gravity Pad",
    "Egg Rock (Act 2) Emerald Token - Disco Room")
    if options.time_emblems:
        create_locs(regERZ, "Egg Rock (Act 1) Time Emblem", "Egg Rock (Act 2) Time Emblem")
    if options.ring_emblems:
        create_locs(regERZ, "Egg Rock (Act 1) Ring Emblem", "Egg Rock (Act 2) Ring Emblem")
    if options.oneup_sanity:
        create_locs(regERZ,"Egg Rock (Act 1) Monitor - x:-64 y:-10848","Egg Rock (Act 1) Monitor - x:-5184 y:-11264","Egg Rock (Act 1) Monitor - x:6944 y:-10560","Egg Rock (Act 1) Monitor - x:6144 y:-2112","Egg Rock (Act 1) Monitor - x:-10976 y:-7296",
        "Egg Rock (Act 1) Monitor - x:-5984 y:-2208","Egg Rock (Act 1) Monitor - x:-6656 y:-2816","Egg Rock (Act 1) Monitor - x:-7488 y:-7872","Egg Rock (Act 2) Monitor - x:-4992 y:17408","Egg Rock (Act 2) Monitor - x:-5056 y:17408","Egg Rock (Act 2) Monitor - x:-5200 y:6304","Egg Rock (Act 2) Monitor - x:-1600 y:8800",
        "Egg Rock (Act 2) Monitor - x:-9216 y:12384","Egg Rock (Act 2) Monitor - x:5216 y:20736","Egg Rock (Act 2) Monitor - x:-11936 y:15264","Egg Rock (Act 2) Monitor - x:-6656 y:8096","Egg Rock (Act 2) Monitor - Top of Turret Room","Egg Rock (Act 2) Monitor - x:2304 y:24960",
        "Egg Rock (Act 2) Monitor - x:-12032 y:7040","Egg Rock (Act 2) Monitor - x:-12864 y:7040","Egg Rock (Act 2) Monitor - x:10112 y:10432","Egg Rock (Act 2) Monitor - x:256 y:7616")

    if options.superring_sanity:
        create_locs(regERZ,"Egg Rock (Act 1) Monitor - x:-11040 y:-7296","Egg Rock (Act 1) Monitor - x:-10912 y:-7296","Egg Rock (Act 1) Monitor - x:-7504 y:-7872",
        "Egg Rock (Act 1) Monitor - x:-5760 y:-2208","Egg Rock (Act 1) Monitor - x:-1056 y:3136","Egg Rock (Act 1) Monitor - x:3336 y:-9024","Egg Rock (Act 1) Monitor - x:384 y:-9952",
        "Egg Rock (Act 1) Monitor - x:384 y:-10912","Egg Rock (Act 1) Monitor - x:-3488 y:2464","Egg Rock (Act 1) Monitor - x:-7360 y:-7872","Egg Rock (Act 1) Monitor - x:-9888 y:-11392",
        "Egg Rock (Act 1) Monitor - x:-5376 y:-9760","Egg Rock (Act 1) Monitor - x:-7296 y:-7872","Egg Rock (Act 1) Monitor - x:7008 y:-10560","Egg Rock (Act 1) Monitor - x:1600 y:-5120",
        "Egg Rock (Act 1) Monitor - x:-5408 y:-288","Egg Rock (Act 1) Monitor - x:-4800 y:2240","Egg Rock (Act 1) Monitor - x:-992 y:3136","Egg Rock (Act 2) Monitor - x:-9248 y:12448",
        "Egg Rock (Act 2) Monitor - x:-9248 y:12320","Egg Rock (Act 2) Monitor - x:-3520 y:15200","Egg Rock (Act 2) Monitor - x:-2016 y:15200","Egg Rock (Act 2) Monitor - x:-3456 y:15200",
        "Egg Rock (Act 2) Monitor - x:-4800 y:17408","Egg Rock (Act 2) Monitor - x:-4864 y:17408","Egg Rock (Act 2) Monitor - x:-2336 y:14144","Egg Rock (Act 2) Monitor - x:-6592 y:8096",
        "Egg Rock (Act 2) Monitor - x:-6720 y:8096","Egg Rock (Act 2) Monitor - x:-13152 y:10784","Egg Rock (Act 2) Monitor - x:1536 y:16896","Egg Rock (Act 2) Monitor - x:9472 y:14976",
        "Egg Rock (Act 2) Monitor - x:64 y:12736","Egg Rock (Act 2) Monitor - x:1024 y:3392","Egg Rock (Act 2) Monitor - x:1024 y:3296","Egg Rock (Act 2) Monitor - x:-11936 y:12704",
        "Egg Rock (Act 2) Monitor - x:768 y:-1408","Egg Rock (Act 2) Monitor - x:864 y:7328","Egg Rock (Act 2) Monitor - x:64 y:12224","Egg Rock (Act 2) Monitor - x:64 y:12096",
        "Egg Rock (Act 2) Monitor - x:9472 y:15936","Egg Rock (Act 2) Monitor - x:3296 y:21600")

    regBCZ = create_region("Black Core Zone", player, world)
    create_locs(regBCZ, "Black Core (Act 1) Clear","Black Core (Act 2) Clear","Black Core (Act 3) Clear")
    if options.time_emblems:
        create_locs(regBCZ, "Black Core (Act 1) Time Emblem", "Black Core (Act 2) Time Emblem", "Black Core (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regBCZ, "Black Core (Act 1) Ring Emblem")
    if options.score_emblems:
        create_locs(regBCZ, "Black Core (Act 2) Score Emblem","Black Core (Act 3) Score Emblem")
    if options.oneup_sanity:
        create_locs(regBCZ,"Black Core (Act 1) Monitor - Half Pillar Above Spike Gate","Black Core (Act 1) Monitor - Behind Arrow Sign","Black Core (Act 2) Monitor - Behind Computers")


    regFHZ = create_region("Frozen Hillside Zone", player, world)
    create_locs(regFHZ, "Frozen Hillside Star Emblem", "Frozen Hillside Spade Emblem", "Frozen Hillside Heart Emblem", "Frozen Hillside Diamond Emblem",
                "Frozen Hillside Club Emblem","Frozen Hillside Clear")
    if options.time_emblems:
        create_locs(regFHZ, "Frozen Hillside Time Emblem")
    if options.ring_emblems:
        create_locs(regFHZ, "Frozen Hillside Ring Emblem")
    if options.oneup_sanity:
        create_locs(regFHZ,"Frozen Hillside Monitor - First Snow Field Behind Ice","Frozen Hillside Monitor - Final Path Ledge Behind Ice")

    if options.superring_sanity:
        create_locs(regFHZ,"Frozen Hillside Monitor - Ledge Near Start 1","Frozen Hillside Monitor - Ledge Near Start 2","Frozen Hillside Monitor - Lower Path Alcove",
"Frozen Hillside Monitor - Right Path Inside Ice","Frozen Hillside Monitor - Left Path Cave Ledge","Frozen Hillside Monitor - First Area Tall Pillar","Frozen Hillside Monitor - First Area Lake Ledge",
"Frozen Hillside Monitor - Left Path Flowing Snow Ledge","Frozen Hillside Monitor - Frozen Lake Middle Platform","Frozen Hillside Monitor - Right Path Flowing Snow Behind Pillar","Frozen Hillside Monitor - Right Path Flowing Snow Lower Ice",
"Frozen Hillside Monitor - Converging Paths Under Overhang")

    regPTZ = create_region("Pipe Towers Zone", player, world)
    create_locs(regPTZ, "Pipe Towers Star Emblem", "Pipe Towers Spade Emblem", "Pipe Towers Heart Emblem", "Pipe Towers Diamond Emblem",
                "Pipe Towers Club Emblem","Pipe Towers Clear")
    if options.time_emblems:
        create_locs(regPTZ, "Pipe Towers Time Emblem")
    if options.ring_emblems:
        create_locs(regPTZ, "Pipe Towers Ring Emblem")
    if options.oneup_sanity:
        create_locs(regPTZ,"Pipe Towers ? Block - Above Start","Pipe Towers ? Block - Purple Mushroom Skylight","Pipe Towers ? Block - Ceiling Hole Near Flowing Water",
                "Pipe Towers ? Block - Near Diamond Emblem","Pipe Towers ? Block - Flowing Water Alt Path on Ledge","Pipe Towers ? Block - Underground Thwomp Room")
    regFFZ = create_region("Forest Fortress Zone", player, world)
    create_locs(regFFZ, "Forest Fortress Star Emblem", "Forest Fortress Spade Emblem", "Forest Fortress Heart Emblem", "Forest Fortress Diamond Emblem",
                "Forest Fortress Club Emblem","Forest Fortress Clear")
    if options.time_emblems:
        create_locs(regFFZ, "Forest Fortress Time Emblem")
    if options.ring_emblems:
        create_locs(regFFZ, "Forest Fortress Ring Emblem")
    if options.oneup_sanity:
        create_locs(regFFZ,"Forest Fortress Monitor - x:-1280 y:-7680","Forest Fortress Monitor - x:1024 y:-6528","Forest Fortress Monitor - x:9088 y:12800","Forest Fortress Monitor - x:5824 y:8368","Forest Fortress Monitor - x:14752 y:10672")

    if options.superring_sanity:
        create_locs(regFFZ,"Forest Fortress Monitor - x:-4512 y:-13968","Forest Fortress Monitor - x:-6240 y:-9024","Forest Fortress Monitor - x:-1280 y:-7616",
        "Forest Fortress Monitor - x:-1280 y:-7744","Forest Fortress Monitor - x:-2816 y:-4992","Forest Fortress Monitor - x:3200 y:-1952","Forest Fortress Monitor - x:3776 y:-832",
        "Forest Fortress Monitor - x:9248 y:2720","Forest Fortress Monitor - x:12928 y:6656","Forest Fortress Monitor - x:9120 y:7392","Forest Fortress Monitor - x:9120 y:12864",
        "Forest Fortress Monitor - x:9056 y:12736","Forest Fortress Monitor - x:2864 y:-6864","Forest Fortress Monitor - x:4456 y:-3944","Forest Fortress Monitor - x:6816 y:6656",
        "Forest Fortress Monitor - x:6776 y:6576","Forest Fortress Monitor - x:8224 y:12064","Forest Fortress Monitor - x:2912 y:-6816","Forest Fortress Monitor - x:2224 y:11392",
        "Forest Fortress Monitor - x:8608 y:3808","Forest Fortress Monitor - x:10976 y:8352")


    regFDZ = create_region("Final Demo Zone", player, world)
    create_locs(regFDZ, "Final Demo Clear","Final Demo Emerald Token - Greenflower (Act 1) Breakable Wall Near Bridge",
    "Final Demo Emerald Token - Greenflower (Act 2) Underwater Cave",
    "Final Demo Emerald Token - Greenflower (Act 2) Under Bridge Near End",
    "Final Demo Emerald Token - Techno Hill (Act 1) On Pipes",
    "Final Demo Emerald Token - Techno Hill (Act 1) Alt Path Fans",
    "Final Demo Emerald Token - Techno Hill (Act 2) Breakable Wall",
    "Final Demo Emerald Token - Techno Hill (Act 2) Under Poison Near End",
    "Final Demo Emerald Token - Castle Eggman (Act 1) Small Lake Near Start",
    "Final Demo Emerald Token - Castle Eggman (Act 1) Tunnel Before Act Clear",
    "Final Demo Emerald Token - Castle Eggman (Act 2) Water Flow in Sewers")
    if options.oneup_sanity:
        create_locs(regFDZ,"Final Demo Monitor - Greenflower (Act 1) Ledge After Main Bridge","Final Demo Monitor - Greenflower (Act 2) Skylight in 2nd Cave","Final Demo Monitor - Greenflower (Act 2) Open Area Small Cave",
"Final Demo Monitor - Techno Hill (Act 1) Barrels Across Poison Lake","Final Demo Monitor - Techno Hill (Act 2) Ledge Near End","Final Demo Monitor - Techno Hill (Act 2) In Poison Near End","Final Demo Monitor - Castle Eggman (Act 1) On Castle Wall",
"Final Demo Monitor - Castle Eggman (Act 1) Red Spring Secret Cave 1","Final Demo Monitor - Castle Eggman (Act 1) Red Spring Secret Cave 2","Final Demo Monitor - Castle Eggman (Act 1) High Ledge Near Start","Final Demo Monitor - Castle Eggman (Act 2) Secret in Fountain 1",
"Final Demo Monitor - Castle Eggman (Act 2) Right Courtyard on Platform 1","Final Demo Monitor - Red Volcano (Act 1) Start","Final Demo Monitor - Red Volcano (Act 1) Across Broken Bridge 1","Final Demo Monitor - Red Volcano (Act 1) Cave Near Falling Platforms")

    if options.superring_sanity:
        create_locs(regFDZ,"Final Demo Monitor - x:-27570 y:-28152","Final Demo Monitor - x:-26848 y:-30720","Final Demo Monitor - x:-28896 y:-21056",
        "Final Demo Monitor - x:-23328 y:-21952","Final Demo Monitor - x:-26872 y:-30672","Final Demo Monitor - x:-26824 y:-30672","Final Demo Monitor - x:-14488 y:-23296",
        "Final Demo Monitor - x:-14488 y:-23256","Final Demo Monitor - x:-6400 y:-17312","Final Demo Monitor - x:-3200 y:-18496","Final Demo Monitor - x:-3136 y:-18496",
        "Final Demo Monitor - x:-3136 y:-18560","Final Demo Monitor - x:-3136 y:-18624","Final Demo Monitor - x:-3200 y:-18624","Final Demo Monitor - x:-3264 y:-18624",
        "Final Demo Monitor - x:-3264 y:-18560","Final Demo Monitor - x:-3264 y:-18496","Final Demo Monitor - x:-14528 y:-23296","Final Demo Monitor - x:-6344 y:-16184",
        "Final Demo Monitor - x:15936 y:-27840","Final Demo Monitor - x:16128 y:-26624","Final Demo Monitor - x:9280 y:-17280","Final Demo Monitor - x:6208 y:-18326",
        "Final Demo Monitor - x:23008 y:-23200","Final Demo Monitor - x:15936 y:-27800","Final Demo Monitor - x:9120 y:-160","Final Demo Monitor - x:9120 y:-288",
        "Final Demo Monitor - x:28832 y:-2464","Final Demo Monitor - x:25280 y:15232","Final Demo Monitor - x:19264 y:16448","Final Demo Monitor - x:19456 y:16448",
        "Final Demo Monitor - x:24320 y:7552","Final Demo Monitor - x:24896 y:6272","Final Demo Monitor - x:26368 y:6592","Final Demo Monitor - x:27136 y:7616",
        "Final Demo Monitor - x:22912 y:12480","Final Demo Monitor - x:26816 y:16640","Final Demo Monitor - x:18336 y:11040","Final Demo Monitor - x:18272 y:10976",
        "Final Demo Monitor - x:18272 y:11040","Final Demo Monitor - x:18336 y:10976","Final Demo Monitor - x:20512 y:24640","Final Demo Monitor - x:20256 y:25536",
        "Final Demo Monitor - x:20256 y:25472","Final Demo Monitor - x:20192 y:25472","Final Demo Monitor - x:25440 y:22912","Final Demo Monitor - x:25376 y:22912",
        "Final Demo Monitor - x:28512 y:20320","Final Demo Monitor - x:24672 y:18880","Final Demo Monitor - x:24672 y:18944","Final Demo Monitor - x:24672 y:18816",
        "Final Demo Monitor - x:25888 y:24384","Final Demo Monitor - x:27136 y:23968","Final Demo Monitor - x:27200 y:23904","Final Demo Monitor - x:27200 y:23968",
        "Final Demo Monitor - x:28192 y:25792","Final Demo Monitor - x:28192 y:26240","Final Demo Monitor - x:15792 y:17664","Final Demo Monitor - x:432 y:28416",
        "Final Demo Monitor - x:8016 y:26656")

    regHHZ = create_region("Haunted Heights Zone", player, world)
    create_locs(regHHZ, "Haunted Heights Star Emblem", "Haunted Heights Spade Emblem", "Haunted Heights Heart Emblem", "Haunted Heights Diamond Emblem",
                "Haunted Heights Club Emblem","Haunted Heights Clear")
    if options.time_emblems:
        create_locs(regHHZ, "Haunted Heights Time Emblem")
    if options.ring_emblems:
        create_locs(regHHZ, "Haunted Heights Ring Emblem")
    if options.oneup_sanity:
        create_locs(regHHZ,"Haunted Heights Monitor - x:3216 y:4240","Haunted Heights Monitor - x:13568 y:12576","Haunted Heights Monitor - x:1408 y:18112","Haunted Heights Monitor - x:-6209 y:15690","Haunted Heights Monitor - x:-4000 y:18112","Haunted Heights Monitor - x:4288 y:12240",
    "Haunted Heights Monitor - x:6080 y:11872","Haunted Heights Monitor - x:-12320 y:11200","Haunted Heights Monitor - x:-10976 y:5632","Haunted Heights Monitor - x:-7712 y:18400","Haunted Heights Monitor - x:10048 y:9696","Haunted Heights Monitor - x:7648 y:24160",
    "Haunted Heights Monitor - x:11840 y:17312","Haunted Heights Monitor - x:-3008 y:20720","Haunted Heights Monitor - x:1792 y:2656","Haunted Heights Monitor - x:8254 y:11910","Haunted Heights Monitor - x:8768 y:14464")

    if options.superring_sanity:
        create_locs(regHHZ,"Haunted Heights Monitor - x:1984 y:864","Haunted Heights Monitor - x:320 y:-160","Haunted Heights Monitor - x:9088 y:480",
        "Haunted Heights Monitor - x:3424 y:4608","Haunted Heights Monitor - x:-10304 y:21440","Haunted Heights Monitor - x:-10432 y:21440","Haunted Heights Monitor - x:2848 y:12704",
        "Haunted Heights Monitor - x:-2880 y:18208","Haunted Heights Monitor - x:5184 y:3360","Haunted Heights Monitor - x:12960 y:7616","Haunted Heights Monitor - x:9657 y:6182",
        "Haunted Heights Monitor - x:3968 y:7136","Haunted Heights Monitor - x:-1440 y:14112","Haunted Heights Monitor - x:8736 y:19456","Haunted Heights Monitor - x:1056 y:16192",
        "Haunted Heights Monitor - x:6240 y:21504","Haunted Heights Monitor - x:4976 y:23376","Haunted Heights Monitor - x:7360 y:17952","Haunted Heights Monitor - x:5376 y:20736",
        "Haunted Heights Monitor - x:3520 y:20224","Haunted Heights Monitor - x:9952 y:13120","Haunted Heights Monitor - x:-6208 y:15936","Haunted Heights Monitor - x:-6528 y:18592")

    regAGZ = create_region("Aerial Garden Zone", player, world)
    create_locs(regAGZ, "Aerial Garden Star Emblem", "Aerial Garden Spade Emblem", "Aerial Garden Heart Emblem", "Aerial Garden Diamond Emblem",
                "Aerial Garden Club Emblem","Aerial Garden Clear","Aerial Garden Emerald Token - First Room High Tower",
    "Aerial Garden Emerald Token - Underwater on Pillar",
    "Aerial Garden Emerald Token - Diamond Emblem 1",
    "Aerial Garden Emerald Token - Diamond Emblem 2",
    "Aerial Garden Emerald Token - Diamond Emblem 3",
    "Aerial Garden Emerald Token - Diamond Emblem 4")
    if options.time_emblems:
        create_locs(regAGZ, "Aerial Garden Time Emblem")
    if options.ring_emblems:
        create_locs(regAGZ, "Aerial Garden Ring Emblem")
    if options.oneup_sanity:
        create_locs(regAGZ,"Aerial Garden Monitor - x:-13920 y:5120","Aerial Garden Monitor - x:-7264 y:-13472","Aerial Garden Monitor - x:-8000 y:-5568","Aerial Garden Monitor - x:10080 y:-9312","Aerial Garden Monitor - x:5024 y:14112","Aerial Garden Monitor - x:-960 y:9792",
        "Aerial Garden Monitor - x:-4224 y:10816","Aerial Garden Monitor - x:-1280 y:-19936","Aerial Garden Monitor - x:-1280 y:-17088","Aerial Garden Monitor - x:-14528 y:-5632","Aerial Garden Monitor - x:-8832 y:12544","Aerial Garden Monitor - x:-8832 y:12416",
        "Aerial Garden Monitor - x:-8960 y:12416","Aerial Garden Monitor - x:-8960 y:12544","Aerial Garden Monitor - x:-13600 y:864","Aerial Garden Monitor - x:-8896 y:-8128","Aerial Garden Monitor - x:-9568 y:3552","Aerial Garden Monitor - x:-8224 y:3552","Aerial Garden Monitor - x:16256 y:-9440",
        "Aerial Garden Monitor - x:9888 y:-18336","Aerial Garden Monitor - x:7840 y:-14208","Aerial Garden Monitor - x:7136 y:-14208","Aerial Garden Monitor - x:19584 y:-9856","Aerial Garden Monitor - x:13824 y:-14784","Aerial Garden Monitor - x:5472 y:14112",
        "Aerial Garden Monitor - x:3040 y:-352","Aerial Garden Monitor - x:5248 y:20640","Aerial Garden Monitor - x:5248 y:12352","Aerial Garden Monitor - x:5120 y:9024","Aerial Garden Monitor - x:-1184 y:-10592","Aerial Garden Monitor - x:2912 y:21280",
        "Aerial Garden Monitor - x:3424 y:18592")

    if options.superring_sanity:
        create_locs(regAGZ,"Aerial Garden Monitor - x:-8960 y:-2816","Aerial Garden Monitor - x:-8832 y:-2816","Aerial Garden Monitor - x:-13920 y:5056",
        "Aerial Garden Monitor - x:-13920 y:5184","Aerial Garden Monitor - x:7840 y:-5280","Aerial Garden Monitor - x:-8896 y:12416","Aerial Garden Monitor - x:-8832 y:12480",
        "Aerial Garden Monitor - x:-8896 y:12544","Aerial Garden Monitor - x:-8960 y:12480","Aerial Garden Monitor - x:-9024 y:12416","Aerial Garden Monitor - x:-8960 y:12352",
        "Aerial Garden Monitor - x:-8832 y:12352","Aerial Garden Monitor - x:-8768 y:12416","Aerial Garden Monitor - x:-8768 y:12544","Aerial Garden Monitor - x:-8832 y:12608",
        "Aerial Garden Monitor - x:-960 y:9984","Aerial Garden Monitor - x:-14176 y:-9504","Aerial Garden Monitor - x:-15168 y:-8768","Aerial Garden Monitor - x:-8896 y:-15520",
        "Aerial Garden Monitor - x:-8960 y:12608","Aerial Garden Monitor - x:13792 y:-14816","Aerial Garden Monitor - x:13856 y:-14816","Aerial Garden Monitor - x:13856 y:-14752",
        "Aerial Garden Monitor - x:13792 y:-14752","Aerial Garden Monitor - x:2336 y:21664","Aerial Garden Monitor - x:-4288 y:13248","Aerial Garden Monitor - x:-14816 y:1888",
        "Aerial Garden Monitor - x:-10368 y:-8224","Aerial Garden Monitor - x:-10336 y:-8256","Aerial Garden Monitor - x:-7424 y:-8224","Aerial Garden Monitor - x:-7456 y:-8256",
        "Aerial Garden Monitor - x:-8960 y:-8128","Aerial Garden Monitor - x:-8832 y:-8128","Aerial Garden Monitor - x:-960 y:9920","Aerial Garden Monitor - x:13184 y:-9792",
        "Aerial Garden Monitor - x:8256 y:-16256","Aerial Garden Monitor - x:14752 y:-5984","Aerial Garden Monitor - x:6336 y:22528","Aerial Garden Monitor - x:7104 y:21696",
        "Aerial Garden Monitor - x:2432 y:15424","Aerial Garden Monitor - x:8064 y:15424","Aerial Garden Monitor - x:832 y:4736","Aerial Garden Monitor - x:9632 y:5344",
        "Aerial Garden Monitor - x:7104 y:21824","Aerial Garden Monitor - x:4864 y:15936","Aerial Garden Monitor - x:5632 y:15936","Aerial Garden Monitor - x:5184 y:12352",
        "Aerial Garden Monitor - x:5312 y:12352","Aerial Garden Monitor - x:-9024 y:12544","Aerial Garden Monitor - x:-2304 y:-20160")


    regATZ = create_region("Azure Temple Zone", player, world)
    create_locs(regATZ, "Azure Temple Star Emblem", "Azure Temple Spade Emblem", "Azure Temple Heart Emblem", "Azure Temple Diamond Emblem",
                "Azure Temple Clear")
    if options.time_emblems:
        create_locs(regATZ, "Azure Temple Time Emblem")
    if options.ring_emblems:
        create_locs(regATZ, "Azure Temple Ring Emblem")
    if options.oneup_sanity:
        create_locs(regATZ,"Azure Temple Monitor - x:1824 y:8608","Azure Temple Monitor - x:-32 y:6688","Azure Temple Monitor - x:1856 y:9952","Azure Temple Monitor - x:512 y:14016","Azure Temple Monitor - x:-2272 y:12864",
"Azure Temple Monitor - x:-3232 y:14112","Azure Temple Monitor - x:1440 y:14688","Azure Temple Monitor - x:-2528 y:7296","Azure Temple Monitor - x:-2976 y:17888",
"Azure Temple Monitor - x:-1216 y:22528","Azure Temple Monitor - x:4160 y:12384","Azure Temple Monitor - x:3648 y:25696","Azure Temple Monitor - x:-1056 y:4128","Azure Temple Monitor - x:-2752 y:19936","Azure Temple Monitor - x:3648 y:25888")

    if options.superring_sanity:
        create_locs(regATZ,"Azure Temple Monitor - x:-832 y:704","Azure Temple Monitor - x:1344 y:-288","Azure Temple Monitor - x:1248 y:2304",
        "Azure Temple Monitor - x:-2592 y:2688","Azure Temple Monitor - x:0 y:6048","Azure Temple Monitor - x:-4448 y:2240","Azure Temple Monitor - x:-4448 y:2208",
        "Azure Temple Monitor - x:-352 y:7520","Azure Temple Monitor - x:-928 y:8256","Azure Temple Monitor - x:-736 y:6112","Azure Temple Monitor - x:-4000 y:10080",
        "Azure Temple Monitor - x:-3936 y:10080","Azure Temple Monitor - x:-3328 y:10752","Azure Temple Monitor - x:2848 y:9312","Azure Temple Monitor - x:512 y:13952",
        "Azure Temple Monitor - x:2752 y:11008","Azure Temple Monitor - x:-1184 y:11104","Azure Temple Monitor - x:672 y:12544","Azure Temple Monitor - x:224 y:12576",
        "Azure Temple Monitor - x:512 y:14080","Azure Temple Monitor - x:-2272 y:10432","Azure Temple Monitor - x:-2944 y:13344","Azure Temple Monitor - x:-3232 y:14048",
        "Azure Temple Monitor - x:-3232 y:14176","Azure Temple Monitor - x:1248 y:14432","Azure Temple Monitor - x:-3968 y:16768","Azure Temple Monitor - x:384 y:9568",
        "Azure Temple Monitor - x:320 y:9568","Azure Temple Monitor - x:-3040 y:17888","Azure Temple Monitor - x:-2976 y:17952","Azure Temple Monitor - x:-2752 y:18432",
        "Azure Temple Monitor - x:4192 y:12320","Azure Temple Monitor - x:4096 y:12416","Azure Temple Monitor - x:4064 y:25248","Azure Temple Monitor - x:2208 y:22560",
        "Azure Temple Monitor - x:2208 y:22624","Azure Temple Monitor - x:3424 y:16528","Azure Temple Monitor - x:-2976 y:20320","Azure Temple Monitor - x:3600 y:25696",
        "Azure Temple Monitor - x:3696 y:25696","Azure Temple Monitor - x:-4768 y:9600","Azure Temple Monitor - x:-800 y:9312","Azure Temple Monitor - x:1952 y:11552",
        "Azure Temple Monitor - x:6112 y:22560")

    regSPFFZ = create_region("Floral Field Zone", player, world)
    create_locs(regSPFFZ, "Floral Field Sun Emblem", "Floral Field Moon Emblem","Floral Field Clear")
    regSPTPZ = create_region("Toxic Plateau Zone", player, world)
    create_locs(regSPTPZ, "Toxic Plateau Sun Emblem", "Toxic Plateau Moon Emblem","Toxic Plateau Clear")
    regSPFCZ = create_region("Flooded Cove Zone", player, world)
    create_locs(regSPFCZ, "Flooded Cove Sun Emblem", "Flooded Cove Moon Emblem","Flooded Cove Clear")
    regSPCFZ = create_region("Cavern Fortress Zone", player, world)
    create_locs(regSPCFZ, "Cavern Fortress Sun Emblem", "Cavern Fortress Moon Emblem","Cavern Fortress Clear")
    regSPDWZ = create_region("Dusty Wasteland Zone", player, world)
    create_locs(regSPDWZ, "Dusty Wasteland Sun Emblem", "Dusty Wasteland Moon Emblem","Dusty Wasteland Clear")
    regSPMCZ = create_region("Magma Caves Zone", player, world)
    create_locs(regSPMCZ, "Magma Caves Sun Emblem", "Magma Caves Moon Emblem","Magma Caves Clear")
    regSPESZ = create_region("Egg Satellite Zone", player, world)
    create_locs(regSPESZ, "Egg Satellite Sun Emblem", "Egg Satellite Moon Emblem","Egg Satellite Clear")
    regSPBHZ = create_region("Black Hole Zone", player, world)
    create_locs(regSPBHZ, "Black Hole Sun Emblem", "Black Hole Moon Emblem","Black Hole Clear")
    regSPCCZ = create_region("Christmas Chime Zone", player, world)
    create_locs(regSPCCZ, "Christmas Chime Sun Emblem", "Christmas Chime Moon Emblem","Christmas Chime Clear")
    regSPDHZ = create_region("Dream Hill Zone", player, world)
    create_locs(regSPDHZ, "Dream Hill Sun Emblem", "Dream Hill Moon Emblem","Dream Hill Clear")
    regSPAPZ = create_region("Alpine Paradise Zone", player, world)
    create_locs(regSPAPZ, "Alpine Paradise (Act 1) Sun Emblem", "Alpine Paradise (Act 1) Moon Emblem","Alpine Paradise (Act 1) Clear","Alpine Paradise (Act 2) Sun Emblem", "Alpine Paradise (Act 2) Moon Emblem","Alpine Paradise (Act 2) Clear")
    
    if options.ntime_emblems:
        create_locs(regSPFFZ, "Floral Field Time Emblem")
        create_locs(regSPTPZ, "Toxic Plateau Time Emblem")
        create_locs(regSPFCZ, "Flooded Cove Time Emblem")
        create_locs(regSPCFZ, "Cavern Fortress Time Emblem")
        create_locs(regSPDWZ, "Dusty Wasteland Time Emblem")
        create_locs(regSPMCZ, "Magma Caves Time Emblem")
        create_locs(regSPESZ, "Egg Satellite Time Emblem")
        create_locs(regSPBHZ, "Black Hole Time Emblem")
        create_locs(regSPCCZ, "Christmas Chime Time Emblem")
        create_locs(regSPDHZ, "Dream Hill Time Emblem")
        create_locs(regSPAPZ, "Alpine Paradise (Act 1) Time Emblem","Alpine Paradise (Act 2) Time Emblem")
        
    if options.rank_emblems:
        create_locs(regSPFFZ, "Floral Field A Rank Emblem")
        create_locs(regSPTPZ, "Toxic Plateau A Rank Emblem")
        create_locs(regSPFCZ, "Flooded Cove A Rank Emblem")
        create_locs(regSPCFZ, "Cavern Fortress A Rank Emblem")
        create_locs(regSPDWZ, "Dusty Wasteland A Rank Emblem")
        create_locs(regSPMCZ, "Magma Caves A Rank Emblem")
        create_locs(regSPESZ, "Egg Satellite A Rank Emblem")
        create_locs(regSPBHZ, "Black Hole A Rank Emblem")
        create_locs(regSPCCZ, "Christmas Chime A Rank Emblem")
        create_locs(regSPDHZ, "Dream Hill A Rank Emblem")
        create_locs(regSPAPZ, "Alpine Paradise (Act 1) A Rank Emblem","Alpine Paradise (Act 2) A Rank Emblem")

    if options.match_maps and options.oneup_sanity:
        create_locs(regMPSFZ,"Sapphire Falls Monitor - x:-80 y:3728")



    if options.match_maps and options.superring_sanity:
        create_locs(regMPJVZ, "Jade Valley Monitor - x:-336 y:768","Jade Valley Monitor - x:1440 y:-768","Jade Valley Monitor - x:1341 y:2218",
            "Jade Valley Monitor - x:1216 y:4960","Jade Valley Monitor - x:1921 y:564","Jade Valley Monitor - x:1890 y:497","Jade Valley Monitor - x:-4960 y:5312",
            "Jade Valley Monitor - x:-4928 y:5376","Jade Valley Monitor - x:1112 y:3915","Jade Valley Monitor - x:528 y:6672","Jade Valley Monitor - x:-6288 y:3296",
            "Jade Valley Monitor - x:-4199 y:4879","Jade Valley Monitor - x:-2288 y:-208","Jade Valley Monitor - x:-3416 y:1356","Jade Valley Monitor - x:4320 y:4576",
            "Jade Valley Monitor - x:4448 y:5984","Jade Valley Monitor - x:384 y:5248","Jade Valley Monitor - x:384 y:5312")
        create_locs(regMPNFZ, "Noxious Factory Monitor - x:1600 y:2624","Noxious Factory Monitor - x:-2048 y:3904","Noxious Factory Monitor - x:1472 y:2624",
            "Noxious Factory Monitor - x:-2752 y:256","Noxious Factory Monitor - x:-1728 y:-256","Noxious Factory Monitor - x:3424 y:1472","Noxious Factory Monitor - x:3456 y:1440",
            "Noxious Factory Monitor - x:-2464 y:2208","Noxious Factory Monitor - x:-2400 y:2208","Noxious Factory Monitor - x:-2400 y:2144","Noxious Factory Monitor - x:-2464 y:2144",
            "Noxious Factory Monitor - x:-1568 y:1312","Noxious Factory Monitor - x:-1376 y:1760","Noxious Factory Monitor - x:-1504 y:1760","Noxious Factory Monitor - x:1472 y:2752",
            "Noxious Factory Monitor - x:1600 y:2752","Noxious Factory Monitor - x:416 y:576","Noxious Factory Monitor - x:736 y:768","Noxious Factory Monitor - x:2112 y:-1920",
            "Noxious Factory Monitor - x:2496 y:3264","Noxious Factory Monitor - x:2496 y:3136","Noxious Factory Monitor - x:1440 y:-2336")
        create_locs(regMPTPZ, "Tidal Palace Monitor - x:-2624 y:-3072","Tidal Palace Monitor - x:-1920 y:-3616","Tidal Palace Monitor - x:0 y:-3232",
            "Tidal Palace Monitor - x:-4672 y:-1472","Tidal Palace Monitor - x:-4640 y:-1504","Tidal Palace Monitor - x:4128 y:-1824","Tidal Palace Monitor - x:3104 y:1088",
            "Tidal Palace Monitor - x:320 y:-1824","Tidal Palace Monitor - x:-3264 y:896","Tidal Palace Monitor - x:2784 y:1856","Tidal Palace Monitor - x:1472 y:-2304",
            "Tidal Palace Monitor - x:1184 y:-2976","Tidal Palace Monitor - x:-4384 y:-2560","Tidal Palace Monitor - x:-4256 y:-2560","Tidal Palace Monitor - x:-4096 y:384",
            "Tidal Palace Monitor - x:-2912 y:-2976","Tidal Palace Monitor - x:3136 y:1120","Tidal Palace Monitor - x:4064 y:-1824","Tidal Palace Monitor - x:4096 y:-1792",
            "Tidal Palace Monitor - x:-2656 y:-2656","Tidal Palace Monitor - x:1504 y:-96","Tidal Palace Monitor - x:1504 y:-224","Tidal Palace Monitor - x:-4160 y:1536",
            "Tidal Palace Monitor - x:-224 y:-672","Tidal Palace Monitor - x:224 y:-672")
        create_locs(regMPTCZ, "Thunder Citadel Monitor - x:-1234 y:-1124","Thunder Citadel Monitor - x:224 y:1760","Thunder Citadel Monitor - x:3520 y:4928",
            "Thunder Citadel Monitor - x:-4928 y:1856","Thunder Citadel Monitor - x:-448 y:1728","Thunder Citadel Monitor - x:3136 y:3200","Thunder Citadel Monitor - x:-1088 y:3232",
            "Thunder Citadel Monitor - x:-1056 y:3200","Thunder Citadel Monitor - x:-1088 y:3168","Thunder Citadel Monitor - x:-5056 y:1728","Thunder Citadel Monitor - x:-4603 y:7411",
            "Thunder Citadel Monitor - x:2341 y:6261","Thunder Citadel Monitor - x:2528 y:6016","Thunder Citadel Monitor - x:3392 y:1856","Thunder Citadel Monitor - x:320 y:2560",
            "Thunder Citadel Monitor - x:3328 y:1600","Thunder Citadel Monitor - x:1536 y:3392")
        create_locs(regMPDTZ, "Desolate Twilight Monitor - x:-512 y:-960","Desolate Twilight Monitor - x:480 y:-960","Desolate Twilight Monitor - x:2768 y:-3792",
            "Desolate Twilight Monitor - x:-768 y:1056","Desolate Twilight Monitor - x:864 y:1184","Desolate Twilight Monitor - x:-2624 y:3008","Desolate Twilight Monitor - x:-2580 y:3059",
            "Desolate Twilight Monitor - x:-128 y:-2688","Desolate Twilight Monitor - x:2913 y:212","Desolate Twilight Monitor - x:2904 y:275","Desolate Twilight Monitor - x:0 y:3584",
            "Desolate Twilight Monitor - x:2704 y:-3856")
        create_locs(regMPFMZ, "Frigid Mountain Monitor - x:3232 y:-3136","Frigid Mountain Monitor - x:1760 y:-1312","Frigid Mountain Monitor - x:6432 y:-384",
            "Frigid Mountain Monitor - x:1728 y:-1376","Frigid Mountain Monitor - x:6432 y:-320","Frigid Mountain Monitor - x:1072 y:558","Frigid Mountain Monitor - x:3744 y:-128",
            "Frigid Mountain Monitor - x:6432 y:-256","Frigid Mountain Monitor - x:5024 y:-2048","Frigid Mountain Monitor - x:5280 y:-4864","Frigid Mountain Monitor - x:5280 y:-4928",
            "Frigid Mountain Monitor - x:3808 y:-192")
        create_locs(regMPOHZ, "Orbital Hangar Monitor - x:4928 y:-4160","Orbital Hangar Monitor - x:4928 y:-5568","Orbital Hangar Monitor - x:3456 y:-2016",
            "Orbital Hangar Monitor - x:192 y:-3776","Orbital Hangar Monitor - x:192 y:-5440","Orbital Hangar Monitor - x:1984 y:-4768","Orbital Hangar Monitor - x:2016 y:-4064",
            "Orbital Hangar Monitor - x:2784 y:-7776","Orbital Hangar Monitor - x:3104 y:-7776","Orbital Hangar Monitor - x:4320 y:-6176","Orbital Hangar Monitor - x:1568 y:-6176",
            "Orbital Hangar Monitor - x:3104 y:-6176","Orbital Hangar Monitor - x:2784 y:-6176","Orbital Hangar Monitor - x:5472 y:-1984","Orbital Hangar Monitor - x:6464 y:-1216",
            "Orbital Hangar Monitor - x:32 y:-3296","Orbital Hangar Monitor - x:832 y:-7392","Orbital Hangar Monitor - x:2368 y:-2304","Orbital Hangar Monitor - x:2304 y:-2304",
            "Orbital Hangar Monitor - x:2240 y:-2304","Orbital Hangar Monitor - x:5952 y:-6592","Orbital Hangar Monitor - x:5344 y:-1984","Orbital Hangar Monitor - x:448 y:-4320",
            "Orbital Hangar Monitor - x:-320 y:-4896","Orbital Hangar Monitor - x:6592 y:-5760")
        create_locs(regMPSFZ, "Sapphire Falls Monitor - x:-912 y:-3872","Sapphire Falls Monitor - x:4288 y:-1248","Sapphire Falls Monitor - x:-4864 y:-832",
            "Sapphire Falls Monitor - x:-3616 y:3120","Sapphire Falls Monitor - x:-3616 y:3184","Sapphire Falls Monitor - x:-3616 y:3248","Sapphire Falls Monitor - x:1920 y:5632",
            "Sapphire Falls Monitor - x:3488 y:3936","Sapphire Falls Monitor - x:3424 y:3936","Sapphire Falls Monitor - x:-1568 y:5024","Sapphire Falls Monitor - x:3680 y:2848",
            "Sapphire Falls Monitor - x:4160 y:2592","Sapphire Falls Monitor - x:1408 y:4384","Sapphire Falls Monitor - x:-1472 y:5120","Sapphire Falls Monitor - x:-912 y:-3616",
            "Sapphire Falls Monitor - x:-16 y:-3136","Sapphire Falls Monitor - x:-544 y:-5344","Sapphire Falls Monitor - x:1184 y:-2176")
        create_locs(regMPDBZ, "Diamond Blizzard Monitor - x:64 y:-3520","Diamond Blizzard Monitor - x:2688 y:-3136","Diamond Blizzard Monitor - x:1856 y:-3968",
            "Diamond Blizzard Monitor - x:-2432 y:3168","Diamond Blizzard Monitor - x:-2752 y:1920","Diamond Blizzard Monitor - x:-1088 y:2432","Diamond Blizzard Monitor - x:1184 y:-1840",
            "Diamond Blizzard Monitor - x:0 y:-1024","Diamond Blizzard Monitor - x:-1408 y:-896","Diamond Blizzard Monitor - x:-1856 y:-5184","Diamond Blizzard Monitor - x:-1216 y:-3456",
            "Diamond Blizzard Monitor - x:1088 y:960","Diamond Blizzard Monitor - x:-64 y:2432","Diamond Blizzard Monitor - x:1056 y:2272","Diamond Blizzard Monitor - x:-1856 y:4224",
            "Diamond Blizzard Monitor - x:-1920 y:-2752","Diamond Blizzard Monitor - x:1296 y:400","Diamond Blizzard Monitor - x:1904 y:-1040","Diamond Blizzard Monitor - x:-576 y:-3744",
            "Diamond Blizzard Monitor - x:608 y:-4544","Diamond Blizzard Monitor - x:928 y:-4544","Diamond Blizzard Monitor - x:3392 y:2240","Diamond Blizzard Monitor - x:0 y:-3808",
            "Diamond Blizzard Monitor - x:-128 y:-3808","Diamond Blizzard Monitor - x:4160 y:-680","Diamond Blizzard Monitor - x:4160 y:-728")
        create_locs(regMPCSZ, "Celestial Sanctuary Monitor - x:1504 y:3168","Celestial Sanctuary Monitor - x:2880 y:6208","Celestial Sanctuary Monitor - x:-764 y:-1802",
            "Celestial Sanctuary Monitor - x:10048 y:4928","Celestial Sanctuary Monitor - x:6144 y:6720","Celestial Sanctuary Monitor - x:1792 y:64","Celestial Sanctuary Monitor - x:-2320 y:-1088",
            "Celestial Sanctuary Monitor - x:-1856 y:1472","Celestial Sanctuary Monitor - x:1792 y:-64","Celestial Sanctuary Monitor - x:4096 y:5088","Celestial Sanctuary Monitor - x:3648 y:2848",
            "Celestial Sanctuary Monitor - x:10112 y:4928","Celestial Sanctuary Monitor - x:4800 y:128","Celestial Sanctuary Monitor - x:7040 y:-3008","Celestial Sanctuary Monitor - x:4480 y:6592",
            "Celestial Sanctuary Monitor - x:4544 y:6592","Celestial Sanctuary Monitor - x:9088 y:320","Celestial Sanctuary Monitor - x:3084 y:2461","Celestial Sanctuary Monitor - x:-2368 y:-1136",
            "Celestial Sanctuary Monitor - x:192 y:5952","Celestial Sanctuary Monitor - x:256 y:5952","Celestial Sanctuary Monitor - x:4128 y:-1120")
        create_locs(regMPFCZ, "Frost Columns Monitor - x:-3776 y:3904","Frost Columns Monitor - x:-3872 y:3808","Frost Columns Monitor - x:-3616 y:1120",
            "Frost Columns Monitor - x:-1568 y:-1152","Frost Columns Monitor - x:1856 y:-1728","Frost Columns Monitor - x:1888 y:-1728","Frost Columns Monitor - x:1888 y:-1760",
            "Frost Columns Monitor - x:608 y:640","Frost Columns Monitor - x:1312 y:-960","Frost Columns Monitor - x:2048 y:768","Frost Columns Monitor - x:-1152 y:-1056",
            "Frost Columns Monitor - x:0 y:-3520","Frost Columns Monitor - x:-64 y:-3520","Frost Columns Monitor - x:560 y:736","Frost Columns Monitor - x:-1472 y:-96",
            "Frost Columns Monitor - x:-1472 y:-32","Frost Columns Monitor - x:-3296 y:3200","Frost Columns Monitor - x:-3328 y:3168","Frost Columns Monitor - x:-2080 y:-896",
            "Frost Columns Monitor - x:2112 y:-1088","Frost Columns Monitor - x:2112 y:-1344","Frost Columns Monitor - x:832 y:-1376")
        create_locs(regMPMMZ, "Meadow Match Monitor - x:-1536 y:1472","Meadow Match Monitor - x:-2688 y:320","Meadow Match Monitor - x:3520 y:-576",
            "Meadow Match Monitor - x:-64 y:-1088","Meadow Match Monitor - x:-1472 y:512","Meadow Match Monitor - x:1472 y:-864")
        create_locs(regMPGLZ, "Granite Lake Monitor - x:1728 y:3264","Granite Lake Monitor - x:-432 y:-1168","Granite Lake Monitor - x:4764 y:7933",
            "Granite Lake Monitor - x:5045 y:7647","Granite Lake Monitor - x:2352 y:384","Granite Lake Monitor - x:2064 y:-1136","Granite Lake Monitor - x:2304 y:1056",
            "Granite Lake Monitor - x:5472 y:1344","Granite Lake Monitor - x:1075 y:5651","Granite Lake Monitor - x:1293 y:7833","Granite Lake Monitor - x:4288 y:3040")
        create_locs(regMPSSZ, "Summit Showdown Monitor - x:5344 y:1952","Summit Showdown Monitor - x:4640 y:2400","Summit Showdown Monitor - x:-6624 y:-64",
            "Summit Showdown Monitor - x:-6480 y:-64","Summit Showdown Monitor - x:-6352 y:-64","Summit Showdown Monitor - x:-6176 y:1888","Summit Showdown Monitor - x:-6464 y:2592",
            "Summit Showdown Monitor - x:-4736 y:-128","Summit Showdown Monitor - x:2144 y:-1856","Summit Showdown Monitor - x:-1728 y:-1568","Summit Showdown Monitor - x:1696 y:-1568",
            "Summit Showdown Monitor - x:3056 y:976","Summit Showdown Monitor - x:1824 y:-800","Summit Showdown Monitor - x:-7456 y:-1696","Summit Showdown Monitor - x:-7008 y:-2144",
            "Summit Showdown Monitor - x:-7456 y:384","Summit Showdown Monitor - x:5600 y:2208","Summit Showdown Monitor - x:5088 y:1696","Summit Showdown Monitor - x:-1536 y:-2848",
            "Summit Showdown Monitor - x:3936 y:-1408","Summit Showdown Monitor - x:0 y:-224","Summit Showdown Monitor - x:-1216 y:-928","Summit Showdown Monitor - x:-4321 y:1792")
        create_locs(regMPSShZ, "Silver Shiver Monitor - x:4560 y:-8688","Silver Shiver Monitor - x:3648 y:-10176","Silver Shiver Monitor - x:6080 y:-12416",
            "Silver Shiver Monitor - x:7040 y:-11264","Silver Shiver Monitor - x:7680 y:-12608","Silver Shiver Monitor - x:7168 y:-11872","Silver Shiver Monitor - x:6976 y:-11872",
            "Silver Shiver Monitor - x:13824 y:-7392","Silver Shiver Monitor - x:13088 y:-3840","Silver Shiver Monitor - x:5440 y:-2688","Silver Shiver Monitor - x:5728 y:-2688",
            "Silver Shiver Monitor - x:8512 y:-3264","Silver Shiver Monitor - x:9024 y:-3904","Silver Shiver Monitor - x:2400 y:-3920","Silver Shiver Monitor - x:3392 y:-1824",
            "Silver Shiver Monitor - x:3392 y:-1728","Silver Shiver Monitor - x:3392 y:-1888","Silver Shiver Monitor - x:-96 y:-2768","Silver Shiver Monitor - x:32 y:-2768",
            "Silver Shiver Monitor - x:-192 y:-4672","Silver Shiver Monitor - x:1984 y:-5184","Silver Shiver Monitor - x:3056 y:-5568","Silver Shiver Monitor - x:3056 y:-5760",
            "Silver Shiver Monitor - x:-1344 y:-6464","Silver Shiver Monitor - x:176 y:-10384","Silver Shiver Monitor - x:4928 y:-17600","Silver Shiver Monitor - x:1952 y:-15648",
            "Silver Shiver Monitor - x:1856 y:-16320","Silver Shiver Monitor - x:192 y:-16960","Silver Shiver Monitor - x:-2368 y:-15424","Silver Shiver Monitor - x:-192 y:-15808",
            "Silver Shiver Monitor - x:-1120 y:-14048","Silver Shiver Monitor - x:9152 y:-15168","Silver Shiver Monitor - x:8384 y:-15168","Silver Shiver Monitor - x:11200 y:-17216",
            "Silver Shiver Monitor - x:11584 y:-13120","Silver Shiver Monitor - x:13632 y:-12320","Silver Shiver Monitor - x:15280 y:-26560","Silver Shiver Monitor - x:15696 y:-26560",
            "Silver Shiver Monitor - x:11744 y:-20960","Silver Shiver Monitor - x:11872 y:-21088","Silver Shiver Monitor - x:15360 y:-27360","Silver Shiver Monitor - x:15552 y:-27360",
            "Silver Shiver Monitor - x:6240 y:-13776","Silver Shiver Monitor - x:6304 y:-13808")
        create_locs(regMPUBZ, "Uncharted Badlands Monitor - x:1337 y:-1608","Uncharted Badlands Monitor - x:515 y:502","Uncharted Badlands Monitor - x:2522 y:114",
            "Uncharted Badlands Monitor - x:2080 y:2560","Uncharted Badlands Monitor - x:1920 y:1024","Uncharted Badlands Monitor - x:-1379 y:-2638","Uncharted Badlands Monitor - x:-992 y:32",
            "Uncharted Badlands Monitor - x:1152 y:3008","Uncharted Badlands Monitor - x:40 y:3323")
        create_locs(regMPPSZ, "Pristine Shores Monitor - x:6208 y:10720","Pristine Shores Monitor - x:4736 y:12288","Pristine Shores Monitor - x:4272 y:3440",
            "Pristine Shores Monitor - x:14272 y:7488","Pristine Shores Monitor - x:15808 y:12160","Pristine Shores Monitor - x:14936 y:13448","Pristine Shores Monitor - x:10336 y:11296",
            "Pristine Shores Monitor - x:11754 y:6506","Pristine Shores Monitor - x:16782 y:8472","Pristine Shores Monitor - x:13472 y:9024","Pristine Shores Monitor - x:13288 y:10444",
            "Pristine Shores Monitor - x:6080 y:8832","Pristine Shores Monitor - x:9296 y:12928","Pristine Shores Monitor - x:10672 y:6576","Pristine Shores Monitor - x:10680 y:12616",
            "Pristine Shores Monitor - x:3008 y:6528","Pristine Shores Monitor - x:2088 y:5240","Pristine Shores Monitor - x:4160 y:7176","Pristine Shores Monitor - x:6528 y:7936",
            "Pristine Shores Monitor - x:9944 y:7616")
        create_locs(regMPCHZ, "Crystalline Heights Monitor - x:4288 y:12384","Crystalline Heights Monitor - x:7392 y:8832","Crystalline Heights Monitor - x:3250 y:8402",
            "Crystalline Heights Monitor - x:7888 y:5600","Crystalline Heights Monitor - x:4416 y:11560","Crystalline Heights Monitor - x:2018 y:1218","Crystalline Heights Monitor - x:7314 y:-366",
            "Crystalline Heights Monitor - x:6418 y:3026","Crystalline Heights Monitor - x:1120 y:6192","Crystalline Heights Monitor - x:-360 y:12136","Crystalline Heights Monitor - x:2832 y:13836",
            "Crystalline Heights Monitor - x:6386 y:15954","Crystalline Heights Monitor - x:3104 y:17064","Crystalline Heights Monitor - x:7288 y:17568","Crystalline Heights Monitor - x:-784 y:-632",
            "Crystalline Heights Monitor - x:5410 y:1266","Crystalline Heights Monitor - x:1032 y:10464","Crystalline Heights Monitor - x:5384 y:5984","Crystalline Heights Monitor - x:5554 y:9730",
            "Crystalline Heights Monitor - x:6384 y:19336","Crystalline Heights Monitor - x:-544 y:4064","Crystalline Heights Monitor - x:-2704 y:12592")
        create_locs(regMPMAZ, "Midnight Abyss Monitor - x:-3264 y:3136","Midnight Abyss Monitor - x:3264 y:3136","Midnight Abyss Monitor - x:3264 y:-3136",
            "Midnight Abyss Monitor - x:-3264 y:-3136","Midnight Abyss Monitor - x:-2624 y:-2624","Midnight Abyss Monitor - x:2624 y:-2624","Midnight Abyss Monitor - x:2624 y:2624",
            "Midnight Abyss Monitor - x:-2624 y:2624","Midnight Abyss Monitor - x:-3136 y:3264","Midnight Abyss Monitor - x:3136 y:3264","Midnight Abyss Monitor - x:3136 y:-3264",
            "Midnight Abyss Monitor - x:-3136 y:-3264")
        create_locs(regMPATZ, "Airborne Temple Monitor - x:-2432 y:2432","Airborne Temple Monitor - x:2432 y:2432","Airborne Temple Monitor - x:2432 y:-2432",
            "Airborne Temple Monitor - x:-2432 y:-2432","Airborne Temple Monitor - x:-128 y:-128","Airborne Temple Monitor - x:128 y:-128","Airborne Temple Monitor - x:128 y:128",
            "Airborne Temple Monitor - x:-128 y:128","Airborne Temple Monitor - x:-256 y:256","Airborne Temple Monitor - x:256 y:256","Airborne Temple Monitor - x:256 y:-256",
            "Airborne Temple Monitor - x:-256 y:-256")

def connect_regions(world: MultiWorld, player: int, source: str, target: str, rule=None) -> Entrance:
    sourceRegion = world.get_region(source, player)
    targetRegion = world.get_region(target, player)
    return sourceRegion.connect(targetRegion, rule=rule)


def create_region(name: str, player: int, world: MultiWorld) -> SRB2Region:
    region = SRB2Region(name, player, world)
    world.regions.append(region)
    return region


def create_subregion(source_region: Region, name: str, *locs: str) -> SRB2Region:
    region = SRB2Region(name, source_region.player, source_region.multiworld)
    connection = Entrance(source_region.player, name, source_region)
    source_region.exits.append(connection)
    connection.connect(region)
    source_region.multiworld.regions.append(region)
    create_locs(region, *locs)
    return region


def set_subregion_access_rule(world, player, region_name: str, rule):
    world.get_entrance(world, player, region_name).access_rule = rule


def create_default_locs(reg: Region, default_locs: dict):
    create_locs(reg, *default_locs.keys())


def create_locs(reg: Region, *locs: str):
    reg.locations += [SRB2Location(reg.player, loc_name, location_table[loc_name], reg) for loc_name in locs]
