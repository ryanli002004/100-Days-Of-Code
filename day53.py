import os
lst = []

f= open(os.path.join("day53folder","day53.inventory"), "r")
try:
    lst = eval(f.read())
except SyntaxError:
    lst = []
f.close()

while True:
    ask = input("1:add to inventory, 2:remove from inventory, 3: view inventory > ")
    if ask == '1' :
        additem = input("what item would you like to add? ")
        lst.append(additem)
    elif ask == "2":
        remove = input("what item would you like to remove from inventory?")
        if remove not in lst:
            print("you dont have that item in your inventory")
        else:
            counter = 0
            for item in lst:
                if item == remove:
                    counter += 1
            if counter >= 1:
                howmany = int(input(f"you have {counter} of those items how many would you like to remove? "))
                counter1 = 0
                for item in lst:
                    if item == remove:
                        lst.remove(item)
                        counter1 += 1
                        if howmany == counter1:
                            break
    elif ask == "3":
        count = {}
        print("your inventory:")
        for item in lst:
            if item not in count.keys():
                count[item] = 1
            elif item in count.keys():
                count[item] += 1
        for item,num in count.items():
            if num > 1:
                print(f"{item}({num})")
            else:
                print(f"{item}")

    f = open("day53folder/day53.inventory","w")
    f.write(str(lst))
    f.close()