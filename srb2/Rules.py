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
    return dict(zip(keys, values))from typing import Callable, Union, Dict, Set

from BaseClasses import MultiWorld, CollectionState
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









#can_break_weak_walls
#can_break_strong_walls
#can_break_floors
#can_pound_springs
#can_climb_walls
#can_break_spikes
#can_fit_under_roll_gaps
#can_generate_speed (spindash)
#jump_height_includes_flying
#makes_hard_stages_easy

#jump_height
#hover_length





def set_rules(world, options: SRB2Options, player: int, area_connections: dict, move_rando_bitvec: int):

    #set up info array
    character_info = {'Sonic': [100,'weak_walls','spin_walls', 'fits_under_gaps','instant_speed',"midair_speed","roll","badnik_bounce",'can_use_shields'],
                      'Tails': [1500,'weak_walls','spin_walls', 'fits_under_gaps','instant_speed',"roll", 'free_flyer','makes_stages_easy','soft_jump',"badnik_bounce",'can_use_shields'],
                      'Knuckles': [80,'weak_walls','spin_walls','strong_walls','climbs_walls', 'fits_under_gaps','instant_speed',"roll",'low_grav',"midair_speed",'soft_jump',"badnik_bounce",'can_use_shields'],
                      'Amy': [115,'weak_walls','spin_walls', 'strong_walls', 'strong_floors', 'breaks_spikes', 'pounds_springs','soft_jump',"badnik_bounce",'can_use_shields'],
                      'Fang': [200,'strong_floors','lava_immune','soft_jump'],
                      'Metal Sonic': [100,'weak_walls','spin_walls', 'fits_under_gaps','instant_speed',"can_hover",'breaks_spikes',"roll",'soft_jump','makes_stages_easy',"badnik_bounce",'can_use_shields'],
                      }
