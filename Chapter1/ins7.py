#########################################################################
# File Name: ins7.py
# Author: King
# mail: arturiapendragon_1@163.com
# Created Time: 2017年11月18日 星期六 20时04分10秒
#########################################################################
#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
from urllib.request import urlopen 
from bs4 import BeautifulSoup

html = urlopen("http://pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")
print(bsObj.find("img", {"src":"../img/gifts/img1.jpg"
    }).parent.previous_sibling.get_text())

