#encoding=utf-8
'''
Created on 2019-8-14

@author: zhangxiao
'''

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

labels = ['衣服','饮食','房贷','交通','育儿','娱乐','其他']
sizes = [5,15,50,5,10,5,10]
explode = (0,0,0.1,0,0,0,0)
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)
plt.title("饼图示例-2019年上半年家庭支出")
plt.axis('equal')#将饼图显示为正圆形
plt.show()  
