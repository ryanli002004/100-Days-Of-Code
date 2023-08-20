import tkinter as tk
window = tk.Tk()
window.title("story")
window.geometry("500x500")

imagefight = tk.PhotoImage(file = "day69fight.png")
imageman = tk.PhotoImage(file = "day69man.png")
imagerun = tk.PhotoImage(file = "day69run.png")
imageyoudied = tk.PhotoImage(file = "day69youdied.png")
imageyouwin = tk.PhotoImage(file = "day69youwin.png")

def yourun():
    canvas.itemconfig(container , image = imagerun)
    runbutton.pack_forget()
    fightbutton.pack_forget()
    canvas.pack_forget()
    manappear.pack_forget()
    run.pack()
    doorbutton.pack()
    hallwaybutton.pack()
    canvas.pack()


def youhallway():
    canvas.itemconfig(container , image = imageyoudied)
    run.pack_forget()
    doorbutton.pack_forget()
    hallwaybutton.pack_forget()
    canvas.pack_forget()
    hallway.pack()
    restartbutton.pack()
    canvas.pack()

def youdoor():
    canvas.itemconfig(container , image = imageyoudied)
    run.pack_forget()
    doorbutton.pack_forget()
    hallwaybutton.pack_forget()
    canvas.pack_forget()
    door.pack()
    restartbutton.pack()
    canvas.pack()

def youfight():
    canvas.itemconfig(container , image = imagefight)
    runbutton.pack_forget()
    fightbutton.pack_forget()
    canvas.pack_forget()
    manappear.pack_forget()
    fight.pack()
    blockbutton.pack()
    dodgebutton.pack()
    canvas.pack()

def youblock():
    canvas.itemconfig(container , image = imageyoudied)
    fight.pack_forget()
    blockbutton.pack_forget()
    dodgebutton.pack_forget()
    canvas.pack_forget()
    block.pack()
    restartbutton.pack()
    canvas.pack()

def youdodge():
    canvas.itemconfig(container , image = imageyouwin)
    fight.pack_forget()
    blockbutton.pack_forget()
    dodgebutton.pack_forget()
    canvas.pack_forget()
    dodge.pack()
    restartbutton.pack()
    canvas.pack()

def restartgame():
    canvas.itemconfig(container , image = imageman)
    restartbutton.pack_forget()
    canvas.pack_forget()
    door.pack_forget()
    hallway.pack_forget()
    dodge.pack_forget()
    block.pack_forget()
    manappear.pack()
    runbutton.pack()
    fightbutton.pack()
    canvas.pack()


manappear = tk.Label(text="a man has appeared!!! what do you do?")
manappear.pack()
run = tk.Label(text="you decided to run, do you run towards the door or down a hallway?")
hallway = tk.Label(text="you choose to run down a hallway but the man was faster and you died!")
door = tk.Label(text = "you choose to run towards a door, but you tripped and fell and died!")
fight = tk.Label(text="you decided to fight and he throws a kick what do you do?")
block = tk.Label(text="you decided to block, but his kick was too strong and it still knocked you out!, and you died!")
dodge = tk.Label(text="you decided to dodge and counter with a punch! the man has died and you win!")

runbutton = tk.Button(command = yourun, text="run")
runbutton.pack()
hallwaybutton = tk.Button(command = youhallway, text ="hallway")
doorbutton = tk.Button(command = youdoor, text ="door")
fightbutton = tk.Button(command = youfight, text ="fight")
fightbutton.pack()
blockbutton = tk.Button(command = youblock, text ="block")
dodgebutton = tk.Button(command = youdodge, text ="dodge")
restartbutton = tk.Button(command = restartgame, text="restart")

canvas = tk.Canvas(window, height = 300, width = 300)
canvas.pack()
container = canvas.create_image(130,100,  image = imageman)




tk.mainloop()