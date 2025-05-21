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
        create_locs(regGFZ,"Greenflower (Act 1) Monitor - x:5408 y:3040","Greenflower (Act 1) Monitor - x:10560 y:2240","Greenflower (Act 1) Monitor - x:1184 y:5824","Greenflower (Act 2) Monitor - x:-480 y:-4480","Greenflower (Act 2) Monitor - x:2880 y:-6208",
"Greenflower (Act 2) Monitor - x:-2976 y:-4672","Greenflower (Act 2) Monitor - x:188 y:-347","Greenflower (Act 2) Monitor - x:-1184 y:512","Greenflower (Act 2) Monitor - x:3296 y:6624","Greenflower (Act 2) Monitor - x:-7072 y:-9696","Greenflower (Act 2) Monitor - x:720 y:-10320",
"Greenflower (Act 2) Monitor - x:-3968 y:4800")

    regTHZ = create_region("Techno Hill Zone", player, world)
    create_locs(regTHZ, "Techno Hill (Act 1) Star Emblem", "Techno Hill (Act 1) Spade Emblem","Techno Hill (Act 1) Heart Emblem", "Techno Hill (Act 1) Diamond Emblem",
                        "Techno Hill (Act 1) Club Emblem","Techno Hill (Act 2) Star Emblem", "Techno Hill (Act 2) Spade Emblem","Techno Hill (Act 2) Heart Emblem", "Techno Hill (Act 2) Diamond Emblem",
                        "Techno Hill (Act 2) Club Emblem","Techno Hill (Act 1) Clear","Techno Hill (Act 2) Clear","Techno Hill (Act 3) Clear","Techno Hill (Act 1) Emerald Token - On Pipes",
                "Techno Hill (Act 1) Emerald Token - Alt Path Under Slime","Techno Hill (Act 2) Emerald Token - Deep in Slime","Techno Hill (Act 2) Emerald Token - Knuckles Path Backtrack as Amy")
    if options.time_emblems:
        create_locs(regTHZ, "Techno Hill (Act 1) Time Emblem","Techno Hill (Act 2) Time Emblem","Techno Hill (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regTHZ, "Techno Hill (Act 1) Ring Emblem","Techno Hill (Act 2) Ring Emblem")
    if options.score_emblems:
        create_locs(regTHZ, "Techno Hill (Act 3) Score Emblem")
    if options.oneup_sanity:
        create_locs(regTHZ,
        "Techno Hill (Act 1) Monitor - x:5568 y:-3360","Techno Hill (Act 1) Monitor - x:-3904 y:-12224","Techno Hill (Act 1) Monitor - x:3008 y:-9152","Techno Hill (Act 1) Monitor - x:-960 y:-12128","Techno Hill (Act 1) Monitor - x:16320 y:-9472",
        "Techno Hill (Act 1) Monitor - x:20160 y:-7904","Techno Hill (Act 1) Monitor - x:10944 y:-11584","Techno Hill (Act 1) Monitor - x:14400 y:-6208","Techno Hill (Act 1) Monitor - x:2976 y:4384","Techno Hill (Act 2) Monitor - x:-17536 y:2048",
        "Techno Hill (Act 2) Monitor - x:0 y:2240","Techno Hill (Act 2) Monitor - x:-13152 y:7968","Techno Hill (Act 2) Monitor - x:-3136 y:-448","Techno Hill (Act 2) Monitor - x:1760 y:5472","Techno Hill (Act 2) Monitor - x:-18592 y:-4096",
        "Techno Hill (Act 2) Monitor - x:-11584 y:-4768","Techno Hill (Act 2) Monitor - x:-2048 y:-7872","Techno Hill (Act 2) Monitor - x:5600 y:-11168","Techno Hill (Act 2) Monitor - x:832 y:-6144","Techno Hill (Act 2) Monitor - x:-16000 y:-6464",
        "Techno Hill (Act 2) Monitor - x:4128 y:-224")

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

    regRVZ = create_region("Red Volcano Zone", player, world)
    create_locs(regRVZ, "Red Volcano (Act 1) Star Emblem", "Red Volcano (Act 1) Spade Emblem", "Red Volcano (Act 1) Heart Emblem", "Red Volcano (Act 1) Diamond Emblem",
                "Red Volcano (Act 1) Club Emblem","Red Volcano (Act 1) Clear","Red Volcano (Act 1) Emerald Token - First Outside Area","Red Volcano (Act 1) Emerald Token - Hidden Ledge Near 4th Checkpoint",
    "Red Volcano (Act 1) Emerald Token - Rollout Rock Lavafall","Red Volcano (Act 1) Emerald Token - Behind Ending Rocket")
    if options.time_emblems:
        create_locs(regRVZ, "Red Volcano (Act 1) Time Emblem")
    if options.ring_emblems:
        create_locs(regRVZ, "Red Volcano (Act 1) Ring Emblem")
    if options.oneup_sanity:
        create_locs(regRVZ,"Red Volcano (Act 1) Monitor - x:-8624 y:-8192","Red Volcano (Act 1) Monitor - x:23524 y:4224","Red Volcano (Act 1) Monitor - x:26208 y:6976","Red Volcano (Act 1) Monitor - x:12760 y:8392","Red Volcano (Act 1) Monitor - x:10336 y:-3872",
        "Red Volcano (Act 1) Monitor - x:2176 y:11104","Red Volcano (Act 1) Monitor - x:-4032 y:-16448","Red Volcano (Act 1) Monitor - x:7264 y:-5888","Red Volcano (Act 1) Monitor - x:7552 y:11936")

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
        "Egg Rock (Act 2) Monitor - x:-9216 y:12384","Egg Rock (Act 2) Monitor - x:5216 y:20736","Egg Rock (Act 2) Monitor - x:-11936 y:15264","Egg Rock (Act 2) Monitor - x:-6656 y:8096","Egg Rock (Act 2) Monitor - x:11136 y:15456","Egg Rock (Act 2) Monitor - x:2304 y:24960",
        "Egg Rock (Act 2) Monitor - x:-12032 y:7040","Egg Rock (Act 2) Monitor - x:-12864 y:7040","Egg Rock (Act 2) Monitor - x:10112 y:10432","Egg Rock (Act 2) Monitor - x:256 y:7616")


    regBCZ = create_region("Black Core Zone", player, world)
    create_locs(regBCZ, "Black Core (Act 1) Clear","Black Core (Act 2) Clear","Black Core (Act 3) Clear")
    if options.time_emblems:
        create_locs(regBCZ, "Black Core (Act 1) Time Emblem", "Black Core (Act 2) Time Emblem", "Black Core (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regBCZ, "Black Core (Act 1) Ring Emblem")
    if options.score_emblems:
        create_locs(regBCZ, "Black Core (Act 2) Score Emblem","Black Core (Act 3) Score Emblem")
    if options.oneup_sanity:
        create_locs(regBCZ,"Black Core (Act 1) Monitor - x:-12144 y:-3328","Black Core (Act 1) Monitor - x:-10352 y:-2848")


    regFHZ = create_region("Frozen Hillside Zone", player, world)
    create_locs(regFHZ, "Frozen Hillside Star Emblem", "Frozen Hillside Spade Emblem", "Frozen Hillside Heart Emblem", "Frozen Hillside Diamond Emblem",
                "Frozen Hillside Club Emblem","Frozen Hillside Clear")
    if options.time_emblems:
        create_locs(regFHZ, "Frozen Hillside Time Emblem")
    if options.ring_emblems:
        create_locs(regFHZ, "Frozen Hillside Ring Emblem")
    if options.oneup_sanity:
        create_locs(regFHZ,"Frozen Hillside Monitor - x:6656 y:-4624","Frozen Hillside Monitor - x:-2944 y:-19168")



    regPTZ = create_region("Pipe Towers Zone", player, world)
    create_locs(regPTZ, "Pipe Towers Star Emblem", "Pipe Towers Spade Emblem", "Pipe Towers Heart Emblem", "Pipe Towers Diamond Emblem",
                "Pipe Towers Club Emblem","Pipe Towers Clear")
    if options.time_emblems:
        create_locs(regPTZ, "Pipe Towers Time Emblem")
    if options.ring_emblems:
        create_locs(regPTZ, "Pipe Towers Ring Emblem")
    if options.oneup_sanity:
        create_locs(regPTZ,"Pipe Towers Monitor - x:-1576 y:55","Pipe Towers Monitor - x:-216 y:5097","Pipe Towers Monitor - x:7000 y:6520","Pipe Towers Monitor - x:11496 y:-5097","Pipe Towers Monitor - x:7704 y:616","Pipe Towers Monitor - x:8744 y:-3752")

    regFFZ = create_region("Forest Fortress Zone", player, world)
    create_locs(regFFZ, "Forest Fortress Star Emblem", "Forest Fortress Spade Emblem", "Forest Fortress Heart Emblem", "Forest Fortress Diamond Emblem",
                "Forest Fortress Club Emblem","Forest Fortress Clear")
    if options.time_emblems:
        create_locs(regFFZ, "Forest Fortress Time Emblem")
    if options.ring_emblems:
        create_locs(regFFZ, "Forest Fortress Ring Emblem")
    if options.oneup_sanity:
        create_locs(regFFZ,"Forest Fortress Monitor - x:-1280 y:-7680","Forest Fortress Monitor - x:1024 y:-6528","Forest Fortress Monitor - x:9088 y:12800","Forest Fortress Monitor - x:5824 y:8368","Forest Fortress Monitor - x:14752 y:10672")


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
        create_locs(regFDZ,"Final Demo Monitor - x:-27232 y:-20000","Final Demo Monitor - x:-9312 y:-20512","Final Demo Monitor - x:-6080 y:-26560","Final Demo Monitor - x:9216 y:-25728","Final Demo Monitor - x:29504 y:-9984",
"Final Demo Monitor - x:21056 y:-6400","Final Demo Monitor - x:18880 y:15104","Final Demo Monitor - x:27520 y:7552","Final Demo Monitor - x:27712 y:7360","Final Demo Monitor - x:24448 y:12352","Final Demo Monitor - x:20192 y:25536",
"Final Demo Monitor - x:28192 y:26688","Final Demo Monitor - x:-9104 y:16320","Final Demo Monitor - x:496 y:28416","Final Demo Monitor - x:8496 y:26880")
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
    #TODO add the rest of the zones here


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
