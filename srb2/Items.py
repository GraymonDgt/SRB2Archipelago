from typing import NamedTuple

from BaseClasses import Item, ItemClassification


class SRB2Item(Item):
    game: str = "Sonic Robo Blast 2"


class SRB2ItemData(NamedTuple):
    code: int | None = None
    classification: ItemClassification = ItemClassification.progression


generic_item_data_table: dict[str, SRB2ItemData] = {
    "Emblem": SRB2ItemData(1, ItemClassification.progression_skip_balancing),
    "Chaos Emerald": SRB2ItemData(2),
    "Progressive Emblem Hint": SRB2ItemData(3, ItemClassification.useful),
    "1UP": SRB2ItemData(4, ItemClassification.filler),
    "Forced Gravity Boots": SRB2ItemData(5, ItemClassification.trap),
    "Forced Pity Shield": SRB2ItemData(6, ItemClassification.trap),
# disable auto brake
    "Replay Tutorial": SRB2ItemData(7, ItemClassification.trap),
    "Ring Loss": SRB2ItemData(8, ItemClassification.trap),
    "Dropped Inputs": SRB2ItemData(9, ItemClassification.trap),
    "& Knuckles": SRB2ItemData(70, ItemClassification.filler),
    "50 Rings": SRB2ItemData(71, ItemClassification.filler),
    "20 Rings": SRB2ItemData(72, ItemClassification.filler),
    "10 Rings": SRB2ItemData(73, ItemClassification.filler),
    "+5 Starting Rings": SRB2ItemData(74, ItemClassification.useful),
    "Slippery Floors": SRB2ItemData(75, ItemClassification.trap),
    "1000 Points": SRB2ItemData(76, ItemClassification.filler),
    "Sonic Forces": SRB2ItemData(77, ItemClassification.trap),
    "Temporary Invincibility": SRB2ItemData(78, ItemClassification.filler),
    "Temporary Super Sneakers": SRB2ItemData(79, ItemClassification.filler),
    "Sound Test": SRB2ItemData(80, ItemClassification.filler),
    "Self-Propelled Bomb": SRB2ItemData(81, ItemClassification.trap),
    "Shrink Monitor": SRB2ItemData(82, ItemClassification.trap),
    "Grow Monitor": SRB2ItemData(83, ItemClassification.trap),
    "Double Rings": SRB2ItemData(84, ItemClassification.filler),


    "Extended Invincibility": SRB2ItemData(90, ItemClassification.useful),
    "Extended Super Sneakers": SRB2ItemData(91, ItemClassification.useful),
    "Max Drill Increase": SRB2ItemData(92, ItemClassification.useful),



# killing dead
# 1 ring

# gambling

# toss flag or die
# eggman virus

# play credits
# flashbang


# super ring drain - drains rings and kills you when you run out
# no character ability - no thok, no flying, no player.charability
# get made fun of - hud element that makes fun of you


# quit game - brings up the "press y to quit" screen
# blast jump - get knocked back very far
#start at id 70 for new traps/ items


# Spindash
# progressive tails flight
# progressive force shield
# shield spike protection (shields now protect from spikes)
# +10 Max Rings



# knuckles break strength (allows knuckles to break walls)
# amy/fang downward floor break

#object locks
    # zoom tubes
    # rope hangs
    # mace swing
    # minecarts
    # rollout rocks
# lock thz slime

}

