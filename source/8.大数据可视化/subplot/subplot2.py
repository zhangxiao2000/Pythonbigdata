'''
Created on 2019-8-18

@author: zhangxiao
'''

import matplotlib.pyplot as plt

fig = plt.figure()
fig.subplots_adjust(hspace=0.2,wspace=0.3)
for i in range(1,7):
    ax = fig.add_subplot(2,3,i)
    ax.text(0.5,0.5,str((2,3,i)),fontsize=16,ha='center')
plt.show()

