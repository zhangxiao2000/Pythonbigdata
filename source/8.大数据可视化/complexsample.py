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
marker=[str(x)+'年' for x in year]

fig,ax1=plt.subplots()

ax1.bar(year,population,width=0.5,label="出生人口(万人)")
for x, y in zip(year, population):
        plt.text(x, y, str(y), ha='center', va='bottom', fontsize=10.5)
ax1.set_ylim([33.00,44.00])
ax1.set_yticks(range(33,44))
ax1.hlines(range(34,44),2010,2018,linestyle="--",linewidth=0.5)
ax1.annotate("2016.1.1\n开放二胎",xy=(2015.8,40.46),xytext=(2013,41),arrowprops=dict(facecolor='black', shrink=0.05))
ax1.legend(loc=1)

ax2=ax1.twinx()
ax2.plot(year,growth,"r",label="出生率(%)")
for x, y in zip(year, growth):
        plt.text(x+0.5, y-0.1, str(y), ha='center', va='bottom', fontsize=10.5)
ax2.set_ylim([9.00,12])
ax2.legend(loc=2)

plt.xticks(year,marker)
plt.title("2010-2018年陕西省出生率及出生人口")
plt.show()