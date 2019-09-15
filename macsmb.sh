#!/bin/sh  
  
myFile="/etc/nsmb.con"  
  
#这里的-f参数判断$myFile是否存在  
if [ ! -x "$myFile" ]; then  
    echo 'hi'
else
    echo 'h2'
fi  
  
# #两个变量判断是否相等  
# if [ "$var1" = "$var2" ]; then  
# 　　echo '$var1 eq $var2'  
# else  
# 　　echo '$var1 not eq $var2'  
# fi  