#tag descriptions:
    #jump_height
    #weak_walls (fhz ice)
    #spin_walls (dsz2 heart emblem wall)
    #strong_walls (most knuckles paths)
    #stronger_walls (ACZ2 minecart doors)
    #strong_floors (most nospin paths)
    #roll (can get momentum from slopes)
    #fits_under_gaps (most spin path gaps)
    #instant_speed (usually spindash, used when you need speed for a slope jump or momentum with little space)
    #midair_speed (instant speed but can be done faster/ midair, ie sonic's thok)
    #free_flyer (jump height includes being able to fly or a double jump that can get under things)
    #climbs_walls (only needs 1 wall to get to the top)
    #wall_jump (can use 2 walls to scale them, ie mario's wall jump)
    #low_grav (cez2 diamond emblem bullshit)
    #breaks_spikes
    #pounds_springs (extra height from hitting springs, such as amy's hammer)
    #can_spindash (dsz2 spindash switches)
    #can_use_shields (for active shield abilities)
    #soft_jump (can stand on monitors/tnt barrels by jumping/using their ability)
    #can_stomp (elemental shield replacement)
    #can_skim_water
    #lava_immune
    #makes_stages_easy (forces hard stages to require this tag on easy logic difficulty)

    # Destination Format: LVL | AREA with LVL = LEVEL_x, AREA = Area as used in sm64 code
    # Cast to int to not rely on availability of SM64Levels enum. Will cause crash in MultiServer otherwise
    def char_needs_tags(state: CollectionState,tag_list,jump_height):
        for i in character_info:
            if state.has(i,player):
                if character_info[i][0] < jump_height:
                    continue
                if set(tag_list).issubset(character_info[i]):
                    return True
        return False


    rf = RuleFactory(world, options, player, move_rando_bitvec)

    connect_regions(world, player, "Menu", "Greenflower Zone 1", lambda state: state.has("Greenflower Zone", player) or state.has("Greenflower Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Greenflower Zone 2", lambda state: state.has("Greenflower Zone", player) or state.has("Greenflower Zone (Act 2)", player))
    connect_regions(world, player, "Menu", "Greenflower Zone 3", lambda state: state.has("Greenflower Zone", player) or state.has("Greenflower Zone (Act 3)", player))

    connect_regions(world, player, "Menu", "Techno Hill Zone 1", lambda state: state.has("Techno Hill Zone", player) or state.has("Techno Hill Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Techno Hill Zone 2", lambda state: state.has("Techno Hill Zone", player) or state.has("Techno Hill Zone (Act 2)", player))
    connect_regions(world, player, "Menu", "Techno Hill Zone 3", lambda state: state.has("Techno Hill Zone", player) or state.has("Techno Hill Zone (Act 3)", player))

    connect_regions(world, player, "Techno Hill Zone 2", "Techno Hill Zone 2 Main",lambda state: state.has("Buoyant Slime", player))

    connect_regions(world, player, "Menu", "Deep Sea Zone 1", lambda state: state.has("Deep Sea Zone", player) or state.has("Deep Sea Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Deep Sea Zone 2", lambda state: state.has("Deep Sea Zone", player) or state.has("Deep Sea Zone (Act 2)", player))
    connect_regions(world, player, "Menu", "Deep Sea Zone 3", lambda state: state.has("Deep Sea Zone", player) or state.has("Deep Sea Zone (Act 3)", player))

    connect_regions(world, player, "Menu", "Castle Eggman Zone 1", lambda state: state.has("Castle Eggman Zone", player) or state.has("Castle Eggman Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Castle Eggman Zone 2", lambda state: state.has("Castle Eggman Zone", player) or state.has("Castle Eggman Zone (Act 2)", player))
    connect_regions(world, player, "Menu", "Castle Eggman Zone 3", lambda state: state.has("Castle Eggman Zone", player) or state.has("Castle Eggman Zone (Act 3)", player))

    connect_regions(world, player, "Menu", "Arid Canyon Zone 1", lambda state: state.has("Arid Canyon Zone", player) or state.has("Arid Canyon Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Arid Canyon Zone 2", lambda state: state.has("Arid Canyon Zone", player) or state.has("Arid Canyon Zone (Act 2)", player))
    connect_regions(world, player, "Menu", "Arid Canyon Zone 3", lambda state: state.has("Arid Canyon Zone", player) or state.has("Arid Canyon Zone (Act 3)", player))

    connect_regions(world, player, "Menu", "Red Volcano Zone 1", lambda state: state.has("Red Volcano Zone", player) or state.has("Red Volcano Zone (Act 1)", player))

    connect_regions(world, player, "Menu", "Egg Rock Zone 1", lambda state: state.has("Egg Rock Zone", player) or state.has("Egg Rock Zone (Act 1)", player))
    connect_regions(world, player, "Menu", "Egg Rock Zone 2", lambda state: state.has("Egg Rock Zone", player) or state.has("Egg Rock Zone (Act 2)", player))

    if options.bcz_emblem_percent==0:
        connect_regions(world, player, "Menu", "Black Core Zone 1", lambda state: state.has("Black Core Zone", player) or state.has("Black Core Zone (Act 1)", player))
        connect_regions(world, player, "Menu", "Black Core Zone 2", lambda state: state.has("Black Core Zone", player) or state.has("Black Core Zone (Act 2)", player))
        connect_regions(world, player, "Menu", "Black Core Zone 3", lambda state: state.has("Black Core Zone", player) or state.has("Black Core Zone (Act 3)", player))
    else:
        connect_regions(world, player, "Menu", "Black Core Zone 1", lambda state: state.has("Emblem", player, options.bcz_emblem_percent))
        connect_regions(world, player, "Menu", "Black Core Zone 2", lambda state: state.has("Emblem", player, options.bcz_emblem_percent))
        connect_regions(world, player, "Menu", "Black Core Zone 3", lambda state: state.has("Emblem", player, options.bcz_emblem_percent))

    connect_regions(world, player, "Black Core Zone 3", "Credits",lambda state: state.count("Chaos Emerald", player) > 6)

#todo re add credits as a region
    #fix dsz and atz chaos emerald locations
    #all time/ring emblems must use can_reach(zone clear)

    connect_regions(world, player, "Menu", "Frozen Hillside Zone", lambda state: state.has("Frozen Hillside Zone", player))
    connect_regions(world, player, "Menu", "Pipe Towers Zone", lambda state: state.has("Pipe Towers Zone", player))
    connect_regions(world, player, "Menu", "Forest Fortress Zone", lambda state: state.has("Forest Fortress Zone", player))
    connect_regions(world, player, "Menu", "Final Demo Zone", lambda state: state.has("Final Demo Zone", player))
    connect_regions(world, player, "Menu", "Haunted Heights Zone", lambda state: state.has("Haunted Heights Zone", player))
    connect_regions(world, player, "Menu", "Aerial Garden Zone", lambda state: state.has("Aerial Garden Zone", player))
    connect_regions(world, player, "Menu", "Azure Temple Zone", lambda state: state.has("Azure Temple Zone", player))
    if options.nights_maps:
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


        connect_regions(world, player, "Menu", "Alpine Paradise Zone 1", lambda state: state.has("Alpine Paradise Zone", player) or state.has("Alpine Paradise Zone (Act 1)", player))
        connect_regions(world, player, "Menu", "Alpine Paradise Zone 2",lambda state: state.has("Alpine Paradise Zone", player) or state.has("Alpine Paradise Zone (Act 2)", player))

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


    # TODO add emerald token logic and other zones
    if options.difficulty != 2:
        # Greenflower
        if options.difficulty == 0:
            add_rule(world.get_location("Greenflower (Act 1) Heart Emblem", player),
                     lambda state: char_needs_tags(state, [], 500))#badnik bounce
            add_rule(world.get_location("Greenflower (Act 1) Clear", player),
                     lambda state: state.has("Yellow Springs", player) or
                                   char_needs_tags(state, [], 150) or
                                   char_needs_tags(state, ['climbs_walls'], -1) or
                                   (char_needs_tags(state, ["can_use_shields"], 100) and state.has("Whirlwind Shield",player)))
        else:

            add_rule(world.get_location("Greenflower (Act 1) Clear", player),
                 lambda state: state.has("Yellow Springs",player) or
                        char_needs_tags(state, [], 150) or
                        char_needs_tags(state, ['climbs_walls'], -1) or
                        (char_needs_tags(state, ["can_use_shields"], 100) and state.has("Whirlwind Shield",player))or
                        char_needs_tags(state, ['instant_speed'], 100))

        add_rule(world.get_location("Greenflower (Act 1) Emerald Token - Midair Top Path", player),
                 lambda state: state.has("Yellow Springs",player) or
                               char_needs_tags(state, [], 400) or
                                char_needs_tags(state, ["can_hover"], -1))


        add_rule(world.get_location("Greenflower (Act 1) Club Emblem", player),
                 lambda state: char_needs_tags(state,['spin_walls'],-1))#probably needs yellow springs

        add_rule(world.get_location("Greenflower (Act 1) Emerald Token - Breakable Wall Near Bridge", player),
                 lambda state: char_needs_tags(state,['spin_walls'],-1))

        add_rule(world.get_location("Greenflower (Act 2) Clear", player),
                 lambda state: (state.has("Yellow Springs", player) and state.has("Red Springs", player)) or
                               (state.has("Red Springs", player) and char_needs_tags(state, [], 250)) or
                               (state.has("Yellow Springs", player) and (char_needs_tags(state, [], 250)) or
                               char_needs_tags(state, ["wall_jump"], -1)) or
                               char_needs_tags(state, [], 1200) or
                               char_needs_tags(state, ['climbs_walls'], -1))
        #fuck this is going to get messy



        add_rule(world.get_location("Greenflower (Act 2) Star Emblem", player),
                 lambda state: (state.has("Yellow Springs", player) and state.has("Red Springs", player) and char_needs_tags(state,['spin_walls'],-1)) or
                               (state.has("Red Springs", player) or (state.has("Yellow Springs", player) and char_needs_tags(state, ['spin_walls'], 250))) or
                                char_needs_tags(state, ["wall_jump",'spin_walls'], -1) or
                                char_needs_tags(state, ['spin_walls'], 1200) or
                                char_needs_tags(state, ['climbs_walls','spin_walls'], -1))
        add_rule(world.get_location("Greenflower (Act 2) Spade Emblem", player),
                 lambda state: (state.has("Yellow Springs", player) and state.has("Red Springs", player) and char_needs_tags(state,['fits_under_gaps'],-1)) or
                               (state.has("Red Springs", player) and char_needs_tags(state, ['fits_under_gaps'], 250)) or
                               (state.has("Yellow Springs", player) and (char_needs_tags(state, ['fits_under_gaps'], 250))) or
                               char_needs_tags(state, ["wall_jump",'fits_under_gaps'], -1) or
                               char_needs_tags(state, ['fits_under_gaps'], 1200) or
                               char_needs_tags(state, ['climbs_walls','fits_under_gaps'], -1))
        add_rule(world.get_location("Greenflower (Act 2) Heart Emblem", player),
                 lambda state: (state.has("Yellow Springs", player) and state.has("Red Springs",player) and char_needs_tags(state, ['strong_walls', 'strong_floors', "pounds_springs", "breaks_spikes"], -1)) or
                               (state.has("Red Springs", player) or (state.has("Yellow Springs", player) and char_needs_tags(state, ['strong_walls', 'strong_floors', "pounds_springs", "breaks_spikes"], 250))) or
                               char_needs_tags(state, ['strong_walls', 'strong_floors', "wall_jump"], -1) or
                               char_needs_tags(state, ['strong_walls', 'strong_floors'], 1200) or
                               char_needs_tags(state, ['strong_walls', 'strong_floors', "climbs_walls"], -1))
        add_rule(world.get_location("Greenflower (Act 2) Diamond Emblem", player),
                 lambda state: (state.has("Yellow Springs", player) and state.has("Red Springs",player) and (char_needs_tags(state,['strong_walls',"can_use_shields"],-1) and state.has("Whirlwind Shield",player))) or
                               (state.has("Red Springs", player) or state.has("Yellow Springs", player) and (char_needs_tags(state,['strong_walls',"can_use_shields"],250) and state.has("Whirlwind Shield",player))) or
                               char_needs_tags(state, ['strong_walls', "wall_jump"], -1) or
                               char_needs_tags(state, ['strong_walls'], 1200) or
                               char_needs_tags(state, ['strong_walls', "climbs_walls"], -1))
        add_rule(world.get_location("Greenflower (Act 2) Club Emblem", player),
                 lambda state: (state.has("Yellow Springs", player) and state.has("Red Springs", player) or
                                char_needs_tags(state, [], 1200) or
                                char_needs_tags(state, ["climbs_walls"], -1)))
        add_rule(world.get_location("Greenflower (Act 2) Emerald Token - No Spin High on Ledge", player),
                 lambda state: (state.has("Yellow Springs", player) and state.has("Red Springs",player) and (char_needs_tags(state, ['strong_floors', "pounds_springs", "breaks_spikes"], -1) or char_needs_tags(state, ['strong_floors'], 150))) or
                               (state.has("Red Springs", player) or (state.has("Yellow Springs", player) and char_needs_tags(state,['strong_floors'],250))) or
                               char_needs_tags(state, ['strong_floors'], 1200) or
                               char_needs_tags(state, ['strong_floors', "climbs_walls"], -1))
        add_rule(world.get_location("Greenflower (Act 2) Emerald Token - Main Path Cave", player),
                 lambda state: state.has("Yellow Springs", player) or char_needs_tags(state, [], 300))
        add_rule(world.get_location("Greenflower (Act 2) Emerald Token - Under Bridge Near End", player),
                 lambda state: state.can_reach_location("Greenflower (Act 2) Clear", player))

        if options.time_emblems:
            add_rule(world.get_location("Greenflower (Act 1) Time Emblem", player),
                     lambda state: state.can_reach_location("Greenflower (Act 1) Clear", player))
            add_rule(world.get_location("Greenflower (Act 2) Time Emblem", player),
                     lambda state: state.can_reach_location("Greenflower (Act 2) Clear", player))
        if options.ring_emblems:
            add_rule(world.get_location("Greenflower (Act 1) Ring Emblem", player),
                     lambda state: state.can_reach_location("Greenflower (Act 1) Clear", player))
            add_rule(world.get_location("Greenflower (Act 2) Ring Emblem", player),
                     lambda state: state.can_reach_location("Greenflower (Act 2) Clear", player))

        if options.oneup_sanity:
            add_rule(world.get_location("Greenflower (Act 1) Monitor - Upper Spin Path in Cave", player),
                     lambda state: (state.has("Yellow Springs", player) and char_needs_tags(state, ["spin_walls"], -1)) or
                                   (state.has("Red Springs", player) and char_needs_tags(state, ["fits_under_gaps"], -1)) or
                                   char_needs_tags(state, ["fits_under_gaps","climbs_walls"], -1) or
                                   char_needs_tags(state, ["fits_under_gaps", "wall_jump"], -1) or
                                   char_needs_tags(state, ["fits_under_gaps"], 600) or
                                   char_needs_tags(state, ["spin_walls"], 350) or
                                   char_needs_tags(state, ["spin_walls","climbs_walls"], -1) or
                                   char_needs_tags(state, ["spin_walls", "wall_jump"], -1))
            add_rule(world.get_location("Greenflower (Act 1) Monitor - Highest Ledge", player),
                     lambda state:char_needs_tags(state, ["climbs_walls"], -1) or
                     char_needs_tags(state, [], 350) or (state.has("Yellow Springs", player) and state.has("Whirlwind Shield", player) and char_needs_tags(state, ["can_use_shields"], -1)))
            add_rule(world.get_location("Greenflower (Act 1) Monitor - Single Pillar Near End", player),
                     lambda state:state.can_reach_location("Greenflower (Act 1) Clear", player))




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



        add_rule(world.get_location("Techno Hill (Act 1) Heart Emblem", player),
                 lambda state: char_needs_tags(state,[],900))
        add_rule(world.get_location("Techno Hill (Act 1) Diamond Emblem", player),
                 lambda state: char_needs_tags(state, [], 900) or char_needs_tags(state, ["climbs_walls"], -1))
        add_rule(world.get_location("Techno Hill (Act 1) Club Emblem", player),
                 lambda state: char_needs_tags(state, ['strong_walls'], 250) or char_needs_tags(state, ['strong_walls','climbs_walls'], -1))
        add_rule(world.get_location("Techno Hill (Act 1) Emerald Token - Alt Path Under Slime", player),
                 lambda state: state.has("Buoyant Slime", player))
        add_rule(world.get_location("Techno Hill (Act 2) Clear", player),
                 lambda state: state.has("Yellow Springs", player) or char_needs_tags(state, ['climbs_walls'], -1) or
                               char_needs_tags(state, ['wall_jump'], -1) or char_needs_tags(state, [], 400))

        add_rule(world.get_location("Techno Hill (Act 2) Heart Emblem", player),
                 lambda state:(char_needs_tags(state, ["can_use_shields"], -1) and state.has("Elemental Shield",player)) or char_needs_tags(state, ["can_stomp"], -1) or state.has("Red Springs",player))


        add_rule(world.get_location("Techno Hill (Act 2) Star Emblem", player),
                 lambda state: char_needs_tags(state,['spin_walls'],-1))
        add_rule(world.get_location("Techno Hill (Act 2) Emerald Token - Knuckles Path Backtrack", player),
                 lambda state: char_needs_tags(state,['strong_walls','strong_floors'],-1))


        if options.difficulty == 0:
            add_rule(world.get_location("Techno Hill (Act 1) Clear", player),
                     lambda state: state.has("Yellow Springs", player) or char_needs_tags(state, [], 300) or state.has("Buoyant Slime", player))
            add_rule(world.get_location("Techno Hill (Act 1) Spade Emblem", player),
                     lambda state:((char_needs_tags(state, ["can_use_shields"], -1) and state.has("Elemental Shield",player)) or char_needs_tags(state, ["can_stomp"], -1)) and state.has("Buoyant Slime", player))
            add_rule(world.get_location("Techno Hill (Act 2) Emerald Token - Deep in Slime", player),
                     lambda state:(char_needs_tags(state, ["can_use_shields"], -1) and state.has("Elemental Shield",player)) or char_needs_tags(state, ["can_stomp"], -1))
            add_rule(world.get_location("Techno Hill (Act 2) Club Emblem", player),
                     lambda state: char_needs_tags(state, [], 1400))

            add_rule(world.get_location("Techno Hill (Act 1) Star Emblem", player),
                     lambda state: char_needs_tags(state, [], 300) or char_needs_tags(state,['climbs_walls'],-1))
        else:
            add_rule(world.get_location("Techno Hill (Act 1) Spade Emblem", player),
                     lambda state: state.has("Buoyant Slime", player))
            add_rule(world.get_location("Techno Hill (Act 2) Emerald Token - Deep in Slime", player),
                     lambda state:(char_needs_tags(state, ["can_use_shields"], -1) and state.has("Elemental Shield",player)) or char_needs_tags(state, ["can_stomp"], -1) or state.has("Red Springs",player))


        if options.time_emblems:
            add_rule(world.get_location("Techno Hill (Act 1) Time Emblem", player),
                     lambda state: state.can_reach_location("Techno Hill (Act 1) Clear", player))
            add_rule(world.get_location("Techno Hill (Act 2) Time Emblem", player),
                     lambda state: state.can_reach_location("Techno Hill (Act 2) Clear", player))
        if options.ring_emblems:
            add_rule(world.get_location("Techno Hill (Act 1) Ring Emblem", player),
                     lambda state: state.can_reach_location("Techno Hill (Act 1) Clear", player))
            add_rule(world.get_location("Techno Hill (Act 2) Ring Emblem", player),
                     lambda state: state.can_reach_location("Techno Hill (Act 2) Clear", player))


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

            add_rule(world.get_location("Techno Hill (Act 2) Monitor - Near Heart Emblem 1", player),
                     lambda state: state.can_reach_location("Techno Hill (Act 2) Heart Emblem", player))
            add_rule(world.get_location("Techno Hill (Act 2) Monitor - Near Heart Emblem 2", player),
                     lambda state: state.can_reach_location("Techno Hill (Act 2) Heart Emblem", player))
            add_rule(world.get_location("Techno Hill (Act 2) Monitor - Near Heart Emblem 3", player),
                     lambda state: state.can_reach_location("Techno Hill (Act 2) Heart Emblem", player))



            if options.difficulty == 0:
                rf.assign_rule("Techno Hill (Act 1) Monitor - Before End on Crates", "TAILS | KNUCKLES | AMY | FANG | WIND")#idk why this is here this is piss easy
                rf.assign_rule("Techno Hill (Act 2) Monitor - High Ledge Outside 2", "TAILS | KNUCKLES | FANG | WIND")
                rf.assign_rule("Techno Hill (Act 2) Monitor - High Ledge Outside 3", "TAILS | KNUCKLES | FANG | WIND")




        # Deep Sea

        add_rule(world.get_location("Deep Sea (Act 1) Clear", player),
                 lambda state: char_needs_tags(state,[],250) or char_needs_tags(state,['can_hover'],-1) or char_needs_tags(state,['climbs_walls'],-1) or state.has("Yellow Springs",player))

        add_rule(world.get_location("Deep Sea (Act 1) Star Emblem", player),
                 lambda state: ((char_needs_tags(state,['strong_walls',"pounds_springs",'can_hover'],-1) or
                                char_needs_tags(state,['strong_walls',"pounds_springs"],250) or
                                char_needs_tags(state,['strong_walls',"pounds_springs",'climbs_walls'],-1) or
                                (char_needs_tags(state,['strong_walls',"pounds_springs"],-1) and state.has("Yellow Springs",player))) and
                                state.has("Red Springs",player)) or char_needs_tags(state,['strong_walls'],1500))


        add_rule(world.get_location("Deep Sea (Act 1) Spade Emblem", player),
                 lambda state:  (((char_needs_tags(state,[],200) and state.has("Yellow Springs",player)) or
                                char_needs_tags(state, [], 250) or
                                (char_needs_tags(state, ["can_use_shields"], 100) and state.has("Whirlwind Shield",player)) or
                               char_needs_tags(state,['can_hover'],-1)) and state.has("Red Springs",player)) or
                                ((char_needs_tags(state, ['instant_speed'], 200) and state.has("Yellow Springs", player)) or
                                  char_needs_tags(state, ['instant_speed'], 250) or
                                  (char_needs_tags(state, ["can_use_shields",'instant_speed'], 100) and state.has("Whirlwind Shield",player)) or
                                  char_needs_tags(state, ['can_hover','instant_speed'], -1)) or
                                char_needs_tags(state, ["climbs_walls"], -1))
        add_rule(world.get_location("Deep Sea (Act 1) Diamond Emblem", player),
                 lambda state: ((char_needs_tags(state, [], 250) or
                                char_needs_tags(state, ['climbs_walls'], -1) or
                                char_needs_tags(state, ['wall_jump'], -1)) or
                               (state.has("Yellow Springs", player) and state.has("Gargoyle Statues",player)))
                               and (state.has("Air Bubbles",player)or state.has("Elemental Shield",player)))


        add_rule(world.get_location("Deep Sea (Act 1) Club Emblem", player),
                 lambda state: (char_needs_tags(state, [], 250) or char_needs_tags(state, ['can_hover'],-1) or char_needs_tags(state, ['climbs_walls'], -1) or state.has("Yellow Springs", player)) and state.has("Gargoyle Statues",player))


        add_rule(world.get_location("Deep Sea (Act 1) Emerald Token - Underwater Air Pocket on Right Path", player),
                 lambda state: ((char_needs_tags(state, [], 250) or
                                char_needs_tags(state, ['climbs_walls'], -1) or
                                char_needs_tags(state, ['wall_jump'], -1)) or
                               (state.has("Yellow Springs", player) and state.has("Gargoyle Statues",player))))

#115
        add_rule(world.get_location("Deep Sea (Act 1) Emerald Token - Large Underwater Curve", player),
                 lambda state: ((char_needs_tags(state, [], 250) or
                                 char_needs_tags(state, ['climbs_walls'], -1) or
                                 char_needs_tags(state, ['wall_jump'], -1)) or
                                (state.has("Yellow Springs", player) and state.has("Gargoyle Statues",player))))


        add_rule(world.get_location("Deep Sea (Act 1) Emerald Token - Waterslide Gargoyles", player),
                 lambda state: (char_needs_tags(state,[],250) or
                                char_needs_tags(state,['can_hover'],-1) or
                                char_needs_tags(state,['climbs_walls'],-1) or
                                state.has("Yellow Springs",player))and state.has("Gargoyle Statues",player))
        add_rule(world.get_location("Deep Sea (Act 1) Emerald Token - Large Underwater Curve", player),
                 lambda state: ((char_needs_tags(state, ['can_hover'], -1) or state.has("Yellow Springs", player)) and (state.has("Red Springs", player) or state.has("Air Bubbles", player) or state.has("Elemental Shield", player)) and state.has("Gargoyle Statues",player)) or
                                (char_needs_tags(state, [], 250)) and (state.has("Red Springs", player) or state.has("Air Bubbles", player) or state.has("Elemental Shield", player)) or
                                char_needs_tags(state, [], 500) or char_needs_tags(state, ['climbs_walls'], -1))

        add_rule(world.get_location("Deep Sea (Act 1) Emerald Token - Yellow Doors", player),
                 lambda state: (char_needs_tags(state, ["instant_speed",'fits_under_gaps'], -1) and state.has("Yellow Springs",player)) or
                               char_needs_tags(state, ['fits_under_gaps'], 1200) or char_needs_tags(state, ['fits_under_gaps',"climbs_walls"],-1))

        add_rule(world.get_location("Deep Sea (Act 2) Clear", player),
                 lambda state:((state.has("Red Springs",player) and state.has("Yellow Springs",player)) or
                              (state.has("Red Springs",player) and char_needs_tags(state, ["strong_floor"],-1))) or char_needs_tags(state, ["climbs_walls"],0) or char_needs_tags(state, [],800))#todo or climb
        add_rule(world.get_location("Deep Sea (Act 2) Star Emblem", player),
                 lambda state: (state.has("Red Springs",player) or state.has("Gargoyle Statues",player)) and char_needs_tags(state, ['strong_floors'], -1))#technically this requires either jump height or 'strong_walls' but no reasonable character would make this impossible
        add_rule(world.get_location("Deep Sea (Act 2) Spade Emblem", player),
                 lambda state: char_needs_tags(state, ["climbs_walls"], -1) or char_needs_tags(state, [],400))
        add_rule(world.get_location("Deep Sea (Act 2) Heart Emblem", player),
                 lambda state: char_needs_tags(state, ['spin_walls'], -1))
        add_rule(world.get_location("Deep Sea (Act 2) Diamond Emblem", player),
                 lambda state: char_needs_tags(state, ['strong_walls',"climbs_walls"], -1) or
                               (char_needs_tags(state, ['strong_walls','strong_floors',"pounds_springs"], 115) and state.has("Yellow Springs",player) and state.has("Gargoyle Statues",player)) or
                               char_needs_tags(state, ['strong_walls'], 400))
        add_rule(world.get_location("Deep Sea (Act 2) Club Emblem", player),
                 lambda state: char_needs_tags(state, ["climbs_walls"], -1) or
                               char_needs_tags(state, ["wall_jump"], -1) or
                               char_needs_tags(state, [], 1400))
        add_rule(world.get_location("Deep Sea (Act 2) Emerald Token - Near Heart Emblem", player),
                 lambda state: char_needs_tags(state, ['spin_walls'], -1))
        add_rule(world.get_location("Deep Sea (Act 2) Emerald Token - No Spin Spring Turnaround", player),
                 lambda state: char_needs_tags(state, ['strong_floors'], -1) and (state.has("Air Bubbles", player) or state.has("Elemental Shield", player)))

        add_rule(world.get_location("Deep Sea (Act 2) Emerald Token - Down Right From Goal", player),
                 lambda state: ((state.has("Yellow Springs", player)) or
                                (state.has("Red Springs", player) and char_needs_tags(state, ["strong_floor"],-1))) or char_needs_tags(state,[], 800))
        add_rule(world.get_location("Deep Sea (Act 2) Emerald Token - Red and Yellow Springs", player),
                 lambda state: ((state.has("Red Springs", player) and char_needs_tags(state,["can_spindash"], -1)) or char_needs_tags(state,[], 1200)))




        if options.difficulty == 0:
            #not possible for amy
            add_rule(world.get_location("Deep Sea (Act 1) Heart Emblem", player),
                     lambda state: (char_needs_tags(state, ["climbs_walls"], -1) or
                                   char_needs_tags(state, [], 1000)) and (state.has("Air Bubbles",player)or state.has("Elemental Shield",player)))
        else:
            add_rule(world.get_location("Deep Sea (Act 1) Heart Emblem", player),
                     lambda state: (char_needs_tags(state, ["climbs_walls"], -1) or
                                   char_needs_tags(state, [], 1000) or
                                    (char_needs_tags(state, ["instant_speed"], 100) and state.has("Yellow Springs",player))) and (state.has("Air Bubbles",player) or state.has("Elemental Shield",player))
                     )

        if options.time_emblems:
            add_rule(world.get_location("Deep Sea (Act 1) Time Emblem", player),
                     lambda state: state.can_reach_location("Deep Sea (Act 1) Clear", player))
            add_rule(world.get_location("Deep Sea (Act 2) Time Emblem", player),
                     lambda state: state.can_reach_location("Deep Sea (Act 2) Clear", player))
        if options.ring_emblems:
            add_rule(world.get_location("Deep Sea (Act 1) Ring Emblem", player),
                     lambda state: state.can_reach_location("Deep Sea (Act 1) Clear", player))
            add_rule(world.get_location("Deep Sea (Act 2) Ring Emblem", player),
                     lambda state: state.can_reach_location("Deep Sea (Act 2) Clear", player))


        if options.oneup_sanity:


            rf.assign_rule("Deep Sea (Act 1) Monitor - Waterslide Hidden Spring Room", "TAILS | KNUCKLES | FANG | WIND")
            rf.assign_rule("Deep Sea (Act 1) Monitor - Waterfall Cave Opposite Spade Emblem", "TAILS | KNUCKLES | METAL SONIC | WIND")
            rf.assign_rule("Deep Sea (Act 1) Monitor - Broken Wall Near End", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")
            rf.assign_rule("Deep Sea (Act 1) Monitor - Yellow Switch", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Deep Sea (Act 1) Monitor - Left Path Waterfall Cave", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Deep Sea (Act 1) Monitor - Right Right Subpath Breakable Wall Between Columns", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")

            #"Deep Sea (Act 1) Monitor - x:8640 y:3168" - maybe at least require wind for normal - have to check other emblems if so (Club emblem) (NAH)

            rf.assign_rule("Deep Sea (Act 2) Monitor - Spindash Fast Door 1", "SONIC | KNUCKLES")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Spindash Fast Door 2", "SONIC | KNUCKLES")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Spindash Fast Door 3", "SONIC | KNUCKLES")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Gargoyle Path Wall Under Oval Platform", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Main Path Roll Down Ramp Into Breakable Wall", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Knuckles Path Dark High Ledge", "KNUCKLES | AMY")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Knuckles Path Crushing Ceiling", "KNUCKLES | AMY")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Near Club Emblem", "TAILS | KNUCKLES")


            if options.difficulty == 0:
                rf.assign_rule("Deep Sea (Act 1) Monitor - Heart Emblem Backtrack to Club 1","TAILS | KNUCKLES")  # heart emblem club emblem opened bullshit
                rf.assign_rule("Deep Sea (Act 1) Monitor - Heart Emblem Backtrack to Club 2","TAILS | KNUCKLES")  # heart emblem club emblem opened bullshit
                rf.assign_rule("Deep Sea (Act 2) Monitor - Gargoyle Path Spiked Cliff Top", "TAILS | KNUCKLES | FANG")
                rf.assign_rule("Deep Sea (Act 1) Monitor - Behind Fast Closing Door 1", "METAL SONIC")
                rf.assign_rule("Deep Sea (Act 1) Monitor - Behind Fast Closing Door 2","METAL SONIC")
            else:
                rf.assign_rule("Deep Sea (Act 1) Monitor - Heart Emblem Backtrack to Club 1","TAILS | KNUCKLES | WIND")  # heart emblem club emblem opened bullshit
                rf.assign_rule("Deep Sea (Act 1) Monitor - Heart Emblem Backtrack to Club 2","TAILS | KNUCKLES | WIND")  # heart emblem club emblem opened bullshit

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

        add_rule(world.get_location("Castle Eggman (Act 1) Clear", player),
                 lambda state: (state.has("Swinging Maces",player) and state.has("Yellow Springs",player) and state.has("Red Springs",player)) or
                               (state.has("Swinging Maces", player) and char_needs_tags(state, ["can_hover","instant_speed"], -1)) or
                                (state.has("Swinging Maces", player) and state.has("Yellow Springs",player) and char_needs_tags(state, ["can_hover"], -1)) or
                               char_needs_tags(state, ["climbs_walls"], -1) or
                                char_needs_tags(state, [], 1200))

        add_rule(world.get_location("Castle Eggman (Act 1) Star Emblem", player),
                 lambda state: char_needs_tags(state, ["climbs_walls"], -1) or
                               char_needs_tags(state, [], 1400))#wall jumps DONT work
        add_rule(world.get_location("Castle Eggman (Act 1) Spade Emblem", player),
                 lambda state: (state.has("Swinging Maces",player) and state.has("Yellow Springs",player) and state.has("Red Springs",player)) or
                               (state.has("Swinging Maces", player) and char_needs_tags(state, ["can_hover","instant_speed"], -1)) or
                               (state.has("Swinging Maces", player) and state.has("Yellow Springs",player) and char_needs_tags(state, ["can_hover"], -1)) or
                               char_needs_tags(state, ["climbs_walls"], -1) or
                                char_needs_tags(state, [], 1200))
        add_rule(world.get_location("Castle Eggman (Act 1) Heart Emblem", player),
                 lambda state: (state.has("Swinging Maces", player) and state.has("Yellow Springs",player) and state.has("Red Springs",player)) or
                               (state.has("Swinging Maces", player) and char_needs_tags(state, ["can_hover","instant_speed"], -1)) or
                               (state.has("Swinging Maces", player) and state.has("Yellow Springs",player) and char_needs_tags(state,["can_hover"],-1)) or
                               char_needs_tags(state, ["climbs_walls"], -1) or
                               char_needs_tags(state, [], 1200))
        add_rule(world.get_location("Castle Eggman (Act 1) Diamond Emblem", player),
                 lambda state: state.has("Swinging Maces",player) or
                               char_needs_tags(state, ["climbs_walls"], -1) or
                               char_needs_tags(state, [], 1000))

        add_rule(world.get_location("Castle Eggman (Act 1) Club Emblem", player),
                 lambda state: state.has("Swinging Maces",player) and (state.has("Yellow Springs",player) or char_needs_tags(state, ["midair_speed"], -1) or char_needs_tags(state, ["can_hover"], -1)) or
                               char_needs_tags(state, ["climbs_walls"], -1) or
                               char_needs_tags(state, [], 1000))

        add_rule(world.get_location("Castle Eggman (Act 1) Emerald Token - Inside Castle", player),
                 lambda state: state.has("Swinging Maces",player) and (state.has("Yellow Springs",player) or char_needs_tags(state, ["midair_speed"], -1) or char_needs_tags(state, ["can_hover"], -1)) or
                               char_needs_tags(state, ["climbs_walls"], -1) or
                               char_needs_tags(state, [], 1000))
        add_rule(world.get_location("Castle Eggman (Act 1) Emerald Token - Spring Side Path", player),
                lambda state: (state.has("Swinging Maces", player)and (char_needs_tags(state, ["can_hover"], -1) or (char_needs_tags(state, ["instant_speed"], -1)and state.has("Yellow Springs",player))) or state.has("Red Springs",player)) or
                        char_needs_tags(state, ["climbs_walls"], -1) or
                        char_needs_tags(state, [], 1000))


        add_rule(world.get_location("Castle Eggman (Act 2) Clear", player),
                 lambda state: (state.has("Swinging Maces",player) and state.has("Yellow Springs",player)) or
                 (state.has("Swinging Maces",player) and char_needs_tags(state, [], 200)) or
                 char_needs_tags(state, ['climbs_walls'], -1) or char_needs_tags(state, [], 1000))
        add_rule(world.get_location("Castle Eggman (Act 2) Star Emblem", player),
                 lambda state: (state.has("Red Springs", player) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 200))) or
                               (state.has("Yellow Springs", player) and (char_needs_tags(state, ['can_hover'], -1)) or char_needs_tags(state, [], 200)) or
                               char_needs_tags(state, ['climbs_walls'], -1) or char_needs_tags(state, [], 250))
        add_rule(world.get_location("Castle Eggman (Act 2) Spade Emblem", player),
                 lambda state: (state.has("Swinging Maces", player) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 200))) or
                               char_needs_tags(state, ['climbs_walls'], -1) or char_needs_tags(state, [], 1400))
        add_rule(world.get_location("Castle Eggman (Act 2) Heart Emblem", player),
                 lambda state: (state.has("Swinging Maces", player) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 200))) or
                               (state.has("Yellow Springs", player) and char_needs_tags(state, ['can_hover'], -1)) or
                               char_needs_tags(state, ['climbs_walls'], -1) or char_needs_tags(state, [], 1200))
        add_rule(world.get_location("Castle Eggman (Act 2) Diamond Emblem", player),
                 lambda state: (state.has("Swinging Maces", player) and state.has("Yellow Springs", player) and char_needs_tags(state, ["low_grav"], -1)) or
                               (state.has("Swinging Maces", player) and char_needs_tags(state, ["low_grav"], 200)) or
                               (state.has("Swinging Maces", player) and char_needs_tags(state, ['climbs_walls',"low_grav"], -1)) or char_needs_tags(state, [], 1500))
        add_rule(world.get_location("Castle Eggman (Act 2) Club Emblem", player),
                 lambda state: (state.has("Swinging Maces", player) and state.has("Yellow Springs", player) and state.has("Red Springs", player)) or
                               (state.has("Swinging Maces", player) and char_needs_tags(state, [], 200)) or
                               (char_needs_tags(state, ["can_hover"], -1) and state.has("Yellow Springs", player)) or
                               char_needs_tags(state, ["can_hover"], 200) or
                               char_needs_tags(state, ['climbs_walls'], -1) or char_needs_tags(state, [], 1200)
                               )
        add_rule(world.get_location("Castle Eggman (Act 2) Emerald Token - First Outside Area", player),
                 lambda state: (state.has("Red Springs", player) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 250))) or
                               char_needs_tags(state, ['climbs_walls'], -1) or char_needs_tags(state, [], 600))
        add_rule(world.get_location("Castle Eggman (Act 2) Emerald Token - Corner of Right Courtyard", player),
                 lambda state: state.can_reach_location("Castle Eggman (Act 2) Heart Emblem", player))#laziness
        add_rule(world.get_location("Castle Eggman (Act 2) Emerald Token - Back Window of Left Courtyard", player),
                 lambda state: state.can_reach_location("Castle Eggman (Act 2) Spade Emblem", player))

        add_rule(world.get_location("Castle Eggman (Act 2) Emerald Token - Spring Near Club Emblem", player),
                 lambda state: (state.has("Swinging Maces", player) and state.has("Yellow Springs",player) and state.has("Red Springs",player)) or
                               (state.has("Swinging Maces", player) and char_needs_tags(state, [], 800)) or
                               char_needs_tags(state, ['climbs_walls'], -1) or char_needs_tags(state, [], 1200))
        add_rule(world.get_location("Castle Eggman (Act 2) Emerald Token - High Ledge Before Final Tower", player),
                 lambda state: (state.has("Swinging Maces", player) and state.has("Yellow Springs", player) and char_needs_tags(state, ["instant_speed"], -1)) or
                               (state.has("Swinging Maces", player) and char_needs_tags(state, ["instant_speed"], 200)) or
                               (char_needs_tags(state, ["can_hover",'instant_speed'], -1) and state.has("Yellow Springs", player) and (state.has("Red Springs", player) or state.has("Swinging Maces", player))) or
                               (char_needs_tags(state, ["can_hover",'instant_speed'], 200) and (state.has("Red Springs", player) or state.has("Swinging Maces", player))) or
                               char_needs_tags(state, ['climbs_walls'], -1) or char_needs_tags(state, [], 1200)
                               )
        if options.time_emblems:
            add_rule(world.get_location("Castle Eggman (Act 1) Time Emblem", player),
                     lambda state: state.can_reach_location("Castle Eggman (Act 1) Clear", player))
            add_rule(world.get_location("Castle Eggman (Act 2) Time Emblem", player),
                     lambda state: state.can_reach_location("Castle Eggman (Act 2) Clear", player))
        if options.ring_emblems:
            add_rule(world.get_location("Castle Eggman (Act 1) Ring Emblem", player),
                     lambda state: state.can_reach_location("Castle Eggman (Act 1) Clear", player))
            add_rule(world.get_location("Castle Eggman (Act 2) Ring Emblem", player),
                     lambda state: state.can_reach_location("Castle Eggman (Act 2) Clear", player))
        #if options.difficulty == 0:
        #    rf.assign_rule("Castle Eggman (Act 2) Club Emblem", "TAILS | KNUCKLES | FANG | WIND")tbh this isnt really hard
        if options.oneup_sanity:
            rf.assign_rule("Castle Eggman (Act 2) Monitor - Rafter Above Starting Area", "TAILS | KNUCKLES")
            rf.assign_rule("Castle Eggman (Act 2) Monitor - High Bookshelf Before Final Tower", "TAILS | KNUCKLES | AMY")
            rf.assign_rule("Castle Eggman (Act 2) Monitor - Front Left Path High Ledge Before Swinging Chains", "TAILS | KNUCKLES")
            rf.assign_rule("Castle Eggman (Act 2) Monitor - Right Path Thin Gray Bookshelf Top", "TAILS | KNUCKLES | WIND")


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
        add_rule(world.get_location("Arid Canyon (Act 1) Clear", player),
                 lambda state: (state.has("Rope Hangs",player) and state.has("Yellow Springs",player)and state.has("Red Springs",player) and (char_needs_tags(state, ['fits_under_gaps'], -1) or state.has("Dust Devils",player))) or
                               (state.has("Rope Hangs",player) and state.has("Red Springs",player) and char_needs_tags(state, ['can_hover'], -1) ) or char_needs_tags(state, [], 600) or
                               char_needs_tags(state, ['climbs_walls'], -1))#ropes,ys,rs,spinchar
        add_rule(world.get_location("Arid Canyon (Act 1) Star Emblem", player),
                 lambda state: char_needs_tags(state, ["climbs_walls"],-1) or
                               (char_needs_tags(state, ["pounds_springs",'strong_floors'],-1) and state.has("Red Springs",player) and state.has("Rope Hangs",player)) or
                               (char_needs_tags(state, ["pounds_springs", 'strong_floors',"instant_speed"], -1) and state.has("Red Springs",player) and state.has("Yellow Springs",player) and state.has("Dust Devils",player)) or
                               char_needs_tags(state, [],800))
