#encoding=utf-8
'''
Created on 2019-11-11

@author: zhangxiao
'''

import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

data = {
'中国': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2500],
'美国': [1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100],
'英国': [1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],
"俄罗斯": [800, 1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900]
}
df = pd.DataFrame(data)
df.plot.box(title="各国消费对比")
plt.grid(linestyle="--", alpha=0.3)
plt.show()
