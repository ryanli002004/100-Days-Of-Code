from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('day81.html')

@app.route('/process',methods= ["POST"])
def process():
    page = ""
    form = request.form
    if form['food']=="human food" and form['robot']=="no":
        page+="welcome human"
    else:
        page+="go away robot!"
    return page

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0",port=5000)