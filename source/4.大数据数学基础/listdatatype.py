#encoding=utf-8
'''
Created on 2019-8-1

@author: zhangxiao
'''

import numpy as np
datatypes=['int','int8','int16','int32','int64','uint8','uint16','uint32','uint64',
           'float','float16','float32','float64',
           'complex','complex64','complex128']


for x in datatypes:
    darray=np.arange(10,dtype=x)
    print("type:{}\t size:{} bytes".format(x,darray.dtype.itemsize))

