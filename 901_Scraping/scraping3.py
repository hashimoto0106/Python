# -*- coding: utf-8 -*-

import urllib.request
from bs4 import BeautifulSoup

res = urllib.request.urlopen("http://itpro.nikkeibp.co.jp/NSW/?rt=nocnt")

soup = BeautifulSoup(res,'html.parser')

for i, td in enumerate(soup.findAll("td", class_="txt8")):
    a = td.find("a")
    if(a != None):
        print(str(i) + "位", a.text)

