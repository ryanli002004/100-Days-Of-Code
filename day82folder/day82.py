from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods =["GET"])
def index():
    page = ""

    language = request.args.get('language', '').lower()

    if language == "english":
        page += "hi how are you?"
    elif language == "espanol":
        page += "hola, como estas"
    else:
        page += "Language not supported"

    return page


if __name__ =="__main__":
    app.run(debug = True, host ="0.0.0.0", port = 5000)
