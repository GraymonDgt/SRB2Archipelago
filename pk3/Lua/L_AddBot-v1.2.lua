-- This is a relatively simple script which provides tools for adding and removing 2P bots for use in single player and co-op.

local t = {
	-- Mod Settings,
	addon = "AddBot", -- Change this to the name of your addon
	-- Info
	version = 1,
	subversion = 2,
	develop = false,
	
}

if type(AddBotVersionInfo) == "table"
	print("AddBot already registered by previous addon: "..tostring(AddBotVersionInfo.addon))
	return
end

rawset(_G,"AddBotVersionInfo", t)




local BotPermissions = CV_RegisterVar{
	name = "botperms",
	defaultvalue = 0,
	flags = CV_NETVAR,
	PossibleValue = CV_OnOff
}

local MPBotPermissions = CV_RegisterVar{
	name = "mpbotperms",
	defaultvalue = 0,
	flags = CV_NETVAR,
	PossibleValue = CV_OnOff
}

local AutoJoinTeams = CV_RegisterVar{
	name = "botautojoin",
	defaultvalue = 1,
	flags = CV_NETVAR,
	PossibleValue = CV_OnOff
}

local BotLeaderPermissions = CV_RegisterVar{
	name = "botleaderperms",
	defaultvalue = 1,
	flags = CV_NETVAR,
	PossibleValue = CV_OnOff
}

local AutoMax = CV_RegisterVar {
	name = "botautomaxplayers",
	defaultvalue = 0,
	flags = CV_NETVAR,
	PossibleValue = CV_OnOff
}

local MaxBots = CV_RegisterVar{
	name = "maxbots",
	defaultvalue = 8,
	flags = CV_NETVAR,
	PossibleValue = {
		MIN = 0,
		MAX = 32
	}
}

local BotFollow = function(leader, bot)
	if leader and not(leader.spectate) and leader.lives
		bot.botleader = leader
		return true
	end
	return false
end

local AddBot = function(player, versus, skin, color, name)
	-- Skin
	if not(skins[skin])
		CONS_Printf(player, "Specified skin does not exist!")
		return
	else
		skin = skins[skin].name
	end
	-- Color
	if color 
		if not tonumber(color)
			color = R_GetColorByName($)
		else
			color = tonumber($)
		end
	end
	
	if not(color)
		color = skins[skin].prefcolor
	end
	-- Name
	if name == nil
		name = skins[skin].realname
	end

	-- Bot type
	local bottype = versus and BOT_MPAI
		or BOT_2PAI

	-- Create player
	local bot = G_AddPlayer(skin, color, name, bottype)
	if not bot
		CONS_Printf(player, "Failed to spawn bot "..name..". (Has max players been reached?)")
		return bot
	end
	
	-- Set follow target
	BotFollow(player, bot)

	-- Raise maxplayers
	if AutoMax.value
		local maxplayers = CV_FindVar("maxplayers")
		print('Maxplayers has been automatically adjusted to '..maxplayers.value+1)
		CV_AddValue(maxplayers, 1)
	end
	return bot
end

local CanAddBot = function(player, versus, ...)
	if not(G_AddPlayer)
		CONS_Printf(player, "This command isn't available! Are you using the correct version of SRB2?")
		return
	end
	if gamestate != GS_LEVEL
		CONS_Printf(player, 'You must be in a level to use this command')
		return
	end
	if (not versus and BotPermissions.value == 0 or versus and MPBotPermissions.value == 0)
	and player != server and not IsPlayerAdmin(player)
		CONS_Printf(player, 'Server has set this command to admin-only.')
		return
	end
	if gametyperules & GTR_RINGSLINGER and not versus
		CONS_Printf(player, "This gametype doesn't support co-op bots! (Use addmpbot instead)")
		return
	end
	local maxplayers = CV_FindVar('maxplayers').value
	local automax = AutoMax.value
	if automax and maxplayers == 32
		CONS_Printf(player, 'Cannot make more room for human players! (Playermax is at 32)')
		return
	end
	local bots = 0
	local all = 0
	for player in players.iterate do
		if player.bot
			bots = $+1
		end
		all = $+1
	end
	if bots >= MaxBots.value
		CONS_Printf(player, 'Cannot add bots right now! (Too many bots)')
		return
	end
	if not automax and all >= maxplayers
	or all == 32 -- Absolute limit
		CONS_Printf(player, 'The server is already completely full!')
		return
	end
	return true
end

COM_AddCommand("addbot", function(player, ...)
	if not CanAddBot(player, false, ...)
		return
	end
	-- Prompt
	if ... == nil
		CONS_Printf(player, 'addbot <skin> <color> <name>')
		return
	end
	AddBot(player, false, ...)
end)

