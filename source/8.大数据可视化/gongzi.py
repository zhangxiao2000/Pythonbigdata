#encoding=utf-8
'''
Created on 2019年8月15日

@author: zhangxiao
'''
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

gongzi=[200,220,250]
gudong=[100,120,150]
year=[2016,2017,2018]

plt.figure(figsize=(15, 5))

plt.subplot(1,3,1)
plt.plot(range(3),gongzi,label="职工工资")
plt.plot(range(3),gudong,label="股东利润")
plt.xlabel("年份")
plt.ylabel("工资总额与利润（万元）")
plt.ylim(0,300)
plt.xticks(range(3),year)
plt.legend()
plt.title("股东:总额同步增长")

plt.subplot(1,3,2)
plt.plot(range(3),[x/200*100 for x in gongzi],label="职工工资增长幅度")
plt.plot(range(3),[x/100*100 for x in gudong],label="股东利润增长")
plt.xlabel("年份")
plt.ylabel("增长情况（%）")
plt.ylim(100,160)
plt.xticks(range(3),year)
plt.legend()
plt.title("工会:增长幅度有差异")

plt.subplot(1,3,3)
plt.plot(range(3),[x/100 for x in gongzi],label="人均职工工资")
plt.plot(range(3),[x/5 for x in gudong],label="人均股东利润")
plt.xlabel("年份")
plt.ylabel("人均工资总额与利润（万元）")
plt.ylim(0,40)
plt.xticks(range(3),year)
plt.legend()
plt.title("工人:人均工资几乎没变化")

plt.show()