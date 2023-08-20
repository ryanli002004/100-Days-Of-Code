import random
def healthgen ():
    h1 = random.randint(1,6)
    h2 = random.randint(1,8)
    hp = h1 * h2
    return hp
while True:
    name = input("what do you want to name your character? ")
    health = healthgen()
    print("your character has", health, "hp")
    q = input("another? ")
    if q != "yes":
        break