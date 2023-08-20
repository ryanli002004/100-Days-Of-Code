#used sqlite3 instead of replit's own DB 

import sqlite3
import datetime
import os

connection = sqlite3.connect(os.path.join('day61folder','day61.db'))
cursor = connection.cursor()

#cursor.execute("""CREATE TABLE twitter(date TEXT,time TEXT,tweet TEXT)""")

while True:
    today = datetime.datetime.now()
    currentday = f"{today.year}-{today.month}-{today.day}"
    currenttime = f"{today.hour}-{today.minute}-{today.second}"

    ask = input("1:tweet, 2:view tweets, 3:exit > ")
    if ask == "3":
        connection.close()
        exit()
    if ask == "1":
        tweet = input("tweet > ")
        cursor.execute("""
        INSERT INTO twitter VALUES(?, ?, ?)
        """, (currentday,currenttime,tweet))
        connection.commit()
    if ask == "2":
        cursor.execute("""
        SELECT * FROM twitter
        """)
        rows = cursor.fetchall()
        for loop in rows:
            print(f"""
                  time : {loop[0]}{loop[1]}
                  tweet : {loop[2]}    
""")