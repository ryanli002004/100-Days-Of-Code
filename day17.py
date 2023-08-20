from getpass import getpass as input
player1wins = 0
player2wins = 0
while True:
    print("select R, P or S")
    player1 = input("Player 1: ")
    player2 = input("Player 2: ")
    if player1=="R" and player2=="R":
        print("draw")
    if player1=="R" and player2=="P":
        print("player 2 wins")
        player2wins += 1
    if player1=="R" and player2=="S":
        print("player 1 wins")
        player1wins += 1
    if player1=="P" and player2=="R":
        print("player 1 wins")
        player1wins += 1
    if player1=="P" and player2=="P":
        print("draw")
    if player1=="P" and player2=="S":
        print("player 2 wins")
        player2wins +=1
    if player1=="S" and player2=="R":
        print("player 2 wins")
        player2wins +=1
    if player1=="S" and player2=="P":
        print("player 1 wins")
        player1wins +=1
    if player1=="S" and player2=="S":
        print("draw")
    if player1wins == 3:
        print("player 1 wins with 3 wins!")
        break
    if player2wins == 3:
        print("player 2 wins with 3 wins!")
        break