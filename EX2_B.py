from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/robots.txt"
html=urlopen(url)
Soup=BeautifulSoup(html,'lxml')
pri=Soup.prettify()
print(pri)

