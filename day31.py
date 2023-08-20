def changecolor(color):
    if color == "red":
        id = "\033[31m"
        return id
    elif color == "green":
        id = "\033[32m"
        return id
    elif color == "pink":
        id = "\033[35m"
        return id
    elif color == "yellow":
        id = "\033[33m"
        return id
    elif color == "blue":
        id = "\033[34m"
        return id
    elif color == "white":
        id = "\033[0m"
        return id

first = f"{changecolor('red')}={changecolor('white')}={changecolor('blue')}={changecolor('yellow')} Music App {changecolor('blue')}={changecolor('white')}={changecolor('red')}="
print(f"                           {first}")
print()
second = f"""{changecolor('white')}🔥▶️  Radio Gaga{changecolor('yellow')}    
     Queen"""
print(second)
print()
prev = f"{changecolor('white')}PREV"
next = f"{changecolor('green')}NEXT"
pause = f"{changecolor('pink')}PAUSE"
print(f"{prev}")
print(f"{next:>15}")
print(f"{pause:>22}")
welt = f"{changecolor('white')}WELCOME TO"
print(f"{welt:>45}")
armb = f"{changecolor('blue')}--   ARMBOOK   --"
print(f"{armb:>50}")
a = f"{changecolor('yellow')}Definitely not a rip off of"
b = "a certain other social"
c = "networking site."
print(f"{a:>76}")
print(f"{b:>71}")
print(f"{c:>71}")
print()
ho = f"{changecolor('red')}Honest."
print(f"{ho:>45}")
print()
use = f"{changecolor('white')}Username:"
pas = "Password:"
print(f"{use:>45}")
print(f"{pas:>41}")