#encoding=utf-8
'''
Created on 2019-8-18

@author: zhangxiao
'''

import matplotlib.pyplot as plt

for i in range(1,7):
    plt.subplot(2,3,i)
    plt.subplots_adjust(wspace=0.3, hspace=0.2)#调整子图间距
    plt.text(0.5,0.5,str((2,3,i)),fontsize=16,ha='center')
    
plt.show()
