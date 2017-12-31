#########################################################################
# File Name: ins2_3.py
# Author: King
# mail: arturiapendragon_1@163.com
# Created Time: 2017年12月31日 星期日 13时42分36秒
#########################################################################
#!/usr/bin/env python3
#! -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/page3.html")

bsObj = BeautifulSoup(html, "lxml")


for sibling in bsObj.find("table", {"id":"giftList"}).tr.next_siblings:
    print(sibling)
