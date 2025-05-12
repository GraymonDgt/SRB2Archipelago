COM_AddCommand("hub", function(player)
if not isServer and multiplayer then 
print("You must be the server host to run this command")
return end
if gamemap == 1000 then
print("Nope, you have to complete the tutorial to go back")
return end
G_SetCustomExitVars(125, 1)
G_ExitLevel()
end)

--addHook("MobjSpawn", function(object)
--P_SpawnMobjFromMobj(object,0,0,0,MT_CUSTOMRING_BOX)
--P_RemoveMobj(object)
--end,MT_1UP_BOX)
--removed until i find a way to distribute 3d models in a pk3

local enabledrill = 0
local enabletime = 0

addHook("PlayerSpawn",function(player)
player.extrarings = 0
player.startingrings = 0
end)


addHook("NetVars",function(network)
for player in players.iterate()
        if player and player.valid then
            player.extrarings = network($)
			player.startingrings = network($)
        end
    end
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
end)


addHook("TouchSpecial", function(object,toucher)
if not isServer and multiplayer then return false end
print("herema")
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


addHook("PlayerThink", function()-- stupid dumb idiot code
for player in players.iterate() do
if player.frictiontrap then
	if player.frictiontrap>0 then
		player.mo.friction = 63820
		player.mo.movefactor = FRACUNIT/2
		player.frictiontrap = player.frictiontrap - 1
		if player.frictiontrap == 0 then
			player.mo.friction = 59392
			player.mo.movefactor = FRACUNIT
		end
	end
	end
end
end)

addHook("PlayerThink", function()-- stupid dumb idiot code
for player in players.iterate() do
if player.extrarings then
	if player.extrarings>0 then
		player.rings = $ + player.extrarings
		player.extrarings = 0
		end
	end
	end
end)


addHook("PlayerThink", function()-- stupid dumb idiot code
for player in players.iterate() do
if player.forcestrap then
	if player.forcestrap>0 then
		local angle = player.mo.angle
		player.mo.momx = FixedMul(36*FRACUNIT, cos(angle))  -- Knockback in facing direction
        player.mo.momy = FixedMul(36*FRACUNIT, sin(angle))
		player.drawangle = angle
		player.forcestrap = player.forcestrap - 1
	end
end
end
end)

addHook("PlayerSpawn",function(player)
if player.startingrings then
player.rings = player.startingrings
end
end)

addHook("MobjDeath", function(object, source, inflictor)
if not isserver and multiplayer then return end
local f = assert(io.openlocal("APTokens.txt","a"))
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
local f = assert(io.openlocal("APTokens.txt","a"))
f:write(gamemap)
f:write(":")
f:write(object.x)
f:write(object.y)
local stringma = [[ 
]]
f:write(stringma)
token = 0
f:close()
end, MT_1UP_BOX)



local function HUDstuff(v)

if not players[0].currentemblems then return end
local curembl = players[0].currentemblems
local goalembl = players[0].goalemblems

if goalembl != 0 then
for player in players.iterate() do
if player and player.valid then

v.drawString(16*v.dupx(), 54*v.dupy(), "Emblems:",V_NOSCALESTART)
v.drawString(16*v.dupx(), 64*v.dupy(), curembl,V_NOSCALESTART)
v.drawString(42*v.dupx(), 64*v.dupy(), "/",V_NOSCALESTART)
v.drawString(50*v.dupx(), 64*v.dupy(), goalembl,V_NOSCALESTART)
end
end
end
end

hud.add(HUDstuff,score)

--player.exiting force to be lower to exit faster



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




local function readupdates()
if not isserver and multiplayer then return end
local f = assert(io.openlocal("APTranslator.dat","r+b"))

f:seek("set",0)
local bytes = {}
while true do
    local byte = f:read(1)
    if byte == nil then
        break
    else
        bytes[#bytes+1] = string.byte(byte)
    end
end






if bytes[1] != 0 then --deathlink
for player in players.iterate() do
        if player and player.valid and player.mo then
            player.nightstime = 0
	    player.powers[pw_invulnerability] = 0
	    player.powers[pw_super] = 0
            P_DamageMobj(player.mo, nil, nil, 1, DMG_INSTAKILL)
        end
    end
f:seek("set",0)
f:write("\0")
f:flush()
print("Recieved Deathlink")
end

for player in players.iterate() do
        if player and player.valid and player.mo then
            if player.deadtimer == 1 then --send a deathlink
		f:seek("set",1)
		f:write("x")
		f:flush()
		end
        end
    end






if bytes[3] != 0 then --traps
if bytes[3] == 1 then --1up
for player in players.iterate() do
        if player and player.valid then
            player.lives = $ + 1
	    P_PlayLivesJingle(player)
        end
    end
--if not multiplayer then print("Recieved 1UP")
--else COM_BufInsertText(server, "say Recieved 1UP") end


end
if bytes[3] == 2 then --force pity shield
for player in players.iterate() do
        if player and player.valid and player.mo then
	    player.powers[pw_shield] = SH_PITY
	    P_SpawnShieldOrb(player)
        end
    end
end
if bytes[3] == 3 then --force gravity boots
for player in players.iterate() do
        if player and player.valid and player.mo then
	    player.powers[pw_gravityboots] = 20*TICRATE
        end
    end
end
if bytes[3] == 4 then --replay tutorial

	    G_SetCustomExitVars(1000, 1)
        G_ExitLevel()
	    print("Replay the Tutorial IDIOT")

end
if bytes[3] == 5 then --ring drain
for player in players.iterate() do
        if player and player.valid and player.mo then
	   player.extrarings = -100
        end
    end
end


if bytes[3] == 6 then --& knuckles
for player in players.iterate() do
        if player and player.valid and player.mo then
	    COM_BufInsertText(server, "addbot knuckles")


	    S_StartSound(player.mo, sfx_bowl)
        end
    end
end
if bytes[3] == 7 then --dropped inputs
for player in players.iterate() do
        if player and player.valid and player.mo then
		player.powers[pw_nocontrol] = 3*TICRATE

        end
    end
end

if bytes[3] == 8 then --50 rings
for player in players.iterate() do
	        player.extrarings = 50
    end
end

if bytes[3] == 9 then --20 rings
for player in players.iterate() do
        if player and player.valid and player.mo then
	        player.extrarings = 20

        end
    end
end

if bytes[3] == 10 then --10 rings
for player in players.iterate() do
        if player and player.valid and player.mo then
	        player.extrarings = 10
        end
    end
end
if bytes[3] == 11 then --icy floors
for player in players.iterate() do
        if player and player.valid and player.mo then
	        player.frictiontrap = TICRATE*60

        end
    end
end

if bytes[3] == 12 then --1000 points
for player in players.iterate() do

			P_AddPlayerScore(player, 1000)

    end
end

if bytes[3] == 13 then --sonic forces
for player in players.iterate() do
        if player and player.valid and player.mo then
			player.forcestrap = TICRATE*20
        end
    end
end


if bytes[3] == 14 then --invincibility
for player in players.iterate() do
        if player and player.valid and player.mo then
		player.powers[pw_invulnerability] = 20*TICRATE

        end
    end

S_ChangeMusic("_INV", true)
end

if bytes[3] == 15 then --speed shoes
for player in players.iterate() do
        if player and player.valid and player.mo then
		player.powers[pw_sneakers] = 20*TICRATE

        end
    end
	S_ChangeMusic("_SHOES", true)

end

f:seek("set",2)
f:write("\0")
f:flush()
end
  if bytes[25]>0 then
    local g = assert(io.openlocal("APTextTransfer.txt","r+"))
g:seek("set",0)
local string = g:read()
while (string != nil) do
if not multiplayer then print(string)
else COM_BufInsertText(players[0], "say "..string)
end

string = g:read()
 end
f:seek("set",24)
f:write("\0")
f:flush()
    end	


players[0].currentemblems = bytes[22]
players[0].goalemblems = bytes[23]


f:close()
if bytes[4] == 0 then --whirlwind
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_WHIRLWIND then
		player.powers[pw_shield] = SH_NONE
		end
        end
    end
end
if (bytes[5] & 1) == 0 then --armageddon
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_ARMAGEDDON then
		player.powers[pw_shield] = SH_NONE
		end
        end
    end
end
if (bytes[5] & 2) == 0 then --super paraloop
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_nights_superloop] != 0 then
		player.powers[pw_nights_superloop] = 0
		end
        end
    end
end
if (bytes[5] & 4) == 0 then --nightopian helper
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_nights_helper] != 0 then
		player.powers[pw_nights_helper] = 0
		end
        end
    end
