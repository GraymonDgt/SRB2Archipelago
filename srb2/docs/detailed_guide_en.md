Go to
https://github.com/ArchipelagoMW/Archipelago/releases
and download the latest release

run through the setup guide, by default it will be installed to C:\ProgramData\Archipelago

install an apworld by double clicking or moving it into C:\ProgramData\Archipelago\custom_worlds (in this case, srb2.apworld)

close/ restart the archipelago launcher if it is open

click 'generate template options' and a folder will open, find the one for the game you want and open it as a text file in this case, 'Sonic Robo Blast 2.yaml'

These are the settings for the randomizer, change the values depending on what you want.

if you wanted to change a setting, set one value to be non-zero and the others to 0 such as:

  time_emblems:
    'false': 50
    'true': 0

keep in mind the options are weighted so you could potentially randomize whether or not a setting is enabled
for example if you were to put:

time_emblems:
    'false': 50
    'true': 50

this would result in %50 of the time enabling time emblems and %50 not
(the numbers do not need to add up to 100)

the same thing holds true for ranges, with the main difference being you can define what number you want
for example say you wanted to change the number of emblems from the default 180 to 100, you would put

  num_emblems:
    # You can define additional values between the minimum and maximum values.
    # Minimum value is 50
    # Maximum value is 250
    100: 50
    random: 0
    random-low: 0
    random-high: 0

(the 4 spaces before the value matter)

When you are done setting up your yaml, move it to the folder C:\ProgramData\Archipelago\Players
place a yaml for every game you want to play with in this folder

when you have all your yamls in the folder, click 'Generate' in the archipelago launcher

a terminal will open and when its finished a zip file will be created in C:\ProgramData\Archipelago\output
(if the terminal remains open then read what it says. If the issue is with a yaml it should give a line number)

To host a game, go to archipelago.gg and under 'Getting started' click 'Host game'

upload the zip file from C:\ProgramData\Archipelago\output and click 'create room'

You may now connect to the room using whatever method is required per game using the 5 digit number
