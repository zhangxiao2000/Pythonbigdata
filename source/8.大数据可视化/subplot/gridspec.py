#encoding=utf-8
'''
Created on 2019-8-18

@author: zhangxiao
'''

import matplotlib.pyplot as plt

grid = plt.GridSpec(2,3,wspace=0.3,hspace=0.2) #生成两行三列的网格

plt.subplot(grid[0,0]) #将0,0的位置使用
plt.text(0.5,0.5,"[0,0]",fontsize=16,ha='center')
plt.subplot(grid[0,1]) #将0,1的位置使用
plt.text(0.5,0.5,"[0,1]",fontsize=16,ha='center')

plt.subplot(grid[1,:2]) #使用1,1-2的位置
plt.text(0.5,0.5,"[1,0-1]",fontsize=16,ha='center')
plt.subplot(grid[:2,2])#使用1-2,2的位置
plt.text(0.5,0.5,"[0-1,2]",fontsize=16,ha='center')
plt.show()


