import sqlite3
import datetime
import os

connection = sqlite3.connect(os.path.join("day62folder","day62.db"))
cursor = connection.cursor()
password = "pooppants"

#cursor.execute("CREATE TABLE diary (entrynum ID, entrytime TEXT, entry TEXT)")

while True:
    ask = input("what is the password? ")
    if ask != "password1":
        print('wrong password')
    else:
        while True:
            cursor.execute("SELECT COUNT(*) FROM diary")
            count = cursor.fetchone()[0]
            currenttime = datetime.datetime.now()
            askdiary = input("1: add to diary, 2: view diary entry, 3: exit: ")
            if askdiary == '3':
                connection.close()
                exit()
            if askdiary == '1':
                count += 1
                entry = input("entry > ")
                cursor.execute("INSERT INTO diary VALUES(?, ?, ?)", (count, currenttime, entry))
                connection.commit()
            if askdiary == '2':
                if count == 0:
                    print('your diary is empty')
                else:
                    offset = 0
                    while True:
                        cursor.execute(f"SELECT * FROM diary ORDER BY entrynum DESC LIMIT 1 OFFSET {offset}")
                        rows = cursor.fetchone()
                        if rows is None:
                            break
                        timeof = rows[1]
                        entrys = rows[2]
                        print(f"time of entry: {timeof}")
                        print(f"entry{rows[0]}:{entrys}")
                        ask2 = input("1:go back, 2: view another:")
                        offset += 1
                        if ask2 == "1":
                            break
                        if ask2 == "2":
                            continue