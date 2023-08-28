import json
import requests
import os

for x in range(0,10):
    result = requests.get('https://randomuser.me/api/')
    user = result.json()
    #print(json.dumps(user,indent=2))
    firstname = user['results'][0]['name']['first']
    lastname = user['results'][0]['name']['last']
    image = user['results'][0]['picture']['medium']
    picture = requests.get(image)
    f = open(os.path.join('day90folder',f"{firstname} {lastname}.jpeg"),'wb')
    f.write(picture.content)
    f.close()