COM_AddCommand("addmpbot", function(player, ...)
	if not CanAddBot(player, true, ...)
		return
	end
	-- Prompt
	if ... == nil
		CONS_Printf(player, 'addmpbot <skin> <color> <name>')
		return
	end
	AddBot(player, true, ...)
end)

local ResolvePlayerByNum = function(num)
	if type(num) != "number"
		num = tonumber(num)
	end
	if num != nil and num >= 0 and num < 32
		return players[num]
	end
	return nil
end

local GetPlayerNum = function(player)
	local n = 0
	for p in players.iterate do
		n = $+1
		if p == player
			return n
		end
	end
	return nil
end

local RemoveBot = function(player)
	if player.bot
		G_RemovePlayer(#player)
		return true
	end
	return false
end

local RemoveAllBots = function(admin, versus)
	local count = 0
	for player in players.iterate do
		if versus == false and player.bot == BOT_MPAI
			continue
		end
		if RemoveBot(player)
			count = $+1
		end
	end
	if count == 0
		CONS_Printf(admin, "There are no bots to kick.")
	end
	-- Reduce maxplayers
	if AutoMax.value
		local maxplayers = CV_FindVar("maxplayers")
		print('Maxplayers has been automatically adjusted to '..maxplayers.value-count)
		CV_AddValue(maxplayers, -count)
	end
end

COM_AddCommand("botleader", function(player, ...)
	if BotLeaderPermissions.value == 0 and player != server and not IsPlayerAdmin(player)
		CONS_Printf(player, 'Server has set "botleader" to admin-only.')
		return
	end
	local p1, p2 = ...
	if not(p1 and p2)
		CONS_Printf(player, "botleader <player node> <bot node>")
		return
	end
	p1 = tonumber($)
	p2 = tonumber($)
	local leader = players[p1]
	local bot = players[p2]
	local fail = false
	if not leader
		CONS_Printf(player, "No player with node "..tostring(p1))
		fail = true
	end
	if not bot
		CONS_Printf(player, "No bot with node "..tostring(p2))
		fail = true
	end
	if fail == true
		return
	end
	
	bot.botleader = leader	
	P_TeleportMove(bot.mo, leader.mo.x, leader.mo.y, leader.mo.z)
	bot.powers[pw_flashing] = TICRATE*2
	CONS_Printf(player, bot.name.." is following "..player.name)
end)

COM_AddCommand("kickbot", function(player, bot)
	if tonumber(bot) == nil
		CONS_Printf(player, "kickbot <bot node>")
		return
	end
	local pbot = players[tonumber(bot)]
	if not pbot
		CONS_Printf(player, "No bot with node "..bot)
		return
	end
	if (BotPermissions.value == 0 and pbot.bot != BOT_MPAI or MPBotPermissions.value == 0 and pbot.bot == BOT_MPAI)
	and player != server and not IsPlayerAdmin(player)
		CONS_Printf(player, 'Only an admin can remove this bot currently.')
		return
	end
	if not RemoveBot(pbot)
		CONS_Printf(player, pbot.name.." is not a bot!")
	else
		CONS_Printf(player, "Successfully kicked bot with node "..bot)
		-- Reduce maxplayers
		if AutoMax.value
			local maxplayers = CV_FindVar("maxplayers")
			print('Maxplayers has been automatically adjusted to '..maxplayers.value-1)
			CV_AddValue(maxplayers, -1)
		end
	end
end)

COM_AddCommand("kickbots", RemoveAllBots, COM_ADMIN)


COM_AddCommand("listbots", do
	for n = 0, 31 do
		local player = players[n]
		if not player or not player.bot
			continue
		end
		local str = "\x83".."#"..n.."\x80"..": "..player.name.." \x86"
		local str2 = player.bot == BOT_2PAI and "2P AI"
			or player.bot == BOT_2PHUMAN and "2P HUMAN"
			or player.bot == BOT_MPAI and "MP AI"
			or "? ("..player.bot..")"
		print(str..str2)
	end
end, COM_LOCAL)



addHook("MapChange", do
	if gametyperules & GTR_RINGSLINGER
		RemoveAllBots(server, false) -- Necessary due to a hardcode glitch
	end
end)

addHook("PlayerThink", function(player)
	if AutoJoinTeams.value and player.bot and player.spectator
		-- Force the bot into the game
		COM_BufInsertText(server, "serverchangeteam "..tostring(#player).." "..tostring((#player+leveltime)&1 + 1))
	end
end)

print('\x83 Bot commands')
print('botperms, mpbotperms, botleaderperms, botautomaxplayers, maxbots, botautojoin, addbot, addmpbot, botleader, kickbot, kickbots, listbots')