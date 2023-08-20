text = input("what would you like printed? ")
color = input("what color would you like the text? ")
def colorprint(color, text):
    if color == "red":
        print("\033[0;31m", text, sep="")
    elif color == "blue":
        print("\033[0;34m", text, sep="")
    else:
        print("sorry we dont support that color")
colorprint(color, text)