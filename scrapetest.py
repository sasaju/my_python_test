from urllib.request import urlopen
from urllib.error import HTTPError
import re

from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError:
        return None
    try:
        bs0bj = BeautifulSoup(html.read())
        images = bs0bj.findAll("img", {"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")})
    except AttributeError:
        return None
    return images
"""
title = getTitle("http://pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
"""
#正则表达式测试
img = getTitle("http://pythonscraping.com/pages/page3.html")
for image in img:
    print(image["src"])
