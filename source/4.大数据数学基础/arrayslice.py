#encoding=utf-8
'''
Created on 2019-8-1

@author: zhangxiao
'''

import numpy as np

arr=np.arange(12)
print(arr)    #输出：[ 0  1  2  3  4  5  6  7  8  9 10 11]
print()

print(arr[0])      #输出：0
print(arr[:2])      #输出：[0 1]
print(arr[3:6])     #默认步长是1，输出：[3 4 5]
print(arr[3:6:2])   #步长是2，输出：[3 5]


arr=np.arange(12)
arr=arr.reshape(3,4)
print(arr)        #输出：[ [ 0  1  2  3] [ 4  5  6  7]  [ 8  9 10 11]]
print()

print(arr[0])       #输出：[0 1 2 3]
print(arr[:2])      #输出：[[0 1 2 3]  [4 5 6 7]]


print(arr[0][1])    #（1）递归，输出：1
print(arr[0,1])     #（2）逗号分隔符列表输出：1


