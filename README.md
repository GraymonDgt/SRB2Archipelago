# SRB2APClient
The APworld, client, and mod files to be used with Archipelago randomizer

Avoid mentioning/ linking this on the main AP Discord because of the "no fangames" rule.
All discussion/ development of this APworld will take place here:
https://discord.gg/kkH4wBUmG9

## Required Software

- Sonic Robo Blast 2 v2.2.15 (https://www.srb2.org/download/)

- The most recent Archipelago client or the most recent MultiworldGG client

  (https://github.com/ArchipelagoMW/Archipelago/releases)
  (https://multiworld.gg/downloads/)

## Setup Guide

- Download SL_ArchipelagoSRB2_Vxxx.pk3 and srb2.apworld from releases (https://github.com/GraymonDgt/SRB2Archipelago/releases)

- Install the srb2.apworld by opening it or moving it to either

C:\ProgramData\Archipelago\custom_worlds\ or C:\ProgramData\MultiworldGG\custom_worlds\ .

- Move SL_ArchipelagoSRB2_Vxxx.pk3 into the addons folder of your desired SRB2 installation.

Extra steps for linux setup:

- in your SRB2 directory go to or create the directory "luafiles/archipelago" and inside create an empty file named "APTranslator.dat"

  (this is a known bug that will hopefully be fixed soon)

## Joining a Multiworld Game

- After opening the Archipelago/MultiworldGG client, there will be an option labeled "Sonic Robo Blast 2 Client".

- When opening that, a dialogue will open asking for your SRB2 directory, select the same folder as srb2win.exe/gamedata.dat.

- After connecting using the server address and port number, SRB2 will automatically open with the AP mod loaded.

# FAQ

- How do I set up an Archipelago game?
  
  This guide should hopefully help you get started:
  https://github.com/GraymonDgt/SRB2Archipelago/blob/main/srb2/docs/detailed_guide_en.md

- Do modded characters work?
  
  Currently, 16 different modded characters are supported and can be enabled in the yaml settings. The AP addon does not contain these characters by default, so you will have to download them seperately (links in addition notes)
  If you want to use non-supported modded characters with no logic issues, include all vanilla characters as your starting character in the yaml settings.

- Do modded level packs work?

  No

- The AP mod didn't load when connecting.

  You can load the AP mod manually and everything will work fine.

- Something something can't read APTranslator.dat.
  
  I swear I'm working on fixing that, keep restarting the client until it works or see the above linux step.

- SRB2 was closed, do I have to restart the client?

  No, you can reopen SRB2 and reload the AP mod without any issues.

- The heavily lags after loading the pk3.

  Make sure you aren't running SRB2 off of an external drive that may have a slow file transfer speed.

# ADDITIONAL NOTES

Type "hub" into the console to return to the hub at any time.

Contact me in the #sonic-robo-blast-2 channel in the discord above if you run into any issues!

Links to all supported custom characters:

https://mb.srb2.org/addons/metal-knuckles-tails-doll-sonic-r-characters.587/
https://mb.srb2.org/addons/the-chaotix.5734/
https://mb.srb2.org/threads/modern-sonic-v5-12.27514/
https://mb.srb2.org/addons/shadow-the-hedgehog.517/
https://mb.srb2.org/addons/silver-the-hedgehog.503/
https://mb.srb2.org/addons/ray-the-flying-squirrel.6348/
https://mb.srb2.org/addons/the-werehog-v2-3.505/
https://mb.srb2.org/addons/super-mario-bros.3420/
https://mb.srb2.org/addons/yoshi.687/
