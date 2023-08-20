exit = ""
while exit != "yes":
    sound = input("What animal sound do you want to hear?")
  
    if sound == "cow":
        print(" Moo")
    elif sound == "pig":
        print (" Oink")
    elif sound == "sheep":
        print (" Baaa")
    elif sound == "duck":
        print(" Quack")
    elif sound == "dog":
        print(" Woof")
    elif sound == "cat":
        print(" Meow")
    else: 
        print("sorry i dont know that animal")
    exit = input("exit? ")