#########################################################################
# File Name: ins3.py
# Author: King
# mail: arturiapendragon_1@163.com
# Created Time: 2017年11月17日 星期五 17时14分23秒
#########################################################################
#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "lxml")

nameList = bsObj.findAll("span", {"class" : "green"})
for name in nameList:
    print(name.get_text())