end
if (bytes[5] & 8) == 0 then --link freeze
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_nights_linkfreeze] != 0 then
		player.powers[pw_nights_linkfreeze] = 0
		end
        end
    end
end
if (bytes[5] & 16) != 0 then
enabletime = 1

end
if (bytes[5] & 32) != 0 then
enabledrill = 1
end



if bytes[6] == 0 then --elemental
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_ELEMENTAL then
		player.powers[pw_shield] = SH_NONE
		end
        end
    end
end

if bytes[7] == 0 then --attraction
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_ATTRACT then
		player.powers[pw_shield] = SH_NONE
		end
        end
    end
end
if bytes[8] == 0 then --force
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] & SH_FORCE then
		player.powers[pw_shield] = SH_NONE
		end
        end
    end
end

if bytes[9] == 0 then --s3k flame
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_FLAMEAURA then
		player.powers[pw_shield] = SH_NONE
		end
        end
    end
end

if bytes[10] == 0 then --s3k bubble
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_BUBBLEWRAP then
		player.powers[pw_shield] = SH_NONE
		end
        end
    end
end

if bytes[11] == 0 then --s3k lightning
for player in players.iterate() do
        if player and player.valid and player.mo then
	    if player.powers[pw_shield] == SH_THUNDERCOIN then
		player.powers[pw_shield] = SH_NONE
		end
        end
    end
