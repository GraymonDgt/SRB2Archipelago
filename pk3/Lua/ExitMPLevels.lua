


addHook("ThinkFrame", function()
if gamemap > 531 then
local totalrings = 0
local exitlevel = false
for player in players.iterate() do
totalrings = $ + player.rings
end

if gamemap == 543 or gamemap == 547 then
if totalrings >= 150 then
exitlevel = true end
end

if gamemap == 536 or gamemap == 537 or gamemap == 568 then
if totalrings >= 200 then
exitlevel = true end
end

if gamemap == 532 or gamemap == 533 or gamemap == 538 or gamemap == 535 or gamemap == 545 or gamemap == 569 or gamemap == 542 then
if totalrings >= 250 then
exitlevel = true end
end

if gamemap == 534 or gamemap == 540 or gamemap == 541 or gamemap == 544 or gamemap == 549 or gamemap == 570 then
if totalrings >= 300 then
exitlevel = true end
end

if gamemap == 539 or gamemap == 546 or gamemap == 548 then
if totalrings >= 500 then
exitlevel = true end
end

if exitlevel == true then

		for player in players.iterate() do
		if player.bot == BOT_NONE then
		player.rings = totalrings
		P_DoPlayerFinish(player)
		end
		end
		
	end
end

end)
