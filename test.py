
import requests
from bs4 import BeautifulSoup

url = 'http://kazhydromet.kz/ru/almaty'
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")
wtext = soup.select(".w_map span")[0].text
degree = wtext[:-12]
degree1 = degree.replace("Сейчас",'')
print(degree1)