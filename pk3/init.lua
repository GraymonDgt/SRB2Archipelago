
dofile("SPB_Recreation.lua")
dofile("ExitMPLevels.lua")
COM_AddCommand("hub", function(player)
if (player != server) and multiplayer then 
print("You must be the server host to run this command")
return end
if gamemap == 1000 then
print("Nope, you have to complete the tutorial to go back")
return end
G_SetCustomExitVars(125, 1)
G_ExitLevel()
end)



COM_AddCommand("apinfo", function(player)
print("‡Archipelago is a multiworld randomizer. This means we recieve zones, characters, objects and shields from other people and in return we are collecting emblems to find other peoples' items. The person sending messages in chat is showing what is being sent.")
end)
 

--addHook("MobjSpawn", function(object)
--if bytes[3] == 0 then
--P_SpawnMobjFromMobj(object,0,0,0,MT_CUSTOMRING_BOX)
--P_RemoveMobj(object)
--end,MT_1UP_BOX)
--removed until i find a way to distribute 3d models in a pk3

local enabledrill = 0
local enabletime = 0
local showcoords = false
local monitorid = 0
local senddeath = false
local jumpscaretype = 0
local jumpscaretime = 0
local lastknownrings = 0
local unlockedchars = {}
local manualringlink = 0
local lastknowngamemap = 0
local supportedchars = {"sonic","tails","knuckles","amy","fang","metalsonic","mario","luigi","yoshi","ray","silver","shadow","modernsonic","werehog","metalknuckles","tailsdoll","espio","mighty","charmy","vector","heavy","bomb","bean","eggman","adventuresonic","tangle","blaze","marine","inazuma","aether"}




--local bytes = {}
rawset(_G,"bytes",{0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0})
rawset(_G,"num_images",5)
local syncfile = 0
local downloading = 0
addHook("NetVars", function(network)
    bytes = network(bytes)
	showcoords = network(showcoords)
	lastknownrings = network(lastknownrings)
end)
COM_AddCommand("syncfile",function(player)
if not multiplayer then return end
syncfile = 1
downloading = 1
end)
COM_AddCommand("printme",function(player,string)
if not multiplayer then return end
print(string)
end)
COM_AddCommand("setrings",function(player, setrings)
for player in players.iterate() do
player.rings = setrings
player.prevrings = setrings
end
lastknownrings = setrings
end,COM_ADMIN)


addHook("MapChange", function()
monitorid = 0



end)
addHook("MapLoad", function() --thanks to Vadapega for this FDZ death fix
monitorid = 0

if solchars then
for player in players.iterate() do
player.solemeralds = emeralds //temporary because no ap item exists
end
end




if bytes[30] == 3 then
for player in players.iterate() do
player.rings = bytes[23]*5 //Todo dont rely on player 0
end
end


if lastknowngamemap != gamemap then//map change;
if bytes[30] != 0 then
if (bytes[20] & 64) == 64 then
lastknownrings = bytes[23]*5
for player in players.iterate() do

player.rings = 0
player.prevrings = 0
manualringlink = 0
end
end
lastknowngamemap = gamemap
end
end






end)


addHook("MobjSpawn", function(object)
object.checkid = monitorid
monitorid = $ + 1
--P_KillMobj(object)
end,MT_1UP_BOX)
addHook("MobjSpawn", function(object)
object.checkid = monitorid
monitorid = $ + 1
--P_KillMobj(object)
end,MT_RING_BOX)



COM_AddCommand("showcoords", function(player)
showcoords = not showcoords
--print("WIP")
--print("x: "..player.mo.x/FRACUNIT .." y: "..player.mo.y/FRACUNIT)
end)

addHook("PlayerSpawn",function(player)
player.shrinktrap = 1

player.prevrings = 0
if not player.selected then
player.selected = 1 end
end)






addHook("TouchSpecial", function(object,toucher)
if object.collected then 
object.collected = object.collected +1
if object.collected >10 then
P_RemoveMobj(object) end
return end
if not multiplayer then return end
object.collected = 1
S_StartSound(toucher.mo, sfx_ncitem)
P_SetOrigin(object,players[0].mo.x,players[0].mo.y,players[0].mo.z)

end,MT_EMBLEM)

addHook("ThinkFrame", function()
if gamemap >49 and gamemap <60 then
G_SetCustomExitVars(125, 0)
end
if jumpscaretime > 0 then
jumpscaretime = $ - 1
end
if gamemap == 33 then
monitorid = 0 end
end)


addHook("TouchSpecial", function(object,toucher)
if not isServer and multiplayer then return false end
if enabledrill == 0 then
P_RemoveMobj(object)
return false end
end,MT_NIGHTSDRILLREFILL)

addHook("TouchSpecial", function(object,toucher)
if not isServer and multiplayer then return false end
if enabletime == 0 then
P_RemoveMobj(object)
return false end
end,MT_NIGHTSEXTRATIME)

addHook("PlayerThink", function(player)-- stupid dumb idiot code
if player.shrinktrap and player.mo then
	if player.shrinktrap>0 then
		player.mo.destscale = FRACUNIT/2
		player.shrinktrap = player.shrinktrap - 1
	end
	if player.shrinktrap<0 then
		player.mo.destscale = FRACUNIT*2
		player.shrinktrap = player.shrinktrap + 1
	end
	if player.shrinktrap == 0 then
		player.mo.destscale = FRACUNIT
	end
end
end)

addHook("PlayerThink", function(player)-- stupid dumb idiot code
if player.doublerings then
	if player.doublerings>0 then
		if player.rings > player.oldrings then
		player.rings = player.rings+(player.rings-player.oldrings)
		player.oldrings = player.rings
		end
		if player.rings < player.oldrings then
		player.oldrings = player.rings end
		player.doublerings = player.doublerings - 1
	end
	end
end)

