from flask import Flask, render_template, request, redirect, session
import sqlite3
import os

app = Flask(__name__, static_url_path='/static')
app.secret_key = "secretkey"

connection = sqlite3.connect(os.path.join('day86folder','day86.db'))
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS blog(title TEXT, date TEXT, entry TEXT)")
connection.commit()

blogusername = "ryan"
blogpassword = "password1"

@app.route('/')
def index():
    connection = sqlite3.connect(os.path.join('day86folder','day86.db'))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM blog")
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
    if form['loginusername'] == blogusername and form['loginpassword']== blogpassword:
        session['username'] = blogusername
        return redirect("/dashboard")
    else:
        return redirect('/')
    
@app.route('/dashboard')
def dashboard():
    connection = sqlite3.connect(os.path.join('day86folder','day86.db'))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM blog")
    rows = cursor.fetchall()
    return render_template("dashboard.html", rows=rows)

@app.route('/saveentry', methods = ['POST'])
def saveentry():
    form = request.form
    title = form['title']
    date = form['date']
    entry = form['entry']
    connection = sqlite3.connect(os.path.join('day86folder','day86.db'))
    cursor = connection.cursor()
    cursor.execute("INSERT INTO blog VALUES(?,?,?)",(title,date,entry))
    connection.commit()
    return redirect('/dashboard')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)