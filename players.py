players = ["charles", "martina", "michael", "florence", "eli"]
#print(players[1:4]) #hämtar från position 1(2 alltså) till och men inte med 4(stannar på den tredje alltså)
#print(players[:4]) #utan första siffra går den till angivet nummer från början
#print(players[2:]) #utan sista siffra börjar den från angivet nummer och går till listans slut
#print(players[-3:]) #skriver de tre sista i listan
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())