import random
player1=0
player2=0
f=int(input("how many time to play  :"))
for i in range(f):
    print(str(input("player1 your turn  : press enter")))
    d=str(random.randint(1,6))
    print(d)
    player1=player1+int(d)
    print(str(input("player2 your turn  : press enter")))
    e=str(random.randint(1,6))
    print(e)
    player2=player2+int(e)
print("player1 total:" + str(player1))
print("player2 total:" + str(player2))
if player1>player2:
    print("player1 is winner")
else:
    print("player2 is winner")