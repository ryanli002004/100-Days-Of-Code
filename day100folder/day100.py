import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
import os
import requests
from bs4 import BeautifulSoup
import schedule 
import time

connection = sqlite3.connect(os.path.join("day99folder","day99.db"))
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS price(item INT)")
connection.commit()

def getprice():
    url = f"https://us.shop.gymshark.com/products/gymshark-oversized-t-shirt-black-aw21"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    cursor.execute("SELECT * FROM price")
    results = cursor.fetchall()
    results = [x[0] for x in results]
    mylinks = soup.find_all("span", {'class':"product-information_price__6g6xM"})
    for link in mylinks:
        price = int(link.text[1:])
        if price not in results:
            cursor.execute("SELECT * FROM price")
            get = cursor.fetchall()
            get = [x[0] for x in get]
            get.append(price)
            get.sort()
            if int(price) == get[0]:
                cursor.execute("INSERT INTO price VALUES (?)",(price,))
                connection.commit()
                message = f"<p><a href='{link['href']}'>Oversized Essentials Men's T-shirt has a new low price!: {link.text}</a></p>"
                priceupdater(message)

def priceupdater(x):
    message = x
    host = "smtp.gmail.com"
    port = 587
    #emailpass = i had to remove the password before uploading to github
    emailuser = "ryanli002004@gmail.com"
    s = smtplib.SMTP(host=host, port=port)
    s.starttls()
    s.login(emailuser,emailpass)
    msg = MIMEMultipart()
    msg['To'] = emailuser
    msg['From'] = emailuser
    msg['Subject'] = "new low price!"
    msg.attach(MIMEText(message, 'html'))
    s.send_message(msg)
    del msg

schedule.every(5).minutes.do(priceupdater)

while True:
    schedule.run_pending()
    time.sleep(1)