from urllib.request import urlopen
from bs4 import BeautifulSoup
url="http://en.wikipedia.org/wiki/Main_Page/"
html=urlopen(url)
Soup=BeautifulSoup(html,'lxml')
list=['h1','h2','h3','h4','h5','h6']
t=Soup.find_all(list)
print(*t,sep='\n')