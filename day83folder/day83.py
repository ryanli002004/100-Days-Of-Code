import datetime
from flask import Flask, redirect, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def blog():
    return ""

@app.route("/blog/blog1")
def rd1():
    return redirect("/blog1")

@app.route("/blog/blog2")
def rd2():
    return redirect("/blog2")

@app.route("/blog1", methods = ["GET"])
def blog1():
    get = request.args
    page = render_template('day83.html')
    if get == {}:
        page = page.replace("{theme}", "static/yellow.css")
    elif get['theme'].lower() == "pink":
        page = page.replace("{theme}", "static/pink.css")
    elif get['theme'].lower() == "blue":
        page = page.replace("{theme}", "static/blue.css")
    else:
        page = page.replace("{theme}", "static/yellow.css")
    title = "blog1"
    date = f"{datetime.datetime.now()}"
    text = "hello this is my first blog"
    page = page.replace("{title}",title)
    page = page.replace("{date}",date)
    page = page.replace("{text}",text)
    return page

@app.route("/blog2", methods = ["GET"])
def blog2():
    get = request.args
    page = render_template('day83.html')
    if get == {}:
        page = page.replace("{theme}", "static/yellow.css")
    elif get['theme'].lower() == "pink":
        page = page.replace("{theme}", "static/pink.css")
    elif get['theme'].lower() == "blue":
        page = page.replace("{theme}", "static/blue.css")
    else:
        page = page.replace("{theme}", "static/yellow.css")
    title = "blog2"
    date = f"{datetime.datetime.now()}"
    text = "hello this is my secondblog blog"
    page = page.replace("{title}",title)
    page = page.replace("{date}",date)
    page = page.replace("{text}",text)
    return page

if __name__ =="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)