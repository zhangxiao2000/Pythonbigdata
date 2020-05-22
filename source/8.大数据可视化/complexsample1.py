#encoding=utf-8
'''
Created on 2019年8月31日

@author: zhangxiao
'''

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

#数据来自陕西省统计局
#http://tjj.shaanxi.gov.cn/126/111/19566.html
population=[36.34,36.45,37.93,37.62,38.18,38.22,40.46,42.48,41.08]
year=range(2010,2019)
growth=[9.73,9.75,10.12,10.01,10.13,10.1,10.64,11.11,10.67]

fig,ax1=plt.subplots()

ax1.bar(year,population,width=0.5,label="出生人口(万人)")
ax1.set_ylim([33.00,44.00])
ax1.set_yticks(range(33,44))

ax2=ax1.twinx()  #绘制y轴的次坐标轴
ax2.plot(year,growth,"r",label="出生率(%)")
ax2.set_ylim([9.00,11.5])

plt.show()