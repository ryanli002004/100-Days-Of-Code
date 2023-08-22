list = []

while True:
    print("select 1 to add an item, 2 to remove an item, 3 to view list of items, 4 to change an item, or 5 to empty the list")
    choice = input("")
    if choice == "1":
        item = input("what item would you like to add? ")
        if item not in list:
            list.append(item)
        else:
            print(f"sorry {item} is already in the list")
    elif choice == "2":
        item = input("what item would you like to remove? ")
        if item in list:
            list.remove(item)
        else:
            print(f"{item} is not in the list")
    elif choice == "3":
        if list == []:
            print("there is no items in the list")
        else:
            for item in list:
                print(item)
    elif choice == "4":
        item = input("what item would you like to change? ")
        if item not in list:
            print(f"sorry {item} is not in the list")
        else:
            index = list.index(item)
            chng = input(f"what would you like to change {item} to? ")
            if chng in list:
                print(f"sorry {chng} is already in list")
            else:
                list[index] = chng
    elif choice == "5":
        list.clear()
    else:
        print("sorry choices are only 1, 2, 3, or 4")