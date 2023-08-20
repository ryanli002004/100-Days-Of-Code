print("pizza orders!")

allorders = {}

f = open("day52.pizzaorders","r")
try:
    allorders = eval(f.read())
except SyntaxError:
  allorders = {}
f.close()

while True:
    makeorder = input("would you like to place an order? ").strip().lower()
    if makeorder == "yes":
        name = input("please enter your name: ").lower().strip()
        quantity = 0
        size = None
        total = 0
        while True:
            try:
                quantity = int(input("how many pizzas would you like? "))
                break
            except ValueError:
                print("please enter a whole number!")
        while True:
            size = input(f"what size would your pizzas to be? (small($10), medium($15), or large($20))").lower().strip()
            if size in ["small", "medium", "large"]:
                break
            else:
                print("please enter only 'small', 'medium', or 'large'!")
        if size == "small":
            total = 10 * quantity
        elif size == "medium":
            total = 15 * quantity
        else:
            total = 20 * quantity
        allorders[name] = {"quantity":quantity, "size":size, "total":total}
        for keys in allorders.keys():
            print(f"{keys} bought {quantity} pizzas in size {size} and their total comes out to {total}")
    elif makeorder == "no": 
        break
    else:
        print("please enter only 'yes' or 'no'!")
    f = open("day52.pizzaorders","w")
    f.write(str(allorders))
    f.close()