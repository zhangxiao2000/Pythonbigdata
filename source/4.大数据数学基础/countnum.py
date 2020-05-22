#encoding=utf-8
'''
Created on 2019-8-3

@author: zhangxiao
'''


import numpy as np
from collections import Counter
 
data = np.array([1,2,4,7,1,2,6,2,7,6])
 
# 方法一:使用Counter统计次数
print("Counter(data):",Counter(data)) # 调用Counter函数
 
# 方法二：使用np.sum函数统计次数
print("np.unique(data):",np.unique(data)) # unique返回的是已排序数组
 
for i in np.unique(data):
    print("{}:{}".format(i,np.sum(data==i))) # 对照unique数组，依次统计每个元素出现的次数

#使用unique函数也可以直接统计出每个元素出现的个数
# unique返回的是一个两个元素的元组，第一个是已排序的数组，第二个是各个元素出现的个数
print('np.unique(data,return_counts=True)\n',np.unique(data,return_counts=True)) 
 
#方法三:使用np.bincount函数统计次数
#返回值中的每个bin，给出了它的索引值在x中出现的次数（在默认权重下）
count=np.bincount(data)
print("np.bincount(data):",count)

import matplotlib.pyplot as plt
plt.bar(range(len(count)),count)
plt.show()


#累积分布函数
cdf=np.cumsum(count)
print(cdf)
plt.plot(range(len(count)),cdf)
plt.show()

cdf2=[]
for i in range(max(data)+1):
    cdf2.append(np.sum(data<=i)) 

print(cdf2)
    
    


        