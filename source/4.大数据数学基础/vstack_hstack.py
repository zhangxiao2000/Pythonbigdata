
'''
Created on 2019年8月18日

@author: lingyulong
'''


import numpy as np

#vstack()：沿着竖直方向将矩阵堆叠起来。注意：除了第一维可以不一致，其余维的维度必须一致 。
#第一维、第二维的维度都一致
a=np.array([1,2,3])   #维度：a.shape=(3,)
b=np.array([4,5,6])   #维度：a.shape=(3,)
print(a.shape)
print(b.shape)
print(np.vstack((a,b)))


#第一维不一致，第二维的维度一致 
a=np.array([[1],[2],[3]])  #维度：a.shape=(3, 1)
b=np.array([[4],[5],[6],   #维度：b.shape=(3, 2)
            [7],[8],[9]])
print(a.shape)   
print(b.shape)  
print(np.vstack((a,b)))




#hstack()：沿着水平方向将数组堆叠起来。注意：除了第二维外，被堆叠的矩阵各维度要一致。
#第一维、第二维的维度都一致
a=np.array([1,2,3])     #维度：a.shape=(3,)
b=np.array([4,5,6])     #维度：b.shape=(3,)
print(a.shape)   
print(b.shape) 
print(np.hstack((a,b)))


#第一维一致，第二维的维度不一致
a=np.array([[1,2,3],[4,5,6]])    #维度：a.shape=(2,3)
b=np.array([[4,5],[6,7]])        #维度：a.shape=(2,2)
print(a.shape)   
print(b.shape) 
print(np.hstack((a,b)))


