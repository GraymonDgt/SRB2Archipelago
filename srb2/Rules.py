from typing import Callable, Union, Dict, Set

from BaseClasses import MultiWorld
from ..generic.Rules import add_rule, set_rule
from .Locations import location_table
from .Options import SRB2Options
from .Regions import connect_regions, SRB2Zones
from .Items import character_item_data_table
from .Items import zones_item_data_table

def shuffle_dict_keys(world, dictionary: dict) -> dict:
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    world.random.shuffle(keys)
    return dict(zip(keys, values))

def fix_reg(entrance_map: Dict[SRB2Zones, str], entrance: SRB2Zones, invalid_regions: Set[str],
            swapdict: Dict[SRB2Zones, str], world):
    if entrance_map[entrance] in invalid_regions: # Unlucky :C
        replacement_regions = [(rand_entrance, rand_region) for rand_entrance, rand_region in swapdict.items()
                               if rand_region not in invalid_regions]
        rand_entrance, rand_region = world.random.choice(replacement_regions)
        old_dest = entrance_map[entrance]
        entrance_map[entrance], entrance_map[rand_entrance] = rand_region, old_dest
        swapdict[entrance], swapdict[rand_entrance] = rand_region, old_dest
    swapdict.pop(entrance)

def set_rules(world, options: SRB2Options, player: int, area_connections: dict, move_rando_bitvec: int):

    # Destination Format: LVL | AREA with LVL = LEVEL_x, AREA = Area as used in sm64 code
    # Cast to int to not rely on availability of SM64Levels enum. Will cause crash in MultiServer otherwise


    rf = RuleFactory(world, options, player, move_rando_bitvec)

    connect_regions(world, player, "Menu", "Greenflower Zone", lambda state: state.has("Greenflower Zone", player))
    connect_regions(world, player, "Menu", "Techno Hill Zone", lambda state: state.has("Techno Hill Zone", player))
    connect_regions(world, player, "Menu", "Deep Sea Zone", lambda state: state.has("Deep Sea Zone", player))
    connect_regions(world, player, "Menu", "Castle Eggman Zone", lambda state: state.has("Castle Eggman Zone", player))
    connect_regions(world, player, "Menu", "Arid Canyon Zone", lambda state: state.has("Arid Canyon Zone", player))
    connect_regions(world, player, "Menu", "Red Volcano Zone", lambda state: state.has("Red Volcano Zone", player))
    connect_regions(world, player, "Menu", "Egg Rock Zone", lambda state: state.has("Egg Rock Zone", player))
    if options.bcz_emblem_percent==0:
        connect_regions(world, player, "Menu", "Black Core Zone", lambda state: state.has("Black Core Zone", player))
    else:
        connect_regions(world, player, "Menu", "Black Core Zone", lambda state: state.has("Emblem", player, options.bcz_emblem_percent))

    connect_regions(world, player, "Black Core Zone", "Credits", lambda state: state.has("Chaos Emerald", player, 7))
    connect_regions(world, player, "Menu", "Frozen Hillside Zone", lambda state: state.has("Frozen Hillside Zone", player))
    connect_regions(world, player, "Menu", "Pipe Towers Zone", lambda state: state.has("Pipe Towers Zone", player))
    connect_regions(world, player, "Menu", "Forest Fortress Zone", lambda state: state.has("Forest Fortress Zone", player))
    connect_regions(world, player, "Menu", "Final Demo Zone", lambda state: state.has("Final Demo Zone", player))
    connect_regions(world, player, "Menu", "Haunted Heights Zone", lambda state: state.has("Haunted Heights Zone", player))
    connect_regions(world, player, "Menu", "Aerial Garden Zone", lambda state: state.has("Aerial Garden Zone", player))
    connect_regions(world, player, "Menu", "Azure Temple Zone", lambda state: state.has("Azure Temple Zone", player))
    connect_regions(world, player, "Menu", "Floral Field Zone", lambda state: state.has("Floral Field Zone", player))
    connect_regions(world, player, "Menu", "Toxic Plateau Zone", lambda state: state.has("Toxic Plateau Zone", player))
    connect_regions(world, player, "Menu", "Flooded Cove Zone", lambda state: state.has("Flooded Cove Zone", player))
    connect_regions(world, player, "Menu", "Cavern Fortress Zone", lambda state: state.has("Cavern Fortress Zone", player))
    connect_regions(world, player, "Menu", "Dusty Wasteland Zone", lambda state: state.has("Dusty Wasteland Zone", player))
    connect_regions(world, player, "Menu", "Magma Caves Zone", lambda state: state.has("Magma Caves Zone", player))
    connect_regions(world, player, "Menu", "Egg Satellite Zone", lambda state: state.has("Egg Satellite Zone", player))
    connect_regions(world, player, "Menu", "Black Hole Zone", lambda state: state.has("Black Hole Zone", player))
    connect_regions(world, player, "Menu", "Christmas Chime Zone", lambda state: state.has("Christmas Chime Zone", player))
    connect_regions(world, player, "Menu", "Dream Hill Zone", lambda state: state.has("Dream Hill Zone", player))
    connect_regions(world, player, "Menu", "Alpine Paradise Zone", lambda state: state.has("Alpine Paradise Zone", player))

    if options.match_maps:
        connect_regions(world, player, "Menu", "Jade Valley Zone", lambda state: state.has("Jade Valley Zone", player))
        connect_regions(world, player, "Menu", "Noxious Factory Zone", lambda state: state.has("Noxious Factory Zone", player))
        connect_regions(world, player, "Menu", "Tidal Palace Zone", lambda state: state.has("Tidal Palace Zone", player))
        connect_regions(world, player, "Menu", "Thunder Citadel Zone",lambda state: state.has("Thunder Citadel Zone", player))
        connect_regions(world, player, "Menu", "Desolate Twilight Zone", lambda state: state.has("Desolate Twilight Zone", player))
        connect_regions(world, player, "Menu", "Frigid Mountain Zone", lambda state: state.has("Frigid Mountain Zone", player))
        connect_regions(world, player, "Menu", "Orbital Hangar Zone", lambda state: state.has("Orbital Hangar Zone", player))
        connect_regions(world, player, "Menu", "Sapphire Falls Zone",lambda state: state.has("Sapphire Falls Zone", player))
        connect_regions(world, player, "Menu", "Diamond Blizzard Zone", lambda state: state.has("Diamond Blizzard Zone", player))
        connect_regions(world, player, "Menu", "Celestial Sanctuary Zone", lambda state: state.has("Celestial Sanctuary Zone", player))
        connect_regions(world, player, "Menu", "Frost Columns Zone", lambda state: state.has("Frost Columns Zone", player))
        connect_regions(world, player, "Menu", "Meadow Match Zone",lambda state: state.has("Meadow Match Zone" , player))
        connect_regions(world, player, "Menu", "Granite Lake Zone", lambda state: state.has("Granite Lake Zone", player))
        connect_regions(world, player, "Menu", "Summit Showdown Zone", lambda state: state.has("Summit Showdown Zone", player))
        connect_regions(world, player, "Menu", "Silver Shiver Zone", lambda state: state.has("Silver Shiver Zone", player))
        connect_regions(world, player, "Menu", "Uncharted Badlands Zone",lambda state: state.has("Uncharted Badlands Zone", player))
        connect_regions(world, player, "Menu", "Pristine Shores Zone",lambda state: state.has("Pristine Shores Zone" , player))
        connect_regions(world, player, "Menu", "Crystalline Heights Zone", lambda state: state.has("Crystalline Heights Zone", player))
        connect_regions(world, player, "Menu", "Starlit Warehouse Zone", lambda state: state.has("Starlit Warehouse Zone", player))
        connect_regions(world, player, "Menu", "Midnight Abyss Zone", lambda state: state.has("Midnight Abyss Zone", player))
        connect_regions(world, player, "Menu", "Airborne Temple Zone",lambda state: state.has("Airborne Temple Zone", player))

    if options.difficulty == 0:
        connect_regions(world, player, "Azure Temple Zone", "Azure Temple Club",
                        lambda state: state.has("Chaos Emerald", player, 7))
    else:
        connect_regions(world, player, "Azure Temple Zone", "Azure Temple Club")

    if options.oneup_sanity:
        if options.difficulty !=2:
            connect_regions(world, player, "Deep Sea Zone", "Deep Sea Fast Door",
                        lambda state: state.has("Chaos Emerald", player, 7))
        else:
            connect_regions(world, player, "Deep Sea Zone", "Deep Sea Fast Door")

    # TODO add emerald token logic and other zones
    if options.difficulty != 2:
        # Greenflower
        if options.difficulty == 0:
            rf.assign_rule("Greenflower (Act 1) Heart Emblem", "TAILS")

        rf.assign_rule("Greenflower (Act 2) Star Emblem", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
        rf.assign_rule("Greenflower (Act 2) Heart Emblem", "AMY")
        rf.assign_rule("Greenflower (Act 2) Diamond Emblem", "KNUCKLES | AMY+WIND")
        rf.assign_rule("Greenflower (Act 2) Spade Emblem", "SONIC | TAILS | KNUCKLES | METAL SONIC")
        rf.assign_rule("Greenflower (Act 2) Emerald Token - No Spin High on Ledge", "AMY | FANG")

        if options.oneup_sanity:
            rf.assign_rule("Greenflower (Act 1) Monitor - Highest Ledge","TAILS | KNUCKLES | WIND")
            rf.assign_rule("Greenflower (Act 2) Monitor - Breakable Floor Near Springs 1", "AMY | FANG")
            rf.assign_rule("Greenflower (Act 2) Monitor - Skylight in 2nd Cave", "TAILS | KNUCKLES")
            rf.assign_rule("Greenflower (Act 2) Monitor - Near Star Emblem 1", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")



            if options.difficulty == 0:
                rf.assign_rule("Greenflower (Act 2) Monitor - Waterfall Top Near Start","SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND") #Possible as amy but stupid
                rf.assign_rule("Greenflower (Act 2) Monitor - High Ledge After Final Cave", "TAILS | KNUCKLES") #badnik bounce

        if options.superring_sanity:
            if options.difficulty == 0:
                rf.assign_rule("Greenflower (Act 2) Monitor - Very High Alcove 1", "TAILS | KNUCKLES")
                rf.assign_rule("Greenflower (Act 2) Monitor - Very High Alcove 2", "TAILS | KNUCKLES")
                rf.assign_rule("Greenflower (Act 2) Monitor - Very High Alcove 3", "TAILS | KNUCKLES")
                rf.assign_rule("Greenflower (Act 2) Monitor - Very High Alcove 4", "TAILS | KNUCKLES")
                rf.assign_rule("Greenflower (Act 2) Monitor - Very High Alcove 5", "TAILS | KNUCKLES")
                rf.assign_rule("Greenflower (Act 2) Monitor - Very High Alcove 6", "TAILS | KNUCKLES")
                rf.assign_rule("Greenflower (Act 2) Monitor - Very High Alcove 7", "TAILS | KNUCKLES")
                rf.assign_rule("Greenflower (Act 2) Monitor - Very High Alcove 8", "TAILS | KNUCKLES")
            rf.assign_rule("Greenflower (Act 2) Monitor - Spin Path Red Springs", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")




        # Techno Hill


        rf.assign_rule("Techno Hill (Act 1) Heart Emblem", "TAILS")
        rf.assign_rule("Techno Hill (Act 1) Diamond Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Techno Hill (Act 1) Club Emblem", "KNUCKLES")
        rf.assign_rule("Techno Hill (Act 2) Star Emblem", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
        rf.assign_rule("Techno Hill (Act 2) Emerald Token - Knuckles Path Backtrack", "AMY")
        if options.difficulty == 0:
            rf.assign_rule("Techno Hill (Act 1) Spade Emblem", "ELEMENTAL")
            rf.assign_rule("Techno Hill (Act 2) Emerald Token - Deep in Slime", "ELEMENTAL")
            rf.assign_rule("Techno Hill (Act 1) Star Emblem", "TAILS | KNUCKLES")  # INTENDED SONIC PATH FOR THIS BTW

        if options.oneup_sanity:
            rf.assign_rule("Techno Hill (Act 1) Monitor - Spin Under Conveyor Belt Door", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Techno Hill (Act 1) Monitor - Knuckles Path Highest Ledge", "TAILS | KNUCKLES")
            rf.assign_rule("Techno Hill (Act 1) Monitor - Outside Pipe Room High Ledge", "TAILS | KNUCKLES")
            rf.assign_rule("Techno Hill (Act 2) Monitor - Knuckles Path Under Spiked Hallway","KNUCKLES")
            rf.assign_rule("Techno Hill (Act 2) Monitor - Egg Corp Deep in Slime", "ELEMENTAL | KNUCKLES | FANG")
            rf.assign_rule("Techno Hill (Act 2) Monitor - Near Amy Emerald Token", "AMY")
            rf.assign_rule("Techno Hill (Act 2) Monitor - Tall Pillar Outside Glass", "TAILS | KNUCKLES")#probably possible as sonic
            rf.assign_rule("Techno Hill (Act 2) Monitor - Behind Glass Piston Path", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")

            if options.difficulty == 0:
                rf.assign_rule("Techno Hill (Act 1) Monitor - High Ledge in Hole Near Start", "TAILS | KNUCKLES")#INTENDED SONIC PATH FOR THIS BTW
                rf.assign_rule("Techno Hill (Act 2) Monitor - High Ledge Outside 1","TAILS | KNUCKLES | FANG | WIND")  # or 7 emeralds
                rf.assign_rule("Techno Hill (Act 2) Monitor - Egg Corp Cavity Under Slime", "ELEMENTAL | KNUCKLES | FANG")
            #else:
            #    rf.assign_rule("Techno Hill (Act 2) Monitor - High Ledge Outside 1","TAILS | KNUCKLES | AMY | FANG | WIND")  # or 7 emeralds


        if options.superring_sanity:
            rf.assign_rule("Techno Hill (Act 1) Monitor - Knuckles Path Behind Pipe", "TAILS | KNUCKLES")
            rf.assign_rule("Techno Hill (Act 1) Monitor - Knuckles Path on Ledge", "TAILS | KNUCKLES")
            rf.assign_rule("Techno Hill (Act 1) Monitor - Knuckles Path High Ledge", "TAILS | KNUCKLES")
            rf.assign_rule("Techno Hill (Act 1) Monitor - Knuckles Path on Pipes", "TAILS | KNUCKLES")
            rf.assign_rule("Techno Hill (Act 1) Monitor - Knuckles Path in Slime", "SONIC+ELEMENTAL | TAILS | KNUCKLES | METAL SONIC+ELEMENTAL")


            rf.assign_rule("Techno Hill (Act 2) Monitor - Knuckles Path Exit 1", "KNUCKLES | AMY")
            rf.assign_rule("Techno Hill (Act 2) Monitor - Knuckles Path Exit 2", "KNUCKLES | AMY")
            rf.assign_rule("Techno Hill (Act 2) Monitor - Knuckles Path Metal Pillar", "KNUCKLES | AMY+WIND")
            rf.assign_rule("Techno Hill (Act 2) Monitor - Knuckles Path Before Diagonal Conveyors", "KNUCKLES")
            rf.assign_rule("Techno Hill (Act 2) Monitor - Before 2nd Checkpoint Breakable Wall L", "KNUCKLES | AMY")
            rf.assign_rule("Techno Hill (Act 2) Monitor - Before 2nd Checkpoint Breakable Wall R", "KNUCKLES | AMY")

            rf.assign_rule("Techno Hill (Act 2) Monitor - Behind Breakable Wall Near Start", "KNUCKLES | AMY")


            if options.difficulty == 0:
                rf.assign_rule("Techno Hill (Act 1) Monitor - Before End on Crates", "TAILS | KNUCKLES | AMY | FANG | WIND")#idk why this is here this is piss easy
                rf.assign_rule("Techno Hill (Act 2) Monitor - High Ledge Outside 2", "TAILS | KNUCKLES | FANG | WIND")
                rf.assign_rule("Techno Hill (Act 2) Monitor - High Ledge Outside 3", "TAILS | KNUCKLES | FANG | WIND")




        # Deep Sea
        rf.assign_rule("Deep Sea (Act 1) Star Emblem", "AMY")
        rf.assign_rule("Deep Sea (Act 1) Spade Emblem", "TAILS | KNUCKLES | METAL SONIC | WIND")
        rf.assign_rule("Deep Sea (Act 1) Emerald Token - Yellow Doors", "SONIC | TAILS | KNUCKLES | METAL SONIC")


        rf.assign_rule("Deep Sea (Act 2) Star Emblem", "AMY | FANG")
        rf.assign_rule("Deep Sea (Act 2) Spade Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Deep Sea (Act 2) Heart Emblem", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
        rf.assign_rule("Deep Sea (Act 2) Diamond Emblem", "KNUCKLES | AMY")
        rf.assign_rule("Deep Sea (Act 2) Club Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Deep Sea (Act 2) Emerald Token - Near Heart Emblem", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")



        rf.assign_rule("Deep Sea (Act 2) Emerald Token - No Spin Spring Turnaround", "AMY | FANG")
        if options.difficulty == 0:
            rf.assign_rule("Deep Sea (Act 1) Heart Emblem", "TAILS | KNUCKLES")
        if options.oneup_sanity:


            rf.assign_rule("Deep Sea (Act 1) Monitor - x:10304 y:-736", "TAILS | KNUCKLES | FANG | WIND")
            rf.assign_rule("Deep Sea (Act 1) Monitor - x:5088 y:11872", "TAILS | KNUCKLES | METAL SONIC | WIND")
            rf.assign_rule("Deep Sea (Act 1) Monitor - x:20000 y:15136", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")
            rf.assign_rule("Deep Sea (Act 1) Monitor - x:320 y:4544", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Deep Sea (Act 1) Monitor - x:17584 y:-5544", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Deep Sea (Act 1) Monitor - x:64 y:12224", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")

            #"Deep Sea (Act 1) Monitor - x:8640 y:3168" - maybe at least require wind for normal - have to check other emblems if so (Club emblem) (NAH)

            rf.assign_rule("Deep Sea (Act 2) Monitor - x:15104 y:6128", "SONIC | KNUCKLES")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:15104 y:6032", "SONIC | KNUCKLES")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:15104 y:6080", "SONIC | KNUCKLES")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:26848 y:11584", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:5776 y:10304", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:19264 y:-5888", "KNUCKLES | AMY")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:19072 y:-10816", "KNUCKLES | AMY")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:15808 y:2816", "TAILS | KNUCKLES")


            if options.difficulty == 0:
                rf.assign_rule("Deep Sea (Act 1) Monitor - x:11008 y:5696","TAILS | KNUCKLES")  # heart emblem club emblem opened bullshit
                rf.assign_rule("Deep Sea (Act 1) Monitor - x:10880 y:5568","TAILS | KNUCKLES")  # heart emblem club emblem opened bullshit
                rf.assign_rule("Deep Sea (Act 2) Monitor - x:9568 y:16992", "TAILS | KNUCKLES | FANG")
                rf.assign_rule("Deep Sea (Act 1) Monitor - x:3104 y:15520", "METAL SONIC")
                rf.assign_rule("Deep Sea (Act 1) Monitor - x:3296 y:15520","METAL SONIC")
            else:
                rf.assign_rule("Deep Sea (Act 1) Monitor - x:11008 y:5696","TAILS | KNUCKLES | WIND")  # heart emblem club emblem opened bullshit
                rf.assign_rule("Deep Sea (Act 1) Monitor - x:10880 y:5568","TAILS | KNUCKLES | WIND")  # heart emblem club emblem opened bullshit

        if options.superring_sanity:
            if options.difficulty == 0:
                rf.assign_rule("Deep Sea (Act 1) Monitor - x:2800 y:8368", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:7840 y:96", "AMY | FANG")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:10528 y:5232", "AMY | FANG")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:7680 y:3456", "AMY | FANG")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:7680 y:3328", "AMY | FANG")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:9120 y:3680", "AMY | FANG")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:7776 y:3744", "AMY | FANG")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:7776 y:3680", "AMY | FANG")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:9120 y:3744", "AMY | FANG")

        # Castle Eggman
        rf.assign_rule("Castle Eggman (Act 1) Star Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Castle Eggman (Act 2) Diamond Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Castle Eggman (Act 2) Club Emblem", "TAILS | KNUCKLES | FANG | WIND")
        if options.oneup_sanity:
            rf.assign_rule("Castle Eggman (Act 2) Monitor - x:0 y:-21760", "TAILS | KNUCKLES")
            rf.assign_rule("Castle Eggman (Act 2) Monitor - x:2112 y:-320", "TAILS | KNUCKLES | AMY")
            rf.assign_rule("Castle Eggman (Act 2) Monitor - x:3072 y:-16128", "TAILS | KNUCKLES")
            rf.assign_rule("Castle Eggman (Act 2) Monitor - x:12416 y:768", "TAILS | KNUCKLES | WIND")


        if options.superring_sanity:
            rf.assign_rule("Castle Eggman (Act 1) Monitor - x:5280 y:-6496", "TAILS | KNUCKLES")
            rf.assign_rule("Castle Eggman (Act 1) Monitor - x:5472 y:-6496", "TAILS | KNUCKLES")
            if options.difficulty == 0:
                rf.assign_rule("Castle Eggman (Act 2) Monitor - x:-544 y:-1328", "TAILS | KNUCKLES | FANG | METAL SONIC | WIND")
                rf.assign_rule("Castle Eggman (Act 2) Monitor - x:-544 y:-1232", "TAILS | KNUCKLES | FANG | METAL SONIC | WIND")
            else:
                rf.assign_rule("Castle Eggman (Act 2) Monitor - x:-544 y:-1328","SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")
                rf.assign_rule("Castle Eggman (Act 2) Monitor - x:-544 y:-1232","SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")




        #"Castle Eggman (Act 2) Monitor - x:-3584 y:-14720" "directly above another monitor >:("

        # Arid Canyon
        rf.assign_rule("Arid Canyon (Act 1) Star Emblem", "TAILS | KNUCKLES | AMY")
        rf.assign_rule("Arid Canyon (Act 1) Club Emblem", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")

        rf.assign_rule("Arid Canyon (Act 2) Spade Emblem", "AMY | FANG")

        rf.assign_rule("Arid Canyon (Act 2) Diamond Emblem", "FANG")
        rf.assign_rule("Arid Canyon (Act 2) Club Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Arid Canyon (Act 1) Emerald Token - Behind Wall and Spikes", "AMY")
        rf.assign_rule("Arid Canyon (Act 2) Emerald Token - Left No Spin Path Minecarts", "AMY | FANG")
        rf.assign_rule("Arid Canyon (Act 2) Emerald Token - Knuckles Dark Path Around Wall", "TAILS | KNUCKLES | AMY+WIND")
        if options.difficulty == 0:
            rf.assign_rule("Arid Canyon (Act 2) Star Emblem", "AMY | FANG | TAILS | KNUCKLES")#possible as sonic by fucky jump
            rf.assign_rule("Arid Canyon (Act 2) Heart Emblem", "KNUCKLES")#TODO the monitor near here needs a logic update as well
        if options.oneup_sanity:
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:5312 y:-5472", "SONIC | TAILS | KNUCKLES | METAL SONIC | WIND")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:-6592 y:-2896", "TAILS | KNUCKLES | AMY+WIND")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:2816 y:-992", "AMY")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:-5184 y:14912", "TAILS | KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:-11200 y:992", "TAILS | KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:4928 y:-21312", "SONIC | TAILS | KNUCKLES | METAL SONIC | WIND")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:6720 y:-22816","SONIC | TAILS | KNUCKLES | METAL SONIC | WIND")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:3888 y:-16448","SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-10144 y:-4640", "KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:160 y:-10784", "TAILS | KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:2240 y:-15456", "KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-7088 y:-13824", "KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-4992 y:-7744", "TAILS | KNUCKLES")
            if options.difficulty == 0:
                rf.assign_rule("Arid Canyon (Act 2) Monitor - x:2752 y:-9776","TAILS | KNUCKLES | AMY | FANG")
                rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-1408 y:-14976", "TAILS | KNUCKLES | AMY | FANG")

        if options.superring_sanity:
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:3568 y:-1824", "TAILS | KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:3904 y:544", "TAILS | KNUCKLES | METAL SONIC | WIND")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:-7360 y:-2240", "SONIC+WIND | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:3568 y:-1696", "TAILS | KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:-7360 y:-2368", "SONIC+WIND | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:704 y:-12224", "TAILS | KNUCKLES | AMY | FANG | METAL SONIC | WIND")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:3888 y:-16096", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:3888 y:-16800", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-1776 y:-23296", "TAILS | KNUCKLES | AMY | FANG | WIND")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:2176 y:-15456", "KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-7088 y:-13760", "KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-7088 y:-13888", "KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:2304 y:-15456", "KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:6976 y:-22208", "KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:6976 y:-22144", "KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:4928 y:-15488", "KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-4720 y:-17344", "TAILS | KNUCKLES | AMY | FANG")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-3136 y:-17376", "AMY | FANG")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-5008 y:-17344", "TAILS | KNUCKLES | AMY | FANG")
            if options.difficulty == 0:
                rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-768 y:-16512", "TAILS | KNUCKLES | AMY | FANG")


        # Red Volcano
        #fang cant get club emblem
        rf.assign_rule("Red Volcano (Act 1) Club Emblem", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
        rf.assign_rule("Red Volcano (Act 1) Spade Emblem", "TAILS")
        rf.assign_rule("Red Volcano (Act 1) Emerald Token - First Outside Area", "TAILS | KNUCKLES | METAL SONIC | WIND")
        rf.assign_rule("Red Volcano (Act 1) Emerald Token - Hidden Ledge Near 4th Checkpoint", "TAILS | FANG | WIND")
        #no 1up rules in rvz
        if options.superring_sanity:
            rf.assign_rule("Red Volcano (Act 1) Monitor - x:22304 y:8192", "SONIC | TAILS | KNUCKLES | METAL SONIC | WIND")

        # Egg Rock
        rf.assign_rule("Egg Rock (Act 1) Spade Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Egg Rock (Act 1) Emerald Token - Moving Platforms", "SONIC | TAILS | KNUCKLES | METAL SONIC")
        rf.assign_rule("Egg Rock (Act 2) Heart Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Egg Rock (Act 2) Club Emblem", "SONIC | TAILS | KNUCKLES | METAL SONIC")
        if options.difficulty == 0:
            rf.assign_rule("Egg Rock (Act 1) Heart Emblem", "TAILS")
        else:
            rf.assign_rule("Egg Rock (Act 1) Heart Emblem", "TAILS | KNUCKLES")

        if options.oneup_sanity:

            rf.assign_rule("Egg Rock (Act 1) Monitor - x:-64 y:-10848", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Egg Rock (Act 1) Monitor - x:-5184 y:-11264", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Egg Rock (Act 1) Monitor - x:6144 y:-2112", "TAILS | FANG")

            rf.assign_rule("Egg Rock (Act 2) Monitor - x:-12032 y:7040", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Egg Rock (Act 2) Monitor - x:-12864 y:7040", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            if options.difficulty == 0:
                rf.assign_rule("Egg Rock (Act 2) Monitor - Top of Turret Room", "TAILS | KNUCKLES | FANG")
            else:
                rf.assign_rule("Egg Rock (Act 2) Monitor - Top of Turret Room", "TAILS | KNUCKLES | FANG | METAL SONIC")

        if options.superring_sanity:
            rf.assign_rule("Egg Rock (Act 1) Monitor - x:384 y:-9952" , "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Egg Rock (Act 1) Monitor - x:384 y:-10912", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Egg Rock (Act 1) Monitor - x:-5376 y:-9760", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Egg Rock (Act 1) Monitor - x:1600 y:-5120", "KNUCKLES")

        # Black Core - Nothing until rolling/objects are locked

        # Frozen Hillside/ other bonus stages go here
        rf.assign_rule("Frozen Hillside Diamond Emblem", "TAILS | KNUCKLES | WIND")
        rf.assign_rule("Frozen Hillside Heart Emblem", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
        rf.assign_rule("Frozen Hillside Star Emblem", "SONIC | TAILS | KNUCKLES | METAL SONIC")
        if options.difficulty == 0:
            rf.assign_rule("Frozen Hillside Club Emblem", "SONIC+WIND | TAILS | KNUCKLES | AMY+WIND | METAL SONIC+WIND")
        else:
            rf.assign_rule("Frozen Hillside Club Emblem", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
        if options.oneup_sanity:
            rf.assign_rule("Frozen Hillside Monitor - First Snow Field Behind Ice", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
            if options.difficulty == 0:
                rf.assign_rule("Frozen Hillside Monitor - Final Path Ledge Behind Ice", "SONIC+WIND | TAILS | KNUCKLES | AMY+WIND | METAL SONIC+WIND")#remove for hard
            else:
                rf.assign_rule("Frozen Hillside Monitor - Final Path Ledge Behind Ice", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")



        #pipe towers
        rf.assign_rule("Pipe Towers Star Emblem", "TAILS | FANG | WIND")
        rf.assign_rule("Pipe Towers Spade Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Pipe Towers Heart Emblem", "KNUCKLES")

        if options.difficulty == 0:
            if options.oneup_sanity:
                rf.assign_rule("Pipe Towers ? Block - Ceiling Hole Near Flowing Water", "TAILS")



        #none for forest fortress (yet)
        rf.assign_rule("Forest Fortress Star Emblem", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
        rf.assign_rule("Forest Fortress Heart Emblem", "SONIC | TAILS | KNUCKLES | METAL SONIC")
        if options.oneup_sanity:
            rf.assign_rule("Forest Fortress Monitor - x:5824 y:8368", "KNUCKLES")
            rf.assign_rule("Forest Fortress Monitor - x:1024 y:-6528", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")

        if options.superring_sanity:
            rf.assign_rule("Forest Fortress Monitor - x:6816 y:6656", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
            rf.assign_rule("Forest Fortress Monitor - x:6776 y:6576", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")

        rf.assign_rule("Final Demo Emerald Token - Greenflower (Act 1) Breakable Wall Near Bridge", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
        rf.assign_rule("Final Demo Emerald Token - Techno Hill (Act 1) Alt Path Fans","SONIC | TAILS | KNUCKLES | METAL SONIC")

        if options.oneup_sanity:
            rf.assign_rule("Final Demo Monitor - Greenflower (Act 2) Skylight in 2nd Cave", "TAILS | KNUCKLES")
            rf.assign_rule("Final Demo Monitor - Castle Eggman (Act 1) High Ledge Near Start", "TAILS | KNUCKLES")
            if options.difficulty == 0:
                rf.assign_rule("Final Demo Monitor - Red Volcano (Act 1) Start", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC")
                rf.assign_rule("Final Demo Monitor - Red Volcano (Act 1) Across Broken Bridge 1", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC")
                rf.assign_rule("Final Demo Monitor - Red Volcano (Act 1) Cave Near Falling Platforms", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC")



        if options.superring_sanity:
            rf.assign_rule("Final Demo Monitor - x:-26848 y:-30720", "TAILS")
            rf.assign_rule("Final Demo Monitor - x:-26872 y:-30672", "TAILS")
            rf.assign_rule("Final Demo Monitor - x:-26824 y:-30672", "TAILS")

            rf.assign_rule("Final Demo Monitor - x:-3200 y:-18496", "TAILS | KNUCKLES")
            rf.assign_rule("Final Demo Monitor - x:-3136 y:-18496", "TAILS | KNUCKLES")
            rf.assign_rule("Final Demo Monitor - x:-3136 y:-18560", "TAILS | KNUCKLES")
            rf.assign_rule("Final Demo Monitor - x:-3136 y:-18624", "TAILS | KNUCKLES")
            rf.assign_rule("Final Demo Monitor - x:-3200 y:-18624", "TAILS | KNUCKLES")
            rf.assign_rule("Final Demo Monitor - x:-3264 y:-18624", "TAILS | KNUCKLES")
            rf.assign_rule("Final Demo Monitor - x:-3264 y:-18560", "TAILS | KNUCKLES")
            rf.assign_rule("Final Demo Monitor - x:-3264 y:-18496", "TAILS | KNUCKLES")
            if options.difficulty == 0:
                rf.assign_rule("Final Demo Monitor - x:15792 y:17664", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC")
                rf.assign_rule("Final Demo Monitor - x:432 y:28416", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC")
                rf.assign_rule("Final Demo Monitor - x:8016 y:26656", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC")










        # haunted heights
        rf.assign_rule("Haunted Heights Star Emblem", "FANG")
        rf.assign_rule("Haunted Heights Spade Emblem", "TAILS | KNUCKLES | FANG")
        rf.assign_rule("Haunted Heights Diamond Emblem", "KNUCKLES")
        rf.assign_rule("Haunted Heights Club Emblem", "KNUCKLES & ELEMENTAL")
        #heart emblem bullshit as knuckles
        if options.oneup_sanity:
            rf.assign_rule("Haunted Heights Monitor - x:1408 y:18112", "SONIC | TAILS | METAL SONIC")
            rf.assign_rule("Haunted Heights Monitor - x:4288 y:12240", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - x:6080 y:11872", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - x:6080 y:11872", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - x:-7712 y:18400", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | FLAME") #add amy+wind on hard


            rf.assign_rule("Haunted Heights Monitor - x:7648 y:24160", "FANG")
            rf.assign_rule("Haunted Heights Monitor - x:-3008 y:20720", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - x:1792 y:2656", "TAILS | KNUCKLES | FANG") #techincally possible with wind maybe
            rf.assign_rule("Haunted Heights Monitor - x:8254 y:11910", "KNUCKLES | FANG | ELEMENTAL")

        if options.superring_sanity:
            rf.assign_rule("Haunted Heights Monitor - x:2848 y:12704", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - x:1056 y:16192", "SONIC | TAILS | METAL SONIC")
            rf.assign_rule("Haunted Heights Monitor - x:6240 y:21504", "AMY | FANG")
            rf.assign_rule("Haunted Heights Monitor - x:4976 y:23376", "SONIC | TAILS | METAL SONIC")
            rf.assign_rule("Haunted Heights Monitor - x:7360 y:17952", "FANG")
            rf.assign_rule("Haunted Heights Monitor - x:5376 y:20736", "AMY | FANG")
            if options.difficulty == 0:
                rf.assign_rule("Haunted Heights Monitor - x:3520 y:20224", "AMY")
            else:
                rf.assign_rule("Haunted Heights Monitor - x:3520 y:20224", "AMY | FANG")


        if options.difficulty == 0:
            rf.assign_rule("Aerial Garden Club Emblem", "TAILS | METAL SONIC") # easy logic
            rf.assign_rule("Aerial Garden Diamond Emblem", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Spade Emblem", "FANG & LIGHTNING")
            rf.assign_rule("Aerial Garden Emerald Token - Diamond Emblem 1", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Emerald Token - Diamond Emblem 2", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Emerald Token - Diamond Emblem 3", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Emerald Token - Diamond Emblem 4", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Heart Emblem", "TAILS | METAL SONIC") # easy
            if options.time_emblems:
                rf.assign_rule("Aerial Garden Time Emblem", "TAILS | METAL SONIC | LIGHTNING") #BS as sonic
            if options.ring_emblems:
                rf.assign_rule("Aerial Garden Ring Emblem", "TAILS | METAL SONIC | LIGHTNING") #BS as sonic
        else:
            rf.assign_rule("Aerial Garden Spade Emblem", "FANG")



        if options.oneup_sanity:
            rf.assign_rule("Aerial Garden Monitor - x:-8000 y:-5568", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Aerial Garden Monitor - x:-960 y:9792", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Aerial Garden Monitor - x:-1280 y:-17088", "SONIC | TAILS | KNUCKLES | METAL SONIC")

            if options.difficulty == 0:
                rf.assign_rule("Aerial Garden Monitor - x:-13920 y:5120", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:10080 y:-9312", "TAILS | KNUCKLES | METAL SONIC | LIGHTNING")
                rf.assign_rule("Aerial Garden Monitor - x:-4224 y:10816", "TAILS | METAL SONIC | LIGHTNING")
                rf.assign_rule("Aerial Garden Monitor - x:-14528 y:-5632", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8832 y:12544", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8832 y:12416", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8960 y:12416", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-13600 y:864", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8896 y:-8128", "TAILS | KNUCKLES | METAL SONIC | LIGHTNING")
                rf.assign_rule("Aerial Garden Monitor - x:-1184 y:-10592", "TAILS | KNUCKLES")

            else:
                rf.assign_rule("Aerial Garden Monitor - x:-1184 y:-10592", "TAILS | KNUCKLES | AMY & LIGHTNING | FANG")
        if options.superring_sanity:
            rf.assign_rule("Aerial Garden Monitor - x:-960 y:9984", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Aerial Garden Monitor - x:-4288 y:13248", "TAILS | KNUCKLES")
            rf.assign_rule("Aerial Garden Monitor - x:-960 y:9920", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            if options.difficulty == 0:
                rf.assign_rule("Aerial Garden Monitor - x:-13920 y:5056", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-13920 y:5184", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8896 y:12416", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8832 y:12480", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8896 y:12544", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8960 y:12480", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-9024 y:12416", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8960 y:12352", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8832 y:12352", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8768 y:12416", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8768 y:12544", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8832 y:12608", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-14176 y:-9504", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-15168 y:-8768", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8960 y:12608", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-14816 y:1888", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-10368 y:-8224", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-10336 y:-8256", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-7424 y:-8224", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-7456 y:-8256", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8960 y:-8128", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-8832 y:-8128", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - x:-9024 y:12544", "TAILS | KNUCKLES | METAL SONIC")


        rf.assign_rule("Azure Temple Star Emblem", "TAILS | KNUCKLES+BUBBLE")
        rf.assign_rule("Azure Temple Spade Emblem", "TAILS")#knuckles+bubble on hard
        rf.assign_rule("Azure Temple Club Emblem", "ARMAGEDDON")
        if options.difficulty == 0:
            if options.time_emblems:
                rf.assign_rule("Azure Temple Time Emblem", "TAILS | METAL SONIC")
            if options.ring_emblems:
                rf.assign_rule("Azure Temple Ring Emblem","TAILS/METAL SONIC & FORCE/BUBBLE | KNUCKLES+BUBBLE")

            # easy version


        if options.oneup_sanity:
            rf.assign_rule("Azure Temple Monitor - x:512 y:14016", "TAILS | KNUCKLES")
            rf.assign_rule("Azure Temple Monitor - x:-2528 y:7296", "TAILS | KNUCKLES & BUBBLE")
            rf.assign_rule("Azure Temple Monitor - x:-4192 y:21344","ARMAGEDDON")
            rf.assign_rule("Azure Temple Monitor - x:-4192 y:21280","ARMAGEDDON")
            rf.assign_rule("Azure Temple Monitor - x:-4192 y:21408","ARMAGEDDON")
            rf.assign_rule("Azure Temple Monitor - x:4160 y:12384", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            if options.difficulty == 0:
                rf.assign_rule("Azure Temple Monitor - x:-32 y:6688", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:1440 y:14688", "TAILS | KNUCKLES+BUBBLE | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-2272 y:12864", "TAILS | KNUCKLES+BUBBLE | FANG")
                rf.assign_rule("Azure Temple Monitor - x:-3232 y:14112", "TAILS | KNUCKLES | FANG")
                rf.assign_rule("Azure Temple Monitor - x:3648 y:25888", "TAILS | KNUCKLES | FANG")

            else:

                rf.assign_rule("Azure Temple Monitor - x:1856 y:9952", "SONIC | TAILS | BUBBLE | AMY | FANG | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-2272 y:12864","TAILS | KNUCKLES+BUBBLE | AMY+BUBBLE | FANG")
                rf.assign_rule("Azure Temple Monitor - x:-3232 y:14112", "TAILS | KNUCKLES | AMY+BUBBLE | FANG")
                rf.assign_rule("Azure Temple Monitor - x:3648 y:25888", "TAILS | KNUCKLES | AMY+BUBBLE | FANG")

        if options.superring_sanity:
            rf.assign_rule("Azure Temple Monitor - x:-928 y:8256", "KNUCKLES | AMY")

            #rf.assign_rule("Azure Temple Monitor - x:1856 y:9952", "SONIC | TAILS | BUBBLE | AMY | FANG | METAL SONIC")
            #rf.assign_rule("Azure Temple Monitor - x:1856 y:9952", "SONIC | TAILS | BUBBLE | AMY | FANG | METAL SONIC")
            #rf.assign_rule("Azure Temple Monitor - x:1856 y:9952", "SONIC | TAILS | BUBBLE | AMY | FANG | METAL SONIC")
            #rf.assign_rule("Azure Temple Monitor - x:1856 y:9952", "SONIC | TAILS | BUBBLE | AMY | FANG | METAL SONIC")
            #rf.assign_rule("Azure Temple Monitor - x:1856 y:9952", "SONIC | TAILS | BUBBLE | AMY | FANG | METAL SONIC")
            rf.assign_rule("Azure Temple Monitor - x:2848 y:9312", "SONIC | TAILS | AMY | FANG | METAL SONIC | BUBBLE")
            rf.assign_rule("Azure Temple Monitor - x:512 y:13952", "TAILS | KNUCKLES")
            rf.assign_rule("Azure Temple Monitor - x:2752 y:11008", "SONIC | TAILS | AMY | FANG | METAL SONIC | BUBBLE")
            rf.assign_rule("Azure Temple Monitor - x:-1184 y:11104", "KNUCKLES")
            rf.assign_rule("Azure Temple Monitor - x:672 y:12544", "TAILS | KNUCKLES | BUBBLE")
            rf.assign_rule("Azure Temple Monitor - x:224 y:12576", "TAILS | KNUCKLES | AMY | FANG | BUBBLE")
            rf.assign_rule("Azure Temple Monitor - x:512 y:14080", "TAILS | KNUCKLES")
            rf.assign_rule("Azure Temple Monitor - x:1248 y:14432", "SONIC | TAILS | AMY | FANG | METAL SONIC | BUBBLE")
            rf.assign_rule("Azure Temple Monitor - x:384 y:9568", "SONIC | TAILS | AMY | FANG | METAL SONIC | BUBBLE")
            rf.assign_rule("Azure Temple Monitor - x:320 y:9568", "SONIC | TAILS | AMY | FANG | METAL SONIC | BUBBLE")
            rf.assign_rule("Azure Temple Monitor - x:3424 y:16528", "SONIC | TAILS | AMY | FANG | METAL SONIC | BUBBLE")
            rf.assign_rule("Azure Temple Monitor - x:-800 y:9312", "KNUCKLES")
            rf.assign_rule("Azure Temple Monitor - x:1952 y:11552", "KNUCKLES")
            rf.assign_rule("Azure Temple Monitor - x:6112 y:22560", "AMY | FANG")


            if options.difficulty == 0:
                rf.assign_rule("Azure Temple Monitor - x:-4000 y:10080","SONIC | TAILS | KNUCKLES+BUBBLE | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-3936 y:10080","SONIC | TAILS | KNUCKLES+BUBBLE | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-2272 y:10432","SONIC | TAILS | KNUCKLES+BUBBLE | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-2944 y:13344", "SONIC | TAILS | KNUCKLES+BUBBLE | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-3232 y:14048", "SONIC | TAILS | KNUCKLES+BUBBLE | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-3232 y:14176", "SONIC | TAILS | KNUCKLES+BUBBLE | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:4192 y:12320", "SONIC | TAILS | KNUCKLES+BUBBLE | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:4096 y:12416", "SONIC | TAILS | KNUCKLES+BUBBLE | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-4768 y:9600", "SONIC | TAILS | KNUCKLES+BUBBLE | METAL SONIC")

            else:
                rf.assign_rule("Azure Temple Monitor - x:-4000 y:10080","SONIC | TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-3936 y:10080", "SONIC | TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-3328 y:10752", "SONIC | TAILS | AMY | FANG | METAL SONIC | BUBBLE")
                rf.assign_rule("Azure Temple Monitor - x:-2272 y:10432","SONIC | TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-2944 y:13344", "SONIC | TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-3232 y:14048", "SONIC | TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-3232 y:14176", "SONIC | TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:4192 y:12320", "SONIC | TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:4096 y:12416", "SONIC | TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-4768 y:9600", "SONIC | TAILS | KNUCKLES | METAL SONIC")

        if options.superring_sanity and options.match_maps:
            rf.assign_rule("Noxious Factory Monitor - x:416 y:576", "TAILS | KNUCKLES | FANG")
            rf.assign_rule("Noxious Factory Monitor - x:736 y:768", "TAILS | KNUCKLES | FANG")
            rf.assign_rule("Noxious Factory Monitor - x:2112 y:-1920", "TAILS | KNUCKLES | FANG")
            rf.assign_rule("Noxious Factory Monitor - x:2496 y:3264", "TAILS | KNUCKLES | FANG | WIND")
            rf.assign_rule("Noxious Factory Monitor - x:2496 y:3136", "TAILS | KNUCKLES | FANG | WIND")
            rf.assign_rule("Noxious Factory Monitor - x:1440 y:-2336", "TAILS | KNUCKLES | FANG")

            rf.assign_rule("Tidal Palace Monitor - x:-2624 y:-3072", "TAILS")
            rf.assign_rule("Tidal Palace Monitor - x:-2912 y:-2976", "TAILS")
            rf.assign_rule("Tidal Palace Monitor - x:-2656 y:-2656", "TAILS")
            rf.assign_rule("Tidal Palace Monitor - x:1504 y:-96",  "TAILS | KNUCKLES")
            rf.assign_rule("Tidal Palace Monitor - x:1504 y:-224",  "TAILS | KNUCKLES")
            rf.assign_rule("Tidal Palace Monitor - x:-224 y:-672", "TAILS | KNUCKLES")
            rf.assign_rule("Tidal Palace Monitor - x:224 y:-672", "TAILS | KNUCKLES")

            rf.assign_rule("Desolate Twilight Monitor - x:-128 y:-2688", "TAILS | KNUCKLES")
            rf.assign_rule("Desolate Twilight Monitor - x:2913 y:212", "TAILS | KNUCKLES")
            rf.assign_rule("Desolate Twilight Monitor - x:2904 y:275", "TAILS | KNUCKLES")
            rf.assign_rule("Desolate Twilight Monitor - x:0 y:3584", "TAILS | KNUCKLES")

            rf.assign_rule("Diamond Blizzard Monitor - x:1296 y:400", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")
            rf.assign_rule("Diamond Blizzard Monitor - x:1904 y:-1040","SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")
            rf.assign_rule("Diamond Blizzard Monitor - x:608 y:-4544","TAILS | KNUCKLES | AMY+WIND | FANG+WIND")
            rf.assign_rule("Diamond Blizzard Monitor - x:928 y:-4544", "TAILS | KNUCKLES | AMY+WIND | FANG+WIND")

            rf.assign_rule("Frost Columns Monitor - x:0 y:-3520", "TAILS | KNUCKLES | AMY+WIND | FANG+WIND")
            rf.assign_rule("Frost Columns Monitor - x:-64 y:-3520", "TAILS | KNUCKLES | AMY+WIND | FANG+WIND")
            rf.assign_rule("Frost Columns Monitor - x:-1472 y:-96", "TAILS | KNUCKLES | AMY+WIND | FANG")
            rf.assign_rule("Frost Columns Monitor - x:-1472 y:-32", "TAILS | KNUCKLES | AMY+WIND | FANG")
            rf.assign_rule("Frost Columns Monitor - x:-3296 y:3200", "TAILS | KNUCKLES | AMY+WIND | FANG+WIND")
            rf.assign_rule("Frost Columns Monitor - x:-3328 y:3168", "TAILS | KNUCKLES | AMY+WIND | FANG+WIND")
            rf.assign_rule("Frost Columns Monitor - x:2112 y:-1088", "TAILS | AMY+WIND | FANG")
            rf.assign_rule("Frost Columns Monitor - x:2112 y:-1344", "TAILS | AMY+WIND | FANG")
            rf.assign_rule("Frost Columns Monitor - x:832 y:-1376", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")

            rf.assign_rule("Summit Showdown Monitor - x:-7456 y:-1696","SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")
            rf.assign_rule("Summit Showdown Monitor - x:-7008 y:-2144","SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")

            rf.assign_rule("Silver Shiver Monitor - x:-96 y:-2768","SONIC+WIND | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Silver Shiver Monitor - x:32 y:-2768", "SONIC+WIND | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Silver Shiver Monitor - x:15280 y:-26560", "TAILS | AMY | FANG | WIND")
            rf.assign_rule("Silver Shiver Monitor - x:15696 y:-26560", "TAILS | AMY | FANG | WIND")

            rf.assign_rule("Uncharted Badlands Monitor - x:1920 y:1024", "TAILS | KNUCKLES")

            rf.assign_rule("Pristine Shores Monitor - x:15808 y:12160", "TAILS | KNUCKLES")
            rf.assign_rule("Pristine Shores Monitor - x:14936 y:13448", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")
            rf.assign_rule("Pristine Shores Monitor - x:4160 y:7176", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Pristine Shores Monitor - x:9944 y:7616", "TAILS | KNUCKLES")


            if options.difficulty == 0:
                rf.assign_rule("Summit Showdown Monitor - x:5600 y:2208","SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")
                rf.assign_rule("Summit Showdown Monitor - x:5088 y:1696","SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")






        #special stages
        if options.difficulty == 0:
            rf.assign_rule("Flooded Cove Sun Emblem", "PARALOOP")
            rf.assign_rule("Magma Caves Moon Emblem", "PARALOOP")
            rf.assign_rule("Egg Satellite Sun Emblem", "PARALOOP")

        rf.assign_rule("Black Hole Sun Emblem", "PARALOOP")
        if options.ntime_emblems:
            rf.assign_rule("Magma Caves Time Emblem", "PARALOOP")
        if options.rank_emblems:
            rf.assign_rule("Egg Satellite A Rank Emblem", "EXTIME")
            rf.assign_rule("Black Hole A Rank Emblem", "EXTIME")


    if options.completion_type == 0:
        world.completion_condition[player] = lambda state: state.can_reach("Black Core Zone", 'Region', player)
    else:
        world.completion_condition[player] = lambda state: state.can_reach("Credits", 'Region', player)



class RuleFactory:

    world: MultiWorld
    player: int
    move_rando_bitvec: bool
    area_randomizer: bool
    capless: bool
    cannonless: bool
    moveless: bool

    token_table = {
        "SONIC": "Sonic",
        "TAILS": "Tails",
        "KNUCKLES": "Knuckles",
        "AMY": "Amy",
        "FANG": "Fang",
        "METAL SONIC": "Metal Sonic",
        # future concepts to implement
        #"SPIN": "Spindash",
        "WIND": "Whirlwind Shield",
        "ELEMENTAL": "Elemental Shield",
        "ARMAGEDDON": "Armageddon Shield",
        "BUBBLE": "Bubble Shield",
        "FLAME": "Flame Shield",
        "FORCE": "Force Shield",
        "LIGHTNING": "Lightning Shield",
        "PARALOOP": "Super Paraloop",
        "EXTIME" : "Extra Time",
        "EM1": "Green Chaos Emerald",
        "EM2": "Pink Chaos Emerald",
        "EM3": "Blue Chaos Emerald",
        "EM4": "Cyan Chaos Emerald",
        "EM5": "Yellow Chaos Emerald",
        "EM6": "Red Chaos Emerald",
        "EM7": "Gray Chaos Emerald"

        #"INVINCIBILITY": "Invincibility Monitors"
        # all other shields arent used in getting emblems directly
        # speed shoes, Attraction, Force, lightning, fire, bubble?
        # bubble might technically allow knuckles to get some emblem

    }

    class SRB2LogicException(Exception):
        pass

    def __init__(self, world, options: SRB2Options, player: int, move_rando_bitvec: int):
        self.world = world
        self.player = player
        #self.move_rando_bitvec = move_rando_bitvec
        #self.area_randomizer = options.area_rando > 0
        #self.capless = not options.strict_cap_requirements
        #self.cannonless = not options.strict_cannon_requirements
        #self.moveless = not options.strict_move_requirements

    def assign_rule(self, target_name: str, rule_expr: str):
        target = self.world.get_location(target_name, self.player) if target_name in location_table else self.world.get_entrance(target_name, self.player)
        cannon_name = "Cannon Unlock " + target_name.split(':')[0]
        try:
            rule = self.build_rule(rule_expr, cannon_name)
        except RuleFactory.SRB2LogicException as exception:
            raise RuleFactory.SRB2LogicException(
                f"Error generating rule for {target_name} using rule expression {rule_expr}: {exception}")
        if rule:
            set_rule(target, rule)

    def build_rule(self, rule_expr: str, cannon_name: str = '') -> Callable:
        expressions = rule_expr.split(" | ")
        rules = []
        for expression in expressions:
            or_clause = self.combine_and_clauses(expression, cannon_name)
            if or_clause is True:
                return None
            if or_clause is not False:
                rules.append(or_clause)
        if rules:
            if len(rules) == 1:
                return rules[0]
            else:
                return lambda state: any(rule(state) for rule in rules)
        else:
            return None

    def combine_and_clauses(self, rule_expr: str, cannon_name: str) -> Union[Callable, bool]:
        expressions = rule_expr.split(" & ")
        rules = []
        for expression in expressions:
            and_clause = self.make_lambda(expression, cannon_name)
            if and_clause is False:
                return False
            if and_clause is not True:
                rules.append(and_clause)
        if rules:
            if len(rules) == 1:
                return rules[0]
            return lambda state: all(rule(state) for rule in rules)
        else:
            return True

    def make_lambda(self, expression: str, cannon_name: str) -> Union[Callable, bool]:
        if '+' in expression:
            tokens = expression.split('+')
            items = set()
            for token in tokens:
                item = self.parse_token(token, cannon_name)
                if item is True:
                    continue
                if item is False:
                    return False
                items.add(item)
            if items:
                return lambda state: state.has_all(items, self.player)
            else:
                return True
        if '/' in expression:
            tokens = expression.split('/')
            items = set()
            for token in tokens:
                item = self.parse_token(token, cannon_name)
                if item is True:
                    return True
                if item is False:
                    continue
                items.add(item)
            if items:
                return lambda state: state.has_any(items, self.player)
            else:
                return False
        if '{{' in expression:
            return lambda state: state.can_reach(expression[2:-2], "Location", self.player)
        if '{' in expression:
            return lambda state: state.can_reach(expression[1:-1], "Region", self.player)
        item = self.parse_token(expression, cannon_name)
        if item in (True, False):
            return item
        return lambda state: state.has(item, self.player)

    def parse_token(self, token: str, cannon_name: str) -> Union[str, bool]:
        item = self.token_table.get(token, None)
        if not item:
            raise Exception(f"Invalid token: '{item}'")

        return item

