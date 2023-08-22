moke = {"name":None,"type":None,"specialmove":None,"HP":None,"MP":None}
for keys in moke.keys():
    ask = input(f"please enter {keys}: ").lower()
    moke[keys] = ask

if moke["type"] == "earth":
    print("\033[0;32m", end="")
elif moke["type"] == "fire":
    print("\033[0;31m", end="")
elif moke["type"] == "water":
    print("\033[0;34m", end="")
elif moke["type"] == "spirit":
    print("\033[0;33m", end="")
elif moke["type"] == "air":
    print("\033[0;0m", end="")

print(f"your beast is called {moke['name']}, it is the type {moke['type']}, it's special move is {moke['specialmove']}, {moke['name']} has {moke['HP']} hp and {moke['MP']} mp")