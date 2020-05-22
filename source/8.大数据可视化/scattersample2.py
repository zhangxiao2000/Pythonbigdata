#encoding=utf-8
'''
Created on 2019年8月15日

@author: zhangxiao
'''

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

x=np.random.randn(1000)
y1=2*x+np.random.randn(1000)
y2=-2*x+np.random.randn(1000)
y3=np.random.randn(1000)

plt.figure(figsize=(15, 5))

plt.subplot(1,3,1)
plt.scatter(x,y1)
plt.title('散点图示例-正相关')

plt.subplot(1,3,2)
plt.scatter(x,y2)
plt.title('散点图示例-负相关')

plt.subplot(1,3,3)
plt.scatter(x,y3)
plt.title('散点图示例-不相关')

plt.show()