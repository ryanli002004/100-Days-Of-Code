#day 88 also wants me to do stuff with replit only authentication feature. so instead I'm going to order my blog entries.
from flask import Flask, render_template, request, redirect, session
import sqlite3
import os
import hashlib

app = Flask(__name__, static_url_path='/static')
app.secret_key = "secretkey"

connection = sqlite3.connect(os.path.join('day88folder','day88.db'))
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS logininfo(username TEXT, password TEXT, salt TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS blog(id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, date TEXT, entry TEXT)")
#cursor.execute("INSERT INTO logininfo VALUES (?,?,?)",(blogusername,blogpassword,salt))
connection.commit()


@app.route('/')
def index():
    connection = sqlite3.connect(os.path.join('day88folder','day88.db'))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM blog ORDER BY id DESC")
    rows = cursor.fetchall()
    return render_template('blog.html', rows = rows)

@app.route('/login')
def login():
    if 'username' in session:
        return redirect('/dashboard')
    return render_template('login.html')

@app.route('/result', methods = ['POST'])
def result():
    form = request.form
    connection = sqlite3.connect(os.path.join('day88folder','day88.db'))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM logininfo")
    info = cursor.fetchall()
    salt = info[0][2]
    if form['loginusername'] == info[0][0] and hashlib.pbkdf2_hmac("sha256", form['loginpassword'].encode('utf-8'), bytes(salt), 100000) == info[0][1]:
        session['username'] = info[0][0]
        return redirect("/dashboard")
    else:
        return redirect('/')
    
@app.route('/dashboard')
def dashboard():
    connection = sqlite3.connect(os.path.join('day88folder','day88.db'))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM blog ORDER BY id DESC")
    rows = cursor.fetchall()
    return render_template("dashboard.html", rows=rows)

@app.route('/saveentry', methods = ['POST'])
def saveentry():
    form = request.form
    title = form['title']
    date = form['date']
    entry = form['entry']
    connection = sqlite3.connect(os.path.join('day88folder','day88.db'))
    cursor = connection.cursor()
    cursor.execute("INSERT INTO blog(title,date,entry) VALUES(?,?,?)",(title,date,entry))
    connection.commit()
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)