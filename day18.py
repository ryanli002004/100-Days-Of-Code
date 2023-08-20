print("Welcome to the number guessing game!")
secretnumber = 485937
counter = 0
while True:
    guess = int(input("please make your guess: "))
    counter += 1
    if guess == secretnumber:
        print("congrats you guessed the right number in", counter,"tries")
        break
    elif guess > secretnumber:
        print("the number you guessed was too big")
    elif guess < secretnumber and guess > 0:
        print("the number you guessed was too small")
    else:
        print("you suck you cant input a negative number you lose")
        exit()