'''
Created on 2019-7-29

@author: zhangxiao
'''

import numpy as np

a=np.arange(0,5)
b=np.arange(5,10)
c=np.array([a,b])
print(a,a.dtype)
print(c,c.dtype)
print(c.shape)

ll=[1,3,5,7,9]
a2=np.array(ll)
print(a2,a2.dtype)
ll=[[1,3,4,7],[2,4,6,8]]
a3=np.array(ll)
print(a3,a3.dtype)
a4=a3.tolist()
print(type(a3))
print(type(a4))