end

   for player in players.iterate() do
        if player and player.valid and player.mo then
		player.startingrings = bytes[24]*5
		
		
		
		end
	end



if gamemap == 125 then
  if (bytes[12] & 1) == 1 then
  P_LinedefExecute(100)
  end
  if (bytes[12] & 2) == 2 then
  P_LinedefExecute(101)
  end
  if (bytes[12] & 4) == 4 then
  P_LinedefExecute(102)
  end
  if (bytes[12] & 8) == 8 then
  P_LinedefExecute(103)
  end
  if (bytes[12] & 16) == 16 then
  P_LinedefExecute(104)
  end
  if (bytes[12] & 32) == 32 then
  P_LinedefExecute(105)
  end
  if (bytes[12] & 64) == 64 then
  P_LinedefExecute(106)
  end
  if (bytes[12] & 128) == 128 then
  P_LinedefExecute(107)
  end
  if (bytes[13] & 1) == 1 then
  P_LinedefExecute(108)
  end
  if (bytes[13] & 2) == 2 then
  P_LinedefExecute(109)
  end
  if (bytes[13] & 4) == 4 then
  P_LinedefExecute(110)
  end
  if (bytes[13] & 8) == 8 then
  P_LinedefExecute(111)
  end
  if (bytes[13] & 16) == 16 then
  P_LinedefExecute(112)
  end
  if (bytes[13] & 32) == 32 then
  P_LinedefExecute(113)
  end
  if (bytes[13] & 64) == 64 then
  P_LinedefExecute(114)
  end
  if (bytes[13] & 128) == 128 then
  P_LinedefExecute(115)
  end
  if (bytes[14] & 1) == 1 then
  P_LinedefExecute(116)
  end
  if (bytes[14] & 2) == 2 then
  P_LinedefExecute(117)
  end
  if (bytes[14] & 4) == 4 then
  P_LinedefExecute(118)
  end
  if (bytes[14] & 8) == 8 then
  P_LinedefExecute(119)
  end
  if (bytes[14] & 16) == 16 then
  P_LinedefExecute(120)
  end
  if (bytes[14] & 32) == 32 then
  P_LinedefExecute(121)
  end
  if (bytes[14] & 64) == 64 then
  P_LinedefExecute(122)
  end
  if (bytes[14] & 128) == 128 then
  P_LinedefExecute(123)
  end
  if (bytes[15] & 1) == 1 then
  P_LinedefExecute(124)
  end
  if (bytes[15] & 2) == 2 then
  P_LinedefExecute(125)
  end
  if (bytes[15] & 4) == 4 then
  P_LinedefExecute(126)
  end
  if (bytes[15] & 8) == 8 then
  P_LinedefExecute(127)
  end
  if (bytes[15] & 16) == 16 then
  P_LinedefExecute(128)
  end
  if (bytes[15] & 32) == 32 then
  P_LinedefExecute(129)
  end
  if (bytes[15] & 64) == 64 then
  P_LinedefExecute(130)
  end
    if (bytes[21] & 1) then
    P_LinedefExecute(41)
    end
  if (bytes[21] & 2) then -- emblemhints
    P_LinedefExecute(42)
    end
	if (bytes[21] & 4) then--soundtest
    P_LinedefExecute(43)
    end
	
	
end
  emeralds = emeralds | bytes[16]
  emeralds = emeralds & bytes[16]


	

end

addHook("ThinkFrame", readupdates,"DEATHL")









