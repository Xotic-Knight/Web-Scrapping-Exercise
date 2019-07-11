from urllib.request import urlopen
from bs4 import BeautifulSoup

import requests
url="http://maps.googleapis.com/maps/api/geocode/json"
address={
    'Address':'1600 Amphitheatre Parkway, Mountain View, CA'
}
response=requests.get(url,params=address)
q=response.json()
print(q)
