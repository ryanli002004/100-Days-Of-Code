import requests
from bs4 import BeautifulSoup

for loop in range(1,50):
        
    url = f"https://news.ycombinator.com?p={loop}"
 
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    mylinks = soup.find_all("a", {'rel':"noreferrer"})

    for link in mylinks:
        if "Python" in str(link.text) or "Replit" in str(link.text):
            print(link.text)
            print(link['href'])


