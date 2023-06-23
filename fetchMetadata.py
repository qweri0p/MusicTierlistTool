import requests
from bs4 import BeautifulSoup

def getdata(url):
    # url = "https://dreamcatalogue.bandcamp.com/album/--18"
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'html.parser')
    cover = soup.find(class_="popupImage").get('href')
    name = soup.find(class_="trackTitle").get_text(strip=True)
    artist = soup.find(id="name-section").h3.span.a.get_text(strip=True)
    return name, artist, cover
