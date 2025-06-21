import typing
import os
import json
from .Items import (item_data_table, zones_item_data_table, character_item_data_table, other_item_table, item_table, mpmatch_item_table, traps_item_data_table, special_item_data_table,
                    nights_item_table, SRB2Item)
from .Locations import location_table, GFZ_table, THZ_table, DSZ_table, CEZ_table,ACZ_table,RVZ_table,ERZ_table,BCZ_table,FHZ_table,PTZ_table,FFZ_table,HHZ_table,AGZ_table,ATZ_table,FFSP_table,TPSP_table,FCSP_table,CFSP_table,DWSP_table,MCSP_table,ESSP_table,BHSP_table,CCSP_table,DHSP_table,APSP_table,EXTRA_table,tokens_table,oneupcoords_table,ringmonitors_table, SRB2Location
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
    from .Client import launch
    launch_subprocess(launch, name="SRB2Client")


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

    item_name_groups = {
        "Zone":zones_item_data_table,
        "Character":character_item_data_table,
        "Match Zone":mpmatch_item_table,
        "Trap":traps_item_data_table,
        "Shield":other_item_table,
        "Powerup":nights_item_table,
        "Nights Stage":special_item_data_table
    }

    location_name_groups = {
        "Greenflower Zone":GFZ_table,
        "Techno Hill Zone": THZ_table,
        "Deep Sea Zone": DSZ_table,
        "Castle Eggman Zone":CEZ_table,
        "Arid Canyon Zone":ACZ_table,
        "Red Volcano Zone":RVZ_table,
        "Egg Rock Zone":ERZ_table,
        "Black Core Zone":BCZ_table,
        "Frozen Hillside Zone":FHZ_table,
        "Pipe Towers Zone":PTZ_table,
        "Forest Fortress Zone":FFZ_table,
        #"Final Demo Zone": oh thats non sorted things
        "Haunted Heights Zone":HHZ_table,
        "Aerial Garden Zone":AGZ_table,
        "Azure Temple Zone":ATZ_table,
        "Floral Field Zone":FFSP_table,
        "Toxic Plateau Zone":TPSP_table,
        "Flooded Cove Zone":FCSP_table,
        "Cavern Fortress Zone":CFSP_table,
        "Dusty Wasteland Zone":DWSP_table,
        "Egg Satellite Zone":ESSP_table,
        "Black Hole Zone":BHSP_table,
        "Christmas Chime Zone":CCSP_table,
        "Dream Hill Zone":DHSP_table,
        "Alpine Paradise Zone":APSP_table,
        "Emerald Tokens":tokens_table,
        "1UP Monitors":oneupcoords_table,
        "Super Ring Monitors":ringmonitors_table



    }



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

        max_locations = 259+57+246+597+380#TODO up this once i have enough locations
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
        if not self.options.match_maps:
            max_locations -= 21

        if not self.options.oneup_sanity or not self.options.match_maps:
            max_locations -= 1
        if not self.options.superring_sanity or not self.options.match_maps:
            max_locations -= 379
        if not self.options.superring_sanity:
            max_locations -= 597
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
            self.multiworld.push_precollected(self.create_item("Sonic"))
            slots_to_fill = self.number_of_locations
            for zone_name in zones_item_data_table.keys():
                if zone_name == Starting_zone:
                    continue
                if zone_name == "Black Core Zone" and self.options.bcz_emblem_percent > 0:
                    self.multiworld.itempool += [self.create_item("1UP")] #replace bcz with a 1up to match item numbers
                    slots_to_fill -= 1
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
            for spstage in special_item_data_table.keys():
                self.multiworld.itempool += [self.create_item(spstage)]
                slots_to_fill -=1
            for shield in nights_item_table.keys():
                self.multiworld.itempool += [self.create_item(shield)]
                slots_to_fill -=1

            if self.options.match_maps:
                for zone in mpmatch_item_table.keys():
                    self.multiworld.itempool += [self.create_item(zone)]
                    slots_to_fill -= 1



            self.multiworld.itempool += [self.create_item("Chaos Emerald") for i in range(7)]
            slots_to_fill -= 7

            if self.options.radar_start:
                self.multiworld.push_precollected(self.create_item("Progressive Emblem Hint"))
                self.multiworld.push_precollected(self.create_item("Progressive Emblem Hint"))
            else:
                self.multiworld.itempool += [self.create_item("Progressive Emblem Hint")]
                self.multiworld.itempool += [self.create_item("Progressive Emblem Hint")]
                slots_to_fill -= 2

            self.multiworld.itempool += [self.create_item("+5 Starting Rings") for i in range(2)]
            slots_to_fill -= 2


            target_emblems = self.options.num_emblems

            if target_emblems > slots_to_fill:
                target_emblems = slots_to_fill

            for i in range(0,target_emblems):
                self.multiworld.itempool += [self.create_item("Emblem")]
                slots_to_fill -=1


            self.options.bcz_emblem_percent.value = round(target_emblems * (self.options.bcz_emblem_percent.value/100))

            if slots_to_fill != 0:
                self.multiworld.itempool += [self.create_item("Sound Test")]
                slots_to_fill -= 1

            if slots_to_fill>99:
                for i in range(int(slots_to_fill/100)):
                    self.multiworld.itempool += [self.create_item("+5 Starting Rings")]
                    slots_to_fill -= 1


            if slots_to_fill!= 0:
                trap_slots = int(slots_to_fill*self.options.trap_percentage/100)
                while trap_slots != 0:
                    trapnum = random.randrange(70)
                    if trapnum<3:
                        self.multiworld.itempool += [self.create_item("Replay Tutorial")]#4
                    elif trapnum<8:
                        self.multiworld.itempool += [self.create_item("Self-Propelled Bomb")]#5
                    elif trapnum < 14:
                        self.multiworld.itempool += [self.create_item("Sonic Forces")]
                    elif trapnum < 22:
                        self.multiworld.itempool += [self.create_item("Slippery Floors")]
                    elif trapnum < 26:
                        self.multiworld.itempool += [self.create_item("Shrink Monitor")]
                    elif trapnum < 32:
                        self.multiworld.itempool += [self.create_item("Grow Monitor")]
                    #elif trapnum < 42:
                    #    self.multiworld.itempool += [self.create_item("Reversed Controls")]
                    elif trapnum < 42:
                        self.multiworld.itempool += [self.create_item("Dropped Inputs")]
                    elif trapnum < 52:
                        self.multiworld.itempool += [self.create_item("Ring Loss")]
                    elif trapnum < 70:
                        self.multiworld.itempool += [self.create_item("Forced Pity Shield")]
                    trap_slots-=1
                    slots_to_fill-=1



            if slots_to_fill != 0:
                filler_slots = slots_to_fill
                while filler_slots != 0:
                    fillernum = random.randrange(90)
                    if fillernum<8:
                        self.multiworld.itempool += [self.create_item("1UP")]
                    elif fillernum<28:
                        self.multiworld.itempool += [self.create_item("10 Rings")]
                    elif fillernum < 38:
                        self.multiworld.itempool += [self.create_item("20 Rings")]
                    elif fillernum < 42:
                        self.multiworld.itempool += [self.create_item("50 Rings")]
                    elif fillernum < 48:
                        self.multiworld.itempool += [self.create_item("& Knuckles")]
                    elif fillernum < 58:
                        self.multiworld.itempool += [self.create_item("1000 Points")]
                    elif fillernum < 68:
                        self.multiworld.itempool += [self.create_item("Temporary Invincibility")]
                    elif fillernum < 80:
                        self.multiworld.itempool += [self.create_item("Temporary Super Sneakers")]
                    elif fillernum < 90:
                        self.multiworld.itempool += [self.create_item("Double Rings")]
                    filler_slots-=1
                    slots_to_fill-=1


    def generate_basic(self): #use to force items in a specific location
        return
           #self.multiworld.get_location("BoB: Bob-omb Buddy", self.player).place_locked_item(self.create_item("Cannon Unlock BoB"))


    def get_filler_item_name(self) -> str:
        return "1UP"

    def fill_slot_data(self):
        return {
            "DeathLink": self.options.death_link.value,
            "CompletionType": self.options.completion_type.value,
            "BlackCoreEmblems": self.options.bcz_emblem_percent.value,
            "EnableMatchMaps": self.options.match_maps.value
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


