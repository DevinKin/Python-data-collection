#########################################################################
# File Name: ins6.py
# Author: King
# mail: arturiapendragon_1@163.com
# Created Time: 2017年11月18日 星期六 19时49分33秒
#########################################################################
#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")

for sibling in bsObj.find("table", {"id": "giftList"}).children:
    print(sibling)

