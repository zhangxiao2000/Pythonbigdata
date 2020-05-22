#encoding=utf-8
'''
Created on 2019年8月14日

@author: zhangxiao
'''

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

x=range(31)
huoqi=[1.0035**(i+1) for i in x]   #活期利率0.35%
dingqi1=[1.015**(i+1) for i in x]  #一年定期利率1.5%
dingqi3=[1.0275**(i+1) for i in x] #活期利率2.75%

plt.plot(huoqi,color='r',linewidth=5,linestyle=':',label='活期')#color指定线条颜色，labeL标签内容
plt.plot(dingqi1,color='g',linewidth=2,linestyle='--',label='一年定期')#linewidth指定线条粗细
plt.plot(dingqi3,color='b',linewidth=0.5,linestyle='-.',label='三年定期')#linestyle指定线形为点
plt.legend(loc=2)#标签展示位置，数字代表标签具位置
plt.axis([0,30,1,2.5])
plt.xlabel('时间')
plt.ylabel('现金价值(万元)')
plt.title('折线图示例-利率的时间价值')

plt.show()