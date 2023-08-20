import random
list = ["hola","hi","bonjour"]
while True:
    counter = random.randint(1,3)
    if counter == 1:
        print(f"{list[0]}")
    elif counter == 2:
        print(f"{list[1]}")
    else:
        print(f"{list[2]}")
    ask = input("again? ")
    if ask == "yes":
        continue
    else:
        break