#########################################################################
# File Name: ins2_4.py
# Author: King
# mail: arturiapendragon_1@163.com
# Created Time: 2017年12月31日 星期日 16时27分37秒
#########################################################################
#!/usr/bin/env python3
#! -*- coding: utf-8 -*-


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")
print(bsObj.find("img", {"src" : "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
