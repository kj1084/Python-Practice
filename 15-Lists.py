players=["Jemimah","Sneh","Laura","Healy","Harleen","Sophie","Metthews","Fatima"]
print(players)
print(players[1])
print(players[4])
players.append("Shreyanka")
print(players)
players.insert(2,"Pratika")
print(players)
players.remove("Fatima")
print(players)
players.pop()
print(players)
for player in players:
    print(player)
len(players)
print("Total number of players in the list is",len(players))
if "Harleen" in players:
    print("Harleen is in the list")
else:    print("Harleen is not in the list.")