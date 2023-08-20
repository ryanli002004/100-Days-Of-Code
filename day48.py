f = open("day48.list", "a+" )
while True:
    ask = input("add new? y/n >")
    if ask == "y":
        initials = input("initials > ")
        score = input("score > ")
        f.write(f"{initials} {score}\n")
    elif ask == "n":
        f.close()
        break