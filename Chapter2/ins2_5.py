#########################################################################
# File Name: ins2_5.py
# Author: King
# mail: arturiapendragon_1@163.com
# Created Time: 2017年12月31日 星期日 17时00分48秒
#########################################################################
#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")
images = bsObj.findAll("img", {"src" : re.compile("\.\./img\/gifts\/img.*\.jpg")})
for image in images:
    print(image)
    print(image["src"])
