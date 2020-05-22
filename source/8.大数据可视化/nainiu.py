#encoding=utf-8
'''
Created on 2019年8月15日

@author: zhangxiao
'''

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

chanliang=[20,7.5,17,25,16,18]
pinzhong=['A','B','C','D','E','F']


plt.subplot(2,2,1)
 
plt.pie(chanliang,labels=pinzhong,autopct='%1.1f%%',shadow=False,startangle=150)
plt.axis("equal")
plt.title("饼图")
 
plt.subplot(2,2,2)
plt.plot(chanliang)
#plt.xlabel("牛的品种")
plt.ylabel("平均产奶量(升)")
plt.grid()
plt.xticks(range(6),pinzhong)
plt.title("折线图 ")
 
 
plt.subplot(2,2,3)
plt.bar(range(6),chanliang)
plt.xlabel("牛的品种")
plt.ylabel("平均产奶量(升)")
plt.xticks(range(6),pinzhong)
plt.title("直方图1 ")
 
plt.subplot(2,2,4)
plt.bar(range(6),chanliang)
plt.ylim(5,27)
plt.xlabel("牛的品种")
plt.ylabel("平均产奶量(升)")
plt.xticks(range(6),pinzhong)
plt.title("直方图2")
 
plt.show()