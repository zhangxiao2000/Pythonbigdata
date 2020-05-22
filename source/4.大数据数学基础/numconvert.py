#encoding=utf-8
'''
Created on 2019-8-1

@author: zhangxiao
'''
import numpy as np
#无损转换，拟转换的类型所占空间小于将转换的类型
#int8->int16->int32

a=np.int8(12)
b=np.int16(a)
c=np.int32(b)
print(a,b,c)

#有损转换，超出范围的数值会丢失
#300超过了int8的范围，300转换为16进制为0x12C,需要2个字节保存
#在转换为int16时没有问题，转为int8时高位的1丢失，变成了0x2C,即44
a=np.int32(300)
b=np.int16(a)
c=np.int8(b)
print(a,b,c)

#浮点数转换，拟转换的类型所占空间小于将转换的类型，但是精度会发生变化
#float16->float32->float64
a=np.float16(3.14159265357979)
b=np.float32(a)
c=np.float64(b)
print(a,b,c)

#浮点数转换，拟转换的类型所占空间小于将转换的类型，但是精度会发生变化
#float64->float32->float16
a=np.float64(3.14159265357979)
b=np.float32(a)
c=np.float16(b)
print(a,b,c)


