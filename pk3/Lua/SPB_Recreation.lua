freeslot(
"S_SPB1",
"S_SPB2",
"S_SPB3",
"S_SPB4",
"S_SPB5",
"MT_SPBM",
"SPR_SPBM"
)
mobjinfo[MT_SPBM] = {
	doomednum = 1337,
	spawnstate = S_SPB1,
	spawnhealth = 1,
	seestate = S_SPB1,
	seesound = sfx_kc57,
	reactiontime = TICRATE,
	attacksound = sfx_kc57,
	painstate = S_SPB1,
	painchance = 0,
	painsound = sfx_kc57,
	meleestate = S_SPB1,
	missilestate = S_SPB1,
	deathstate = S_NULL,
	xdeathstate = S_NULL,
	deathsound = sfx_kc57,
	speed = 10,
	radius = 16*FRACUNIT,
	height = 32*FRACUNIT,
	dispoffset = 0,
	mass = 100,
	damage = 0,
	activesound = sfx_None,
	flags = MF_SPECIAL|MF_MISSILE|MF_NOCLIP|MF_NOGRAVITY,
	raisestate = S_SPB1
}

states[S_SPB1] = {
	sprite = SPR_SPBM,
	frame = 0,
	tics = -1,
	action = A_Look,
	var1 = 0,
	var2 = 0,
	nextstate = S_SPB1}
 
 states[S_SPB2] = {
	sprite = SPR_SPBM,
	frame = 2,
	tics = 2,
	action = A_Look,
	var1 = 0,
	var2 = 0,
	nextstate = S_SPB3}
 
 states[S_SPB3] = {
	sprite = SPR_SPBM,
	frame = 4,
	tics = 2,
	action = A_Look,
	var1 = 0,
	var2 = 0,
	nextstate = S_SPB4}
	
 states[S_SPB4] = {
	sprite = SPR_SPBM,
	frame = 6,
	tics = 2,
	action = A_Look,
	var1 = 0,
	var2 = 0,
	nextstate = S_SPB5}
	
 states[S_SPB5] = {
	sprite = SPR_SPBM,
	frame = 8,
	tics = 2,
	action = A_Look,
	var1 = 0,
	var2 = 0,
	nextstate = S_SPB1}	
	
addHook("MobjSpawn",function(object)
S_StartSound(object, sfx_kc57)
local highscore = -1
for player in players.iterate()
if player.score > highscore then
object.target = player.mo
highscore = player.score
end

end

end,MT_SPBM)

addHook("MobjThinker",function(object)
if object.target == nil then
P_RemoveMobj(object) end


local angle = R_PointToAngle2(object.x, object.y, object.target.x, object.target.y)
if object.target.z > object.z then
object.momz = object.momz+(FRACUNIT/2)
end
if object.target.z < object.z then
object.momz = object.momz-(FRACUNIT/2)
end
object.angle = angle
P_MoveOrigin(object, object.x+FixedMul(32*FRACUNIT, cos(angle)), object.y+FixedMul(32*FRACUNIT, sin(angle)), object.z)

end,MT_SPBM)

addHook("TouchSpecial",function(object,player)
P_DamageMobj(player, object, nil, 1, DMG_NUKE)
local boom = P_SpawnMobj(object.x, object.y, object.z, MT_BOSSEXPLODE)
boom.scale = FRACUNIT * 2
P_StartQuake(FRACUNIT*40,12,{object.x, object.y, object.z})
S_StartSound(player.mo, sfx_s3k4e)
P_RemoveMobj(object)
end, MT_SPBM)
--P_SupermanLook4Players(mobj_t actor) 