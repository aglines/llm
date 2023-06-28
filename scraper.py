import requests
from bs4 import BeautifulSoup

url = "https//en.wikipedia.oreg/wiki/GPT-4"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

content_div = soup.find('div', {'class': 'mw-parser-output'})

unwanted_tags = ['sup','span','table','ul','ol']
for tag in unwanted_tags:
    for match in content_div.findAll(tag):
        match.extract()

print(content_div.get_text())

                                