#any + strong floors
        add_rule(world.get_location("Arid Canyon (Act 1) Heart Emblem", player),
                 lambda state: char_needs_tags(state, ["climbs_walls"], -1) or
                               (state.has("Red Springs",player) and state.has("Rope Hangs",player) and char_needs_tags(state,["roll"],-1)) or
                                (state.has("Red Springs",player) and state.has("Rope Hangs",player) and ((state.has("Yellow Springs",player) or char_needs_tags(state, [], 300))and state.has("Dust Devils",player)) or char_needs_tags(state, ["wall_jump"], -1)) or
                               (state.has("Red Springs",player) and state.has("Yellow Springs",player) and state.has("Dust Devils",player)) or
                               char_needs_tags(state, [], 800))
        add_rule(world.get_location("Arid Canyon (Act 1) Club Emblem", player),
                 lambda state: char_needs_tags(state, ["climbs_walls"], -1) or
                               (state.has("Red Springs",player) and state.has("Rope Hangs",player) and char_needs_tags(state, ["roll"],-1)) or
                               (state.has("Red Springs",player) and state.has("Yellow Springs",player) and state.has("Dust Devils",player) and char_needs_tags(state, ["roll"],-1)) or
                               (state.has("Red Springs",player) and state.has("Yellow Springs",player)and state.has("Rope Hangs",player)and state.has("Dust Devils",player) and char_needs_tags(state, ['strong_floors'],200)) or
                               char_needs_tags(state, [], 800))
