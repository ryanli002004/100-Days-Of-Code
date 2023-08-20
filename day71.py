#used sqlite3 instead of replit's DB 

import sqlite3
import hashlib
import random

connection = sqlite3.connect("day71hashsaltpasswords.db")
cursor = connection.cursor()

#cursor.execute("CREATE TABLE logininfo (username TEXT, password TEXT, salt TEXT)")

while True:

    options = input("enter 1 if you want to add a new user, enter 2 if you want to login, or 3 to exit: ")

    if options == "1":
        while True:
            salt = random.randint(1000,9999) #better to use salt = os.urandom(16)
            username = input("what is your name: ")
            userpassword = input("what is your password: ")
            hashedpassword = hashlib.pbkdf2_hmac("sha256", userpassword.encode('utf-8'), bytes(salt), 100000)
            hashedpassword = hashedpassword.hex()
            cursor.execute("SELECT username FROM logininfo")
            knownusernames = cursor.fetchall()
            if username in knownusernames:
                print("sorry that username already exists please choose another")
            else:
                cursor.execute("INSERT INTO logininfo VALUES(?,?,?)",(username,hashedpassword,salt))
                connection.commit()
                break
    elif options =="2":
        while True:
            askusername = input("what is your name: ")
            cursor.execute("SELECT * FROM logininfo WHERE username = ?",(askusername,))
            getinfo = cursor.fetchall()
            if getinfo == []:
                print("sorry username not found")
                break
            else:
                askpassword = input("what is your password: ")
                hashedpassword = hashlib.pbkdf2_hmac("sha256", askpassword.encode('utf-8'), bytes(int(getinfo[0][2])), 100000)
                hashedpassword = hashedpassword.hex()
                if getinfo[0][1] == hashedpassword:
                    print(f"welcome, {askusername}")
                    break
                else:
                    print("wrong password")
                    break
    elif options == "3":
        print("goodbye")
        connection.close()
        exit()
    else:
        print("please choose either '1', '2', or '3'")