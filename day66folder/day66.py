#tkinter works on mac only if python is updated to the latest version
import tkinter as tk
window = tk.Tk()
window.title("calculator")
window.geometry("500x500")

answer = None
operator = None
oldnum = None

def updateanswer():
    global oldnum
    global operator
    global answer
    if answer == 0 and operator == "/":
        print("you cant divide by 0")
    else:
        answer =(eval(f"{oldnum}{operator}{answer}"))
    answerlabel["text"]=answer

def inputnum1():
    global answer
    if answer is None:
        answer=1
    else:
        answer = int(str(answer)+str(1))
    answerlabel["text"]=answer
def inputnum2():
    global answer
    if answer is None:
        answer =2
    else:
        answer = int(str(answer)+str(2))
    answerlabel["text"]=answer
def inputnum3():
    global answer
    if answer is None:
        answer = 3
    else:
        answer = int(str(answer)+str(3))
    answerlabel["text"]=answer
def inputnum4():
    global answer
    if answer is None:
        answer = 4
    else:
        answer = int(str(answer)+str(4))
    answerlabel["text"]=answer
def inputnum5():
    global answer
    if answer is None:
        answer =5
    else:
        answer = int(str(answer)+str(5))
    answerlabel["text"]=answer
def inputnum6():
    global answer
    if answer is None:
        answer =6
    else:
        answer = int(str(answer)+str(6))
    answerlabel["text"]=answer
def inputnum7():
    global answer
    if answer is None:
        answer =7
    else:
        answer = int(str(answer)+str(7))
    answerlabel["text"]=answer
def inputnum8():
    global answer
    if answer is None:
        answer =8
    else:
        answer = int(str(answer)+str(8))
    answerlabel["text"]=answer
def inputnum9():
    global answer
    if answer is None:
        answer = 9
    else:
        answer = int(str(answer)+str(9))
    answerlabel["text"]=answer
def inputnum0():
    global answer
    if answer is None:
        answer = 0
    else:
        answer = int(str(answer)+str(0))
    answerlabel["text"]=answer

def inputopeadd():
    global answer
    global oldnum
    global operator
    operator = "+"
    oldnum = answer
    answer = 0
    answerlabel["text"]=operator
def inputopesub():
    global answer
    global oldnum
    global operator
    operator = "-"
    oldnum = answer
    answer = 0
    answerlabel["text"]=operator
def inputopemul():
    global answer
    global oldnum
    global operator
    operator = "*"
    oldnum = answer
    answer = 0
    answerlabel["text"]=operator
def inputopediv():
    global answer
    global oldnum
    global operator
    operator = "/"
    oldnum = answer
    answer = 0
    answerlabel["text"]=operator


answerlabel = tk.Label(text = answer, height = 3, width = 15)
answerlabel.grid(row=0,column=1)

button1 = tk.Button(text = "1", command= inputnum1, height=5, width=10)
button1.grid(row=1,column=1)
button2 = tk.Button(text = "2", command= inputnum2, height=5, width=10)
button2.grid(row=1,column=2)
button3 = tk.Button(text = "3", command= inputnum3, height=5, width=10)
button3.grid(row=1,column=3)
button4 = tk.Button(text = "4", command= inputnum4, height=5, width=10)
button4.grid(row=2,column=1)
button5 = tk.Button(text = "5", command= inputnum5, height=5, width=10)
button5.grid(row=2,column=2)
button6 = tk.Button(text = "6", command= inputnum6, height=5, width=10)
button6.grid(row=2,column=3)
button7 = tk.Button(text = "7", command= inputnum7, height=5, width=10)
button7.grid(row=3,column=1)
button8 = tk.Button(text = "8", command= inputnum8, height=5, width=10)
button8.grid(row=3,column=2)
button9 = tk.Button(text = "9", command= inputnum9, height=5, width=10)
button9.grid(row=3,column=3)
button0 = tk.Button(text = "0", command= inputnum0, height=5, width=10)
button0.grid(row=4,column=2)
buttonadd = tk.Button(text = "+", command= inputopeadd, height=5, width=10)
buttonadd.grid(row=1,column=4)
buttonsub = tk.Button(text = "-", command= inputopesub, height=5, width=10)
buttonsub.grid(row=2,column=4)
buttonmul = tk.Button(text = "*", command= inputopemul, height=5, width=10)
buttonmul.grid(row=3,column=4)
buttondiv = tk.Button(text = "/", command= inputopediv, height=5, width=10)
buttondiv.grid(row=4,column=3)
buttoneql = tk.Button(text = "=", command= updateanswer, height=5, width=10)
buttoneql.grid(row=4,column=1)

tk.mainloop()