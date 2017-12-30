#########################################################################
# File Name: ins1.py
# Author: King
# mail: arturiapendragon_1@163.com
# Created Time: 2017年11月17日 星期五 16时53分26秒
#########################################################################
#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), "lxml")
print(bsObj)
