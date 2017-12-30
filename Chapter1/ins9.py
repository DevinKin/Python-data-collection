#########################################################################
# File Name: ins9.py
# Author: King
# mail: arturiapendragon_1@163.com
# Created Time: 2017年11月18日 星期六 20时26分06秒
#########################################################################
#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html , "lxml")
    for link in bsObj.find("div", {"id", "bodyContent"}).findAll("a",
            href=re.compile("^(/wiki/)((?!:))*$")):
        if 'href' in link.attrs:
            print(link.attrs['href'])

links = getLinks("/wiki/Kevin_Bacon")
while len(links):
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