addHook("PlayerThink", function(player)-- stupid dumb idiot code
if player.frictiontrap then
	if player.frictiontrap>0 then
		player.mo.friction = 63815
		player.mo.movefactor = FRACUNIT/3
		player.frictiontrap = player.frictiontrap - 1
		if player.frictiontrap == 0 then
			player.mo.friction = 59392
			player.mo.movefactor = FRACUNIT
		end
	end
end
end)



addHook("PlayerThink", function(player)-- stupid dumb idiot code
if player.forcestrap then
	if player.forcestrap>0 and (player.powers[pw_carry] & CR_ROPEHANG == 0)  then
		local angle = player.mo.angle
		player.mo.momx = FixedMul(36*FRACUNIT, cos(angle))
        player.mo.momy = FixedMul(36*FRACUNIT, sin(angle))
		player.drawangle = angle
		player.forcestrap = player.forcestrap - 1
	end
end
end)

addHook("PlayerSpawn",function(player)

player.rings = $ + bytes[23]*5

end)


addHook("MobjDeath", function(object, source, inflictor)
if not isserver and multiplayer then return end
local f = assert(io.openlocal("archipelago/APTokens.txt","a"))
f:write(gamemap)
f:write(object.x)
f:write(object.y)
local stringma = [[ 
]]
f:write(stringma)

token = 0
f:close()
end, MT_TOKEN)

addHook("MobjDeath", function(object, source, inflictor)
if not isserver and multiplayer then return end
local f = assert(io.openlocal("archipelago/APTokens.txt","a"))
f:write(gamemap)
f:write(":")
--f:write(object.x)
--f:write(object.y)
f:write("L")
f:write(object.checkid)
local stringma = [[ 
]]
f:write(stringma)
f:close()
end, MT_1UP_BOX)






addHook("MobjDeath", function(object, source, inflictor)
if not isserver and multiplayer then return end
local f = assert(io.openlocal("archipelago/APTokens.txt","a"))
f:write(gamemap)
f:write(":")
--f:write(object.x)
--f:write(object.y)
f:write("R")
f:write(object.checkid)
local stringma = [[ 
]]
f:write(stringma)
f:close()
end, MT_RING_BOX)

--addHook("MobjSpawn", function(object)
--if not isserver and multiplayer then return end
--local f = assert(io.openlocal("APTokens.txt","a"))
--f:write("MAP")
--f:write(gamemap)
--f:write(" Monitor - x:")
--f:write(object.x/65536)
--f:write(" y:")
--f:write(object.y/65536)
--local stringma = [[ 
--]]
--f:write(stringma)
--f:close()
--P_RemoveMobj(object)
--end, MT_GARGOYLE)

local function HUDstuff(v)



local curembl = bytes[21]
local goalembl = bytes[22]

if goalembl != 0 then

--if (bytes[10] & 64) == 6

	
v.drawString(16*v.dupx(), 74*v.dupy(), "Emblems:",V_NOSCALESTART)
v.drawString(16*v.dupx(), 84*v.dupy(), curembl,V_NOSCALESTART)
v.drawString(42*v.dupx(), 84*v.dupy(), "/",V_NOSCALESTART)
v.drawString(50*v.dupx(), 84*v.dupy(), goalembl,V_NOSCALESTART)


end
end

hud.add(HUDstuff,"scores")



local function coords(v,player)
if showcoords then


if player and player.valid and player.bot == BOT_NONE then

v.drawString(16*v.dupx(), 54*v.dupy(), "X:",V_NOSCALESTART)
v.drawString(30*v.dupx(), 54*v.dupy(), player.mo.x/FRACUNIT,V_NOSCALESTART)
v.drawString(16*v.dupx(), 64*v.dupy(), "Y:",V_NOSCALESTART)
v.drawString(30*v.dupx(), 64*v.dupy(), player.mo.y/FRACUNIT,V_NOSCALESTART)
end
end


end

hud.add(coords,"game")






local function charSwitcher(line, mo)

//lock/stop player movement
mo.player.inswitcher = 1
//construct global available character list
end
addHook("LinedefExecute", charSwitcher, "CHARSWI")


addHook("PlayerThink", function(player)
if player.inswitcher then
//player.mo.momx = 0
//player.mo.momy = 0
//player.mo.angle = player.initialangle


if (player.cmd.buttons & BT_JUMP) or (player.cmd.buttons & BT_SPIN) then
		player.inswitcher = 0
		if skins[unlockedchars[player.selected]] and skins[unlockedchars[player.selected]].valid then
		S_StartSound(object, sfx_strpst)
		else
		S_StartSound(object, sfx_lose)
		end
    end



local c1held = false
local c2held = false

if player.cmd.buttons & BT_CUSTOM1 then --deadzone
c1held = true
end
if player.cmd.buttons & BT_CUSTOM2 then --deadzone
c2held = true
end


if not player.c1held or player.c1held> TICRATE/2 then

if (c1held) then
        player.selected = $ + 1
		if player.selected > #unlockedchars then
		player.selected = #unlockedchars
		else
		S_StartSound(object, sfx_menu1)
		end
		if skins[unlockedchars[player.selected]] then
		if player.mo.skin != unlockedchars[player.selected] then
		R_SetPlayerSkin(player, unlockedchars[player.selected])
		end
		else
		print("Character addon not loaded")
		end
    end
	end
	
	if not player.c2held or player.c2held> TICRATE/2 then
if (c2held) then
        player.selected = $ - 1
		if player.selected < 1 then
		player.selected = 1 else
		S_StartSound(object, sfx_menu1)
		end
		if skins[unlockedchars[player.selected]] and skins[unlockedchars[player.selected]].valid then
		if player.mo.skin != unlockedchars[player.selected] then
		R_SetPlayerSkin(player, unlockedchars[player.selected])
		end
		else
		print("Character addon not loaded")
		end
    end
	end

if c1held then
player.c1held = $ + 1
else
player.c1held = 0
end
if c2held then
player.c2held = $ + 1
else
player.c2held = 0
end
player.powers[pw_nocontrol]=1
end
end)

