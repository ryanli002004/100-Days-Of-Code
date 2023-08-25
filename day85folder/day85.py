from flask import Flask, render_template, request, redirect, session
import sqlite3
import os

connection = sqlite3.connect(os.path.join('day84folder','day84.db'))
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS logininfo(username TEXT, name TEXT, password TEXT)")
connection.commit()
connection.close()

app = Flask(__name__, static_url_path='/static')
app.secret_key = "supersecretkey"

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/login')
def login():
        if "username" in session:
            return redirect('/dashboard')
        else:
            return render_template("login.html")

@app.route('/result', methods = ['POST'])
def result():
    form = request.form
    loginusername = form['loginusername']
    loginpassword = form['loginpassword']
    connection = sqlite3.connect(os.path.join('day84folder','day84.db'))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM logininfo WHERE username = ?", (loginusername,))
    data = cursor.fetchone()
    connection.close()
    if data[0]==loginusername and data[2]==loginpassword:
        session['username'] = loginusername
        session['name'] = data[1]
        return redirect("/dashboard")
    else:
        return render_template("Llogin.html")
    
@app.route('/dashboard')
def dashboard():
        if 'username' in session:
            page = render_template("Wlogin.html")
            page = page.replace('{name}',session['name'])
            return page

@app.route('/createuser')
def create():
    return render_template("createuser.html")

@app.route('/saveuser', methods = ['POST'])
def saveuser():
    form = request.form
    createusername = form['createusername']
    createpassword = form['createpassword']
    name = form['name']
    connection = sqlite3.connect(os.path.join('day84folder','day84.db'))
    cursor = connection.cursor()
    cursor.execute("INSERT INTO logininfo values(?,?,?)",(createusername,name,createpassword))
    connection.commit()
    connection.close()
    return redirect("/login")

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=5000)