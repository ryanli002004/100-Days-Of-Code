#uploaded to public github repository so I had to hide the clientsecret
import requests
from requests.auth import HTTPBasicAuth
from flask import Flask, request

app = Flask(__name__)

def gettracks(year):


    clientID = "45a410b48e4a4ae6b056940dd0bc11d3"
    #clientSecret = I hid the clientsecret code before uploading to github
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type":"client_credentials"}
    auth = HTTPBasicAuth(clientID, clientSecret) 
    response = requests.post(url, data=data, auth=auth)
    accessToken = response.json()["access_token"]

    offset = 0

    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization":f"Bearer {accessToken}"}
    search = f"?q=year%3A{year}&type=track&limit=10&offset={offset}"
    fullURL = f"{url}{search}"

    response = requests.get(fullURL, headers=headers)
    data = response.json()

    f = open("/Users/ryanli/Desktop/replit100daysofcode/day93folder/templates/songs.html", "r")
    songs = f.read()
    f.close()
     
    listsongs = ""

    for loop in data['tracks']['items']:
        track = songs
        track = track.replace("{name}",f"{loop['name']} by {loop['artists'][0]['name']}")
        track = track.replace("{url}",f"{loop['preview_url']}")
        listsongs += track
    
    return listsongs

@app.route("/")
def index():
    page = ""
    f = open("/Users/ryanli/Desktop/replit100daysofcode/day93folder/templates/spotify.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{songs}","")
    page = page.replace("{value}","1990")
    return page

@app.route("/", methods = ["POST"])
def change(): 
    page = ""
    f = open("/Users/ryanli/Desktop/replit100daysofcode/day93folder/templates/spotify.html", "r")
    page = f.read()
    f.close()
    year = request.form["year"]
    songs = gettracks(year)
    page = page.replace("{songs}",songs)
    page = page.replace("{value}",year)
    return page


if __name__ == "__main__":
    app.run(debug = True)