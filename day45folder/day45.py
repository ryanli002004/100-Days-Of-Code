print("To Do list")
dic1 = {}

while True:
    print("1: Add, 2: view, 3: Remove, 4: Edit ")
    choice1 = input("what would you like to do? ")

    if choice1 == "1":
        ask1 = input("what is it? ")
        if ask1 in dic1.keys():
            print("you already have that on your list")
            continue
        else:
            ask2 = input("when is it due? ")
            ask3 = input("how important? (high, med, or low)? ")
            dic1[ask1] = {"due": ask2, "importance": ask3}
    
    elif choice1 == "2":
        print("1: View All, 2: View Priority")
        choice2 = input("what would you like to do? ")
        if len(dic1) == 0:
            print("your list is empty")
        else:
            if choice2 == "1":
                for keys in dic1.keys():
                    print(f"{keys}, due:{dic1[keys]['due']}, importance:{dic1[keys]['importance']}")
            elif choice2 == "2":
                for keys in dic1.keys():
                    if dic1[keys]["importance"] != "low":
                        print(f"{keys}, due:{dic1[keys]['due']}, importance:{dic1[keys]['importance']}")
    
    elif choice1 == "3":
        ask4 = input("what would you like to remove? ")
        if ask4 in dic1.keys():
            del dic1[ask4]
        else:
            print("that item isn't in your list")
    
    elif choice1 == "4":
        ask5 = input("what would you like to edit? ")
        if ask5 in dic1.keys():
            print("1: Change What it is, 2: Change when it is due, 3: Change how important")
            choice3 = input("what would you like to do? ")
            if choice3 == "1":
                ask6 = input("what would you like to change it to? ")
                if ask6 in dic1.keys():
                    print("sorry, that item is already in your list")
                else:
                    dic1[ask6] = dic1.pop(ask5)
            elif choice3 == "2":
                ask7 = input("when do you want to change the due time to? ")
                dic1[ask5]["due"] = ask7
            elif choice3 == "3":
                ask8 = input("what importance level do you want to change it to? ")
                dic1[ask5]["importance"] = ask8
        else:
            print("that item isn't in your list")