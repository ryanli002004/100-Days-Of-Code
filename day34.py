import time
import os

list = []

def prettyprint():
    os.system("clear")
    counter = 0
    for loop in list:
        counter += 1
        if counter > 10:
            break
        print(f"""Dear {loop}
        you pooped your pants.
        love,
        ryan""")
        time.sleep(1)

def viewlist():
    for loop in list:
        print(loop)
        time.sleep(1)

while True:
    print("1 to add email, 2 to remove email, 3 to view emails, 4 to SPAM")
    ask = input("select 1, 2, 3, or 4: ")
    if ask == "1":
        email = input("please enter email you would like to add to list: ")
        if email not in list:
            list.append(email)
        else:
            print(f"{email} already in list")
    elif ask == "2":
        email = input("please enter email you would like to remove from the list: ")
        if email in list:
            list.remove(email)
        else:
            print(f"sorry {email} is not in the list")
    elif ask == "3":
        if list == []:
            print("the list is empty")
        else:
            viewlist()
    elif ask == "4":
        prettyprint()
    else:
        print("the options are only 1, 2, 3, or 4")
    print()
    time.sleep(1)