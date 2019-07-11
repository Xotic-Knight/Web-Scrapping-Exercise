from urllib.request import urlopen
from bs4 import BeautifulSoup
url="https://en.wikipedia.org/wiki/Python"
html=urlopen(url)
Soup=BeautifulSoup(html,'lxml')
data=Soup.find_all('a')
for i in data:
    print(i.text)