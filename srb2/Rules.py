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
    if options.bcz_emblems==0:
        connect_regions(world, player, "Menu", "Black Core Zone", lambda state: state.has("Black Core Zone", player))
    else:
        connect_regions(world, player, "Menu", "Black Core Zone", lambda state: state.has("Emblem", player, options.bcz_emblems))

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
    # TODO add emerald token logic and other zones
    if options.difficulty != 2:
        # Greenflower
        if options.difficulty == 0:
            rf.assign_rule("Greenflower (Act 1) Heart Emblem", "TAILS")

        rf.assign_rule("Greenflower (Act 2) Heart Emblem", "AMY")
        rf.assign_rule("Greenflower (Act 2) Diamond Emblem", "KNUCKLES")
        rf.assign_rule("Greenflower (Act 2) Emerald Token - No Spin High on Ledge", "AMY | FANG")

        if options.oneup_sanity:
            rf.assign_rule("Greenflower (Act 1) Monitor - x:1184 y:5824","TAILS | KNUCKLES | WIND")
            rf.assign_rule("Greenflower (Act 2) Monitor - x:-480 y:-4480", "AMY | FANG")
            rf.assign_rule("Greenflower (Act 2) Monitor - x:188 y:-347", "TAILS | KNUCKLES")
            if options.difficulty == 0:
                rf.assign_rule("Greenflower (Act 2) Monitor - x:3296 y:6624", "TAILS | KNUCKLES | METAL SONIC") #Possible as sonic but stupid
                rf.assign_rule("Greenflower (Act 2) Monitor - x:720 y:-10320", "TAILS | KNUCKLES") #ditto above





        # Techno Hill

        rf.assign_rule("Techno Hill (Act 1) Spade Emblem", "ELEMENTAL")
        rf.assign_rule("Techno Hill (Act 1) Heart Emblem", "TAILS")
        rf.assign_rule("Techno Hill (Act 1) Diamond Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Techno Hill (Act 1) Club Emblem", "KNUCKLES")
        rf.assign_rule("Techno Hill (Act 2) Emerald Token - Deep in Slime", "ELEMENTAL")
        rf.assign_rule("Techno Hill (Act 2) Emerald Token - Knuckles Path Backtrack as Amy", "AMY")
        if options.difficulty == 0:
            rf.assign_rule("Techno Hill (Act 1) Star Emblem", "TAILS | KNUCKLES")  # INTENDED SONIC PATH FOR THIS BTW

        if options.oneup_sanity:
            rf.assign_rule("Techno Hill (Act 1) Monitor - x:-3904 y:-12224", "TAILS | KNUCKLES")
            rf.assign_rule("Techno Hill (Act 1) Monitor - x:14400 y:-6208", "TAILS | KNUCKLES")
            rf.assign_rule("Techno Hill (Act 2) Monitor - x:-11584 y:-4768","KNUCKLES")
            rf.assign_rule("Techno Hill (Act 2) Monitor - x:832 y:-6144", "ELEMENTAL | KNUCKLES | FANG")
            rf.assign_rule("Techno Hill (Act 2) Monitor - x:-16000 y:-6464", "AMY")
            rf.assign_rule("Techno Hill (Act 2) Monitor - x:4128 y:-224", "TAILS | KNUCKLES")#probably possible as sonic
            if options.difficulty == 0:
                rf.assign_rule("Techno Hill (Act 1) Monitor - x:2976 y:4384", "TAILS | KNUCKLES")#INTENDED SONIC PATH FOR THIS BTW
                rf.assign_rule("Techno Hill (Act 2) Monitor - x:0 y:2240","TAILS | KNUCKLES | FANG | WIND")  # or 7 emeralds
                rf.assign_rule("Techno Hill (Act 2) Monitor - x:-2048 y:-7872", "ELEMENTAL | KNUCKLES | FANG")
            else:
                rf.assign_rule("Techno Hill (Act 2) Monitor - x:0 y:2240","TAILS | KNUCKLES | AMY | FANG | WIND")  # or 7 emeralds

        # Deep Sea
        rf.assign_rule("Deep Sea (Act 1) Star Emblem", "AMY")
        rf.assign_rule("Deep Sea (Act 1) Spade Emblem", "TAILS | KNUCKLES | METAL SONIC | WIND")

        rf.assign_rule("Deep Sea (Act 2) Star Emblem", "AMY | FANG")
        rf.assign_rule("Deep Sea (Act 2) Spade Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Deep Sea (Act 2) Diamond Emblem", "KNUCKLES")
        rf.assign_rule("Deep Sea (Act 2) Club Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Deep Sea (Act 2) Emerald Token - No Spin Spring Turnaround", "AMY | FANG")
        if options.difficulty == 0:
            rf.assign_rule("Deep Sea (Act 1) Heart Emblem", "TAILS | KNUCKLES")
        if options.oneup_sanity:

            rf.assign_rule("Deep Sea (Act 1) Monitor - x:3104 y:15520", "METAL SONIC & EMERALD")
            rf.assign_rule("Deep Sea (Act 1) Monitor - x:3296 y:15520", "METAL SONIC & EMERALD")
            rf.assign_rule("Deep Sea (Act 1) Monitor - x:10304 y:-736", "TAILS | KNUCKLES | FANG | WIND")
            rf.assign_rule("Deep Sea (Act 1) Monitor - x:5088 y:11872", "TAILS | KNUCKLES | METAL SONIC | WIND")
            #"Deep Sea (Act 1) Monitor - x:8640 y:3168" - maybe at least require wind for normal - have to check other emblems if so (Club emblem) (NAH)
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:19264 y:-5888", "KNUCKLES | AMY")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:19072 y:-10816", "KNUCKLES | AMY")
            rf.assign_rule("Deep Sea (Act 2) Monitor - x:15808 y:2816", "TAILS | KNUCKLES")
            if options.difficulty == 0:
                rf.assign_rule("Deep Sea (Act 1) Monitor - x:11008 y:5696","TAILS | KNUCKLES")  # heart emblem club emblem opened bullshit
                rf.assign_rule("Deep Sea (Act 1) Monitor - x:10880 y:5568","TAILS | KNUCKLES")  # heart emblem club emblem opened bullshit
                rf.assign_rule("Deep Sea (Act 2) Monitor - x:9568 y:16992", "TAILS | KNUCKLES | FANG")






        # Castle Eggman
        rf.assign_rule("Castle Eggman (Act 1) Star Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Castle Eggman (Act 2) Diamond Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Castle Eggman (Act 2) Club Emblem", "TAILS | KNUCKLES | FANG | WIND")
        if options.oneup_sanity:
            rf.assign_rule("Castle Eggman (Act 2) Monitor - x:0 y:-21760", "TAILS | KNUCKLES")
            rf.assign_rule("Castle Eggman (Act 2) Monitor - x:2112 y:-320", "TAILS | KNUCKLES")
            rf.assign_rule("Castle Eggman (Act 2) Monitor - x:3072 y:-16128", "TAILS | KNUCKLES")
            rf.assign_rule("Castle Eggman (Act 2) Monitor - x:12416 y:768", "TAILS | KNUCKLES | WIND")

        #"Castle Eggman (Act 2) Monitor - x:-3584 y:-14720" "directly above another monitor >:("

        # Arid Canyon
        rf.assign_rule("Arid Canyon (Act 1) Star Emblem", "TAILS | KNUCKLES | AMY")
        rf.assign_rule("Arid Canyon (Act 2) Spade Emblem", "AMY | FANG")
        rf.assign_rule("Arid Canyon (Act 2) Heart Emblem", "KNUCKLES")
        rf.assign_rule("Arid Canyon (Act 2) Diamond Emblem", "FANG")
        rf.assign_rule("Arid Canyon (Act 2) Club Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Arid Canyon (Act 1) Emerald Token - Behind Wall and Spikes", "AMY")
        rf.assign_rule("Arid Canyon (Act 2) Emerald Token - Left No Spin Path Minecarts", "AMY | FANG")
        rf.assign_rule("Arid Canyon (Act 2) Emerald Token - Knuckles Dark Path Around Wall", "KNUCKLES | AMY & WIND")
        if options.difficulty == 0:
            rf.assign_rule("Arid Canyon (Act 2) Star Emblem", "AMY | FANG | TAILS | KNUCKLES")#possible as sonic by fucky jump

        if options.oneup_sanity:
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:-6592 y:-2896", "TAILS | KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:2816 y:-992", "AMY")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:-5184 y:14912", "TAILS | KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 1) Monitor - x:-11200 y:992", "TAILS | KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-10144 y:-4640", "KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:160 y:-10784", "TAILS | KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:2240 y:-15456", "KNUCKLES | AMY")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-7088 y:-13824", "KNUCKLES")
            rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-4992 y:-7744", "TAILS | KNUCKLES")
            if options.difficulty == 0:
                rf.assign_rule("Arid Canyon (Act 2) Monitor - x:2752 y:-9776","TAILS | KNUCKLES | AMY | FANG")
                rf.assign_rule("Arid Canyon (Act 2) Monitor - x:-1408 y:-14976", "TAILS | KNUCKLES | AMY | FANG")

        # Red Volcano
        rf.assign_rule("Red Volcano (Act 1) Spade Emblem", "TAILS")
        rf.assign_rule("Red Volcano (Act 1) Emerald Token - First Outside Area", "TAILS | KNUCKLES | METAL SONIC | WIND")
        rf.assign_rule("Red Volcano (Act 1) Emerald Token - Hidden Ledge Near 4th Checkpoint", "TAILS | WIND")
        #no 1up rules in rvz

        # Egg Rock
        rf.assign_rule("Egg Rock (Act 1) Spade Emblem", "TAILS")
        rf.assign_rule("Egg Rock (Act 1) Heart Emblem", "TAILS")
        if options.oneup_sanity:
            rf.assign_rule("Egg Rock (Act 1) Monitor - x:6144 y:-2112", "TAILS")
            rf.assign_rule("Egg Rock (Act 2) Monitor - x:11136 y:15456", "TAILS | KNUCKLES | FANG")



        # Black Core - Nothing until rolling/objects are locked

        # Frozen Hillside/ other bonus stages go here
        rf.assign_rule("Frozen Hillside Diamond Emblem", "TAILS | KNUCKLES | WIND")
        if options.difficulty == 0:
            rf.assign_rule("Frozen Hillside Club Emblem", "TAILS | KNUCKLES | WIND")
            
        if options.oneup_sanity:
            if options.difficulty == 0:
                rf.assign_rule("Frozen Hillside Monitor - x:-2944 y:-19168", "TAILS | KNUCKLES | WIND")#remove for hard


        #pipe towers
        rf.assign_rule("Pipe Towers Star Emblem", "TAILS | FANG | WIND")
        rf.assign_rule("Pipe Towers Spade Emblem", "TAILS | KNUCKLES")
        rf.assign_rule("Pipe Towers Heart Emblem", "KNUCKLES")

        if options.difficulty == 0:
            if options.oneup_sanity:
                rf.assign_rule("Pipe Towers Monitor - x:7000 y:6520", "TAILS")



        #none for forest fortress (yet)
        if options.oneup_sanity:
            rf.assign_rule("Forest Fortress Monitor - x:5824 y:8368", "KNUCKLES")

        if options.oneup_sanity:
            rf.assign_rule("Final Demo Monitor - x:-9312 y:-20512", "TAILS | KNUCKLES")
            rf.assign_rule("Final Demo Monitor - x:27520 y:7552", "TAILS | KNUCKLES")
            rf.assign_rule("Final Demo Monitor - x:27712 y:7360", "TAILS | KNUCKLES")
            rf.assign_rule("Final Demo Monitor - x:24448 y:12352", "TAILS | KNUCKLES")

        # haunted heights
        rf.assign_rule("Haunted Heights Star Emblem", "FANG")
        rf.assign_rule("Haunted Heights Spade Emblem", "TAILS | KNUCKLES | FANG")
        rf.assign_rule("Haunted Heights Diamond Emblem", "KNUCKLES")
        rf.assign_rule("Haunted Heights Club Emblem", "KNUCKLES & ELEMENTAL")
        if options.oneup_sanity:
            rf.assign_rule("Haunted Heights Monitor - x:4288 y:12240", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - x:6080 y:11872", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - x:7648 y:24160", "AMY | FANG")
            rf.assign_rule("Haunted Heights Monitor - x:-3008 y:20720", "KNUCKLES")
            rf.assign_rule("Haunted Heights Monitor - x:1792 y:2656", "TAILS | KNUCKLES | FANG") #techincally possible with wind maybe
            rf.assign_rule("Haunted Heights Monitor - x:8254 y:11910", "KNUCKLES | FANG | ELEMENTAL")


        rf.assign_rule("Aerial Garden Spade Emblem", "FANG")
        if options.difficulty == 0:
            rf.assign_rule("Aerial Garden Club Emblem", "TAILS | METAL SONIC") # easy logic
            rf.assign_rule("Aerial Garden Diamond Emblem", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Emerald Token - Diamond Emblem 1", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Emerald Token - Diamond Emblem 2", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Emerald Token - Diamond Emblem 3", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Emerald Token - Diamond Emblem 4", "TAILS | METAL SONIC") # easy
            rf.assign_rule("Aerial Garden Heart Emblem", "TAILS | METAL SONIC") # easy
            if options.time_emblems:
                rf.assign_rule("Aerial Garden Time Emblem", "TAILS | METAL SONIC | LIGHTNING") #BS as sonic
            if options.ring_emblems:
                rf.assign_rule("Aerial Garden Ring Emblem", "TAILS | METAL SONIC | LIGHTNING") #BS as sonic

        if options.oneup_sanity:
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



        rf.assign_rule("Azure Temple Star Emblem", "TAILS | KNUCKLES & BUBBLE")
        rf.assign_rule("Azure Temple Spade Emblem", "TAILS")
        if options.difficulty == 0:
            if options.time_emblems:
                rf.assign_rule("Azure Temple Time Emblem", "TAILS | METAL SONIC")
            if options.ring_emblems:
                rf.assign_rule("Azure Temple Ring Emblem","TAILS/METAL SONIC & FORCE/BUBBLE | KNUCKLES+BUBBLE")
            rf.assign_rule("Azure Temple Club Emblem", "ARMAGEDDON & EMERALD")  # easy version
        else:
            rf.assign_rule("Azure Temple Club Emblem", "ARMAGEDDON")


        if options.oneup_sanity:
            rf.assign_rule("Azure Temple Monitor - x:512 y:14016", "TAILS | KNUCKLES")
            rf.assign_rule("Azure Temple Monitor - x:-2528 y:7296", "TAILS | KNUCKLES & BUBBLE")
            if options.difficulty == 0:
                rf.assign_rule("Azure Temple Monitor - x:1440 y:14688", "TAILS | KNUCKLES+BUBBLE | METAL SONIC")
                rf.assign_rule("Azure Temple Monitor - x:-2272 y:12864", "TAILS | KNUCKLES+BUBBLE | FANG")
                rf.assign_rule("Azure Temple Monitor - x:-3232 y:14112", "TAILS | KNUCKLES | FANG")
                rf.assign_rule("Azure Temple Monitor - x:3648 y:25888", "TAILS | KNUCKLES | FANG")
                rf.assign_rule("Azure Temple Monitor - x:-4192 y:21344", "ARMAGEDDON & EMERALD")
                rf.assign_rule("Azure Temple Monitor - x:-4192 y:21280", "ARMAGEDDON & EMERALD")
                rf.assign_rule("Azure Temple Monitor - x:-4192 y:21408", "ARMAGEDDON & EMERALD")
            else:
                rf.assign_rule("Azure Temple Monitor - x:-2272 y:12864","TAILS | KNUCKLES+BUBBLE) | AMY+BUBBLE) | FANG")
                rf.assign_rule("Azure Temple Monitor - x:-3232 y:14112", "TAILS | KNUCKLES | AMY+BUBBLE | FANG")
                rf.assign_rule("Azure Temple Monitor - x:3648 y:25888", "TAILS | KNUCKLES | AMY+BUBBLE | FANG")
                rf.assign_rule("Azure Temple Monitor - x:-4192 y:21344", "ARMAGEDDON")
                rf.assign_rule("Azure Temple Monitor - x:-4192 y:21280", "ARMAGEDDON")
                rf.assign_rule("Azure Temple Monitor - x:-4192 y:21408", "ARMAGEDDON")




    if options.completion_type == 0:
        world.completion_condition[player] = lambda state: state.can_reach("Black Core Zone", 'Region', player)
    else:
        world.completion_condition[player] = lambda state: state.can_reach("Credits", 'Region', player)
    #if options.completion_type == "last_bowser_stage":
    #    world.completion_condition[player] = lambda state: state.can_reach("BitS: Top", 'Region', player)
    #elif options.completion_type == "all_bowser_stages":
    #    world.completion_condition[player] = lambda state: state.can_reach("Bowser in the Dark World", 'Region', player) and \
    #                                                       state.can_reach("BitFS: Upper", 'Region', player) and \
    #                                                       state.can_reach("BitS: Top", 'Region', player)


class RuleFactory:

    world: MultiWorld
    player: int
    move_rando_bitvec: bool
    area_randomizer: bool
    capless: bool
    cannonless: bool
    moveless: bool

    token_table = {
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
        "FORCE": "Force Shield",
        "LIGHTNING": "Lightning Shield",
        "EMERALD": "Chaos Emerald",
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

