import os
lst = []
f = open(os.path.join("day51folder","day51.todolist"), "r")
try:
    lst = eval(f.read())
except SyntaxError:
    lst = []
f.close()

while True:
    print("select 1 to add an item, 2 to remove an item, 3 to view list of items, 4 to change an item, or 5 to empty the list")
    choice = input("")
    if choice == "1":
        item = input("what item would you like to add? ")
        if item not in lst:
            lst.append(item)
        else:
            print(f"sorry {item} is already in the list")
    elif choice == "2":
        item = input("what item would you like to remove? ")
        if item in lst:
            lst.remove(item)
        else:
            print(f"{item} is not in the list")
    elif choice == "3":
        if lst == []:
            print("there is no items in the list")
        else:
            for item in lst:
                print(item)
    elif choice == "4":
        item = input("what item would you like to change? ")
        if item not in lst:
            print(f"sorry {item} is not in the list")
        else:
            index = lst.index(item)
            chng = input(f"what would you like to change {item} to? ")
            if chng in lst:
                print(f"sorry {chng} is already in list")
            else:
                lst[index] = chng
    elif choice == "5":
        lst.clear()
    else:
        print("sorry choices are only 1, 2, 3, or 4")
    
    f = open(os.path.join("day51folder","day51.todolist"), "w")
    f.write(str(lst))
    f.close()