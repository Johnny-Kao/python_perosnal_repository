#_*_coding:utf-8_*_
import os

# =================================
# 目的：执行SHELL指令
# 功能：执行SHELL指令
# 限制：SHELL结果可作为变数，SHELL执行结束时候，一次返回内容
# =================================

def shell_cmd_return(cmd):
    res = os.popen(cmd).read()
    return res

if __name__ == '__main__':
    
    print(shell_cmd_return('ping -c 6 baidu.com'))