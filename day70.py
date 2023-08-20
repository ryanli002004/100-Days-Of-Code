#used sqlite3 instead of replit's DB 
import sqlite3
import os

connection = sqlite3.connect(os.path.join("day70folder","day70plaintextpasswords.db"))
cursor = connection.cursor()

#cursor.execute("CREATE TABLE logininfo (username TEXT, password TEXT)")

while True:

    options = input("enter 1 if you want to add a new user, enter 2 if you want to login, or 3 to exit: ")

    if options == "1":
        while True:
            username = input("what is your name: ")
            userpassword = input("what is your password: ")
            cursor.execute("SELECT username FROM logininfo")
            knownusernames = cursor.fetchall()
            if username in knownusernames:
                print("sorry that username already exists please choose another")
            else:
                cursor.execute("INSERT INTO logininfo VALUES(?,?)",(username,userpassword))
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
                if askpassword == getinfo[0][1]:
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