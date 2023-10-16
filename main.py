import requests
from bs4 import BeautifulSoup

# We get the url
r = requests.get("https://en.wikiquote.org/wiki/Khalil_Gibran")
soup = BeautifulSoup(r.content)

print(r.content)

print('xxx')
