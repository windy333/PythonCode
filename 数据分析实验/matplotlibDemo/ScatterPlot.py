# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年10月11日
"""

# 绘制散点图
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family'] = 'Fangsong'
matplotlib.rcParams['font.size'] = '13'
x = [0.13, 0.22, 0.39, 0.59, 0.68, 0.74, 0.93]
y = [0.75, 0.34, 0.44, 0.52, 0.80, 0.25, 0.55]
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.set_title('散点图')
ax1.scatter(x, y, c='b', marker='o')  # scatter(x,y,s=20,c=None,marker='o',alpha=None,edgecolors=None)
plt.show()  # s表示散点图大小，默认20；c表示颜色；marker指定散点形状

# 绘制散点图，每个点展示不同的大小
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N)) ** 2
colors = np.random.rand(N)
plt.scatter(x, y, s=area, c=colors)
plt.show()
