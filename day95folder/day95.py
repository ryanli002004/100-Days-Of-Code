###couldnt test this code because open AI api requires payment###


import requests
import os
import openai
import json
from requests.auth import HTTPBasicAuth

mylist = []

#newsapikey = had to hide to upload to github
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapikey}"
result = requests.get(url)
data = result.json()
for loop in data['articles']:
    article = (f" summerize {loop['url']} in three words")

#openaikey = had to hide to upload to github
openai.api_key = os.getenv(openaikey)
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": article
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
mylist.append(response['choices'][0]['message']['content'])

clientID = "45a410b48e4a4ae6b056940dd0bc11d3"
#clientSecret = I hid the clientsecret code before uploading to github
url = "https://accounts.spotify.com/api/token"
data = {"grant_type":"client_credentials"}
auth = HTTPBasicAuth(clientID, clientSecret) 
response = requests.post(url, data=data, auth=auth)
accessToken = response.json()["access_token"]
songs = []
for headline in mylist:
    url = "https://api.spotify.com/v1/search"
    search = f"?q={headline}&type=track"
    headers = {"Authorization":f"Bearer {accessToken}"}
    fullURL = f"{url}{search}"
    response = requests.get(fullURL, headers=headers)
    data = response.json()
    songs.append(data['tracks']['items'][0])

for loop in range(10):
    if songs[loop]['name'] != None:
        print(response[loop])
        print(songs[loop]["name"])
        print(songs[loop]["preview_url"])
