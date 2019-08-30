#_*_coding:utf-8_*_
import os

# =================================
# 目的：执行SHELL指令
# 功能：执行SHELL指令
# 限制：SHELL结果仅可以显示，不能作为变数
# =================================

def shell_cmd(cmd):
    os.system(cmd)

if __name__ == '__main__':
    
    shell_cmd('ping -c 6 baidu.com')