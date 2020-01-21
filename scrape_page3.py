from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bs0bj = BeautifulSoup(html)

print(bs0bj.h1)
for sibling in bs0bj.find("table", {"id":"giftList"}).children:
    print(sibling)
