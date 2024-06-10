# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年10月11日
"""

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 1.绘制直方图
pop = np.random.randint(0, 100, 100)
plt.hist(pop, bins=20, label='random')
# 参考 hist() 文档
# orientation='horizontal' 设置直方图的方向
plt.show()

# 2.垂直方向条形图
xvalues = [0, 1, 2, 3]
GDP = [13980.57, 18978.7, 9891.5, 3333.4]
matplotlib.rcParams['font.family'] = 'Fangsong'  # 设置图标的中文显示方式，否则中文标记时会乱码,以下绘图共用这段代码
matplotlib.rcParams['font.size'] = 13
plt.bar(range(4), GDP, align='center', color='black')  # plt.bar()
plt.ylabel("GDP")
plt.title("GDP of city")
plt.xticks(range(4), ['北京', '上海', '广州', '深圳'])
plt.ylim([2000, 20000])
for x, y in enumerate(GDP):
    plt.text(x, y + 100, '%s' % round(y, 1), ha='center')
plt.show()

# 3.水平方向条形图
GDP = [20, 30, 10, 25]
label = ['北京', '上海', '广州', '深圳']
index = np.arange(len(GDP))
plt.barh(index, GDP, color='black')  # plt.barh()
plt.yticks(index, label)
plt.xlabel('GDP')
plt.title('GDP of city')
plt.grid(axis='x')  # 添加垂直网格线
plt.show()

# 4.多序列垂直方向条形图
index = np.arange(5)
label = ['类别1', '类别2', '类别3', '类别4', '类别5']
values1 = [2, 8, 4, 6, 9]
values2 = [6, 7, 3.5, 5, 8]
values3 = [5, 6, 7, 6, 2]
bw = 0.3  # 设置条形的宽度
plt.axis([0, 5.2, 0, 10])
plt.bar(index + bw, values1, bw, color='y')  # index+bw表示x轴的起始位置
plt.bar(index + 2 * bw, values2, bw, color='b')
plt.bar(index + 3 * bw, values3, bw, color='r')
plt.xticks(index + 2 * bw, label)
plt.title('多序列垂直方向条形图')
plt.show()

# 5.多序列水平方向条形图
plt.axis([0, 10, 0, 5.2])
plt.barh(index + bw, values1, bw, color='y')
plt.barh(index + 2 * bw, values2, bw, color='b')
plt.barh(index + 3 * bw, values3, bw, color='r')
plt.yticks(index + bw * 2, label)
plt.title('多序列水平方向条形图')
plt.show()
