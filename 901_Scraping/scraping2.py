# -*- coding: utf-8 -*-

import urllib.request
import lxml.html

res = urllib.request.urlopen("http://itpro.nikkeibp.co.jp/NSW/?rt=nocnt")

dom = lxml.html.fromstring(res.read())

res.close()

match = dom.xpath('//td[@class="txt8"]/a')

for i, m in enumerate(match, start=1):
    print(str(i) + "位", m.text)
