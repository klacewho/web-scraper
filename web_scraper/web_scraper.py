
from web_scraper import requests

URL = "https://en.wikipedia.org/wiki/Battle_of_Blair_Mountain"

page = requests.get(URL)

print(page)