import requests
from bs4 import BeautifulSoup
import schedule 
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sqlite3
import os

connection = sqlite3.connect(os.path.join("day99folder","day99.db"))
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS news (text TEXT)")
connection.commit()

def hackernewssender(x):
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
    msg['Subject'] = "new news!"
    msg.attach(MIMEText(message, 'html'))
    s.send_message(msg)
    del msg

def getnews():
    url = f"https://news.ycombinator.com?"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    mylinks = soup.find_all("a", {'rel':"noreferrer"}) 
    cursor.execute("SELECT * FROM news")
    pastnews = cursor.fetchall()
    pastnews = [x[0] for x in pastnews]
    for link in mylinks:
        if "Python" in str(link.text) or "Replit" in str(link.text) or "Microsoft" in str(link.text):
            if link.text not in pastnews:
                cursor.execute("INSERT INTO news VALUES (?)",(link.text,))
                connection.commit()
                message = f"<p><a href='{link['href']}'>{link.text}</a></p>"
                hackernewssender(message)

schedule.every(5).hours.do(getnews)

while True:
    schedule.run_pending()
    time.sleep(1)