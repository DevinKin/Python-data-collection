#########################################################################
# File Name: ins3_3.py
# Author: King
# mail: arturiapendragon_1@163.com
# Created Time: 2017年12月31日 星期日 19时45分38秒
#########################################################################
#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import re
import random

random.seed(datetime.datetime.now())
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org/" + articleUrl)
    bsObj = BeautifulSoup(html, "lxml")
    return bsObj.find("div", {"id" : "bodyContent"}).findAll("a", 
            href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")

while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)

