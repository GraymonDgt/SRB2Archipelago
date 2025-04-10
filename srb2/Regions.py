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

    regGFZ = create_region("Greenflower Zone", player, world)
    create_locs(regGFZ, "Greenflower (Act 1) Star Emblem", "Greenflower (Act 1) Spade Emblem","Greenflower (Act 1) Heart Emblem", "Greenflower (Act 1) Diamond Emblem",
                        "Greenflower (Act 1) Club Emblem","Greenflower (Act 2) Star Emblem", "Greenflower (Act 2) Spade Emblem","Greenflower (Act 2) Heart Emblem", "Greenflower (Act 2) Diamond Emblem",
                        "Greenflower (Act 2) Club Emblem","Greenflower Act 1 Clear","Greenflower Act 2 Clear","Greenflower Act 3 Clear","Greenflower (Act 1) Emerald Token - Breakable Wall Near Bridge",
                "Greenflower (Act 1) Emerald Token - Midair Top Path","Greenflower (Act 2) Emerald Token - Main Path Cave","Greenflower (Act 2) Emerald Token - Under Bridge Near End",
                "Greenflower (Act 2) Emerald Token - No Spin High on Ledge")
    if options.time_emblems:
        create_locs(regGFZ, "Greenflower (Act 1) Time Emblem","Greenflower (Act 2) Time Emblem","Greenflower (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regGFZ, "Greenflower (Act 1) Ring Emblem","Greenflower (Act 2) Ring Emblem")
    if options.score_emblems:
        create_locs(regGFZ, "Greenflower (Act 3) Score Emblem")
    regTHZ = create_region("Techno Hill Zone", player, world)
    create_locs(regTHZ, "Techno Hill (Act 1) Star Emblem", "Techno Hill (Act 1) Spade Emblem","Techno Hill (Act 1) Heart Emblem", "Techno Hill (Act 1) Diamond Emblem",
                        "Techno Hill (Act 1) Club Emblem","Techno Hill (Act 2) Star Emblem", "Techno Hill (Act 2) Spade Emblem","Techno Hill (Act 2) Heart Emblem", "Techno Hill (Act 2) Diamond Emblem",
                        "Techno Hill (Act 2) Club Emblem","Techno Hill Act 1 Clear","Techno Hill Act 2 Clear","Techno Hill Act 3 Clear","Techno Hill (Act 1) Emerald Token - On Pipes",
                "Techno Hill (Act 1) Emerald Token - Alt Path Under Slime","Techno Hill (Act 2) Emerald Token - Deep in Slime","Techno Hill (Act 2) Emerald Token - Knuckles Path Backtrack as Amy")
    if options.time_emblems:
        create_locs(regTHZ, "Techno Hill (Act 1) Time Emblem","Techno Hill (Act 2) Time Emblem","Techno Hill (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regTHZ, "Techno Hill (Act 1) Ring Emblem","Techno Hill (Act 2) Ring Emblem")
    if options.score_emblems:
        create_locs(regTHZ, "Techno Hill (Act 3) Score Emblem")
    regDSZ = create_region("Deep Sea Zone", player, world)
    create_locs(regDSZ, "Deep Sea (Act 1) Star Emblem", "Deep Sea (Act 1) Spade Emblem","Deep Sea (Act 1) Heart Emblem", "Deep Sea (Act 1) Diamond Emblem",
                        "Deep Sea (Act 1) Club Emblem","Deep Sea (Act 2) Star Emblem", "Deep Sea (Act 2) Spade Emblem","Deep Sea (Act 2) Heart Emblem", "Deep Sea (Act 2) Diamond Emblem",
                        "Deep Sea (Act 2) Club Emblem","Deep Sea Act 1 Clear","Deep Sea Act 2 Clear","Deep Sea Act 3 Clear","Deep Sea (Act 1) Emerald Token - V on Right Path",
                "Deep Sea (Act 1) Emerald Token - Underwater Air Pocket on Right Path","Deep Sea (Act 1) Emerald Token - Yellow Doors",
    "Deep Sea (Act 1) Emerald Token - Large Underwater Curve", "Deep Sea (Act 1) Emerald Token - Waterslide Gargoyles", "Deep Sea (Act 2) Emerald Token - Near Heart Emblem",
    "Deep Sea (Act 2) Emerald Token - Red and Yellow Springs", "Deep Sea (Act 2) Emerald Token - Down Right From Goal", "Deep Sea (Act 2) Emerald Token - No Spin Spring Turnaround")
    if options.time_emblems:
        create_locs(regDSZ, "Deep Sea (Act 1) Time Emblem","Deep Sea (Act 2) Time Emblem","Deep Sea (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regDSZ, "Deep Sea (Act 1) Ring Emblem","Deep Sea (Act 2) Ring Emblem")
    if options.score_emblems:
        create_locs(regDSZ, "Deep Sea (Act 3) Score Emblem")

    regCEZ = create_region("Castle Eggman Zone", player, world)
    create_locs(regCEZ, "Castle Eggman (Act 1) Star Emblem", "Castle Eggman (Act 1) Spade Emblem", "Castle Eggman (Act 1) Heart Emblem", "Castle Eggman (Act 1) Diamond Emblem",
                "Castle Eggman (Act 1) Club Emblem", "Castle Eggman (Act 2) Star Emblem", "Castle Eggman (Act 2) Spade Emblem", "Castle Eggman (Act 2) Heart Emblem", "Castle Eggman (Act 2) Diamond Emblem",
                "Castle Eggman (Act 2) Club Emblem","Castle Eggman Act 1 Clear","Castle Eggman Act 2 Clear","Castle Eggman Act 3 Clear","Castle Eggman (Act 1) Emerald Token - Behind Fence Near Start",
    "Castle Eggman (Act 1) Emerald Token - Spring Side Path","Castle Eggman (Act 1) Emerald Token - Inside Castle","Castle Eggman (Act 2) Emerald Token - First Outside Area","Castle Eggman (Act 2) Emerald Token - Corner of Right Courtyard",
    "Castle Eggman (Act 2) Emerald Token - Window of Back Left Courtyard","Castle Eggman (Act 2) Emerald Token - Spring Near Club Emblem","Castle Eggman (Act 2) Emerald Token - High Ledge Before Final Tower")
    if options.time_emblems:
        create_locs(regCEZ, "Castle Eggman (Act 1) Time Emblem", "Castle Eggman (Act 2) Time Emblem", "Castle Eggman (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regCEZ, "Castle Eggman (Act 1) Ring Emblem", "Castle Eggman (Act 2) Ring Emblem")
    if options.score_emblems:
        create_locs(regCEZ, "Castle Eggman (Act 3) Score Emblem")

    regACZ = create_region("Arid Canyon Zone", player, world)
    create_locs(regACZ, "Arid Canyon (Act 1) Star Emblem", "Arid Canyon (Act 1) Spade Emblem", "Arid Canyon (Act 1) Heart Emblem", "Arid Canyon (Act 1) Diamond Emblem",
                "Arid Canyon (Act 1) Club Emblem", "Arid Canyon (Act 2) Star Emblem", "Arid Canyon (Act 2) Spade Emblem", "Arid Canyon (Act 2) Heart Emblem", "Arid Canyon (Act 2) Diamond Emblem",
                "Arid Canyon (Act 2) Club Emblem","Arid Canyon Act 1 Clear","Arid Canyon Act 2 Clear","Arid Canyon Act 3 Clear","Arid Canyon (Act 1) Emerald Token - Speed Shoes Central Pillar",
    "Arid Canyon (Act 1) Emerald Token - Behind Pillar Before Exploding Ramp","Arid Canyon (Act 1) Emerald Token - Behind Wall and Spikes","Arid Canyon (Act 2) Emerald Token - Left No Spin Path Minecarts",
    "Arid Canyon (Act 2) Emerald Token - Large Arch Cave Right Ledge","Arid Canyon (Act 2) Emerald Token - Knuckles Dark Path Around Wall",)
    if options.time_emblems:
        create_locs(regACZ, "Arid Canyon (Act 1) Time Emblem", "Arid Canyon (Act 2) Time Emblem", "Arid Canyon (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regACZ, "Arid Canyon (Act 1) Ring Emblem", "Arid Canyon (Act 2) Ring Emblem")
    if options.score_emblems:
        create_locs(regACZ, "Arid Canyon (Act 3) Score Emblem")

    regRVZ = create_region("Red Volcano Zone", player, world)
    create_locs(regRVZ, "Red Volcano (Act 1) Star Emblem", "Red Volcano (Act 1) Spade Emblem", "Red Volcano (Act 1) Heart Emblem", "Red Volcano (Act 1) Diamond Emblem",
                "Red Volcano (Act 1) Club Emblem","Red Volcano Act 1 Clear","Red Volcano (Act 1) Emerald Token - First Outside Area","Red Volcano (Act 1) Emerald Token - Hidden Ledge Near 4th Checkpoint",
    "Red Volcano (Act 1) Emerald Token - Rollout Rock Lavafall","Red Volcano (Act 1) Emerald Token - Behind Ending Rocket")
    if options.time_emblems:
        create_locs(regRVZ, "Red Volcano (Act 1) Time Emblem")
    if options.ring_emblems:
        create_locs(regRVZ, "Red Volcano (Act 1) Ring Emblem")

    regERZ = create_region("Egg Rock Zone", player, world)
    create_locs(regERZ, "Egg Rock (Act 1) Star Emblem", "Egg Rock (Act 1) Spade Emblem", "Egg Rock (Act 1) Heart Emblem", "Egg Rock (Act 1) Diamond Emblem",
                "Egg Rock (Act 1) Club Emblem", "Egg Rock (Act 2) Star Emblem", "Egg Rock (Act 2) Spade Emblem", "Egg Rock (Act 2) Heart Emblem", "Egg Rock (Act 2) Diamond Emblem",
                "Egg Rock (Act 2) Club Emblem","Egg Rock Act 1 Clear","Egg Rock Act 2 Clear","Egg Rock (Act 1) Emerald Token - Gravity Conveyor Belts",
    "Egg Rock (Act 1) Emerald Token - Moving Platforms","Egg Rock (Act 2) Emerald Token - Outside on Metal Beam","Egg Rock (Act 2) Emerald Token - Skip Gravity Pad",
    "Egg Rock (Act 2) Emerald Token - Disco Room")
    if options.time_emblems:
        create_locs(regERZ, "Egg Rock (Act 1) Time Emblem", "Egg Rock (Act 2) Time Emblem")
    if options.ring_emblems:
        create_locs(regERZ, "Egg Rock (Act 1) Ring Emblem", "Egg Rock (Act 2) Ring Emblem")

    regBCZ = create_region("Black Core Zone", player, world)
    create_locs(regBCZ, "Black Core Act 1 Clear","Black Core Act 2 Clear","Black Core Act 3 Clear")
    if options.time_emblems:
        create_locs(regBCZ, "Black Core (Act 1) Time Emblem", "Black Core (Act 2) Time Emblem", "Black Core (Act 3) Time Emblem")
    if options.ring_emblems:
        create_locs(regBCZ, "Black Core (Act 1) Ring Emblem")
    if options.score_emblems:
        create_locs(regBCZ, "Black Core (Act 2) Score Emblem","Black Core (Act 3) Score Emblem")

    regFHZ = create_region("Frozen Hillside Zone", player, world)
    create_locs(regFHZ, "Frozen Hillside Star Emblem", "Frozen Hillside Spade Emblem", "Frozen Hillside Heart Emblem", "Frozen Hillside Diamond Emblem",
                "Frozen Hillside Club Emblem","Frozen Hillside Clear")
    if options.time_emblems:
        create_locs(regFHZ, "Frozen Hillside Time Emblem")
    if options.ring_emblems:
        create_locs(regFHZ, "Frozen Hillside Ring Emblem")

    regPTZ = create_region("Pipe Towers Zone", player, world)
    create_locs(regPTZ, "Pipe Towers Star Emblem", "Pipe Towers Spade Emblem", "Pipe Towers Heart Emblem", "Pipe Towers Diamond Emblem",
                "Pipe Towers Club Emblem","Pipe Towers Clear")
    if options.time_emblems:
        create_locs(regPTZ, "Pipe Towers Time Emblem")
    if options.ring_emblems:
        create_locs(regPTZ, "Pipe Towers Ring Emblem")

    regFFZ = create_region("Forest Fortress Zone", player, world)
    create_locs(regFFZ, "Forest Fortress Star Emblem", "Forest Fortress Spade Emblem", "Forest Fortress Heart Emblem", "Forest Fortress Diamond Emblem",
                "Forest Fortress Club Emblem","Forest Fortress Clear")
    if options.time_emblems:
        create_locs(regFFZ, "Forest Fortress Time Emblem")
    if options.ring_emblems:
        create_locs(regFFZ, "Forest Fortress Ring Emblem")

    regFDZ = create_region("Final Demo Zone", player, world)
    create_locs(regFDZ, "Final Demo Clear","Final Demo Emerald Token - Greenflower (Act 1) Breakable Wall Near Bridge",
    "Final Demo Emerald Token - Greenflower (Act 2) Underwater Cave",
    "Final Demo Emerald Token - Greenflower (Act 2) Under Bridge Near End",
    "Final Demo Emerald Token - Techno Hill (Act 1) On Pipes",
    "Final Demo Emerald Token - Techno Hill (Act 1) Alt Path Fans",
    "Final Demo Emerald Token - Techno Hill (Act 2) Breakable Wall",
    "Final Demo Emerald Token - Techno Hill (Act 2) Under Poison Near End",
    "Final Demo Emerald Token - Castle Eggman (Act 1) Small Lake Near Start",
    "Final Demo Emerald Token - Castle Eggman (Act 1) Tunnel Before Act Clear"
    )#"Final Demo Emerald Token - Castle Eggman (Act 2) Water Flow in Sewers"
#Removed until i figure out why its not sending

    regHHZ = create_region("Haunted Heights Zone", player, world)
    create_locs(regHHZ, "Haunted Heights Star Emblem", "Haunted Heights Spade Emblem", "Haunted Heights Heart Emblem", "Haunted Heights Diamond Emblem",
                "Haunted Heights Club Emblem","Haunted Heights Clear")
    if options.time_emblems:
        create_locs(regHHZ, "Haunted Heights Time Emblem")
    if options.ring_emblems:
        create_locs(regHHZ, "Haunted Heights Ring Emblem")

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

    regATZ = create_region("Azure Temple Zone", player, world)
    create_locs(regATZ, "Azure Temple Star Emblem", "Azure Temple Spade Emblem", "Azure Temple Heart Emblem", "Azure Temple Diamond Emblem",
                "Azure Temple Club Emblem","Azure Temple Clear")
    if options.time_emblems:
        create_locs(regATZ, "Azure Temple Time Emblem")
    if options.ring_emblems:
        create_locs(regATZ, "Azure Temple Ring Emblem")

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
    create_locs(regSPAPZ, "Alpine Paradise (Act 1) Sun Emblem", "Alpine Paradise (Act 1) Moon Emblem","Alpine Paradise Act 1 Clear","Alpine Paradise (Act 2) Sun Emblem", "Alpine Paradise (Act 2) Moon Emblem","Alpine Paradise Act 2 Clear")
    
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
