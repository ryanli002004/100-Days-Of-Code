text = input("type a sentence you want to rainbowfy: ")
for letter in text:
    if letter.lower() == "r":
        print("\033[0;31m", end='')
    elif letter.lower() == "b":
        print("\033[0;34m", end="")
    elif letter.lower() == "g":
        print("\033[0;32m", end="")
    elif letter.lower() == "y":
        print("\033[1;33m", end="")
    elif letter == " ":
        print("\033[1;0m", end="")
    print(letter, end = "")