local function switcherhud(v,player)
    -- Only draw if the player is valid and in-game
	
	if player.inswitcher then
    if player and player.valid and player.bot == BOT_NONE then

	v.drawString(16*v.dupx(),4*v.dupy(),"C1/C2 to scroll")
	
	for index,x in pairs(unlockedchars) do
	if not x then
	continue
	end
	
	local offset = 0
	if player.selected > 20 then
	if player.selected < #unlockedchars - 2 then 
	offset = (player.selected-20)*8
	else
	offset = (#unlockedchars-22)*8
	end
	end
	
	
		if index == player.selected then
		v.drawString(300-v.stringWidth(x),((index*3))*3-offset,x,V_YELLOWMAP|V_SNAPTORIGHT)
		else
		v.drawString(300-v.stringWidth(x),((index*3))*3-offset,x,V_SNAPTORIGHT)
		end

	
	
	

	end
    
	end
	end
end

hud.add(switcherhud,"game")
local function beSonic(line, mo)
   R_SetPlayerSkin(mo.player, "sonic")
end

addHook("LinedefExecute", beSonic, "BE_SONIC")


local function beTails(line, mo)
   R_SetPlayerSkin(mo.player, "tails")
end

addHook("LinedefExecute", beTails, "BE_TAILS")


local function beKnuckles(line, mo)
   R_SetPlayerSkin(mo.player, "knuckles")
end

addHook("LinedefExecute", beKnuckles, "BE_KNUX")


local function beAmy(line, mo)
   R_SetPlayerSkin(mo.player, "amy")
end

addHook("LinedefExecute", beAmy, "BE_AMY")


local function beFang(line, mo)
   R_SetPlayerSkin(mo.player, "fang")
end

addHook("LinedefExecute", beFang, "BE_FANG")


local function beMetal(line, mo)
   R_SetPlayerSkin(mo.player, "metalsonic")
end

addHook("LinedefExecute", beMetal, "BE_METAL")




local function dofiller(file)
--print(bytes[2])
if bytes[0] != 0 then --deathlink
print("Received Deathlink")
for player in players.iterate() do
        if player and player.valid and player.mo then
            player.nightstime = 0
	    player.powers[pw_invulnerability] = 0
	    player.powers[pw_super] = 0
            P_DamageMobj(player.mo, nil, nil, 1, DMG_INSTAKILL)
		player.deadtimer = 2
        end
    end
bytes[0] = 0
end
--TODO outgoing deathlink

if bytes[2] != 0 then --traps
if bytes[2] == 1 then --1up
for player in players.iterate() do
        if player and player.valid then
            player.lives = $ + 1
	    P_PlayLivesJingle(player)
        end
    end
--if not multiplayer then print("Recieved 1UP")
--else COM_BufInsertText(server, "say Recieved 1UP") end


end
if bytes[2] == 2 then --force pity shield
for player in players.iterate() do
        if player and player.valid and player.mo then
	    player.powers[pw_shield] = SH_PITY
	    P_SpawnShieldOrb(player)
        end
    end
end
if bytes[2] == 3 then --force gravity boots
for player in players.iterate() do
        if player and player.valid and player.mo then
	    player.powers[pw_gravityboots] = 20*TICRATE
        end
    end
end
if bytes[2] == 4 then --replay tutorial

	    G_SetCustomExitVars(1000, 1)
        G_ExitLevel()
	    print("Replay the Tutorial IDIOT")

end
if bytes[2] == 5 then --ring drain
for player in players.iterate() do
        if player and player.valid and player.mo then
	   player.rings = player.rings - 100
        end
    end
end

if bytes[2] == 6 then --& knuckles
G_AddPlayer(skins[2].name,"Red","Knuckles",BOT_2PAI)
	    --COM_BufInsertText(server, "addbot knuckles")
	    --S_StartSound(player.mo, sfx_bowl)

end

if bytes[2] == 7 then --dropped inputs
for player in players.iterate() do
        if player and player.valid and player.mo then
		player.powers[pw_nocontrol] = 3*TICRATE

        end
    end
end

if bytes[2] == 8 then --50 rings
for player in players.iterate() do
	        player.rings =  $ + 50
    end
end

if bytes[2] == 9 then --20 rings
for player in players.iterate() do
        if player and player.valid and player.mo then
	        player.rings =  $ + 20

        end
    end
end

if bytes[2] == 10 then --10 rings
for player in players.iterate() do
        if player and player.valid and player.mo then
	        player.rings =  $ + 10
        end
    end
end
if bytes[2] == 11 then --icy floors
for player in players.iterate() do
        if player and player.valid and player.mo then
	        player.frictiontrap = TICRATE*75

        end
    end
end

if bytes[2] == 12 then --1000 points
for player in players.iterate() do

			P_AddPlayerScore(player, 1000)

    end
end

if bytes[2] == 13 then --sonic forces
for player in players.iterate() do
        if player and player.valid and player.mo then
			player.forcestrap = TICRATE*20
        end
    end
end


if bytes[2] == 14 then --invincibility
for player in players.iterate() do
        if player and player.valid and player.mo then
		player.powers[pw_invulnerability] = 20*TICRATE

        end
    end

S_ChangeMusic("_INV", true)
end

if bytes[2] == 15 then --speed shoes
for player in players.iterate() do
        if player and player.valid and player.mo then
		player.powers[pw_sneakers] = 20*TICRATE

        end
    end
	S_ChangeMusic("_SHOES", true)

end

if bytes[2] == 16 then --self propelled bomb
P_SpawnMobjFromMobj(players[0].mo,0,0,400*FRACUNIT,MT_SPBM)
end

if bytes[2] == 17 then --shrink monitor
for player in players.iterate() do
        if player and player.valid and player.mo then
		player.shrinktrap = TICRATE*40

        end
    end
end
if bytes[2] == 18 then --grow monitor
for player in players.iterate() do
        if player and player.valid and player.mo then
		player.shrinktrap = TICRATE*-40

        end
    end
end
if bytes[2] == 19 then --double rings
for player in players.iterate() do
        if player and player.valid and player.mo then
		player.doublerings = 30*TICRATE
		player.oldrings = player.rings
        end
    end
end
if bytes[2] == 20 then --jumpscare
for player in players.iterate do
S_StartSound(object, sfx_kc57)
end
jumpscaretime = TICRATE * 2
if custom_images then
jumpscaretype = P_RandomKey(custom_images)
else
jumpscaretype = P_RandomKey(num_images)
end
end




bytes[2] = 0
end
end








local function readupdates()
--if host or singleplayer open the normal one


if syncfile != 0 and multiplayer then

downloading = 1
io.open("archipelago/APTranslator.dat", "r", function(file)
    if not file then
        print("APTranslator.dat does not exist, let the AP client make it for you")
        return
    end


    local data = file:read(30)
	file:seek("set",0)
--local bytes = {}
local iterator = 0
while true do
    local bite = file:read(1)
    if bite == nil then
        break
    else
        bytes[iterator] = string.byte(bite)
		iterator = $ + 1
    end
end
    local clientFile = io.openlocal("client/archipelago/APTranslator.dat", "w")
	if data then
    clientFile:write(data) end

	
	downloading = 0
end)
syncfile = 0

end
if not multiplayer then

local file = assert(io.openlocal("archipelago/APTranslator.dat","r+b"))


local iterator = 0
while true do
    local bite = file:read(1)
    if bite == nil then
        break
    else
        bytes[iterator] = string.byte(bite)
		iterator = $ + 1
    end
end
file:close()
end

end


local function fuckingdumb()

dofiller()

--ring link/deathlink for multiplayer here\
local collectivedifference = 0
if bytes[30] > 0 then



for player in players.iterate() do
if player.bot == BOT_NONE then

if player.nightstime > 0 and player.rings == 0 and lastknownrings!=0 then 
player.rings = lastknownrings
end

collectivedifference = $ + player.rings - player.prevrings
end
end

lastknownrings = $ + collectivedifference
for player in players.iterate() do
if player.bot == BOT_NONE then
player.rings = lastknownrings
player.prevrings = lastknownrings

end
end
end







  if (bytes[20] & 128) == 128 then --deathlink is on
for player in players.iterate() do
if player.bot == BOT_NONE then
if player.deadtimer == 1 then
if multiplayer then
print(player.name.." sent a Deathlink")
else
print("Sent Deathlink")
end

for player2 in players.iterate() do

            player2.nightstime = 0
	    player2.powers[pw_invulnerability] = 0
	    player2.powers[pw_super] = 0
		
            P_DamageMobj(player2.mo, nil, nil, 1, DMG_INSTAKILL)
		player2.deadtimer = 2
			
			
			
end
end
end
end
end


for player in players.iterate() do
			if bytes[30] > 1 then
			if player.deadtimer == 2 then
			player.rings = 0
			end
			end
end


if isserver or not multiplayer then

for player in players.iterate() do
        if player and player.valid and player.mo then
            if player.deadtimer == 1 and player.bot == BOT_NONE then --send a deathlink
		if bytes[30] > 1 then
			
		player.rings = 0
			
		end
		senddeath = true
		end
        end
    end



if downloading == 0 then


local result = pcall(function()
	local f = assert(io.openlocal("archipelago/APTranslator.dat","r+b"))
    return true
end)
if result == false then
error("€Couldn't find APTranslator.dat. Run the AP client before loading this addon. If you are using linux, you must create .srb2/luafiles/archipelago/APTranslator.dat manually before running the client")
end
local f = assert(io.openlocal("archipelago/APTranslator.dat","r+b"))

local file_flag = false
if f then
result = pcall(function()
	f:seek("set",24)
    file_flag = string.byte(f:read(1))
    return true
end)
if result == true then
f:seek("set",24)
file_flag = string.byte(f:read(1))
else
error("€FILE READ ERROR This is likely a result of APTranslator.dat being read before opening the AP client. Ensure you selected the right folder for the AP client and run it before loading the addon.")
return
end


if bytes[30] > 0 then --ring link


        if players[0] and players[0].valid and players[0].mo and players[0].bot == BOT_NONE then
		local player = players[0]
		f:seek("set",26)--rings set to file
		local low_byte = string.byte(f:read(1))
		local fullrings = string.byte(f:read(1))*256 + low_byte



		if fullrings != 0 then //rings need to be received
		if fullrings >= 0x8000 then
			fullrings = fullrings - 0x10000//convert to signed
		end
		
		player.rings = $ + fullrings
		COM_BufInsertText(player, "setrings "..player.rings)
		f:seek("set",26)//write 0 to file
		f:write("\0")
		f:write("\0")
		end



		if collectivedifference != 0 then//outgoing rings
			f:seek("set",28)
			local low_byte = string.byte(f:read(1))
			local fullrings = string.byte(f:read(1))*256 + low_byte
			player.rings = lastknownrings
			-- run setrings for multiplayer purposes
			COM_BufInsertText(player, "setrings "..player.rings)
			
			f:seek("set",28)
			local rings16bit = (fullrings + collectivedifference) & 0xFFFF
			f:write(string.char(rings16bit&0xFF,(rings16bit>>8)&0xFF))
			f:flush()--love working with binary file why cant i just write an int
			end

		if manualringlink != 0 then 
		f:seek("set",28)
			local low_byte = string.byte(f:read(1))
			local fullrings = string.byte(f:read(1))*256 + low_byte
			
			
		f:seek("set",28)
			local rings16bit = (fullrings-manualringlink) & 0xFFFF
			f:write(string.char(rings16bit&0xFF,(rings16bit>>8)&0xFF))
			f:flush()--love working with binary file why cant i just write an int
			
		COM_BufInsertText(player, "setrings "..player.rings-manualringlink)
			
		manualringlink = 0
			
		end



        end
    end




if file_flag !=0 then
if (file_flag & 1) == 1 then
if multiplayer then downloading = 1
COM_BufInsertText(players[0], "syncfile") end
end

if (file_flag & 2) == 2 then
local g = assert(io.openlocal("archipelago/APTextTransfer.txt","r+"))
g:seek("set",0)
local stringarray = {}
local string = g:read()
while (string != nil) do
if not multiplayer then print(string)
else COM_BufInsertText(players[0], "say "..string)
end
string = g:read()
end
end
f:seek("set",24)
f:write("\0")
f:flush()
bytes[24] = 0

end
if downloading == 0 then
f:seek("set",2)
f:write("\0")
f:seek("set",0)
f:write("\0")
f:flush()
end
if senddeath then
f:seek("set",1)
f:write("x")
f:flush()
senddeath = false
end



f:close()
end
end
end






if bytes[9] & 2 != 2 then --whirlwind
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_WHIRLWIND then
		player.powers[pw_shield] = SH_NONE
		end
		if player.powers[pw_shield] == (SH_WHIRLWIND | SH_FIREFLOWER) then
		player.powers[pw_shield] = SH_FIREFLOWER
		end
        end
    end
end
if bytes[9] & 4 != 4 then --armageddon
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_ARMAGEDDON then
		player.powers[pw_shield] = SH_NONE
		end
		if player.powers[pw_shield] == (SH_ARMAGEDDON | SH_FIREFLOWER) then
		player.powers[pw_shield] = SH_FIREFLOWER
		end
        end
    end
end
if bytes[10] & 2 != 2 then --super paraloop
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_nights_superloop] != 0 then
		player.powers[pw_nights_superloop] = 0
		end
        end
    end
