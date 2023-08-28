from flask import Flask, render_template, redirect, request, session
import sqlite3
import os

connection = sqlite3.connect(os.path.join('day89folder','day89.db'))
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS logininfo(username TEXT, password TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS chat(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, message TEXT)")
connection.commit()
admn = "ryan"

app = Flask(__name__)
app.secret_key='secretkey'

@app.route('/')
def index():
    if 'username' in session:
        if session['username'] == admn:
            return redirect('/admin')
        else:
            return redirect('/chat')
    return render_template('landing.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/createuser')
def createuser():
    return render_template('createuser.html')

@app.route('/accountresult',methods=['POST'])
def accountresult():
    form = request.form
    username = form['username']
    password = form['password']
    connection = sqlite3.connect(os.path.join('day89folder','day89.db'))
    cursor = connection.cursor()
    cursor.execute("INSERT INTO logininfo VALUES(?,?)",(username,password))
    connection.commit()
    return redirect('/login')

@app.route('/loginresult', methods = ['POST'])
def result():
    form = request.form
    username = form['username']
    password = form['password']
    connection = sqlite3.connect(os.path.join('day89folder','day89.db'))
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM logininfo WHERE username = ?',(username,))
    info = cursor.fetchone()
    if info[0] == username and info[1] == password and username == admn:
        session['username']=admn
        return redirect('/admin')
    elif info[0] == username and info[1] == password:
        session['username']=username
        return redirect('/chat')
    else:
        return redirect('/')
    
@app.route('/admin')
def admin():
    connection = sqlite3.connect(os.path.join('day89folder','day89.db'))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM chat ORDER BY id DESC")
    rows = cursor.fetchall()
    return render_template('admin.html',rows=rows)

@app.route('/adminresult', methods = ['POST'])
def adminresult():
    form = request.form
    username = session['username']
    message = form['message']
    connection = sqlite3.connect(os.path.join('day89folder','day89.db'))
    cursor = connection.cursor()
    cursor.execute("INSERT INTO chat(username,message) VALUES(?,?)",(username,message))
    connection.commit()
    return redirect('/admin')


@app.route('/chatresult', methods=['POST'])
def chatresult():
    form = request.form
    username = session['username']
    message = form['message']
    connection = sqlite3.connect(os.path.join('day89folder','day89.db'))
    cursor = connection.cursor()
    cursor.execute("INSERT INTO chat(username,message) VALUES(?,?)",(username,message))
    connection.commit()
    return redirect('/chat')

@app.route('/chat')
def chat():
    connection = sqlite3.connect(os.path.join('day89folder','day89.db'))
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM chat ORDER BY id DESC")
    rows = cursor.fetchall()
    return render_template('chat.html',rows=rows)

@app.route('/deletemessage', methods = ['POST'])
def deletemessage():
    form = request.form
    messageid = form['messageid']
    connection = sqlite3.connect(os.path.join('day89folder','day89.db'))
    cursor = connection.cursor()
    cursor.execute("DELETE FROM chat WHERE id = ?",(messageid,))
    connection.commit()
    return redirect('/admin')

    
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug = True)