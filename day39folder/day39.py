import random
import time

print("welcome to hangman")

list = ["daniella", "robot", "richard", "david", "geroge", "ryan", "tamari", "alison", "sophie", "daniel"]
word = random.choice(list)
counter = 6
tried = []

while True:
    win = True
    time.sleep(1)
    print()
    ask = input("what letter would you like to choose? ")
    if ask in word:
        print("that is correct")
    else:
        print("that is wrong")
        counter -= 1
    if ask in tried:
        print(f"you already tried {ask}")
    else:
        tried.append(ask)
    for i in word:
        if i in tried:
            print(i, end="")
        else:
            print("_", end="")
            win = False
    print()
    print(f"you have {counter} lives left")
    if counter == 0:
        print(f"sorry you lose, the word was {word}")
        exit()
    if win:
        print(f"you win! with {counter} lives left")
        exit()