#whirlwind works but idc
        add_rule(world.get_location("Arid Canyon (Act 1) Emerald Token - Speed Shoes Central Pillar", player),
                 lambda state: char_needs_tags(state, ["climbs_walls"], -1) or
                                (state.has("Red Springs",player) and state.has("Rope Hangs",player)) or
                               (state.has("Red Springs",player) and state.has("Yellow Springs",player) and state.has("Dust Devils",player)) or
                               char_needs_tags(state, [], 800))
        add_rule(world.get_location("Arid Canyon (Act 1) Emerald Token - Behind Pillar Before Exploding Ramp", player),
                 lambda state: state.can_reach_location("Arid Canyon (Act 1) Spade Emblem",player))
        add_rule(world.get_location("Arid Canyon (Act 1) Emerald Token - Behind Wall and Spikes", player),
                 lambda state: char_needs_tags(state, ['strong_walls',"breaks_spikes"], -1))#technically can be done with climbs_walls/jump_height and breaks spikes

        add_rule(world.get_location("Arid Canyon (Act 2) Clear", player),
                 lambda state: (state.has("Minecarts",player) and(
                     (state.has("Dust Devils",player) and (state.has("Yellow Springs",player) or char_needs_tags(state, [], 200)))or
                     ((char_needs_tags(state, ["roll"], -1))or char_needs_tags(state, ["instant_speed"], -1) and state.has("Yellow Springs",player) and state.has("Red Springs",player)) or
                     (char_needs_tags(state, ["climbs_walls",'strong_walls','fits_under_gaps'], -1) or
                      (char_needs_tags(state, [], 800)
                 )))) or (char_needs_tags(state, ["stronger_walls"], -1) and state.has("Dust Devils",player)) or
                      ((char_needs_tags(state, ["instant_speed"], -1) or (char_needs_tags(state, ["stronger_walls","roll"], -1) and state.has("Red Springs",player))) and state.has("Yellow Springs",player) and state.has("Red Springs",player)) or
                      (char_needs_tags(state, ["stronger_walls"], 600)))#todo amy can do this with a bunch of shit
        #strongerwalls + ys+rs/
        add_rule(world.get_location("Arid Canyon (Act 2) Star Emblem", player),
                 lambda state: state.has("Minecarts",player) and ((char_needs_tags(state, ['strong_floors'], 115)and state.has("Dust Devils",player)) or (char_needs_tags(state, ['strong_floors'], 400))) or
                 char_needs_tags(state, ["stronger_walls",'instant_speed'],-1) or char_needs_tags(state, ["stronger_walls"],400) or (state.has("Dust Devils",player) and char_needs_tags(state, ["stronger_walls"],-1))or
                 char_needs_tags(state, ["stronger_walls",'roll'],-1) and state.has("Red Springs",player))

        add_rule(world.get_location("Arid Canyon (Act 2) Spade Emblem", player),
                 lambda state: (state.has("Dust Devils",player) and char_needs_tags(state, ['strong_floors'],-1)) or
                                char_needs_tags(state, ['strong_floors'], 400) or
                               (char_needs_tags(state, ['roll','strong_floors'], -1) and state.has("Red Springs",player)) or
                               char_needs_tags(state, ['instant_speed', 'strong_floors'], -1)#knuckles path can probably backtrack
                 )
        add_rule(world.get_location("Arid Canyon (Act 2) Heart Emblem", player),
                 lambda state: (state.has("Dust Devils",player) and char_needs_tags(state, ["wall_jump"],-1)) or
                               char_needs_tags(state, ["climbs_walls", 'strong_walls', 'fits_under_gaps'], -1) or
                                char_needs_tags(state, [], 1600) or
                               ((char_needs_tags(state, ['roll',"climbs_walls"], 100) or (char_needs_tags(state, ['roll', "wall_jump"], 100))) and state.has("Red Springs",player)) or
                               char_needs_tags(state, ['instant_speed', "climbs_walls"], 100) or char_needs_tags(state, ['instant_speed', "wall_jump"], 100)#knuckles path can probably backtrack
                 )



        add_rule(world.get_location("Arid Canyon (Act 2) Diamond Emblem", player),#can be gotten w/ instant speed and a bunch of other shit from the other side
                 lambda state: (state.has("Minecarts",player) and ((char_needs_tags(state, ['strong_floors'], 200) and state.has("Red Springs",player)) or char_needs_tags(state, ['strong_floors'], 800))) or
                               char_needs_tags(state, ["stronger_walls"], 800) or
                               ((char_needs_tags(state, ['roll', "stronger_walls"], -1) or char_needs_tags(state, ['instant_speed', "stronger_walls"], -1)) and state.has("Red Springs",player))
                               )

        add_rule(world.get_location("Arid Canyon (Act 2) Club Emblem", player),
                 lambda state: state.has("Minecarts",player) and (char_needs_tags(state, ["climbs_walls"],-1) or
                               char_needs_tags(state, [],1400)))
        add_rule(world.get_location("Arid Canyon (Act 2) Emerald Token - Left No Spin Path Minecarts", player),
                 lambda state: state.has("Minecarts",player) and ((char_needs_tags(state, ['strong_floors'], 115)and state.has("Dust Devils",player)) or (char_needs_tags(state, ['strong_floors'], 400))) or
                 char_needs_tags(state, ["stronger_walls",'instant_speed'],-1) or char_needs_tags(state, ["stronger_walls"],400) or (state.has("Dust Devils",player) and char_needs_tags(state, ["stronger_walls"],-1))or
                 char_needs_tags(state, ["stronger_walls",'roll'],-1) and state.has("Red Springs",player))
        add_rule(world.get_location("Arid Canyon (Act 2) Emerald Token - Large Arch Cave Right Ledge", player),
                 lambda state: (state.has("Minecarts",player) and state.has("Dust Devils",player) and state.has("Red Springs",player)) or state.can_reach_location("Arid Canyon (Act 2) Star Emblem",player) or
                               (char_needs_tags(state, ["stronger_walls"],-1) and state.has("Dust Devils",player)) or char_needs_tags(state, ["stronger_walls"],400))
        add_rule(world.get_location("Arid Canyon (Act 2) Emerald Token - Knuckles Dark Path Around Wall", player),
                 lambda state: char_needs_tags(state, ["free_flyer"],600) or
                               (char_needs_tags(state, ["climbs_walls"],100)) or ((char_needs_tags(state, ["climbs_walls"],-1) or (char_needs_tags(state, ['strong_walls',"breaks_spikes","can_use_shields"],-1)and state.has("Whirlwind Shield",player))) and state.has("Yellow Springs",player))
                                )


        if options.difficulty == 0:
            add_rule(world.get_location("Arid Canyon (Act 1) Spade Emblem", player),
                     lambda state: char_needs_tags(state, ["climbs_walls"], -1) or
                                   (state.has("Red Springs",player) and state.has("Rope Hangs",player) and (state.has("Yellow Springs",player) or char_needs_tags(state, [],130))) or  # needs ys or jh130
                                   (state.has("Red Springs",player) and state.has("Yellow Springs",player) and state.has("Dust Devils",player) and (state.has("Rope Hangs",player)) or char_needs_tags(state, [],300)) or
                                   char_needs_tags(state, [], 800))

            add_rule(world.get_location("Arid Canyon (Act 1) Diamond Emblem", player),
                     lambda state: char_needs_tags(state, ["climbs_walls"], -1) or
                                   (state.has("Red Springs",player) and state.has("Rope Hangs",player) and (state.has("Yellow Springs",player) or char_needs_tags(state, ["roll"],130))) or  # needs ys or jh130
                                   (state.has("Red Springs",player) and state.has("Yellow Springs",player) and state.has("Dust Devils",player) and (state.has("Rope Hangs",player)) or char_needs_tags(state, [],300)) or
                                   char_needs_tags(state, [], 800) or
                                   state.can_reach_location("Arid Canyon (Act 1) Heart Emblem",player))


            add_rule(world.get_location("Arid Canyon (Act 2) Star Emblem", player),
                     lambda state: char_needs_tags(state, ["climbs_walls"], -1) or
                                   char_needs_tags(state, ['strong_floors'], -1) or
                                   char_needs_tags(state, [], 250))


            add_rule(world.get_location("Arid Canyon (Act 2) Heart Emblem", player),
                     lambda state: char_needs_tags(state, ["climbs_walls"], -1))#wall jumps/ jump larger than tails
            add_rule(world.get_location("Arid Canyon (Act 2) Diamond Emblem", player),
                     lambda state: char_needs_tags(state, ['strong_floors'], 150))  # wall jumps/ jump larger than tails

        else:
            add_rule(world.get_location("Arid Canyon (Act 1) Spade Emblem", player),
                     lambda state: char_needs_tags(state, ["climbs_walls"], -1) or
                                   (state.has("Red Springs",player) and state.has("Rope Hangs",player) and (state.has("Yellow Springs",player) or char_needs_tags(state, [],130))) or  # needs ys or jh130
                                   (state.has("Red Springs",player) and (state.has("Yellow Springs",player) or char_needs_tags(state, ['instant_speed'],-1)) and state.has("Dust Devils",player) and state.has("Rope Hangs",player)) or
                                   (state.has("Red Springs",player) and state.has("Yellow Springs",player) and state.has("Dust Devils",player) and (state.has("Rope Hangs",player)) or char_needs_tags(state, [],300)) or
                                   char_needs_tags(state, [], 800))

            add_rule(world.get_location("Arid Canyon (Act 1) Diamond Emblem", player),
                     lambda state: char_needs_tags(state, ["climbs_walls"], -1) or
                                   (state.has("Red Springs",player) and state.has("Rope Hangs",player) and (state.has("Yellow Springs",player) or char_needs_tags(state, ['roll'],130))) or  # needs ys or jh130
                                   (state.has("Red Springs",player) and (state.has("Yellow Springs",player) or char_needs_tags(state, ['instant_speed'],-1)) and state.has("Dust Devils",player) and state.has("Rope Hangs",player)) or
                                   (state.has("Red Springs",player) and state.has("Yellow Springs",player) and state.has("Dust Devils",player) and (state.has("Rope Hangs",player)) or char_needs_tags(state, [],300)) or
                                   state.can_reach_location("Arid Canyon (Act 1) Heart Emblem", player) or
                                   char_needs_tags(state, [], 800))

            add_rule(world.get_location("Arid Canyon (Act 2) Star Emblem", player),
                     lambda state: char_needs_tags(state, ["climbs_walls"], -1) or
                                   char_needs_tags(state, ['strong_floors'], -1) or
                                   char_needs_tags(state, [], 250) or
                                   char_needs_tags(state, ["instant_speed"], 100))

            add_rule(world.get_location("Arid Canyon (Act 2) Diamond Emblem", player),
                     lambda state: char_needs_tags(state, ['strong_floors'], 150) or
                                   (char_needs_tags(state, ['strong_floors',"can_use_shields"], 100) and state.has("Whirlwind Shield",player)))

        if options.time_emblems:
            add_rule(world.get_location("Arid Canyon (Act 1) Time Emblem", player),
                     lambda state: state.can_reach_location("Arid Canyon (Act 1) Clear", player))
            add_rule(world.get_location("Arid Canyon (Act 2) Time Emblem", player),
                     lambda state: state.can_reach_location("Arid Canyon (Act 2) Clear", player))
        if options.ring_emblems:
            add_rule(world.get_location("Arid Canyon (Act 1) Ring Emblem", player),
                     lambda state: state.can_reach_location("Arid Canyon (Act 1) Clear", player))
            add_rule(world.get_location("Arid Canyon (Act 2) Ring Emblem", player),
                     lambda state: state.can_reach_location("Arid Canyon (Act 2) Clear", player))
        if options.oneup_sanity:

            rf.assign_rule("Arid Canyon (Act 1) Monitor - TNT Path High Above Exploding Plank", "TAILS | KNUCKLES | AMY+WIND")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - Near Amy Emerald Token", "AMY")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - Final Section Under Ceiling Near Checkpoint", "TAILS | KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - End of TNT Path Above Cave", "TAILS | KNUCKLES")

            rf.assign_rule("Arid Canyon (Act 2) Monitor - Looping Path Small Cave High Up","TAILS | KNUCKLES")

            rf.assign_rule("Arid Canyon (Act 2) Monitor - High Ledge Near Start", "SONIC | TAILS | KNUCKLES | METAL SONIC | WIND")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - Left Cliffside Ledge From Start","SONIC | TAILS | KNUCKLES | METAL SONIC | WIND")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - Canarivore Path Half Pipe Top Middle","SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - Left Path Moving Platform Knuckles Wall", "KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - Left Path High Ledge Cave", "TAILS | KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - End Of Left Knuckles Path Around Corner 1", "KNUCKLES | AMY")

            rf.assign_rule("Arid Canyon (Act 2) Monitor - Very High Ledge Between Left and Looping Path", "TAILS | KNUCKLES")

            if options.difficulty == 0:
                rf.assign_rule("Arid Canyon (Act 2) Monitor - Behind TNT Crates Near Diamond Emblem","TAILS | KNUCKLES | AMY | FANG")
                rf.assign_rule("Arid Canyon (Act 2) Monitor - TNT Barrel Ledge Near Star Emblem","TAILS | KNUCKLES | AMY | FANG")
                rf.assign_rule("Arid Canyon (Act 2) Monitor - Near Heart Emblem 1", "KNUCKLES")
                rf.assign_rule("Arid Canyon (Act 1) Monitor - Main Area High Broken Road","TAILS | KNUCKLES")
            else:
                rf.assign_rule("Arid Canyon (Act 1) Monitor - Main Area High Broken Road","SONIC | TAILS | KNUCKLES | METAL SONIC | WIND")
                rf.assign_rule("Arid Canyon (Act 2) Monitor - TNT Barrel Ledge Near Star Emblem","TAILS | KNUCKLES | AMY | FANG | WIND")


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
        add_rule(world.get_location("Red Volcano (Act 1) Star Emblem", player),
                 lambda state: state.can_reach_location("Red Volcano (Act 1) Clear", player))
        add_rule(world.get_location("Red Volcano (Act 1) Spade Emblem", player),
                 lambda state: char_needs_tags(state, ["free_flyer"],-1) or
                                char_needs_tags(state, [],800))
        add_rule(world.get_location("Red Volcano (Act 1) Heart Emblem", player),
                 lambda state: state.has("Red Springs",player) or
                               char_needs_tags(state, ["wall_jump"], -1) or
                               char_needs_tags(state, ["climbs_walls"],-1) or
                                char_needs_tags(state, [],800))
        add_rule(world.get_location("Red Volcano (Act 1) Diamond Emblem", player),
                 lambda state: state.can_reach_location("Red Volcano (Act 1) Clear", player))
        add_rule(world.get_location("Red Volcano (Act 1) Club Emblem", player),
                 lambda state: (state.has("Rollout Rocks",player) and char_needs_tags(state, ['spin_walls'],-1) ) or
                               char_needs_tags(state, ['spin_walls',"free_flyer"],1400) or
                               char_needs_tags(state, ['spin_walls',"lava_immune"], 150) )

        add_rule(world.get_location("Red Volcano (Act 1) Emerald Token - Rollout Rock Lavafall", player),
                 lambda state: state.can_reach_location("Red Volcano (Act 1) Clear", player))





        add_rule(world.get_location("Red Volcano (Act 1) Emerald Token - Hidden Ledge Near 4th Checkpoint", player),
                 lambda state: char_needs_tags(state, ["free_flyer"],-1) or
                               (char_needs_tags(state, ["can_use_shields"], -1) and state.has("Whirlwind Shield",player) or
                                char_needs_tags(state, [],800)) or
                                state.has("Fang",player))#hardcoded nonsense because fang is unique

        add_rule(world.get_location("Red Volcano (Act 1) Emerald Token - Behind Ending Rocket", player),
                 lambda state: state.can_reach_location("Red Volcano (Act 1) Clear", player))



        if options.difficulty == 0:
            add_rule(world.get_location("Red Volcano (Act 1) Clear", player),
                     lambda state: (state.has("Rollout Rocks", player) and state.has("Red Springs", player) and state.has("Yellow Springs", player)) or
                                   (char_needs_tags(state, ["can_hover"],-1) and state.has("Rollout Rocks", player) and state.has("Yellow Springs", player))or
                                   char_needs_tags(state, ["lava_immune"], 150) or
                                   char_needs_tags(state, [], 1400)or
                                   char_needs_tags(state, ["climbs_walls"],-1))



            add_rule(world.get_location("Red Volcano (Act 1) Emerald Token - First Outside Area", player),
                     lambda state: char_needs_tags(state, ["climbs_walls"], -1) or
                        char_needs_tags(state, [], 1200) or
                        char_needs_tags(state, ["can_hover"], -1) or
                        (char_needs_tags(state, ["can_use_shields"], -1) and state.has("Whirlwind Shield",player))
                     )

        else:
            add_rule(world.get_location("Red Volcano (Act 1) Emerald Token - First Outside Area", player),
                     lambda state: char_needs_tags(state, ["climbs_walls"], -1) or
                                   char_needs_tags(state, [], 1200) or
                                   char_needs_tags(state, ["can_hover"], -1) or
                                   (char_needs_tags(state, ["can_use_shields"], -1) and state.has("Whirlwind Shield",player) or
                                    char_needs_tags(state, ["can_badnik_bounce",'fits_under_gaps'], -1))
                     )
            add_rule(world.get_location("Red Volcano (Act 1) Clear", player),
                     lambda state: (state.has("Rollout Rocks", player) and state.has("Red Springs", player) and state.has("Yellow Springs", player)) or
                                   (char_needs_tags(state, ["badnik_bounce"],-1) and state.has("Rollout Rocks", player) and state.has("Yellow Springs", player)) or
                                   (char_needs_tags(state, ["badnik_bounce","midair_speed"], -1) and state.has("Yellow Springs", player))or
                                   (char_needs_tags(state, ["can_hover"],-1) and state.has("Rollout Rocks", player) and state.has("Yellow Springs", player))or
                                   char_needs_tags(state, ["lava_immune"], 150) or
                                   char_needs_tags(state, [], 1400)or
                                   char_needs_tags(state, ["climbs_walls"],-1))
        #no 1up rules in rvz
        if options.time_emblems:
            add_rule(world.get_location("Red Volcano (Act 1) Time Emblem", player),
                     lambda state: state.can_reach_location("Red Volcano (Act 1) Clear", player))
        if options.ring_emblems:
            add_rule(world.get_location("Red Volcano (Act 1) Ring Emblem", player),
                     lambda state: state.can_reach_location("Red Volcano (Act 1) Clear", player))
            
        if options.superring_sanity:
            rf.assign_rule("Red Volcano (Act 1) Monitor - x:22304 y:8192", "SONIC | TAILS | KNUCKLES | METAL SONIC | WIND")

        # Egg Rock
        add_rule(world.get_location("Egg Rock (Act 1) Clear", player),
                 lambda state: state.has("Zoom Tubes",player) and
                               (state.has("Red Springs",player) and (char_needs_tags(state, [],300) or state.has("Yellow Springs",player)) or
                                char_needs_tags(state, [],800) or char_needs_tags(state, ["climbs_walls"],-1) or char_needs_tags(state, ["wall_jump"],-1) or#walljumps,climb,walljump 800jump
                               (state.has("Yellow Springs",player) and char_needs_tags(state, ['fits_under_gaps'], -1)) or char_needs_tags(state, ['fits_under_gaps'], 800) or char_needs_tags(state, ["climbs_walls",'fits_under_gaps'],-1) or char_needs_tags(state,["wall_jump",'fits_under_gaps'], -1)
                                ))#ys or the other stuff

