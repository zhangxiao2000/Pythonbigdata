'''
Created on 2019-8-1

@author: zhangxiao
'''

import numpy as np

arr=np.arange(12)
a1=arr.reshape(3,4)
a2=arr.reshape(3,4)
a2.shape=(2,6)

print(arr.shape,a1.shape,a2.shape)
print(arr)
print(a1)
print(a2)

arr.resize(4,3)
print(arr)
print(arr.shape)