end
if bytes[10] & 4 != 4 then --nightopian helper
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_nights_helper] != 0 then
		player.powers[pw_nights_helper] = 0
		end
        end
    end
end
if bytes[10] & 8 != 8 then --link freeze
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_nights_linkfreeze] != 0 then
		player.powers[pw_nights_linkfreeze] = 0
		end
        end
    end
end
if bytes[10] & 16 != 16 then
enabletime = 1

end
if bytes[10] & 32 != 32 then
enabledrill = 1
end



if bytes[9] & 8 != 8 then --elemental
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_ELEMENTAL then
		player.powers[pw_shield] = SH_NONE
		end
		if player.powers[pw_shield] == (SH_ELEMENTAL | SH_FIREFLOWER) then
		player.powers[pw_shield] = SH_FIREFLOWER
		end
        end
    end
end

if bytes[9] & 16 != 16 then --attraction
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_ATTRACT then
		player.powers[pw_shield] = SH_NONE
		end
		if player.powers[pw_shield] == (SH_ATTRACT | SH_FIREFLOWER) then
		player.powers[pw_shield] = SH_FIREFLOWER
		end
        end
    end
end
if bytes[9] & 32 != 32 then --force
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] & SH_FORCE then
		player.powers[pw_shield] = SH_NONE
		end
        end
    end
