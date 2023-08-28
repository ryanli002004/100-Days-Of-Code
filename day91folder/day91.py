import sqlite3
import requests
import os

connection = sqlite3.connect(os.path.join('day91folder','day91.db'))
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS jokes(joke TEXT)")
connection.commit()

previous = None

def newjoke():
    global previous
    results = requests.get("https://icanhazdadjoke.com/",headers={"Accept":"application/json"})
    joke = results.json()
    print(joke['joke'])
    previous = joke['joke']

def savejoke():
    global previous
    cursor.execute("INSERT INTO jokes VALUES(?)",(previous,))
    connection.commit()
    print("joke saved!")

def viewjokes():
    cursor.execute('SELECT * FROM jokes')
    rows = cursor.fetchall()
    for loop in rows:
        print(loop[0])

while True:
    ask = input("1: new joke, 2: save joke, 3: view saved jokes > ")
    if ask == "1":
        newjoke()
    if ask == "2":
        savejoke()
    if ask== "3":
        viewjokes()
