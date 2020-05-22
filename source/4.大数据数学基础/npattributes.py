'''
Created on 2019年8月17日

@author: lingyulong
'''
import numpy as np

data=np.array([[1,2],
               [3,4],
               [5,6]])

print("dtype:数组中元素的数据类型")
print(data.dtype)
print()

print("shape:数组的形状")
print(data.shape)

#自己计算的NumPy的size：
s=1
for i in data:
    s=s*i
print("自己计算的NumPy的size：")
print(s)
print()


print("size:")
print(data.size)
print()


print("itemsize(单位：bytes):数组中每个元素的内存大小")
print(data.itemsize)
print()

print("自己计算的数组的字节数:")
print((data.size*data.itemsize))
print()

print("NumPy自带的 nbytes:数组的内存大小")
print(data.nbytes)
print()

print("ndim:数组的维度")
print(data.ndim)
print()

print("real:数组的实数部分")
print(data.real)
print()

print("imag:数组的虚数部分")
print(data.imag)
print()

print("T:数组的转置")
print(data.T)
print()

#ndarray.flat:将数组转换为1-D的迭代器,flat返回的是一个迭代器，可以用for访问数组每一个元素
print("flat:")
print(data.flat)
print()

for i in data.flat:
    print(i)
print()


#ndarray.flatten(order=’C’):将数组的副本转换为1-D的迭代器，并返回.
#C’：C-style，行序优先
#‘F’：Fortran-style，列序优先
#‘A’：如果a是内存中连续的Fortran，则列序优先
#‘K’：按照元素在内存出现的顺序进行排序 
#默认为’C’
print(data.flatten(order="C"))  #行序优先
print()
print(data.flatten(order="F"))  #列序优先
print()
print(data.flatten(order="A"))  #如果a是内存中连续的Fortran，则列序优先
print()

print(data.flatten(order="K"))  #按照元素在内存出现的顺序进行排序
print()


