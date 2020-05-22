'''
Created on 2019-8-3

@author: zhangxiao
'''

import numpy as np

data = np.array([1,3,5,6,9,12,10])

print("Max method:\t", data.max())
print("Max function:\t", np.max(data))

print("Min method:\t", data.min())
print("Min function:\t", np.min(data))

print("Mean method:\t", data.mean())
print("Mean function:\t", np.mean(data))

print("Std method:\t", data.std())
print("Std function:\t", np.std(data))

print("Median:\t\t", np.median(data))

