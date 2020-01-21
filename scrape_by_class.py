from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://pythonscraping.com/pages/warandpeace.html")
bs0bj = BeautifulSoup(html)
namelist = bs0bj.findAll(text="the prince")
for name in namelist:
    print(name)