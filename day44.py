import random
import time

def randomgen():
    num = random.randint(1, 90)
    return num

num1 = randomgen()
num2 = randomgen()
num3 = randomgen()
num4 = randomgen()
num5 = randomgen()
num6 = randomgen()
num7 = randomgen()
num8 = randomgen()

list1 = [
    [num1, num2, num3],
    [num4, "bingo", num5],
    [num6, num7, num8]
]

tried = []

while True:
    time.sleep(0.05)
  
    ran = randomgen()
    if ran not in tried:
        tried.append(ran)
    elif ran in tried:
        continue
    
    counter = 0
  
    for loop in range(len(list1)):
        for i in range(len(list1[loop])):
            if list1[loop][i] in tried:
                list1[loop][i] = "x"

    for loop in list1:
        for i in loop:
            if i == "x":
                counter += 1

    print()
    print(tried)
    print()
    for loop in list1:
        print()
        print("--------------")
        for i in loop:
            print(f"{i:^2}", end=" | ")

    if counter == 8:
        print("you win!")
        exit()