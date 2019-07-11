from urllib.request import urlopen
try:
    url = "https://www.google.com/"
    html=urlopen(url)
except:
    print("Page Not Found")
else:
    print(html.read())
finally:
    print("RUUUNNNIINNNGGG")
