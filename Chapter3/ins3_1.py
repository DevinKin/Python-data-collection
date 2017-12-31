#########################################################################
# File Name: ins3_1.py
# Author: King
# mail: arturiapendragon_1@163.com
# Created Time: 2017年12月31日 星期日 17时13分03秒
#########################################################################
#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html, "lxml")
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