end

if bytes[9] & 64 != 64 then --s3k flame
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_FLAMEAURA then
		player.powers[pw_shield] = SH_NONE
		end
        end
    end
end

if bytes[9] & 128 != 128 then --s3k bubble
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_BUBBLEWRAP then
		player.powers[pw_shield] = SH_NONE
		end
        end
    end
end

if bytes[10] & 1 != 1 then --s3k lightning
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_THUNDERCOIN then
		player.powers[pw_shield] = SH_NONE
		end
        end
    end
end

if bytes[13] & 8 != 8 then --zoom tubes
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_carry] == CR_ZOOMTUBE then
		player.powers[pw_carry] = CR_NONE
		P_DoPlayerPain(player)
		player.powers[pw_flashing] = 0
		end
        end
    end
end
if bytes[13] & 16 != 16 then --rope hangs
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_carry] == CR_ROPEHANG then
		player.powers[pw_carry] = CR_NONE
		P_DoPlayerPain(player)
		player.powers[pw_flashing] = 1
		end
        end
    end
end
if bytes[13] & 32 != 32 then --swinging maces
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_carry] == CR_MACESPIN then
		player.powers[pw_carry] = CR_NONE
		P_DoPlayerPain(player)
		player.powers[pw_flashing] = 1
		end
        end
    end
end
if bytes[13] & 64 != 64 then --minecarts
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_carry] == CR_MINECART then
		player.powers[pw_carry] = CR_NONE
		P_DoPlayerPain(player)
		player.powers[pw_flashing] = 1
		end
        end
    end
end
if bytes[13] & 128 != 128 then --rollout rocks
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_carry] == CR_ROLLOUT then
		--player.powers[pw_carry] = CR_NONE
		P_DoPlayerPain(player)
		player.powers[pw_flashing] = 1
		end
        end
    end
