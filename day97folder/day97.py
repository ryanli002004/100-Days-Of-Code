###couldnt test this code because open AI api requires payment###


import requests
from bs4 import BeautifulSoup
import openai
import os

url = "https://en.wikipedia.org/wiki/Turtle"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,"html.parser")
link = soup.find_all("p")

submit = f"summarize article in only 3 paragraphs {link}"

#openaikey = had to hide to upload to github
openai.api_key = os.getenv(openaikey)
ask = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": submit
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(f""" Here is your summary: 
{ask['choices'][0]['message']['content']}""")