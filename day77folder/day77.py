import datetime
from flask import Flask, redirect, render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def blog():
    return render_template('day77.html')

@app.route("/blog/blog1")
def rd1():
    return redirect("/blog1")

@app.route("/blog/blog2")
def rd2():
    return redirect("/blog2")

@app.route("/blog1")
def blog1():
    title = "blog1"
    date = f"{datetime.datetime.now()}"
    text = "hello this is my first blog"
    page = render_template('day77.html')
    page = page.replace("{title}",title)
    page = page.replace("{date}",date)
    page = page.replace("{text}",text)
    return page

@app.route("/blog2")
def blog2():
    title = "blog2"
    date = f"{datetime.datetime.now()}"
    text = "hello this is my secondblog blog"
    page = render_template('day77.html')
    page = page.replace("{title}",title)
    page = page.replace("{date}",date)
    page = page.replace("{text}",text)
    return page

if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)