zones_item_data_table: dict[str, SRB2ItemData] = {
    "Greenflower Zone": SRB2ItemData(10),
    "Techno Hill Zone": SRB2ItemData(11),
    "Deep Sea Zone": SRB2ItemData(12),
    "Castle Eggman Zone": SRB2ItemData(13),
    "Arid Canyon Zone": SRB2ItemData(14),
    "Red Volcano Zone": SRB2ItemData(15),
    "Egg Rock Zone": SRB2ItemData(16),
    "Black Core Zone": SRB2ItemData(17),

    "Frozen Hillside Zone": SRB2ItemData(18),
    "Pipe Towers Zone": SRB2ItemData(19),
    "Forest Fortress Zone": SRB2ItemData(20),
    "Final Demo Zone": SRB2ItemData(21),

    "Haunted Heights Zone": SRB2ItemData(22),
    "Aerial Garden Zone": SRB2ItemData(23),
    "Azure Temple Zone": SRB2ItemData(24),

    "Floral Field Zone": SRB2ItemData(25),
    "Toxic Plateau Zone": SRB2ItemData(26),
    "Flooded Cove Zone": SRB2ItemData(27),
    "Cavern Fortress Zone": SRB2ItemData(28),
    "Dusty Wasteland Zone": SRB2ItemData(29),
    "Magma Caves Zone": SRB2ItemData(30),
    "Egg Satellite Zone": SRB2ItemData(31),
    "Black Hole Zone": SRB2ItemData(32),

    "Christmas Chime Zone": SRB2ItemData(33),
    "Dream Hill Zone": SRB2ItemData(34),
    "Alpine Paradise Zone": SRB2ItemData(35),
}

character_item_data_table: dict[str, SRB2ItemData] = {
    "Tails": SRB2ItemData(50),
    "Knuckles": SRB2ItemData(51),
    "Fang": SRB2ItemData(52),
    "Amy": SRB2ItemData(53),
    "Metal Sonic": SRB2ItemData(54),
}
other_item_table:dict[str, SRB2ItemData] = {
    "Whirlwind Shield":SRB2ItemData(56),
    "Armageddon Shield":SRB2ItemData(57),
    "Elemental Shield":SRB2ItemData(58),
    "Attraction Shield": SRB2ItemData(59, ItemClassification.useful),
    "Force Shield": SRB2ItemData(60, ItemClassification.useful),
    "Flame Shield": SRB2ItemData(61, ItemClassification.useful),
    "Bubble Shield": SRB2ItemData(62),
    "Lightning Shield": SRB2ItemData(63),
    "Super Paraloop": SRB2ItemData(100, ItemClassification.progression),
    "Nightopian Helper": SRB2ItemData(101, ItemClassification.useful),
    "Link Freeze": SRB2ItemData(102, ItemClassification.useful),
    "Extra Time": SRB2ItemData(103, ItemClassification.progression),
    "Drill Refill": SRB2ItemData(104, ItemClassification.useful),
}
mpmatch_item_table:dict[str, SRB2ItemData] = {
"Jade Valley Zone":SRB2ItemData(200),
"Noxious Factory Zone":SRB2ItemData(201),
"Tidal Palace Zone":SRB2ItemData(202),
"Thunder Citadel Zone":SRB2ItemData(203),
"Desolate Twilight Zone":SRB2ItemData(204),
"Frigid Mountain Zone":SRB2ItemData(205),
"Orbital Hangar Zone":SRB2ItemData(206),
"Sapphire Falls Zone":SRB2ItemData(207),
"Diamond Blizzard Zone":SRB2ItemData(208),
"Celestial Sanctuary Zone":SRB2ItemData(209),
"Frost Columns Zone":SRB2ItemData(210),
"Meadow Match Zone":SRB2ItemData(211),
"Granite Lake Zone":SRB2ItemData(212),
"Summit Showdown Zone":SRB2ItemData(213),
"Silver Shiver Zone":SRB2ItemData(214),
"Uncharted Badlands Zone":SRB2ItemData(215),
"Pristine Shores Zone":SRB2ItemData(216),
"Crystalline Heights Zone":SRB2ItemData(217),
"Starlit Warehouse Zone":SRB2ItemData(218),
"Midnight Abyss Zone":SRB2ItemData(219),
"Airborne Temple Zone":SRB2ItemData(220),

}





item_data_table = {
    **generic_item_data_table,
    **zones_item_data_table,
    **character_item_data_table,
    **other_item_table,
    **mpmatch_item_table
}

item_table = {name: data.code for name, data in item_data_table.items() if data.code is not None}
