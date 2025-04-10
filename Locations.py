from BaseClasses import Location

class SRB2Location(Location):
    game: str = "Sonic Robo Blast 2"

#Bob-omb Battlefield
GFZ_table = {
    "Greenflower (Act 1) Star Emblem": 1,
    "Greenflower (Act 1) Spade Emblem": 2,
    "Greenflower (Act 1) Heart Emblem": 3,
    "Greenflower (Act 1) Diamond Emblem": 4,
    "Greenflower (Act 1) Club Emblem": 5,
    "Greenflower (Act 1) Time Emblem": 6,
    "Greenflower (Act 1) Ring Emblem": 7,

    "Greenflower (Act 2) Star Emblem": 8,
    "Greenflower (Act 2) Spade Emblem": 9,
    "Greenflower (Act 2) Heart Emblem": 10,
    "Greenflower (Act 2) Diamond Emblem": 11,
    "Greenflower (Act 2) Club Emblem": 12,
    "Greenflower (Act 2) Time Emblem": 13,
    "Greenflower (Act 2) Ring Emblem": 14,

    "Greenflower (Act 3) Time Emblem": 15,
    "Greenflower (Act 3) Score Emblem": 16
}

THZ_table = {
    "Techno Hill (Act 1) Star Emblem": 17,
    "Techno Hill (Act 1) Spade Emblem": 18,
    "Techno Hill (Act 1) Heart Emblem": 19,
    "Techno Hill (Act 1) Diamond Emblem": 20,
    "Techno Hill (Act 1) Club Emblem": 21,
    "Techno Hill (Act 1) Time Emblem": 22,
    "Techno Hill (Act 1) Ring Emblem": 23,

    "Techno Hill (Act 2) Star Emblem": 24,
    "Techno Hill (Act 2) Spade Emblem": 25,
    "Techno Hill (Act 2) Heart Emblem": 26,
    "Techno Hill (Act 2) Diamond Emblem": 27,
    "Techno Hill (Act 2) Club Emblem": 28,
    "Techno Hill (Act 2) Time Emblem": 29,
    "Techno Hill (Act 2) Ring Emblem": 30,

    "Techno Hill (Act 3) Time Emblem": 31,
    "Techno Hill (Act 3) Score Emblem": 32
}
DSZ_table = {
    "Deep Sea (Act 1) Star Emblem": 33,
    "Deep Sea (Act 1) Spade Emblem": 34,
    "Deep Sea (Act 1) Heart Emblem": 35,
    "Deep Sea (Act 1) Diamond Emblem": 36,
    "Deep Sea (Act 1) Club Emblem": 37,
    "Deep Sea (Act 1) Time Emblem": 38,
    "Deep Sea (Act 1) Ring Emblem": 39,

    "Deep Sea (Act 2) Star Emblem": 40,
    "Deep Sea (Act 2) Spade Emblem": 41,
    "Deep Sea (Act 2) Heart Emblem": 42,
    "Deep Sea (Act 2) Diamond Emblem": 43,
    "Deep Sea (Act 2) Club Emblem": 44,
    "Deep Sea (Act 2) Time Emblem": 45,
    "Deep Sea (Act 2) Ring Emblem": 46,

    "Deep Sea (Act 3) Time Emblem": 47,
    "Deep Sea (Act 3) Score Emblem": 48
}

