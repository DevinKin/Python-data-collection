#########################################################################
# File Name: ins2.py
# Author: King
# mail: arturiapendragon_1@163.com
# Created Time: 2017年11月17日 星期五 16时58分34秒
#########################################################################
#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)

