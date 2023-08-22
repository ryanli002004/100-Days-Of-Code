import random
import time
print("top trumps")
dic = {
  "1":{"1":80,"2":50,"3":100,"4":100},
  "2":{"1":100,"2":100,"3":25,"4":50},
  "3":{"1":60,"2":60,"3":89,"4":70}
}

while True:
    choose = input("choose your character (1:ryan, 2:daniella, 3:roger) > ")
    comp = str(random.randint(1,3))
    while comp == choose:
        comp = str(random.randint(1,3))
    choose2 = input("pick your stat (1:fire, 2:water, 3:rock, 4:air) > ")
    if choose == "1":
        player = "ryan"
    elif choose == "2":
        player = "daniella"
    elif choose == "3":
        player = "roger"
    if comp == "1":
        compu = "ryan"
    elif comp == "2":
        compu = "daniella"
    elif comp == "3":
        compu = "roger"
    if choose2 == "1":
        stat = "fire"
    if choose2 == "2":
        stat = "water"
    if choose2 == "3":
        stat = "rock"
    if choose2 == "4":
        stat = "air"
    print(f"you chose {player}")
    time.sleep(1)
    print(f"computer chooses {compu}")
    time.sleep(1)
    print(f"we are comparing {stat} stats!")
    time.sleep(1)
    print(f"{player} has a {stat} stat of {dic[choose][choose2]}")
    time.sleep(1)
    print(f"{compu} has a {stat} stat of {dic[comp][choose2]}")
    time.sleep(1)
    if dic[choose][choose2] > dic[comp][choose2]:
        print(f"congats {player}, you win!")
    elif dic[choose][choose2] < dic[comp][choose2]:
        print(f"congats {compu}, you win!")
    time.sleep(1)
    again = input("again? ")
    if again == "yes":
        continue
    else:
        break