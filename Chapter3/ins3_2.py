#########################################################################
# File Name: ins3_2.py
# Author: King
# mail: arturiapendragon_1@163.com
# Created Time: 2017年12月31日 星期日 19时28分35秒
#########################################################################
#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "lxml")
for link in bsObj.find("div", {"id" : "bodyContent"}).findAll("a",
        href=re.compile("^(/wiki/)((?!:).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])
