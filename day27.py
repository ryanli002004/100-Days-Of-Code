import random
import time

print("character creation")
time.sleep(1)

def hpgen():
    hp1 = random.randint(1,6)
    hp2 = random.randint(1,12)
    hp = (hp1 + hp2)/2 + 10
    return hp
  
def strgen():
    str1 = random.randint(1,6)
    str2 = random.randint(1,12)
    str = (str1 + str2)/2 +10
    return str

while True:
    name = input("what will your character's name be? ")
    time.sleep(1)
    type = input("what type of character will it be? ")
    hp = hpgen()
    str = strgen()
    print(name, "the", type)
    time.sleep(1)
    print("Health:", hp)
    time.sleep(1)
    print("Strength:", str)
    time.sleep(1)
    choice = input("make another character? ")
    if choice == "yes":
        continue
    else:
        exit()
  