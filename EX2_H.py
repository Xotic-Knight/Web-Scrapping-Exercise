from urllib.request import urlopen
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)"
html=urlopen(url)
Soup=BeautifulSoup(html,'lxml')
images=Soup.find_all('img')
for i in images:
    print(i['src'])