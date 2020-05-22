'''
Created on 2019-8-18

@author: zhangxiao
'''

import matplotlib.pyplot as plt

fig,axs = plt.subplots(2,3)
fig.subplots_adjust(hspace=0.2,wspace=0.3)
for i in range(2):
    for j in range(3):
        axs[i,j].text(0.5,0.5,str((2,3,i)),fontsize=16,ha='center')
plt.show()