#spin path requires zoom tubes, ys, 350jump or climb or wj

        add_rule(world.get_location("Egg Rock (Act 1) Star Emblem", player),
                 lambda state: (state.has("Yellow Springs",player) and char_needs_tags(state, ['fits_under_gaps'], -1)) or char_needs_tags(state, ['fits_under_gaps'], 800) or char_needs_tags(state, ["climbs_walls",'fits_under_gaps'],-1) or char_needs_tags(state,["wall_jump",'fits_under_gaps'], -1))

        add_rule(world.get_location("Egg Rock (Act 1) Spade Emblem", player),
                 lambda state: char_needs_tags(state, ['fits_under_gaps',"climbs_walls"],-1) or
                                char_needs_tags(state, ['fits_under_gaps'],300))

        add_rule(world.get_location("Egg Rock (Act 1) Diamond Emblem", player),
                 lambda state: state.has("Red Springs",player) or char_needs_tags(state, ["climbs_walls"], -1) or char_needs_tags(state, ["wall_jump"], -1) or char_needs_tags(state, [], 800))

        add_rule(world.get_location("Egg Rock (Act 1) Club Emblem", player),
                 lambda state: state.can_reach_location("Egg Rock (Act 1) Clear", player))

        add_rule(world.get_location("Egg Rock (Act 1) Emerald Token - Moving Platforms", player),
                 lambda state: state.can_reach_location("Egg Rock (Act 1) Star Emblem", player))
        add_rule(world.get_location("Egg Rock (Act 1) Emerald Token - Gravity Conveyor Belts", player),
                 lambda state: state.can_reach_location("Egg Rock (Act 1) Diamond Emblem", player))

        add_rule(world.get_location("Egg Rock (Act 2) Clear", player),
                 lambda state: state.has("Zoom Tubes", player))
        add_rule(world.get_location("Egg Rock (Act 2) Star Emblem", player),
                 lambda state: state.has("Zoom Tubes",player) or char_needs_tags(state, [], 150) or char_needs_tags(state, ["climbs_walls"], -1))#requires invincibilty
        add_rule(world.get_location("Egg Rock (Act 2) Spade Emblem", player),
                 lambda state: state.has("Zoom Tubes",player))

        add_rule(world.get_location("Egg Rock (Act 2) Diamond Emblem", player),
                 lambda state: state.has("Zoom Tubes",player))

        add_rule(world.get_location("Egg Rock (Act 2) Club Emblem", player),
                 lambda state: state.has("Zoom Tubes",player) and (char_needs_tags(state, ["instant_speed"], -1) or
                                char_needs_tags(state, ["free_flyer"], -1) or
                                char_needs_tags(state, ["can_hover"], -1)))

        add_rule(world.get_location("Egg Rock (Act 2) Emerald Token - Skip Gravity Pad", player),
                 lambda state: state.has("Zoom Tubes",player))

        add_rule(world.get_location("Egg Rock (Act 2) Emerald Token - Disco Room", player),
                 lambda state: state.has("Zoom Tubes",player) and char_needs_tags(state, ['fits_under_gaps'], -1))

        if options.difficulty == 0:
            add_rule(world.get_location("Egg Rock (Act 1) Heart Emblem", player),
                     lambda state:  state.has("Zoom Tubes",player) and char_needs_tags(state, [], 1000))
            add_rule(world.get_location("Egg Rock (Act 2) Heart Emblem", player),
                     lambda state: state.has("Zoom Tubes", player) and (char_needs_tags(state, ["climbs_walls"], -1) or
                                                                        char_needs_tags(state, [], 1200)))
        else:
            add_rule(world.get_location("Egg Rock (Act 1) Heart Emblem", player),
                     lambda state:  state.has("Zoom Tubes",player) and (char_needs_tags(state, [], 1000) or
                     char_needs_tags(state, ['strong_walls',"climbs_walls"], -1)))
            add_rule(world.get_location("Egg Rock (Act 2) Heart Emblem", player),
                     lambda state: state.has("Zoom Tubes", player) and (char_needs_tags(state, ["climbs_walls"], -1) or
                                                                        char_needs_tags(state, [], 1200) or
                                                                        char_needs_tags(state, ["wall_jump"], -1))
                                                                        )

        if options.time_emblems:
            add_rule(world.get_location("Egg Rock (Act 1) Time Emblem", player),
                     lambda state: state.can_reach_location("Egg Rock (Act 1) Clear", player))
            add_rule(world.get_location("Egg Rock (Act 2) Time Emblem", player),
                     lambda state: state.can_reach_location("Egg Rock (Act 2) Clear", player))
        if options.ring_emblems:
            add_rule(world.get_location("Egg Rock (Act 1) Ring Emblem", player),
                     lambda state: state.can_reach_location("Egg Rock (Act 1) Clear", player))
            add_rule(world.get_location("Egg Rock (Act 2) Ring Emblem", player),
                     lambda state: state.can_reach_location("Egg Rock (Act 2) Clear", player))

        if options.oneup_sanity:

            rf.assign_rule("Egg Rock (Act 1) Monitor - Spin Path Crushers Corner", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Egg Rock (Act 1) Monitor - Spin Path Guarded by Spincushion", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Egg Rock (Act 1) Monitor - Tails Path in Lava", "TAILS | FANG")

            rf.assign_rule("Egg Rock (Act 2) Monitor - Disco Room 1", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Egg Rock (Act 2) Monitor - Disco Room 2", "SONIC | TAILS | KNUCKLES | METAL SONIC")
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
        add_rule(world.get_location("Frozen Hillside Clear", player),
                 lambda state: (state.has("Yellow Springs",player)) or
                               char_needs_tags(state, [], 200) or
                               char_needs_tags(state, ["climbs_walls"], -1))

        add_rule(world.get_location("Frozen Hillside Star Emblem", player),
                 lambda state: (state.has("Yellow Springs", player) and char_needs_tags(state, ['fits_under_gaps'], -1)) or
                               char_needs_tags(state, ['fits_under_gaps'], 250) or
                               char_needs_tags(state, ["climbs_walls",'fits_under_gaps'], -1))
        add_rule(world.get_location("Frozen Hillside Spade Emblem", player),
                 lambda state: (state.has("Yellow Springs",player)) or
                               char_needs_tags(state, [], 200) or
                               char_needs_tags(state, ["climbs_walls"], -1))
        add_rule(world.get_location("Frozen Hillside Heart Emblem", player),
                 lambda state: (state.has("Yellow Springs",player) and char_needs_tags(state, ["weak_walls"], -1)) or
                               char_needs_tags(state, ["weak_walls"], 200) or
                               char_needs_tags(state, ["climbs_walls","weak_walls"], -1))
        add_rule(world.get_location("Frozen Hillside Diamond Emblem", player),
                 lambda state: (state.has("Yellow Springs",player) and char_needs_tags(state, [], 140)) or
                               char_needs_tags(state, [], 200) or
                               char_needs_tags(state, ["climbs_walls"], -1) or
                            (char_needs_tags(state, ["can_use_shields"], -1) and state.has("Whirlwind Shield",player)))

        if options.difficulty == 0:
            add_rule(world.get_location("Frozen Hillside Club Emblem", player),
                     lambda state:  char_needs_tags(state, ["weak_walls"], 200) or
                                   char_needs_tags(state, ["climbs_walls", "weak_walls"], -1))
        else:
            add_rule(world.get_location("Frozen Hillside Club Emblem", player),
                     lambda state: (state.has("Yellow Springs", player) and char_needs_tags(state, ["weak_walls","badnik_bounce"],-1)) or
                                   char_needs_tags(state, ["weak_walls"], 200) or
                                   char_needs_tags(state, ["climbs_walls", "weak_walls"], -1))

        if options.time_emblems:
            add_rule(world.get_location("Frozen Hillside Time Emblem", player),
                     lambda state: state.can_reach_location("Frozen Hillside Clear", player))
        if options.ring_emblems:
            add_rule(world.get_location("Frozen Hillside Ring Emblem", player),
                     lambda state: state.can_reach_location("Frozen Hillside Clear", player))

        if options.oneup_sanity:
            rf.assign_rule("Frozen Hillside Monitor - First Snow Field Behind Ice", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
            if options.difficulty == 0:
                rf.assign_rule("Frozen Hillside Monitor - Final Path Ledge Behind Ice", "SONIC+WIND | TAILS | KNUCKLES | AMY+WIND | METAL SONIC+WIND")#remove for hard
            else:
                rf.assign_rule("Frozen Hillside Monitor - Final Path Ledge Behind Ice", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")



        #pipe towers
        #yellow springs and red springs or 200jh and red springs or 800jh
        add_rule(world.get_location("Pipe Towers Clear", player),
                 lambda state: (state.has("Red Springs", player) and
                (state.has("Yellow Springs", player)) or char_needs_tags(state, ["pounds_springs"], -1) or char_needs_tags(state, [], 200) or (char_needs_tags(state, ['can_use_shields'], 130) and state.has("Whirlwind Shield", player))) or
                char_needs_tags(state, [], 800))

        add_rule(world.get_location("Pipe Towers Star Emblem", player),
                 lambda state: (state.has("Red Springs", player) and
                                (state.has("Yellow Springs", player) and char_needs_tags(state,[],200)) or (char_needs_tags(state, ['can_use_shields'], 130) and state.has("Whirlwind Shield", player))) or
                               char_needs_tags(state, [], 800))
        add_rule(world.get_location("Pipe Towers Spade Emblem", player),
                 lambda state: char_needs_tags(state, ["climbs_walls"], 200) or
                char_needs_tags(state, [], 800) or (state.has("Red Springs", player) and
                (state.has("Yellow Springs", player) and char_needs_tags(state, ["pounds_springs"], -1)) or char_needs_tags(state, ["pounds_springs"], 200) or (char_needs_tags(state, ['can_use_shields',"pounds_springs"], 130) and state.has("Whirlwind Shield", player))))
        add_rule(world.get_location("Pipe Towers Heart Emblem", player),
                 lambda state: char_needs_tags(state, ["climbs_walls"], -1) or char_needs_tags(state, ['wall_jump'], -1) or
                char_needs_tags(state, [], 1600))
        add_rule(world.get_location("Pipe Towers Diamond Emblem", player),
                 lambda state: state.can_reach_location("Pipe Towers Clear", player))
        add_rule(world.get_location("Pipe Towers Club Emblem", player),
                 lambda state: state.can_reach_location("Pipe Towers Clear", player))


        if options.difficulty == 0:
            if options.oneup_sanity:
                rf.assign_rule("Pipe Towers ? Block - Ceiling Hole Near Flowing Water", "TAILS")

        if options.time_emblems:
            add_rule(world.get_location("Pipe Towers Time Emblem", player),
                     lambda state: state.can_reach_location("Pipe Towers Clear", player))
        if options.ring_emblems:
            add_rule(world.get_location("Pipe Towers Ring Emblem", player),
                     lambda state: state.can_reach_location("Pipe Towers Clear", player))

        #none for forest fortress (yet)
        add_rule(world.get_location("Forest Fortress Clear", player),
                 lambda state: (state.has("Swinging Maces", player) and state.has("Red Springs", player)) or
                               (state.has("Red Springs", player) and char_needs_tags(state, [], 250)) or
                 char_needs_tags(state, [], 500) or
                 char_needs_tags(state, ["climbs_walls"], -1))


        add_rule(world.get_location("Forest Fortress Star Emblem", player),
                 lambda state: char_needs_tags(state, ['spin_walls'], -1))
        add_rule(world.get_location("Forest Fortress Spade Emblem", player),
                 lambda state: state.has("Swinging Maces", player) or char_needs_tags(state, [], 250) or
                 char_needs_tags(state, ["climbs_walls"], -1))
        add_rule(world.get_location("Forest Fortress Heart Emblem", player),
                 lambda state: state.has("Swinging Maces", player) or char_needs_tags(state, ['fits_under_gaps'], 250) or
                 char_needs_tags(state, ["climbs_walls",'fits_under_gaps'], -1))
        add_rule(world.get_location("Forest Fortress Diamond Emblem", player),
                 lambda state: (state.has("Swinging Maces", player) and state.has("Red Springs", player)) or
                               (state.has("Red Springs", player) and char_needs_tags(state, [], 250)) or
                 char_needs_tags(state, [], 500) or
                 char_needs_tags(state, ["climbs_walls"], -1))
        add_rule(world.get_location("Forest Fortress Club Emblem", player),
                 lambda state: (state.has("Swinging Maces", player) and state.has("Red Springs", player) and char_needs_tags(state, ['spin_walls'], -1)) or
                               (state.has("Red Springs", player) and char_needs_tags(state, ['spin_walls'], 250)) or
                 char_needs_tags(state, ['spin_walls'], 500) or
                 char_needs_tags(state, ["climbs_walls",'spin_walls'], -1))

        if options.time_emblems:
            add_rule(world.get_location("Forest Fortress Time Emblem", player),
                     lambda state: state.can_reach_location("Forest Fortress Clear", player))
        if options.ring_emblems:
            add_rule(world.get_location("Forest Fortress Ring Emblem", player),
                     lambda state: state.can_reach_location("Forest Fortress Clear", player))

        if options.oneup_sanity:
            rf.assign_rule("Forest Fortress Monitor - In Ceiling After Final Checkpoint", "KNUCKLES")
            rf.assign_rule("Forest Fortress Monitor - High Ledge Before Second Checkpoint", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")

        if options.superring_sanity:
            rf.assign_rule("Forest Fortress Monitor - x:6816 y:6656", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
            rf.assign_rule("Forest Fortress Monitor - x:6776 y:6576", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")


        add_rule(world.get_location("Final Demo Emerald Token - Greenflower (Act 1) Breakable Wall Near Bridge", player),
                 lambda state: char_needs_tags(state, ['spin_walls'], -1))
        add_rule(world.get_location("Final Demo Emerald Token - Greenflower (Act 2) Under Bridge Near End", player),
            lambda state: state.has("Red Springs", player) or char_needs_tags(state, ["climbs_walls"], -1) or char_needs_tags(state, [], 425))
        add_rule(world.get_location("Final Demo Emerald Token - Greenflower (Act 2) Underwater Cave", player),
            lambda state: (state.has("Red Springs", player) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 250))) or
                          char_needs_tags(state, ["climbs_walls"], -1) or char_needs_tags(state, [], 425))

        add_rule(world.get_location("Final Demo Emerald Token - Techno Hill (Act 1) On Pipes", player),
                 lambda state: (state.has("Red Springs", player) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 250))) or
                               char_needs_tags(state, ["climbs_walls"], -1) or
                               char_needs_tags(state, [], 425))
        add_rule(world.get_location("Final Demo Emerald Token - Techno Hill (Act 1) Alt Path Fans", player),
                 lambda state: (state.has("Red Springs", player) and (state.has("Yellow Springs", player) and char_needs_tags(state, ['fits_under_gaps'], -1)) or char_needs_tags(state, ['fits_under_gaps'], 250)) or
                               char_needs_tags(state, ["climbs_walls",'fits_under_gaps'], -1) or
                               char_needs_tags(state, ['fits_under_gaps'], 425))

        add_rule(world.get_location("Final Demo Emerald Token - Techno Hill (Act 2) Breakable Wall", player),
                 lambda state: (state.has("Red Springs", player) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 250))) or
                               char_needs_tags(state, ["climbs_walls",'fits_under_gaps'], -1) or
                               char_needs_tags(state, [], 425))
        add_rule(world.get_location("Final Demo Emerald Token - Techno Hill (Act 2) Under Poison Near End", player),
                 lambda state: (state.has("Red Springs", player) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 250))) or
                               char_needs_tags(state, ["climbs_walls",'fits_under_gaps'], -1) or
                               char_needs_tags(state, [], 425))
        add_rule(world.get_location("Final Demo Emerald Token - Castle Eggman (Act 1) Small Lake Near Start", player),
                 lambda state: (state.has("Red Springs", player) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 250))) or
                               char_needs_tags(state, ["climbs_walls",'fits_under_gaps'], -1) or
                               char_needs_tags(state, [], 425))
        add_rule(world.get_location("Final Demo Emerald Token - Castle Eggman (Act 1) Small Lake Near Start", player),
                 lambda state: (state.has("Red Springs", player) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 250))) or
                               char_needs_tags(state, ["climbs_walls",'fits_under_gaps'], -1) or
                               char_needs_tags(state, [], 425))
        add_rule(world.get_location("Final Demo Emerald Token - Castle Eggman (Act 1) Tunnel Before Act Clear", player),
                 lambda state: (state.has("Red Springs", player) and state.has("Yellow Springs", player)) or
                               char_needs_tags(state, ["climbs_walls",'fits_under_gaps'], -1) or
                               char_needs_tags(state, [], 600))
        add_rule(world.get_location("Final Demo Emerald Token - Castle Eggman (Act 2) Water Flow in Sewers", player),
                 lambda state: (state.has("Red Springs", player) and state.has("Yellow Springs", player)) or
                               char_needs_tags(state, ["climbs_walls",'fits_under_gaps'], -1) or
                               char_needs_tags(state, [], 600))
        add_rule(world.get_location("Final Demo Clear", player),
                 lambda state: (state.has("Red Springs", player) and state.has("Yellow Springs", player)) or
                               char_needs_tags(state, ["climbs_walls",'fits_under_gaps'], -1) or
                               char_needs_tags(state, [], 600))


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
        add_rule(world.get_location("Haunted Heights Clear", player),
                 lambda state:  (state.has("Buoyant Slime", player) and#FUCK THIS
                                (char_needs_tags(state,['fits_under_gaps'],100) and (state.has("Yellow Springs", player) or char_needs_tags(state,['fits_under_gaps'],300))and (state.has("Red Springs", player) or char_needs_tags(state,['fits_under_gaps'],600))) or
                                 char_needs_tags(state,['fits_under_gaps',"wall_jump"],-1) or
                                 char_needs_tags(state,['fits_under_gaps','climbs_walls'],100) or
                                 char_needs_tags(state,['fits_under_gaps','strong_walls',"climbs_walls"],-1) or
                                 (char_needs_tags(state, ['fits_under_gaps', 'strong_walls'], 300) and state.has("Red Springs", player)) or
                                 char_needs_tags(state, ['fits_under_gaps', 'strong_walls'], 1000) or
                                 (char_needs_tags(state, ['strong_floors','breaks_spikes'], -1) and (state.has("Yellow Springs", player) or char_needs_tags(state,['strong_floors','breaks_spikes'],300))and state.has("Red Springs", player))
                                 ) or (char_needs_tags(state, ['strong_floors'], 200)and state.has("Red Springs", player)) or
                                  char_needs_tags(state, ['strong_floors'], 600))
