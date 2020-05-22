'''
Created on 2019-8-14

@author: zhangxiao
'''

import matplotlib.pyplot as plt
import math

x=range(721)
y=[math.sin(i*3.14/180) for i in x]

plt.axis([0,720,-1.1,1.1])
plt.plot(x,y,'b')
plt.xticks(range(0,721,90))
plt.xlabel("degree")
plt.ylabel("sin")
plt.title("sin function")
plt.show() 

