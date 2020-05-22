#encoding=utf-8
'''
Created on 2019年8月18日

@author: zhangxiao
'''

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import math

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False   #用来正常显示负号

x=range(721)
y=[math.sin(i*3.14/180) for i in x]

plt.axis([0,720,-1.1,1.1])
plt.plot(x,y,'b')
plt.xticks(range(0,721,90))
plt.xlabel("度数")
plt.ylabel("正弦值(sin)")
plt.title("正弦函数")

plt.show()