#300 Y 600 RED
#spin path (100jh,fug,rs,ys,bs
#knuxpath cw,ys(300jh),bs
        #amy Bspike rs600,ys300, sf
        #fang 200jh (rs to leave)



#alt ys(200jh) slime and zoom tube
        add_rule(world.get_location("Haunted Heights Star Emblem", player),
                 lambda state: (state.has("Yellow Springs", player) and char_needs_tags(state, ['strong_floors'], 200)) or
                 char_needs_tags(state, ["climbs_walls",'strong_floors'], -1) or
                 char_needs_tags(state, ['strong_floors'], 250))

        add_rule(world.get_location("Haunted Heights Spade Emblem", player),
                 lambda state:  (state.has("Buoyant Slime", player) and#FUCK THIS
                                (char_needs_tags(state,['fits_under_gaps'],200) and (state.has("Yellow Springs", player) or char_needs_tags(state,['fits_under_gaps'],300))and (state.has("Red Springs", player) or char_needs_tags(state,['fits_under_gaps'],600))) or
                                 char_needs_tags(state,['fits_under_gaps','climbs_walls'],100) or
                                 char_needs_tags(state,['fits_under_gaps','strong_walls',"climbs_walls"],-1) or
                                 (char_needs_tags(state, ['fits_under_gaps', 'strong_walls'], 300) and state.has("Red Springs", player)) or
                                 char_needs_tags(state, ['fits_under_gaps', 'strong_walls'], 1000) or
                                 (char_needs_tags(state, ['strong_floors','breaks_spikes'], 200) and (state.has("Yellow Springs", player) or char_needs_tags(state,['strong_floors','breaks_spikes'],300))and state.has("Red Springs", player))
                                 ) or (char_needs_tags(state, ['strong_floors'], 200)and state.has("Red Springs", player)) or
                                  char_needs_tags(state, ['strong_floors'], 600))

        add_rule(world.get_location("Haunted Heights Heart Emblem", player),
                 lambda state: (state.has("Yellow Springs", player) or char_needs_tags(state, [], 250)) and state.has("Buoyant Slime", player) and state.has("Zoom Tubes", player)
                 )
        add_rule(world.get_location("Haunted Heights Diamond Emblem", player),
                 lambda state: char_needs_tags(state, ['fits_under_gaps', 'strong_walls', "climbs_walls"], -1) or
                                char_needs_tags(state, ['fits_under_gaps', 'strong_walls'], 800)
                 )
        add_rule(world.get_location("Haunted Heights Club Emblem", player),
lambda state:  (state.has("Buoyant Slime", player) and state.has("Red Springs", player) and#FUCK THIS
                                (char_needs_tags(state,['fits_under_gaps','strong_walls',"climbs_walls","can_use_shields"],-1) and state.has("Elemental Shield", player)) or
                                char_needs_tags(state, ['fits_under_gaps', 'strong_walls', "climbs_walls", "can_stomp"], -1) or
                                (char_needs_tags(state, ['fits_under_gaps', 'strong_walls', "can_stomp","can_use_shields"],-1) and state.has("Elemental Shield", player)) or
                                 (char_needs_tags(state, ['fits_under_gaps', 'strong_walls',"can_stomp"], 300))))
        #heart emblem bullshit as knuckles
        if options.time_emblems:
            add_rule(world.get_location("Haunted Heights Time Emblem", player),
                     lambda state: state.can_reach_location("Haunted Heights Clear", player))
        if options.ring_emblems:
            add_rule(world.get_location("Haunted Heights Ring Emblem", player),
                     lambda state: state.can_reach_location("Haunted Heights Clear", player))

        if options.oneup_sanity:
            rf.assign_rule("Haunted Heights Monitor - Spin Path Spinning Maces", "SONIC | TAILS | METAL SONIC")
            rf.assign_rule("Haunted Heights Monitor - Knuckles Path Slime Under Platform", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - Near Diamond Emblem", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - Third Area High Alcove", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | FLAME") #add amy+wind on hard


            rf.assign_rule("Haunted Heights Monitor - Fang Path Breakable Floor Under Slime", "FANG")
            rf.assign_rule("Haunted Heights Monitor - Fang Path End Breakable Wall", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - First Area Highest Pillar", "TAILS | KNUCKLES | FANG") #techincally possible with wind maybe
            rf.assign_rule("Haunted Heights Monitor - First Lower Path Slime Before Checkpoint", "KNUCKLES | FANG | ELEMENTAL")

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


#2r  yellowspring(250) or rs+gs / lightning+IS 100jh

#3r 250jhys
        add_rule(world.get_location("Aerial Garden Clear", player),#laziness
                 lambda state: ((char_needs_tags(state, [], 115) or state.has("Gargoyle Statues", player)) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 300)) and state.has("Red Springs", player)) or
                        char_needs_tags(state, [], 800) or
                       char_needs_tags(state, ["climbs_walls"], -1)

                                         )
