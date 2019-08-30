#_*_coding:utf-8_*_
import os

# =================================
# 目的：获取WIFI名称
# 功能：获取WIFI名称
# 限制：MAC OS ONLY (10.11)
# =================================

def get_ssid():
    cmd = '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I | sed -e "s/^  *SSID: //p" -e d'
    # return example 'GuoAP\n'
    res = os.popen(cmd).read()
    return res[:-1:]

if __name__ == '__main__':
    print(get_ssid())