#encoding=utf-8
'''
Created on 2019年8月18日

@author: zhangxiao
'''

import matplotlib.pyplot as plt

#ax1 = plt.axes([0,0,1,1])  #布满整个画布，没有坐标轴
ax1 = plt.axes()  #使用默认配置，布满整个画布并画上坐标轴
plt.grid()
ax2 = plt.axes([0.4,0.4,0.2,0.2]) #在画布中间绘制一个子图

print(plt.rcParams['datapath'])

plt.show()

