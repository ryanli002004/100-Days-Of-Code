import random
import os

counter = 0
def addidea():
    global counter
    counter += 1
    f = open(os.path.join("day50folder","day50.myideas"),"a+")
    f.close()
    f = open(os.path.join("day50folder","day50.myideas"),"r")
    contents = f.read().split("\n")
    f.close()
    f = open(os.path.join("day50folder","day50.myideas"),"a+")
    idea = input("what is your idea? ")
    string = f"idea {counter}: {idea}\n"
    f.write(string)
    f.close()

def viewidea():
    f = open(os.path.join("day50folder","day50.myideas"),"r")
    contents = f.read().split("\n")
    contents.pop()
    if contents == []:
        print("list is empty")
    else:
        i = random.choice(contents)
        print(i)

while True:
    ask = input("1:add idea, 2:view random idea, 3:exit > ")
    if ask == "1":
        addidea()
    elif ask == "2":
        viewidea()
    else:
        break