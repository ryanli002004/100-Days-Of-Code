import sqlite3 
import hashlib
import os
import datetime
import random

connection = sqlite3.connect('day72.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS login( username TEXT, password TEXT, salt TEXT)")
connection.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS entries(entrynum INT, username TEXT, time TEXT, entry TEXT)")
connection.commit()

def userlogin():
    cursor.execute("SELECT COUNT(*) FROM login")
    counter = cursor.fetchone()[0]
    if counter == 0:
        print("there are no created users")
    else:
        loginusername = input("what is your username? ")
        loginpassword = input("what is your password? ")
        cursor.execute("SELECT * FROM login WHERE username = ?",(loginusername,))
        checkuser = cursor.fetchone()
        if checkuser == None:
            print("sorry username not recgonized")
        else:
            salt = checkuser[2]
            checkpassword = hashlib.pbkdf2_hmac("sha256", loginpassword.encode('utf-8'), bytes(salt), 100000)
            if checkuser[1] == checkpassword.hex():
                while True:
                    choice =  input("1: add to diary, 2: view diary entries, 3: exit: ")
                    if choice == "3":
                        break
                    elif choice == "1":
                        counter = 1
                        currenttime = str(datetime.datetime.now())
                        cursor.execute("SELECT COUNT(*) FROM entries WHERE username = ?",(loginusername,))
                        count = cursor.fetchone()[0]
                        counter += count
                        entry = input("write your entry> ")
                        cursor.execute("INSERT INTO entries VALUES(?,?,?,?)",(counter,loginusername,currenttime,entry))
                        connection.commit()
                    elif choice == "2":
                        cursor.execute("SELECT COUNT(*) FROM entries WHERE username = ?",(loginusername,))
                        counter = cursor.fetchone()[0]
                        if counter == 0:
                            print("you have no entries")
                        else:
                            cursor.execute("SELECT * FROM entries WHERE username = ?",(loginusername,))
                            rows = cursor.fetchall()
                            print("Your Entries:")
                            for loop in rows:
                                print()
                                print(f"""
        Entry{loop[0]} 
        Time:{loop[2]}
        Entry:{loop[3]}
                                    """)
                                print()
            else:
                print("sorry wrong password")


def createuser():
    salt = os.urandom(16)
    while True:
        cursor.execute("SELECT username FROM login")
        checkusername = [i[0] for i in cursor.fetchall()]
        askusername = input("what would you like your username to be? ")
        if askusername in checkusername:
            print("please pick a different username")
        else:
            break
    askpassword = input("what would you like your password to be? ")
    password = hashlib.pbkdf2_hmac("sha256", askpassword.encode('utf-8'), bytes(salt), 100000)
    password = password.hex()
    cursor.execute("INSERT INTO login VALUES( ?, ?, ?)", ( askusername,password,salt))
    connection.commit()

while True:
    loginorcreate = input("enter 1 to login, enter 2 to create new user, or 3 to exit>  ")
    if loginorcreate == "1":
        userlogin()
    elif loginorcreate == "2":
        createuser()
    elif loginorcreate == "3":
        break
    else:
        print("options are only 1,2 or 3")
