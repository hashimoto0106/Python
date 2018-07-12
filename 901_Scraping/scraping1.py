# -*- coding: utf-8 -*-

import urllib.request
import re

res = urllib.request.urlopen("http://itpro.nikkeibp.co.jp/NSW/?rt=nocnt")
html = res.read().decode('utf-8')
res.close()

print(html)

match = re.findall('class="txt8".*?</td>', html,re.DOTALL)
match = re.findall('<a.*?a>', "".join(match), re.DOTALL)

for i, m in enumerate(match, start=1):
    s = re.sub('<.*?>', '', m)
    print(str(i) + "位", s)
