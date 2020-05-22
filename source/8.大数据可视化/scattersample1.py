#encoding=utf-8
'''
Created on 2019年8月15日

@author: zhangxiao
'''

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

height=[152,158,167,172,162,166,180,177,172,172,156,164]
weight=[51,46,55,60,55,56,65,66,68,60,56,55]

plt.scatter(height,weight)
plt.xlabel("身高(cm)")
plt.ylabel("体重(kg)")
plt.title("女生身高体重对应关系")

plt.show()
