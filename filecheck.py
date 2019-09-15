#_*_coding:utf-8_*_
import os

# =================================
# 目的：确认档案是否存在
# 功能：确认档案是否存在
# =================================

def check_file_exists(path):
    res = os.path.exists(path)
    return res

if __name__ == '__main__':
    path = '/etc/nsmb.conf'
    print(check_file_exists(path))

    
