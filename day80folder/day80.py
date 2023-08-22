from flask import Flask, render_template, request

app = Flask(__name__, static_url_path="/static")

@app.route("/")
def index():
    return render_template('day79.html')

@app.route("/process", methods=["POST"])
def process():
    page =""
    form = request.form
    if form['name'] == "Ryan" and form['password'] == "password1":
        page += f"welcome back, {form['name']}"
    elif form['name'] == "Daniella" and form['password'] == "pooppants":
        page += f"welcome back, {form['name']}"
    elif form['name'] == "John" and form['password'] == "john":
        page += f"welcome back, {form['name']}"
    else:
        page += f"GO AWAY!"
    return page


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)