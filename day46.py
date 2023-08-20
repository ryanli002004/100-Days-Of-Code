import time
print("MOKEDEX")
mokedex = {}

def prettyprint():
    print()
    for loop in mokedex.keys():
        print(f"name: {loop} | element: {mokedex[loop]['element']} | special move: {mokedex[loop]['specialmove']} | HP: {mokedex[loop]['hp']} | MP: {mokedex[loop]['mp']}")
        time.sleep(1)
    print()
  
while True:
    name = input("input the beast name: ")
    element = input("input the beast element: ")
    specialmove = input("input the beast special move: ")
    hp = input("input the beast starting HP: ")
    mp = input("input the beast starting MP: ")
    mokedex[name] = {"element":element, "specialmove":specialmove, "hp":hp, "mp":mp}
    again = input("again? y/n > ")
    if again == "y":
        continue
    elif again == "n":
        prettyprint()
        break
