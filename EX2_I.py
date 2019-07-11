import requests
r=requests.get("https://analytics.usa.gov/data/live/browsers.json")
print(r.json()['totals']['browser'])