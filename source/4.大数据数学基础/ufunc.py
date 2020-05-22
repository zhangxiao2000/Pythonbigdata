'''
Created on 2019年8月18日

@author: lingyulong
'''
import numpy as np

#np.abs():每个元素取绝对值
data=np.array([1,2,-3,4,-5,6])
print("原数组:",data)     
print("数组进行abs操作:",np.abs(data))


data=np.array([[1.1,1.5,1.7],
               [-1.1,-1.5,-1.7],
               [2.1,2.6,3.9]])
print(np.rint(data))   #对每个元素进行四舍五入
print(np.trunc(data))  #对每个元素进行向0取整
print(np.isinf(data))
print(np.isfinite(data))
print(np.isnan(data))





#np.add():两个数组的对应元素相加
a=np.array([[1,2,3],
            [11,22,33]])
b=np.array([[1,-1,2],
            [2,3,1]])
print("两个数组对应元素相加得到的新数组：")
c=np.add(a,b)
print(c)

#np.maximum():两个数组的对应元素相加
a=np.array([[1,2,3],
            [11,22,33]])
b=np.array([[1,15,9],
            [2,3,100]])
print("两个数组对应元素的最大值/最小值：")
print(np.maximum(a,b))
print(np.minimum(a,b))

#np.fmax():两个数组的对应元素相加
a=np.array([[1,np.nan,3],
            [11,22,33]])
b=np.array([[1,15,9],
            [2,np.nan,100]])
print("两个数组对应元素的最大值/最小值，忽略nan：")
#因为a，b中含有np.nan，所以使用np.maxmimum会报错，只能使用np.fmax
#print(np.maximum(a,b))
#print(np.minimum(a,b))
print(np.fmax(a,b))
print(np.fmin(a,b))



