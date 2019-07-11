from urllib.request import urlopen
from bs4 import BeautifulSoup
url="https://catalog.data.gov/dataset?q=&sort=metadata_created+desc&as_sfid=AAAAAAXEuk5b-2jg1ZyceC3qMZTYDBWKghRGHm3x03MW-DcgxD-ptBG-h5vIia0RPRE3kW9cJEVBNScLoxfV9PqHNFRMDHFIwZ6COOejcOxqcsMWkQ610iA1rPhdHa1EqwU5K_U%3D&as_fid=4a58414a228737e0ea0c90ed89dddfecac4a5b1c&ext_location=&ext_bbox=&ext_prev_extent=-142.03125%2C8.754794702435618%2C-59.0625%2C61.77312286453146"
html=urlopen(url)
Soup=BeautifulSoup(html,'lxml')
li=Soup.find_all('div',class_='dataset-content')
print(li.__len__())
