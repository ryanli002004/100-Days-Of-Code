###couldnt test this code because open AI api requires payment###


import requests, os, openai

#newsapikey = had to hide to upload to github
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapikey}"
result = requests.get(url)
data = result.json()
for loop in data['articles']:
    article = (f" summerize {loop['url']} in one sentence")


#openaikey = had to hide to upload to github
openaiorg = "org-eWfmnkoeB7U520pSnFT8rLzN"



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

print(response['choices'][0]['message']['content'])