end
if bytes[14] & 4 != 4 then --buoyant slime
for player in players.iterate() do
        if player and player.valid and player.mo then
			for fuck in player.mo.subsector.sector.ffloors()
				if fuck.master.special == 120 and player.mo.z<fuck.sector.ceilingheight then
				--P_DoPlayerPain(player)
				--player.powers[pw_flashing] = 0
				if gamemap == 4 or gamemap == 5 or gamemap == 40 or gamemap == 533 then--stupidhack
					    player.powers[pw_invulnerability] = 0
						player.powers[pw_super] = 0
						P_DamageMobj(player.mo, nil, nil, 1, DMG_INSTAKILL)
						print("Buoyant Slime not unlocked")
						end
				end
				end
		end
        end
end

if gamemap == 125 then


--10&64   10&128



  if (bytes[3] & 1) == 1 then
  P_LinedefExecute(100)
  end
  if (bytes[3] & 2) == 2 then
  P_LinedefExecute(101)
  end
  if (bytes[3] & 4) == 4 then
  P_LinedefExecute(102)
  end
  if (bytes[3] & 8) == 8 then
  P_LinedefExecute(103)
  end
  if (bytes[3] & 16) == 16 then
  P_LinedefExecute(104)
  end
  if (bytes[3] & 32) == 32 then
  P_LinedefExecute(105)
  end
  if (bytes[3] & 64) == 64 then
  P_LinedefExecute(106)
  end
  if (bytes[3] & 128) == 128 then
  P_LinedefExecute(107)
  end
  if (bytes[4] & 1) == 1 then
  P_LinedefExecute(108)
  end
  if (bytes[4] & 2) == 2 then
  P_LinedefExecute(109)
  end
  if (bytes[4] & 4) == 4 then
  P_LinedefExecute(110)
  end
  if (bytes[4] & 8) == 8 then
  P_LinedefExecute(111)
  end
  if (bytes[4] & 16) == 16 then
  P_LinedefExecute(112)
  end
  if (bytes[4] & 32) == 32 then
  P_LinedefExecute(113)
  end
  if (bytes[4] & 64) == 64 then
  P_LinedefExecute(114)
  end
  if (bytes[4] & 128) == 128 then
  P_LinedefExecute(115)
  end
  if (bytes[5] & 4) == 4 then
  P_LinedefExecute(116)
  end
  if (bytes[5] & 8) == 8 then
  P_LinedefExecute(117)
  end
  if (bytes[5] & 32) == 32 then
  P_LinedefExecute(118)
  end
  if (bytes[5] & 64) == 64 then
  P_LinedefExecute(119)
  end
  if (bytes[5] & 128) == 128 then
  P_LinedefExecute(120)
  end
  if (bytes[6] & 1) == 1 then
  P_LinedefExecute(121)
  end
  if (bytes[6] & 2) == 2 then
  P_LinedefExecute(122)
  end
  if (bytes[6] & 4) == 4 then
  P_LinedefExecute(123)
  end
  if (bytes[6] & 8) == 8 then
  P_LinedefExecute(124)
  end
  if (bytes[6] & 16) == 16 then
  P_LinedefExecute(125)
  end
  if (bytes[6] & 32) == 32 then
  P_LinedefExecute(126)
  end
  if (bytes[6] & 64) == 64 then
  P_LinedefExecute(127)
  end
  if (bytes[6] & 128) == 128 then
  P_LinedefExecute(128)
  end
  if (bytes[7] & 1) == 1 then
  P_LinedefExecute(129)
  end
  if (bytes[7] & 2) == 2 then
  P_LinedefExecute(130)
  end
    if (bytes[7] & 4) == 4 then
  P_LinedefExecute(131)
  end
  if (bytes[7] & 8) == 8 then--multiplayer stage toggle
  P_LinedefExecute(132)
  end
if (bytes[7] & 16) == 16 then
  P_LinedefExecute(133)
  end
if (bytes[7] & 32) == 32 then
  P_LinedefExecute(134)
  end
if (bytes[7] & 64) == 64 then
  P_LinedefExecute(135)
  end
if (bytes[7] & 128) == 128 then
  P_LinedefExecute(136)
  end
if (bytes[8] & 1) == 1 then
  P_LinedefExecute(137)
  end
if (bytes[8] & 2) == 2 then
  P_LinedefExecute(138)
  end
if (bytes[8] & 4) == 4 then
  P_LinedefExecute(139)
  end
if (bytes[8] & 8) == 8 then
  P_LinedefExecute(140)
  end
if (bytes[8] & 16) == 16 then
  P_LinedefExecute(141)
  end
if (bytes[8] & 32) == 32 then
  P_LinedefExecute(142)
  end
if (bytes[8] & 64) == 64 then
  P_LinedefExecute(143)
  end
if (bytes[8] & 128) == 128 then
  P_LinedefExecute(144)
  end
if (bytes[9] & 1) == 1 then
  P_LinedefExecute(145)
  end
   if (bytes[14] & 128) == 128 then--match map toggle
  P_LinedefExecute(146)
  end
 if (bytes[10] & 64) == 64 then--match maps
  P_LinedefExecute(147)
  end
if (bytes[10] & 128) == 128 then
  P_LinedefExecute(148)
  end
if (bytes[11] & 1) == 1 then
  P_LinedefExecute(149)
  end
if (bytes[11] & 2) == 2 then
  P_LinedefExecute(150)
  end
if (bytes[11] & 4) == 4 then
  P_LinedefExecute(151)
  end
if (bytes[11] & 8) == 8 then
  P_LinedefExecute(152)
  end
