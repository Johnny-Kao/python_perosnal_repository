#_*_coding:utf-8_*_

# =================================
# 目的：更新PIP3套件
# 功能：更新PIP3套件
# 限制：使用豆瓣来源
# =================================

from subprocess import call
import os
import json

cc = os.popen('pip3 list --format=json ')
cc = cc.read()
print(cc)
cc = json.loads(cc)
for dist in cc:
    print(dist['name'])
    call("pip3 install --timeout 6000 --trusted-host pypi.douban.com --index-url http://pypi.douban.com/simple --upgrade " + dist['name'], shell=True)