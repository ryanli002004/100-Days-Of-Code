from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('day76.html')

@app.route('/videogames')
def videogames():
    return render_template('day75.html')

@app.route('/websites')
def websites():
    return render_template('day73.html')

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)