if (bytes[11] & 16) == 16 then
  P_LinedefExecute(153)
  end
if (bytes[11] & 32) == 32 then
  P_LinedefExecute(154)
  end
 if (bytes[11] & 64) == 64 then
  P_LinedefExecute(155)
  end
  if (bytes[11] & 128) == 128 then
  P_LinedefExecute(156)
  end
  if (bytes[12] & 1) == 1 then
  P_LinedefExecute(157)
  end
  if (bytes[12] & 2) == 2 then
  P_LinedefExecute(158)
  end
  if (bytes[12] & 4) == 4 then
  P_LinedefExecute(159)
  end
  if (bytes[12] & 8) == 8 then
  P_LinedefExecute(160)
  end
  if (bytes[12] & 16) == 16 then
  P_LinedefExecute(161)
  end
  if (bytes[12] & 32) == 32 then
  P_LinedefExecute(162)
  end
  if (bytes[12] & 64) == 64 then
  P_LinedefExecute(163)
  end
  if (bytes[12] & 128) == 128 then
  P_LinedefExecute(164)
  end
  if (bytes[13] & 1) == 1 then
  P_LinedefExecute(165)
  end
  if (bytes[13] & 2) == 2 then
  P_LinedefExecute(166)
  end
  if (bytes[13] & 4) == 4 then
  P_LinedefExecute(167)
  end

    if (bytes[20] & 1) then
    P_LinedefExecute(41)
    end
  if (bytes[20] & 2) then -- emblemhints
    P_LinedefExecute(42)
    end
	if (bytes[20] & 4) then--soundtest
    P_LinedefExecute(43)
    end
	--linedef 63 is something

end
  --emeralds = emeralds | bytes[15]
  --emeralds = emeralds & bytes[15]
emeralds = bytes[31]
end






addHook("ThinkFrame", readupdates,"DEATHL")

addHook("ThinkFrame", fuckingdumb,"DUMBCO")


local function bancharacters()

//construct list of valid characters
unlockedchars = {}

if (bytes[8] & 8) != 0 then
table.insert(unlockedchars,"sonic")
end
if (bytes[8] & 16) != 0 then
table.insert(unlockedchars,"tails")
end
if (bytes[8] & 32) != 0 then
table.insert(unlockedchars,"knuckles")
end
if (bytes[8] & 64) != 0 then
table.insert(unlockedchars,"amy")
end
if (bytes[8] & 128) != 0 then
table.insert(unlockedchars,"fang")
end
if (bytes[9] & 1) != 0 then
table.insert(unlockedchars,"metalsonic")
end

if (bytes[15] & 1) != 0 then
table.insert(unlockedchars,"mario")
end
if (bytes[15] & 2) != 0 then
table.insert(unlockedchars,"luigi")
end
if (bytes[15] & 4) != 0 then
table.insert(unlockedchars,"yoshi")
end
if (bytes[15] & 8) != 0 then
table.insert(unlockedchars,"ray")
end
if (bytes[15] & 16) != 0 then
table.insert(unlockedchars,"silver")
end
if (bytes[15] & 32) != 0 then
table.insert(unlockedchars,"shadow")
end
if (bytes[15] & 64) != 0 then
table.insert(unlockedchars,"modernsonic")
end
if (bytes[15] & 128) != 0 then
table.insert(unlockedchars,"werehog")
end
if (bytes[16] & 1) != 0 then
table.insert(unlockedchars,"metalknuckles")
end
if (bytes[16] & 2) != 0 then
table.insert(unlockedchars,"tailsdoll")
end
if (bytes[16] & 4) != 0 then
table.insert(unlockedchars,"espio")
end
if (bytes[16] & 8) != 0 then
table.insert(unlockedchars,"mighty")
end
if (bytes[16] & 16) != 0 then
table.insert(unlockedchars,"charmy")
end
if (bytes[16] & 32) != 0 then
table.insert(unlockedchars,"vector")
end
if (bytes[16] & 64) != 0 then
table.insert(unlockedchars,"heavy")
end
if (bytes[16] & 128) != 0 then
table.insert(unlockedchars,"bomb")
end

if (bytes[17] & 1) != 0 then
table.insert(unlockedchars,"bean")
end
if (bytes[17] & 2) != 0 then
table.insert(unlockedchars,"eggman")
end
if (bytes[17] & 4) != 0 then
table.insert(unlockedchars,"adventuresonic")
end
if (bytes[17] & 8) != 0 then
table.insert(unlockedchars,"tangle")
end
if (bytes[17] & 16) != 0 then
table.insert(unlockedchars,"blaze")
end
if (bytes[17] & 32) != 0 then
table.insert(unlockedchars,"marine")
end
if (bytes[17] & 64) != 0 then
table.insert(unlockedchars,"inazuma")
end
if (bytes[17] & 128) != 0 then
table.insert(unlockedchars,"aether")
end








for player in players.iterate() do
if player.mo then
if player.bot == BOT_NONE then

local temp = false
for _,v in pairs(unlockedchars) do
  if v == player.mo.skin then
	temp = true
	break
  end
end
local temp2 = false
for _,v in pairs(supportedchars) do
  if v == player.mo.skin then
	temp2 = true
	break
  end
end
if temp == false and temp2 == true then
if skins[unlockedchars[1]] then
R_SetPlayerSkin(player, unlockedchars[1])
else
if player.mo.skin != "sonic" then
R_SetPlayerSkin(player, "sonic")//if default is custom character, fallback to sonic
end
end
end
end


  
  
end
end
end



addHook("ThinkFrame", bancharacters,"BANCHR")


addHook("MobjSpawn", function(object)
if bytes[9] & 2 != 2 then
P_RemoveMobj(object)
end
end,MT_WHIRLWIND_BOX)

