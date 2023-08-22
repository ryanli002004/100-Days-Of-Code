import random
sides = int(input("how many sides? "))
def dice(sides):
    while True:
        roll = random.randint(1,sides)
        print("you rolled", roll)
        con = input("do you want to continue? ")
        if con != "yes":
            break
dice(sides)