from urllib.request import urlopen
from bs4 import BeautifulSoup
url="http://www.example.com/"
html=urlopen(url)
Soup=BeautifulSoup(html,'lxml')
print(Soup.h1)
