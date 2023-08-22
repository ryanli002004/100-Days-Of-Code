import random
import time
import os

print("character creation")
time.sleep(1)

def hpgen():
    hp1 = random.randint(1, 6)
    hp2 = random.randint(1, 12)
    hp = (hp1 + hp2) / 2 + 10
    return hp

def strgen():
    str1 = random.randint(1, 6)
    str2 = random.randint(1, 12)
    str_val = (str1 + str2) / 2 + 10
    return str_val

name1 = input("what will your character's name be? ")
time.sleep(1)
type1 = input("what type of character will it be? ")
hp1 = hpgen()
str1 = strgen()
print(name1, "the", type1)
time.sleep(1)
print("Health:", hp1)
time.sleep(1)
print("Strength:", str1)
time.sleep(1)
print("lets make a second character")
name2 = input("what will your second character's name be? ")
time.sleep(1)
type2 = input("what type of character will it be? ")
hp2 = hpgen()
str2 = strgen()
print(name2, "the", type2)
time.sleep(1)
print("Health:", hp2)
time.sleep(1)
print("Strength:", str2)
time.sleep(1)
print("let the fight begin!")
time.sleep(3)
os.system("clear")

if str1 > str2:
    difference = (str1 - str2) + 1
elif str2 > str1:
    difference = (str2 - str1) + 1
else:
    difference = 1

counter = 0
while True:
    counter += 1
    c1 = random.randint(1, 6)
    c2 = random.randint(1, 6)
    if c1 > c2:
        hp2 -= difference
        print(name1,"the",type1,"rolled higher and attacked! dealing:",difference,"damage",name2,"the",type2,"has",hp2,"health left")
        time.sleep(2)
        if hp2 <= 0:
            print(name1, "the", type1, "has won the battle in", counter, "rounds!")
            break
        else:
            print("both players are still alive and the battle continues!")
            time.sleep(2)
            os.system("clear")
            continue
    elif c2 > c1:
        hp1 -= difference
        print(name2,"the",type2,"rolled higher and attacked! dealing:",difference,"damage",name1,"the",type1,"has",hp1,"health left")
        time.sleep(2)
        if hp1 <= 0:
            print(name2, "the", type2, "has won the battle in", counter, "rounds!")
            break
        else:
            print("both players are still alive and the battle continues!")
            time.sleep(2)
            os.system("clear")
    else:
        continue