'''
Created on 2019-8-2

@author: zhangxiao
'''

import random
import numpy as np
import matplotlib.pyplot as plt

n=random.randint(1,100)
print(n)

out=np.random.binomial(9,0.5,size=10000)

count=np.bincount(out)

plt.plot(np.arange(len(count)),count)
plt.show()

