import typing
import os
import json
from .Items import item_data_table, zones_item_data_table, character_item_data_table, other_item_table, item_table, SRB2Item
from .Locations import location_table, SRB2Location
from .Options import srb2_options_groups, SRB2Options
from .Rules import set_rules
from .Regions import create_regions, SRB2Zones
from BaseClasses import Item, Tutorial, ItemClassification, Region
from ..AutoWorld import World, WebWorld
import random
from multiprocessing import Process
from worlds.LauncherComponents import Component, components, Type, launch_subprocess






#class SM64Web(WebWorld):
#    tutorials = [Tutorial(
#        "Multiworld Setup Guide",
#        "A guide to setting up SM64EX for MultiWorld.",
#        "English",
#        "setup_en.md",
#        "setup/en",
#        ["N00byKing"]
#    )]

option_groups = srb2_options_groups

def launch_client():
    from .Client import run_as_textclient
    launch_subprocess(run_as_textclient, name="SRB2Client")


components.append(Component(
    "Sonic Robo Blast 2 Client",
    "SRB2Client",
    func=launch_client,
    component_type=Type.CLIENT
))

class SRB2World(World):
    """ 
    Peak game
    Remember to actually edit this later
    """
    game: str = "Sonic Robo Blast 2"
    topology_present = False

    item_name_to_id = item_table
    location_name_to_id = location_table

    required_client_version = (0, 3, 5)

    area_connections: typing.Dict[int, int]

    options_dataclass = SRB2Options

    number_of_locations: int
    filler_count: int
    star_costs: typing.Dict[str, int]

    # Spoiler specific variable(s)
    star_costs_spoiler_key_maxlen = len(max([
        'First Floor Big Star Door',
        'Basement Big Star Door',
        'Second Floor Big Star Door',
        'MIPS 1',
        'MIPS 2',
        'Endless Stairs',
    ], key=len))


    def generate_early(self):

        #TODO rewrite this to calculate max locations then add filler based on emblem numbers
        max_locations = 540#TODO up this once i have enough locations
        if not self.options.time_emblems:
            max_locations -= 27
        if not self.options.ring_emblems:
            max_locations -= 20
        if not self.options.score_emblems:
            max_locations -= 7
        if not self.options.rank_emblems:
            max_locations -= 12
        if not self.options.ntime_emblems:
            max_locations -= 12
        if not self.options.oneup_sanity:
            max_locations -= 246

        self.number_of_locations = max_locations
        self.move_rando_bitvec = 0




    def create_regions(self):
        create_regions(self.multiworld, self.options, self.player)

    def set_rules(self):
        self.area_connections = {}
        set_rules(self.multiworld, self.options, self.player, self.area_connections, self.move_rando_bitvec)


    def create_item(self, name: str) -> Item:
        data = item_data_table[name]
        item = SRB2Item(name, data.classification, data.code, self.player)

        return item

    def create_items(self):
        # 1Up Mushrooms

        Valid_starts = ["Greenflower Zone", "Techno Hill Zone", "Deep Sea Zone", "Castle Eggman Zone",
                        "Arid Canyon Zone", "Red Volcano Zone", "Egg Rock Zone"]
        rand_idx = random.randrange(len(Valid_starts))

        Starting_zone = Valid_starts[rand_idx]
        self.multiworld.push_precollected(self.create_item(Starting_zone))
        slots_to_fill = self.number_of_locations
        for zone_name in zones_item_data_table.keys():
            if zone_name == Starting_zone:
                continue
            if zone_name == "Black Core Zone" and self.options.bcz_emblems > 0:
                self.multiworld.itempool += [self.create_item("1UP")] #replace bcz with a 1up to match item numbers
                continue
            slots_to_fill-=1
            self.multiworld.itempool += [self.create_item(zone_name)]#and != starting_zone
        #not concise because I need to keep track of slots_to_fill
        for char_name in character_item_data_table.keys():
            self.multiworld.itempool += [self.create_item(char_name)]
            slots_to_fill -=1
        for shield in other_item_table.keys():
            self.multiworld.itempool += [self.create_item(shield)]
            slots_to_fill -=1

        self.multiworld.itempool += [self.create_item("Chaos Emerald") for i in range(7)]
        slots_to_fill -= 7

        if self.options.radar_start:
            self.multiworld.push_precollected(self.create_item("Progressive Emblem Hint"))
            self.multiworld.push_precollected(self.create_item("Progressive Emblem Hint"))
        else:
            self.multiworld.itempool += [self.create_item("Progressive Emblem Hint")]
            self.multiworld.itempool += [self.create_item("Progressive Emblem Hint")]
            slots_to_fill -= 2

        self.multiworld.itempool += [self.create_item("+5 Starting Rings") for i in range(4)]
        slots_to_fill -= 4


        target_emblems = self.options.num_emblems

        if target_emblems > slots_to_fill:
            target_emblems = slots_to_fill

        for i in range(0,target_emblems):
            self.multiworld.itempool += [self.create_item("Emblem")]
            slots_to_fill -=1


        self.options.bcz_emblems.value = round(target_emblems * (self.options.bcz_emblems.value/100))

        if slots_to_fill!= 0:

            spread = int(slots_to_fill/15)
            print(spread)
            if spread != 0:
                self.multiworld.itempool += [self.create_item("Forced Pity Shield") for i in range(spread)]
                self.multiworld.itempool += [self.create_item("Forced Gravity Boots") for i in range(spread)]
                self.multiworld.itempool += [self.create_item("Dropped Inputs") for i in range(spread)]
                self.multiworld.itempool += [self.create_item("Replay Tutorial") for i in range(spread)]
                self.multiworld.itempool += [self.create_item("Ring Loss") for i in range(spread)]
                self.multiworld.itempool += [self.create_item("& Knuckles") for i in range(spread)]#non functional
                self.multiworld.itempool += [self.create_item("1UP") for i in range(spread)]
                self.multiworld.itempool += [self.create_item("50 Rings") for i in range(spread)]
                self.multiworld.itempool += [self.create_item("20 Rings") for i in range(spread)]
                self.multiworld.itempool += [self.create_item("10 Rings") for i in range(spread)]
                self.multiworld.itempool += [self.create_item("Slippery Floors") for i in range(spread)]
                self.multiworld.itempool += [self.create_item("1000 Points") for i in range(spread)]
                self.multiworld.itempool += [self.create_item("Sonic Forces") for i in range(spread)]
                self.multiworld.itempool += [self.create_item("Temporary Invincibility") for i in range(spread)]
                self.multiworld.itempool += [self.create_item("Temporary Super Sneakers") for i in range(spread)]

            slots_to_fill = slots_to_fill % 15
            if slots_to_fill > 0:
                self.multiworld.itempool += [self.create_item("1UP") for i in range(slots_to_fill)]

    def generate_basic(self): #use to force items in a specific location
        return
           #self.multiworld.get_location("BoB: Bob-omb Buddy", self.player).place_locked_item(self.create_item("Cannon Unlock BoB"))


    def get_filler_item_name(self) -> str:
        return "1UP"

    def fill_slot_data(self):
        return {
            "DeathLink": self.options.death_link.value,
            "CompletionType": self.options.completion_type.value,
            "BlackCoreEmblems": self.options.bcz_emblems.value,
        }

    def generate_output(self, output_directory: str):
        if self.multiworld.players != 1:
            return
        data = {
            "slot_data": self.fill_slot_data(),
            "location_to_item": {self.location_name_to_id[i.name] : item_table[i.item.name] for i in self.multiworld.get_locations()},
            "data_package": {
                "data": {
                    "games": {
                        self.game: {
                            "item_name_to_id": self.item_name_to_id,
                            "location_name_to_id": self.location_name_to_id
                        }
                    }
                }
            }
        }
        filename = f"{self.multiworld.get_out_file_name_base(self.player)}.apsrb2"
        with open(os.path.join(output_directory, filename), 'w') as f:
            json.dump(data, f)

    def extend_hint_information(self, hint_data: typing.Dict[int, typing.Dict[int, str]]):
        return

    def write_spoiler(self, spoiler_handle: typing.TextIO) -> None:
        # Write calculated star costs to spoiler.
        star_cost_spoiler_header = '\n\n' + self.player_name + ' line 159, TODO find out what this does:\n\n'
        spoiler_handle.write(self.player_name)
        # - Reformat star costs dictionary in spoiler to be a bit more readable.