addHook("MobjSpawn", function(object)
if bytes[9] & 2 != 2 then
P_RemoveMobj(object)
end
end,MT_WHIRLWIND_GOLDBOX)

addHook("MobjSpawn", function(object)
if bytes[9] & 4 != 4 then
P_RemoveMobj(object)
end
end,MT_ARMAGEDDON_BOX)

addHook("MobjSpawn", function(object)
if bytes[9] & 4 != 4 then
P_RemoveMobj(object)
end
end,MT_ARMAGEDDON_GOLDBOX)

addHook("MobjSpawn", function(object)
if bytes[9] & 8 != 8 then
P_RemoveMobj(object)
end
end,MT_ELEMENTAL_BOX)

addHook("MobjSpawn", function(object)
if bytes[9] & 8 != 8 then
P_RemoveMobj(object)
end
end,MT_ELEMENTAL_GOLDBOX)

addHook("MobjSpawn", function(object)
if bytes[9] & 16 != 16 then
P_RemoveMobj(object)
end
end,MT_ATTRACT_BOX)

addHook("MobjSpawn", function(object)
if bytes[9] & 16 != 16 then
P_RemoveMobj(object)
end
end,MT_ATTRACT_GOLDBOX)

addHook("MobjSpawn", function(object)
if bytes[9] & 32 != 32 then
P_RemoveMobj(object)
end
end,MT_FORCE_BOX)

addHook("MobjSpawn", function(object)
if bytes[9] & 32 != 32 then
P_RemoveMobj(object)
end
end,MT_FORCE_GOLDBOX)


addHook("MobjSpawn", function(object)
if bytes[9] & 64 != 64 then
P_RemoveMobj(object)
end
end,MT_FLAMEAURA_BOX)

addHook("MobjSpawn", function(object)
if bytes[9] & 64 != 64 then
P_RemoveMobj(object)
end
end,MT_FLAMEAURA_GOLDBOX)

addHook("MobjSpawn", function(object)
if bytes[9] & 128 != 128 then
P_RemoveMobj(object)
end
end,MT_BUBBLEWRAP_BOX)

addHook("MobjSpawn", function(object)
if bytes[9] & 128 != 128 then
P_RemoveMobj(object)
end
end,MT_BUBBLEWRAP_GOLDBOX)

addHook("MobjSpawn", function(object)
if bytes[10] & 1 != 1 then
P_RemoveMobj(object)
end
end,MT_THUNDERCOIN_BOX)

addHook("MobjSpawn", function(object)
if bytes[10] & 1 != 1 then
P_RemoveMobj(object)
end
end,MT_THUNDERCOIN_GOLDBOX)


--addHook("MobjSpawn", function(object)
--if bytes[13] & 2 == 2 then
--P_RemoveMobj(object)
--end
--end,MT_TUBEWAYPOINT)

--addHook("MobjSpawn", function(object)
--if bytes[13] & 4 == 4 then
--P_RemoveMobj(object)
--end
--end,MT_CHAINMACEPOINT)



addHook("MobjSpawn", function(object)
if bytes[14] & 1 != 1 then
P_RemoveMobj(object)
end
end,MT_GARGOYLE)
addHook("MobjSpawn", function(object)
if bytes[14] & 1 != 1 then
P_RemoveMobj(object)
end
end,MT_BIGGARGOYLE)

addHook("MobjSpawn", function(object)
if bytes[14] & 2 != 2 then
P_RemoveMobj(object)
end
end,MT_BUBBLES)

addHook("MobjSpawn", function(object)
if bytes[14] & 8 != 8 then
P_RemoveMobj(object)
end
end,MT_DUSTDEVIL)

addHook("MobjSpawn", function(object)
if bytes[14] & 16 != 16 then
P_RemoveMobj(object)
end
end,MT_YELLOWSPRING)
addHook("MobjSpawn", function(object)
if bytes[14] & 16 != 16 then
P_RemoveMobj(object)
end
end,MT_YELLOWDIAG)

addHook("MobjSpawn", function(object)
if bytes[14] & 16 != 16 then
P_RemoveMobj(object)
end
end,MT_YELLOWHORIZ)

addHook("MobjSpawn", function(object)
if bytes[14] & 32 != 32 then
P_RemoveMobj(object)
end
end,MT_REDSPRING)
addHook("MobjSpawn", function(object)
if bytes[14] & 32 != 32 then
P_RemoveMobj(object)
end
end,MT_REDDIAG)
addHook("MobjSpawn", function(object)
if bytes[14] & 32 != 32 then
P_RemoveMobj(object)
end
end,MT_REDHORIZ)

addHook("MobjSpawn", function(object)
if bytes[14] & 64 != 64 then
P_RemoveMobj(object)
end
end,MT_BLUESPRING)
addHook("MobjSpawn", function(object)
if bytes[14] & 64 != 64 then
P_RemoveMobj(object)
end
end,MT_BLUEDIAG)
addHook("MobjSpawn", function(object)
if bytes[14] & 64 != 64 then
P_RemoveMobj(object)
end
end,MT_BLUEHORIZ)

hud.add(function(v, player, camera)
    -- Only draw if the player is valid and in-game
    if player and player.valid then 

	
	
	local string = "JMP"..tostring(jumpscaretype)
	
    local patch = v.cachePatch(string) -- crack coding
	

    -- Screen width and height
    --local screenWidth = v.width()
    --local screenHeight = v.height()

	if jumpscaretime > 0 then
    v.drawScaled(0, 0,FRACUNIT,patch,V_SNAPTOTOP|V_SNAPTOLEFT|V_HUDTRANS)
	end
	end
end, "game")