CEZ_table = {
    "Castle Eggman (Act 1) Star Emblem": 49,
    "Castle Eggman (Act 1) Spade Emblem": 50,
    "Castle Eggman (Act 1) Heart Emblem": 51,
    "Castle Eggman (Act 1) Diamond Emblem": 52,
    "Castle Eggman (Act 1) Club Emblem": 53,
    "Castle Eggman (Act 1) Time Emblem": 54,
    "Castle Eggman (Act 1) Ring Emblem": 55,

    "Castle Eggman (Act 2) Star Emblem": 56,
    "Castle Eggman (Act 2) Spade Emblem": 57,
    "Castle Eggman (Act 2) Heart Emblem": 58,
    "Castle Eggman (Act 2) Diamond Emblem": 59,
    "Castle Eggman (Act 2) Club Emblem": 60,
    "Castle Eggman (Act 2) Time Emblem": 61,
    "Castle Eggman (Act 2) Ring Emblem": 62,

    "Castle Eggman (Act 3) Time Emblem": 63,
    "Castle Eggman (Act 3) Score Emblem": 64
}
ACZ_table = {
    "Arid Canyon (Act 1) Star Emblem": 65,
    "Arid Canyon (Act 1) Spade Emblem": 66,
    "Arid Canyon (Act 1) Heart Emblem": 67,
    "Arid Canyon (Act 1) Diamond Emblem": 68,
    "Arid Canyon (Act 1) Club Emblem": 69,
    "Arid Canyon (Act 1) Time Emblem": 70,
    "Arid Canyon (Act 1) Ring Emblem": 71,

    "Arid Canyon (Act 2) Star Emblem": 72,
    "Arid Canyon (Act 2) Spade Emblem": 73,
    "Arid Canyon (Act 2) Heart Emblem": 74,
    "Arid Canyon (Act 2) Diamond Emblem": 75,
    "Arid Canyon (Act 2) Club Emblem": 76,
    "Arid Canyon (Act 2) Time Emblem": 77,
    "Arid Canyon (Act 2) Ring Emblem": 78,

    "Arid Canyon (Act 3) Time Emblem": 79,
    "Arid Canyon (Act 3) Score Emblem": 80
}
RVZ_table = {
    "Red Volcano (Act 1) Star Emblem": 81,
    "Red Volcano (Act 1) Spade Emblem": 82,
    "Red Volcano (Act 1) Heart Emblem": 83,
    "Red Volcano (Act 1) Diamond Emblem": 84,
    "Red Volcano (Act 1) Club Emblem": 85,
    "Red Volcano (Act 1) Time Emblem": 86,
    "Red Volcano (Act 1) Ring Emblem": 87,
}
ERZ_table = {
    "Egg Rock (Act 1) Star Emblem": 88,
    "Egg Rock (Act 1) Spade Emblem": 89,
    "Egg Rock (Act 1) Heart Emblem": 90,
    "Egg Rock (Act 1) Diamond Emblem": 91,
    "Egg Rock (Act 1) Club Emblem": 92,
    "Egg Rock (Act 1) Time Emblem": 93,
    "Egg Rock (Act 1) Ring Emblem": 94,

    "Egg Rock (Act 2) Star Emblem": 95,
    "Egg Rock (Act 2) Spade Emblem": 96,
    "Egg Rock (Act 2) Heart Emblem": 97,
    "Egg Rock (Act 2) Diamond Emblem": 98,
    "Egg Rock (Act 2) Club Emblem": 99,
    "Egg Rock (Act 2) Time Emblem": 100,
    "Egg Rock (Act 2) Ring Emblem": 101,
}
BCZ_table = {
    "Black Core (Act 1) Time Emblem": 102,
    "Black Core (Act 1) Ring Emblem": 103,

    "Black Core (Act 2) Time Emblem": 104,
    "Black Core (Act 2) Score Emblem": 105,

    "Black Core (Act 3) Time Emblem": 106,
    "Black Core (Act 3) Score Emblem": 107,
}
FHZ_table = {
    "Frozen Hillside Star Emblem": 108,
    "Frozen Hillside Spade Emblem": 109,
    "Frozen Hillside Heart Emblem": 110,
    "Frozen Hillside Diamond Emblem": 111,
    "Frozen Hillside Club Emblem": 112,
    "Frozen Hillside Time Emblem": 113,
    "Frozen Hillside Ring Emblem": 114,
}
PTZ_table = {
    "Pipe Towers Star Emblem": 115,
    "Pipe Towers Spade Emblem": 116,
    "Pipe Towers Heart Emblem": 117,
    "Pipe Towers Diamond Emblem": 118,
    "Pipe Towers Club Emblem": 119,
    "Pipe Towers Time Emblem": 120,
    "Pipe Towers Ring Emblem": 121,
}
FFZ_table = {
    "Forest Fortress Star Emblem": 122,
    "Forest Fortress Spade Emblem": 123,
    "Forest Fortress Heart Emblem": 124,
    "Forest Fortress Diamond Emblem": 125,
    "Forest Fortress Club Emblem": 126,
    "Forest Fortress Time Emblem": 127,
    "Forest Fortress Ring Emblem": 128,
}
HHZ_table = {
    "Haunted Heights Star Emblem": 129,
    "Haunted Heights Spade Emblem": 130,
    "Haunted Heights Heart Emblem": 131,
    "Haunted Heights Diamond Emblem": 132,
    "Haunted Heights Club Emblem": 133,
    "Haunted Heights Time Emblem": 134,
    "Haunted Heights Ring Emblem": 135,
}
AGZ_table = {
    "Aerial Garden Star Emblem": 136,
    "Aerial Garden Spade Emblem": 137,
    "Aerial Garden Heart Emblem": 138,
    "Aerial Garden Diamond Emblem": 139,
    "Aerial Garden Club Emblem": 140,
    "Aerial Garden Time Emblem": 141,
    "Aerial Garden Ring Emblem": 142,
}
ATZ_table = {
    "Azure Temple Star Emblem": 143,
    "Azure Temple Spade Emblem": 144,
    "Azure Temple Heart Emblem": 145,
    "Azure Temple Diamond Emblem": 146,
    "Azure Temple Club Emblem": 147,
    "Azure Temple Time Emblem": 148,
    "Azure Temple Ring Emblem": 149,
}
FFSP_table = {
"Floral Field Sun Emblem": 150,
"Floral Field Moon Emblem": 151,
"Floral Field A Rank Emblem": 152,
"Floral Field Time Emblem": 153,
}
TPSP_table = {
"Toxic Plateau Sun Emblem": 154,
"Toxic Plateau Moon Emblem": 155,
"Toxic Plateau A Rank Emblem": 156,
"Toxic Plateau Time Emblem": 157,
}
FCSP_table = {
"Flooded Cove Sun Emblem": 158,
"Flooded Cove Moon Emblem": 159,
"Flooded Cove A Rank Emblem": 160,
"Flooded Cove Time Emblem": 161,
}
CFSP_table = {
"Cavern Fortress Sun Emblem": 162,
"Cavern Fortress Moon Emblem": 163,
"Cavern Fortress A Rank Emblem": 164,
"Cavern Fortress Time Emblem": 165,
}
DWSP_table = {
"Dusty Wasteland Sun Emblem": 166,
"Dusty Wasteland Moon Emblem": 167,
"Dusty Wasteland A Rank Emblem": 168,
"Dusty Wasteland Time Emblem": 169,
}
MCSP_table = {
"Magma Caves Sun Emblem": 170,
"Magma Caves Moon Emblem": 171,
"Magma Caves A Rank Emblem": 172,
"Magma Caves Time Emblem": 173,
}
ESSP_table = {
"Egg Satellite Sun Emblem": 174,
"Egg Satellite Moon Emblem": 175,
"Egg Satellite A Rank Emblem": 176,
"Egg Satellite Time Emblem": 177,
}
BHSP_table = {
"Black Hole Sun Emblem": 178,
"Black Hole Moon Emblem": 179,
"Black Hole A Rank Emblem": 180,
"Black Hole Time Emblem": 181,
}
CCSP_table = {
"Christmas Chime Sun Emblem": 182,
"Christmas Chime Moon Emblem": 183,
"Christmas Chime A Rank Emblem": 184,
"Christmas Chime Time Emblem": 185,
}
DHSP_table = {
"Dream Hill Sun Emblem": 186,
"Dream Hill Moon Emblem": 187,
"Dream Hill A Rank Emblem": 188,
"Dream Hill Time Emblem": 189,
}
APSP_table = {
"Alpine Paradise (Act 1) Sun Emblem": 190,
"Alpine Paradise (Act 1) Moon Emblem": 191,
"Alpine Paradise (Act 1) A Rank Emblem": 192,
"Alpine Paradise (Act 1) Time Emblem": 193,
"Alpine Paradise (Act 2) Sun Emblem": 194,
"Alpine Paradise (Act 2) Moon Emblem": 195,
"Alpine Paradise (Act 2) A Rank Emblem": 196,
"Alpine Paradise (Act 2) Time Emblem": 197,
}
EXTRA_table = {
    "Greenflower Act 1 Clear": 198,
    "Greenflower Act 2 Clear": 199,
    "Greenflower Act 3 Clear": 200,
    "Techno Hill Act 1 Clear": 201,
    "Techno Hill Act 2 Clear": 202,
    "Techno Hill Act 3 Clear": 203,
    "Deep Sea Act 1 Clear": 204,
    "Deep Sea Act 2 Clear": 205,
    "Deep Sea Act 3 Clear": 206,
    "Castle Eggman Act 1 Clear": 207,
    "Castle Eggman Act 2 Clear": 208,
    "Castle Eggman Act 3 Clear": 209,
    "Arid Canyon Act 1 Clear": 210,
    "Arid Canyon Act 2 Clear": 211,
    "Arid Canyon Act 3 Clear": 212,
    "Red Volcano Act 1 Clear": 213,
    "Egg Rock Act 1 Clear": 214,
    "Egg Rock Act 2 Clear": 215,
    "Black Core Act 1 Clear": 216,
    "Black Core Act 2 Clear": 217,
    "Black Core Act 3 Clear": 218,
    "Frozen Hillside Clear": 219,
    "Pipe Towers Clear": 220,
    "Forest Fortress Clear": 221,
    "Final Demo Clear": 222,
    "Haunted Heights Clear": 223,
    "Aerial Garden Clear": 224,
    "Azure Temple Clear": 225,
    "Floral Field Clear": 226,
    "Toxic Plateau Clear": 227,
    "Flooded Cove Clear": 228,
    "Cavern Fortress Clear": 229,
    "Dusty Wasteland Clear": 230,
    "Magma Caves Clear": 231,
    "Egg Satellite Clear": 232,
    "Black Hole Clear": 233,
    "Christmas Chime Clear": 234,
    "Dream Hill Clear": 235,
    "Alpine Paradise Act 1 Clear": 236,
    "Alpine Paradise Act 2 Clear": 237,
    "Good Ending": 238,
}
tokens_table = {
    "Greenflower (Act 1) Emerald Token - Breakable Wall Near Bridge": 240,
    "Greenflower (Act 1) Emerald Token - Midair Top Path": 241,
    "Greenflower (Act 2) Emerald Token - Main Path Cave": 242,
    "Greenflower (Act 2) Emerald Token - Under Bridge Near End": 243,
    "Greenflower (Act 2) Emerald Token - No Spin High on Ledge": 244,

    "Techno Hill (Act 1) Emerald Token - On Pipes": 245,
    "Techno Hill (Act 1) Emerald Token - Alt Path Under Slime": 246,
    "Techno Hill (Act 2) Emerald Token - Deep in Slime": 247,
    "Techno Hill (Act 2) Emerald Token - Knuckles Path Backtrack as Amy": 248,

    "Deep Sea (Act 1) Emerald Token - V on Right Path": 249,
    "Deep Sea (Act 1) Emerald Token - Underwater Air Pocket on Right Path": 250,
    "Deep Sea (Act 1) Emerald Token - Yellow Doors": 251,
    "Deep Sea (Act 1) Emerald Token - Large Underwater Curve": 252,
    "Deep Sea (Act 1) Emerald Token - Waterslide Gargoyles": 253,
    "Deep Sea (Act 2) Emerald Token - Near Heart Emblem": 254,
    "Deep Sea (Act 2) Emerald Token - Red and Yellow Springs": 255,
    "Deep Sea (Act 2) Emerald Token - Down Right From Goal": 256,
    "Deep Sea (Act 2) Emerald Token - No Spin Spring Turnaround": 257,

    "Castle Eggman (Act 1) Emerald Token - Behind Fence Near Start": 258,
    "Castle Eggman (Act 1) Emerald Token - Spring Side Path": 259,
    "Castle Eggman (Act 1) Emerald Token - Inside Castle": 260,
    "Castle Eggman (Act 2) Emerald Token - First Outside Area": 261,
    "Castle Eggman (Act 2) Emerald Token - Corner of Right Courtyard": 262,
    "Castle Eggman (Act 2) Emerald Token - Window of Back Left Courtyard": 263,
    "Castle Eggman (Act 2) Emerald Token - Spring Near Club Emblem": 264,
    "Castle Eggman (Act 2) Emerald Token - High Ledge Before Final Tower": 265,

    "Arid Canyon (Act 1) Emerald Token - Speed Shoes Central Pillar": 266,
    "Arid Canyon (Act 1) Emerald Token - Behind Pillar Before Exploding Ramp": 267,
    "Arid Canyon (Act 1) Emerald Token - Behind Wall and Spikes": 268,
    "Arid Canyon (Act 2) Emerald Token - Left No Spin Path Minecarts": 269,
    "Arid Canyon (Act 2) Emerald Token - Large Arch Cave Right Ledge": 270,
    "Arid Canyon (Act 2) Emerald Token - Knuckles Dark Path Around Wall": 271,

    "Red Volcano (Act 1) Emerald Token - First Outside Area": 272,
    "Red Volcano (Act 1) Emerald Token - Hidden Ledge Near 4th Checkpoint": 273,
    "Red Volcano (Act 1) Emerald Token - Rollout Rock Lavafall": 274,
    "Red Volcano (Act 1) Emerald Token - Behind Ending Rocket": 275,

    "Egg Rock (Act 1) Emerald Token - Gravity Conveyor Belts": 276,
    "Egg Rock (Act 1) Emerald Token - Moving Platforms": 277,
    "Egg Rock (Act 2) Emerald Token - Outside on Metal Beam": 278,
    "Egg Rock (Act 2) Emerald Token - Skip Gravity Pad": 279,
    "Egg Rock (Act 2) Emerald Token - Disco Room": 280,

    "Final Demo Emerald Token - Greenflower (Act 1) Breakable Wall Near Bridge": 281,
    "Final Demo Emerald Token - Greenflower (Act 2) Underwater Cave": 282,
    "Final Demo Emerald Token - Greenflower (Act 2) Under Bridge Near End": 283,
    "Final Demo Emerald Token - Techno Hill (Act 1) On Pipes": 284,
    "Final Demo Emerald Token - Techno Hill (Act 1) Alt Path Fans": 285,
    "Final Demo Emerald Token - Techno Hill (Act 2) Breakable Wall": 286,
    "Final Demo Emerald Token - Techno Hill (Act 2) Under Poison Near End": 287,
    "Final Demo Emerald Token - Castle Eggman (Act 1) Small Lake Near Start": 288,
    "Final Demo Emerald Token - Castle Eggman (Act 1) Tunnel Before Act Clear": 289,
    "Final Demo Emerald Token - Castle Eggman (Act 2) Water Flow in Sewers": 290,

    "Aerial Garden Emerald Token - First Room High Tower": 291,
    "Aerial Garden Emerald Token - Diamond Emblem 1": 292,
    "Aerial Garden Emerald Token - Diamond Emblem 2": 293,
    "Aerial Garden Emerald Token - Diamond Emblem 3": 294,
    "Aerial Garden Emerald Token - Diamond Emblem 4": 295,
    "Aerial Garden Emerald Token - Underwater on Pillar": 296,
}




# TODO shields, act clears
# Correspond to 3626000 + course index * 7 + star index, then secret stars, then keys, then 100 Coin Stars
location_table = {**GFZ_table,**THZ_table,**DSZ_table,**CEZ_table,**ACZ_table,
                  **RVZ_table,**ERZ_table,**BCZ_table,**FHZ_table,**PTZ_table,**FFZ_table,**HHZ_table,**AGZ_table,**ATZ_table,
                  **FFSP_table,**TPSP_table,**FCSP_table,**CFSP_table,**DWSP_table,**MCSP_table,**ESSP_table,**BHSP_table,
                  **CCSP_table,**DHSP_table,**APSP_table,**EXTRA_table,**tokens_table}