#knuckles path avoids red springs if you can climb
        add_rule(world.get_location("Aerial Garden Star Emblem", player),
                 lambda state: state.has("Yellow Springs", player) or state.has("Gargoyle Statues", player) or
                               char_needs_tags(state, ["climbs_walls"], -1) or
                               char_needs_tags(state, ["wall_jump"], -1) or
                               (char_needs_tags(state, ["can_use_shields"], -1) and state.has("Lightning Shield", player)) or
                               char_needs_tags(state, [], 115))

        add_rule(world.get_location("Aerial Garden Diamond Emblem", player),
                 lambda state: ((char_needs_tags(state, [], 115) or state.has("Gargoyle Statues", player) or (char_needs_tags(state, ["can_use_shields"], -1) and state.has("Lightning Shield", player))) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 300)) and state.has("Red Springs", player)
                                ) or ((char_needs_tags(state, ["can_use_shields",'instant_speed'], -1) and state.has("Lightning Shield", player) or char_needs_tags(state, ['can_hover'], -1)) and state.has("Yellow Springs", player)) or
                               char_needs_tags(state, [], 500) or char_needs_tags(state, ['climbs_walls'], -1)
                 )

        add_rule(world.get_location("Aerial Garden Heart Emblem", player),
                 lambda state: ((char_needs_tags(state, [], 115) or state.has("Gargoyle Statues", player) or (char_needs_tags(state, ["can_use_shields"], -1) and state.has("Lightning Shield", player))) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 300)) and state.has("Red Springs", player)) or
                               char_needs_tags(state, [], 700) or char_needs_tags(state, ['climbs_walls'], -1)

                 )
        add_rule(world.get_location("Aerial Garden Club Emblem", player),#laziness
                 lambda state: state.can_reach_location("Aerial Garden Clear",player))



        add_rule(world.get_location("Aerial Garden Emerald Token - First Room High Tower", player),
                 lambda state: state.has("Yellow Springs", player) or char_needs_tags(state,[],600) or char_needs_tags(state,["climbs_walls"],-1))

        add_rule(world.get_location("Aerial Garden Emerald Token - Underwater on Pillar", player),#laziness
                 lambda state: state.can_reach_location("Aerial Garden Clear",player))

        add_rule(world.get_location("Aerial Garden Emerald Token - Diamond Emblem 1", player),#laziness
                 lambda state: state.can_reach_location("Aerial Garden Diamond Emblem",player))
        add_rule(world.get_location("Aerial Garden Emerald Token - Diamond Emblem 2", player),#laziness
                 lambda state: state.can_reach_location("Aerial Garden Diamond Emblem",player))
        add_rule(world.get_location("Aerial Garden Emerald Token - Diamond Emblem 3", player),#laziness
                 lambda state: state.can_reach_location("Aerial Garden Diamond Emblem",player))
        add_rule(world.get_location("Aerial Garden Emerald Token - Diamond Emblem 4", player),#laziness
                 lambda state: state.can_reach_location("Aerial Garden Diamond Emblem",player))

        if options.difficulty == 0:
            rf.assign_rule("Aerial Garden Club Emblem", "TAILS | METAL SONIC") # easy logic
            rf.assign_rule("Aerial Garden Diamond Emblem", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Spade Emblem", "FANG & LIGHTNING")
            rf.assign_rule("Aerial Garden Emerald Token - Diamond Emblem 1", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Emerald Token - Diamond Emblem 2", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Emerald Token - Diamond Emblem 3", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Emerald Token - Diamond Emblem 4", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Heart Emblem", "TAILS | METAL SONIC") # easy
        else:
            add_rule(world.get_location("Aerial Garden Spade Emblem", player),
                 lambda state: ((char_needs_tags(state, ['strong_floors'], 200)) and (state.has("Yellow Springs", player) or char_needs_tags(state, [], 300)) and state.has("Red Springs", player)
                                ) or ((char_needs_tags(state, ["can_use_shields",'instant_speed','strong_floors'], -1) and state.has("Lightning Shield", player) or char_needs_tags(state, ['can_hover','strong_floors'], -1)) and state.has("Yellow Springs", player)) or
                               char_needs_tags(state, ['strong_floors'], 500) or char_needs_tags(state, ['climbs_walls','strong_floors'], -1)
                 )
        if options.time_emblems:
            add_rule(world.get_location("Aerial Garden Time Emblem", player),
                     lambda state: state.can_reach_location("Aerial Garden Clear", player))
        if options.ring_emblems:
            add_rule(world.get_location("Aerial Garden Ring Emblem", player),
                     lambda state: state.can_reach_location("Aerial Garden Clear", player))


        if options.oneup_sanity:
            rf.assign_rule("Aerial Garden Monitor - Triangle Hallway Spin Under Seaweed", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Aerial Garden Monitor - Path Left 6 Waterfall Top 1", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Aerial Garden Monitor - Path Left 2 Spin Into Bushes", "SONIC | TAILS | KNUCKLES | METAL SONIC")

            if options.difficulty == 0:
                rf.assign_rule("Aerial Garden Monitor - Path Left 5 Thin Platforms Top 1", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Path Right 1 Across Moving Platforms", "TAILS | KNUCKLES | METAL SONIC | LIGHTNING")
                rf.assign_rule("Aerial Garden Monitor - Path Right 5 Vertical Moving Platforms", "TAILS | METAL SONIC | LIGHTNING")
                rf.assign_rule("Aerial Garden Monitor - Path Left 5 Top Cave Clearing", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Near Heart Emblem 1", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Near Heart Emblem 2", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Near Heart Emblem 3", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Near Heart Emblem 4", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Path Left 5 High Thin Platforms", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Triangle Hallway Rafters 1", "TAILS | KNUCKLES | METAL SONIC | LIGHTNING")
                rf.assign_rule("Aerial Garden Monitor - Path Right 2 Tiny Platform", "TAILS | KNUCKLES")

            else:
                rf.assign_rule("Aerial Garden Monitor - Path Right 2 Tiny Platform", "TAILS | KNUCKLES | AMY & LIGHTNING | FANG")
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







        if options.difficulty == 0:

            add_rule(world.get_location("Azure Temple Clear", player),
                     lambda state: (state.has("Air Bubbles", player)))

            add_rule(world.get_location("Azure Temple Star Emblem", player),
                     lambda state: (state.has("Air Bubbles", player)) and state.has("Bubble Shield", player) and (
                             char_needs_tags(state, ["free_flyer"], 1400) or
                             char_needs_tags(state, ["climbs_walls"], 100) or
                             (char_needs_tags(state, ["climbs_walls", "can_use_shields"], 100) and state.has(
                                 "Bubble Shield", player))
                     ))
            add_rule(world.get_location("Azure Temple Spade Emblem", player),
                     lambda state: (state.has("Air Bubbles", player)) and (
                         char_needs_tags(state, ["free_flyer"], 1400)))
            add_rule(world.get_location("Azure Temple Heart Emblem", player),  # no air needed
                     lambda state: (state.has("Air Bubbles", player)) and (
                         char_needs_tags(state, ['fits_under_gaps'], -1)))

            add_rule(world.get_location("Azure Temple Diamond Emblem", player),  # no air needed
                     lambda state: state.has("Air Bubbles", player) and (
                             char_needs_tags(state, ['fits_under_gaps'], -1) or (
                                 char_needs_tags(state, ['strong_floors'], -1) and state.has("Yellow Springs",player)) or char_needs_tags(state, ['strong_floors'], 400)))

            add_rule(world.get_location("Azure Temple Club Emblem", player),
                     lambda state: state.has("Air Bubbles", player) and state.count("Chaos Emerald",player)>6 and
                         char_needs_tags(state, ["can_use_shields"], -1) and state.has("Armageddon Shield", player))


            if options.time_emblems:
                rf.assign_rule("Azure Temple Time Emblem", "TAILS | METAL SONIC")
            if options.ring_emblems:
                rf.assign_rule("Azure Temple Ring Emblem","TAILS/METAL SONIC & FORCE/BUBBLE | KNUCKLES+BUBBLE")

            # easy version
        else:
            add_rule(world.get_location("Azure Temple Clear", player),
                     lambda state: (state.has("Air Bubbles", player)))

            add_rule(world.get_location("Azure Temple Star Emblem", player),
                     lambda state: (state.has("Air Bubbles", player) or state.has("Bubble Shield", player)) and (
                             char_needs_tags(state, ["free_flyer"], 1400) or
                             char_needs_tags(state, ["climbs_walls"], 100) or
                             (char_needs_tags(state, ["climbs_walls", "can_use_shields"], 100) and state.has(
                                 "Bubble Shield", player))
                     ))
            add_rule(world.get_location("Azure Temple Spade Emblem", player),
                     lambda state: (state.has("Air Bubbles", player) or state.has("Bubble Shield", player)) and (
                         char_needs_tags(state, ["free_flyer"], 1400)))
            add_rule(world.get_location("Azure Temple Heart Emblem", player),  # no air needed
                     lambda state:  (
                         char_needs_tags(state, ['fits_under_gaps'], -1)))

            add_rule(world.get_location("Azure Temple Diamond Emblem", player),
                     lambda state: (state.has("Air Bubbles", player) or state.has("Bubble Shield", player)) and (
                             char_needs_tags(state, ['fits_under_gaps'], -1) or (
                                 char_needs_tags(state, ['strong_floors'], -1) and state.has("Yellow Springs",player)) or char_needs_tags(state, ['strong_floors'], 400)))
            add_rule(world.get_location("Azure Temple Club Emblem", player),  # no air needed
                     lambda state: state.has("Air Bubbles", player) and (
                         char_needs_tags(state, ["can_use_shields"], -1)) and state.has("Armageddon Shield", player))

        if options.time_emblems:
            add_rule(world.get_location("Azure Temple Time Emblem", player),
                     lambda state: state.can_reach_location("Azure Temple Clear", player))
        if options.ring_emblems:
            add_rule(world.get_location("Azure Temple Ring Emblem", player),
                     lambda state: state.can_reach_location("Azure Temple Clear", player))

        if options.oneup_sanity:
            rf.assign_rule("Azure Temple Monitor - Rafters Near Spade Emblem 1", "TAILS | KNUCKLES")
            rf.assign_rule("Azure Temple Monitor - Near Star Emblem", "TAILS | KNUCKLES & BUBBLE")
            rf.assign_rule("Azure Temple Monitor - Near Club Emblem 1","ARMAGEDDON")
            rf.assign_rule("Azure Temple Monitor - Near Club Emblem 2","ARMAGEDDON")
            rf.assign_rule("Azure Temple Monitor - Near Club Emblem 3","ARMAGEDDON")
            rf.assign_rule("Azure Temple Monitor - Near Heart Emblem 1", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Azure Temple Monitor - Bottom Path Side of Statue Hallway", "SONIC | TAILS | BUBBLE | AMY | FANG | METAL SONIC")
            if options.difficulty == 0:
                rf.assign_rule("Azure Temple Monitor - Main Path High Rocky Ledge", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - Bottom Path Buggle Room Rafters", "TAILS | KNUCKLES+BUBBLE | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - Top Path High Ledge Behind Bars", "TAILS | KNUCKLES+BUBBLE | FANG")
                rf.assign_rule("Azure Temple Monitor - Top Path Near Spiked Platform Ledge 1", "TAILS | KNUCKLES | FANG")
                rf.assign_rule("Azure Temple Monitor - Action Nospin Path Ledge After Spring", "TAILS | KNUCKLES | FANG")

            else:

                rf.assign_rule("Azure Temple Monitor - Bottom Path Buggle Room Rafters","SONIC | TAILS | BUBBLE | AMY | FANG | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - Top Path High Ledge Behind Bars","TAILS | KNUCKLES+BUBBLE | AMY+BUBBLE | FANG")
                rf.assign_rule("Azure Temple Monitor - Top Path Near Spiked Platform Ledge 1", "TAILS | KNUCKLES | AMY+BUBBLE | FANG")
                rf.assign_rule("Azure Temple Monitor - Action Nospin Path Ledge After Spring", "TAILS | KNUCKLES | AMY+BUBBLE | FANG")

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





        if options.nights_maps:
            #special stages
            if options.difficulty == 0:
                rf.assign_rule("Cavern Fortress Sun Emblem", "PARALOOP")
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
        world.completion_condition[player] = lambda state: state.can_reach("Black Core Zone 3", 'Region', player)
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
    if options.nights_maps:
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


            rf.assign_rule("Deep Sea (Act 1) Monitor - Waterslide Hidden Spring Room", "TAILS | KNUCKLES | FANG | WIND")
            rf.assign_rule("Deep Sea (Act 1) Monitor - Waterfall Cave Opposite Spade Emblem", "TAILS | KNUCKLES | METAL SONIC | WIND")
            rf.assign_rule("Deep Sea (Act 1) Monitor - Broken Wall Near End", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | WIND")
            rf.assign_rule("Deep Sea (Act 1) Monitor - Yellow Switch", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Deep Sea (Act 1) Monitor - Left Path Waterfall Cave", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Deep Sea (Act 1) Monitor - Right Right Subpath Breakable Wall Between Columns", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")

            #"Deep Sea (Act 1) Monitor - x:8640 y:3168" - maybe at least require wind for normal - have to check other emblems if so (Club emblem) (NAH)

            rf.assign_rule("Deep Sea (Act 2) Monitor - Spindash Fast Door 1", "SONIC | KNUCKLES")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Spindash Fast Door 2", "SONIC | KNUCKLES")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Spindash Fast Door 3", "SONIC | KNUCKLES")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Gargoyle Path Wall Under Oval Platform", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Main Path Roll Down Ramp Into Breakable Wall", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Knuckles Path Dark High Ledge", "KNUCKLES | AMY")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Knuckles Path Crushing Ceiling", "KNUCKLES | AMY")
            rf.assign_rule("Deep Sea (Act 2) Monitor - Near Club Emblem", "TAILS | KNUCKLES")


            if options.difficulty == 0:
                rf.assign_rule("Deep Sea (Act 1) Monitor - Heart Emblem Backtrack to Club 1","TAILS | KNUCKLES")  # heart emblem club emblem opened bullshit
                rf.assign_rule("Deep Sea (Act 1) Monitor - Heart Emblem Backtrack to Club 2","TAILS | KNUCKLES")  # heart emblem club emblem opened bullshit
                rf.assign_rule("Deep Sea (Act 2) Monitor - Gargoyle Path Spiked Cliff Top", "TAILS | KNUCKLES | FANG")
                rf.assign_rule("Deep Sea (Act 1) Monitor - Behind Fast Closing Door 1", "METAL SONIC")
                rf.assign_rule("Deep Sea (Act 1) Monitor - Behind Fast Closing Door 2","METAL SONIC")
            else:
                rf.assign_rule("Deep Sea (Act 1) Monitor - Heart Emblem Backtrack to Club 1","TAILS | KNUCKLES | WIND")  # heart emblem club emblem opened bullshit
                rf.assign_rule("Deep Sea (Act 1) Monitor - Heart Emblem Backtrack to Club 2","TAILS | KNUCKLES | WIND")  # heart emblem club emblem opened bullshit

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
        if options.difficulty == 0:
            rf.assign_rule("Castle Eggman (Act 2) Club Emblem", "TAILS | KNUCKLES | FANG | WIND")
        if options.oneup_sanity:
            rf.assign_rule("Castle Eggman (Act 2) Monitor - Rafter Above Starting Area", "TAILS | KNUCKLES")
            rf.assign_rule("Castle Eggman (Act 2) Monitor - High Bookshelf Before Final Tower", "TAILS | KNUCKLES | AMY")
            rf.assign_rule("Castle Eggman (Act 2) Monitor - Front Left Path High Ledge Before Swinging Chains", "TAILS | KNUCKLES")
            rf.assign_rule("Castle Eggman (Act 2) Monitor - Right Path Thin Gray Bookshelf Top", "TAILS | KNUCKLES | WIND")


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
            rf.assign_rule("Arid Canyon (Act 1) Monitor - Main Area High Broken Road", "SONIC | TAILS | KNUCKLES | METAL SONIC | WIND")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - TNT Path High Above Exploding Plank", "TAILS | KNUCKLES | AMY+WIND")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - Near Amy Emerald Token", "AMY")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - Final Section Under Ceiling Near Checkpoint", "TAILS | KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - End of TNT Path Above Cave", "TAILS | KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - High Ledge Near Start", "SONIC | TAILS | KNUCKLES | METAL SONIC | WIND")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - Left Cliffside Ledge From Start","SONIC | TAILS | KNUCKLES | METAL SONIC | WIND")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - Canarivore Path Half Pipe Top Middle","SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - Left Path Moving Platform Knuckles Wall", "KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - Left Path High Ledge Cave", "TAILS | KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - End Of Left Knuckles Path Around Corner 1", "KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - Near Heart Emblem 1", "KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - Very High Ledge Between Left and Looping Path", "TAILS | KNUCKLES")

            if options.difficulty == 0:
                rf.assign_rule("Arid Canyon (Act 2) Monitor - Behind TNT Crates Near Spade Emblem","TAILS | KNUCKLES | AMY | FANG")
                rf.assign_rule("Arid Canyon (Act 2) Monitor - TNT Barrel Ledge Near Star Emblem","TAILS | KNUCKLES | AMY | FANG")
            else:
                rf.assign_rule("Arid Canyon (Act 2) Monitor - TNT Barrel Ledge Near Star Emblem","TAILS | KNUCKLES | AMY | FANG | WIND")


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
        rf.assign_rule("Red Volcano (Act 1) Emerald Token - Hidden Ledge Near 4th Checkpoint", "TAILS | FANG | WIND")


        if options.difficulty == 0:
            rf.assign_rule("Red Volcano (Act 1) Emerald Token - First Outside Area","TAILS | KNUCKLES | METAL SONIC | WIND")
        else:
            rf.assign_rule("Red Volcano (Act 1) Emerald Token - First Outside Area","SONIC | TAILS | KNUCKLES | METAL SONIC | WIND")
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

            rf.assign_rule("Egg Rock (Act 1) Monitor - Spin Path Crushers Corner", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Egg Rock (Act 1) Monitor - Spin Path Guarded by Spincushion", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Egg Rock (Act 1) Monitor - Tails Path in Lava", "TAILS | FANG")

            rf.assign_rule("Egg Rock (Act 2) Monitor - Disco Room 1", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Egg Rock (Act 2) Monitor - Disco Room 2", "SONIC | TAILS | KNUCKLES | METAL SONIC")
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
            rf.assign_rule("Forest Fortress Monitor - In Ceiling After Final Checkpoint", "KNUCKLES")
            rf.assign_rule("Forest Fortress Monitor - High Ledge Before Second Checkpoint", "SONIC | TAILS | KNUCKLES | AMY | METAL SONIC")

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
            rf.assign_rule("Haunted Heights Monitor - Spin Path Spinning Maces", "SONIC | TAILS | METAL SONIC")
            rf.assign_rule("Haunted Heights Monitor - Knuckles Path Slime Under Platform", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - Near Diamond Emblem", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - Third Area High Alcove", "SONIC | TAILS | KNUCKLES | FANG | METAL SONIC | FLAME") #add amy+wind on hard


            rf.assign_rule("Haunted Heights Monitor - Fang Path Breakable Floor Under Slime", "FANG")
            rf.assign_rule("Haunted Heights Monitor - Fang Path End Breakable Wall", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - First Area Highest Pillar", "TAILS | KNUCKLES | FANG") #techincally possible with wind maybe
            rf.assign_rule("Haunted Heights Monitor - First Lower Path Slime Before Checkpoint", "KNUCKLES | FANG | ELEMENTAL")

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
            rf.assign_rule("Aerial Garden Monitor - Triangle Hallway Spin Under Seaweed", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Aerial Garden Monitor - Path Left 6 Waterfall Top 1", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Aerial Garden Monitor - Path Left 2 Spin Into Bushes", "SONIC | TAILS | KNUCKLES | METAL SONIC")

            if options.difficulty == 0:
                rf.assign_rule("Aerial Garden Monitor - Path Left 5 Thin Platforms Top 1", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Path Right 1 Across Moving Platforms", "TAILS | KNUCKLES | METAL SONIC | LIGHTNING")
                rf.assign_rule("Aerial Garden Monitor - Path Right 5 Vertical Moving Platforms", "TAILS | METAL SONIC | LIGHTNING")
                rf.assign_rule("Aerial Garden Monitor - Path Left 5 Top Cave Clearing", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Near Heart Emblem 1", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Near Heart Emblem 2", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Near Heart Emblem 3", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Near Heart Emblem 4", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Path Left 5 High Thin Platforms", "TAILS | METAL SONIC")
                rf.assign_rule("Aerial Garden Monitor - Triangle Hallway Rafters 1", "TAILS | KNUCKLES | METAL SONIC | LIGHTNING")
                rf.assign_rule("Aerial Garden Monitor - Path Right 2 Tiny Platform", "TAILS | KNUCKLES")

            else:
                rf.assign_rule("Aerial Garden Monitor - Path Right 2 Tiny Platform", "TAILS | KNUCKLES | AMY & LIGHTNING | FANG")
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
            rf.assign_rule("Azure Temple Monitor - Rafters Near Spade Emblem 1", "TAILS | KNUCKLES")
            rf.assign_rule("Azure Temple Monitor - Near Star Emblem", "TAILS | KNUCKLES & BUBBLE")
            rf.assign_rule("Azure Temple Monitor - Near Club Emblem 1","ARMAGEDDON")
            rf.assign_rule("Azure Temple Monitor - Near Club Emblem 2","ARMAGEDDON")
            rf.assign_rule("Azure Temple Monitor - Near Club Emblem 3","ARMAGEDDON")
            rf.assign_rule("Azure Temple Monitor - Near Heart Emblem 1", "SONIC | TAILS | KNUCKLES | METAL SONIC")
            rf.assign_rule("Azure Temple Monitor - Bottom Path Side of Statue Hallway", "SONIC | TAILS | BUBBLE | AMY | FANG | METAL SONIC")
            if options.difficulty == 0:
                rf.assign_rule("Azure Temple Monitor - Main Path High Rocky Ledge", "TAILS | KNUCKLES | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - Bottom Path Buggle Room Rafters", "TAILS | KNUCKLES+BUBBLE | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - Top Path High Ledge Behind Bars", "TAILS | KNUCKLES+BUBBLE | FANG")
                rf.assign_rule("Azure Temple Monitor - Top Path Near Spiked Platform Ledge 1", "TAILS | KNUCKLES | FANG")
                rf.assign_rule("Azure Temple Monitor - Action Nospin Path Ledge After Spring", "TAILS | KNUCKLES | FANG")

            else:

                rf.assign_rule("Azure Temple Monitor - Bottom Path Buggle Room Rafters","SONIC | TAILS | BUBBLE | AMY | FANG | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - Top Path High Ledge Behind Bars","TAILS | KNUCKLES+BUBBLE | AMY+BUBBLE | FANG")
                rf.assign_rule("Azure Temple Monitor - Top Path Near Spiked Platform Ledge 1", "TAILS | KNUCKLES | AMY+BUBBLE | FANG")
                rf.assign_rule("Azure Temple Monitor - Action Nospin Path Ledge After Spring", "TAILS | KNUCKLES | AMY+BUBBLE | FANG")

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





        if options.nights_maps:
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

