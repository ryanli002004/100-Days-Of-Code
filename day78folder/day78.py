from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

entries = {
    'day78':{
        'entry':"the day was hard 😢",
        'date':"monday August 8th"
    },
    'day79':{
        'entry':"just testing",
        'date':"maybe tomorrow"
    }
}

@app.route("/")
def default():
    return render_template('day78.html',entries = entries)


@app.route("/entries/<day>/")
def showday(day):
    entryinfo = entries.get(day)
    entry = entryinfo['entry']
    date = entryinfo['date']
    return render_template('entries.html', day=day, date=date, entry=entry)


if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)