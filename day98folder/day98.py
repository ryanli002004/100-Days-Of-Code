import schedule 
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random

def quotesender():
    quotes = ["A rose by any other name would smell as sweet.","All that glitters is not gold.","All the world’s a stage, and all the men and women merely players.","Ask, and it shall be given you; seek, and you shall find." , "Eighty percent of success is showing up."]
    quote = random.choice(quotes)
    host = "smtp.gmail.com"
    port = 587
    #emailpass = removed this before uploading tio github
    emailuser = "ryanli002004@gmail.com"
    s = smtplib.SMTP(host=host, port=port)
    s.starttls()
    s.login(emailuser,emailpass)
    msg = MIMEMultipart()
    msg['To'] = emailuser
    msg['From'] = emailuser
    msg['Subject'] = "inspiration"
    msg.attach(MIMEText(quote, 'html'))
    s.send_message(msg)
    del msg

schedule.every(24).hours.do(quotesender)

while True:
    schedule.run_pending()
    time.sleep(1) 