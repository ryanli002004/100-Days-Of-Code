counter = 1
while True:
    lyrics = input("happy birthday to ___")
    if lyrics == "you":
        print("You got it!")
        break
    else:
        print("wrong try again")
        counter +=1
print("Thanks for playing!")
print("you guessed the right lyric in", counter, "tries(s)!")