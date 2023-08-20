list = []

def printlist():
    print()
    for items in list:
        print(items)
    print()

while True:
    print("what would you like to do?(add, remove, or view?)")
    ask = input("")
    if ask == "add":
        choice = input("what would you like to add? ")
        list.append(choice)
        printlist()
    elif ask == "remove":
        choice = input("what would you like to remove? ")
        if choice in list:
            list.remove(choice)
            printlist()
        else:
            print(f"'{choice}' is not in list")
    elif ask == "view":
        printlist()
    else:
        print("options are only 'remove','add' or 'view'")