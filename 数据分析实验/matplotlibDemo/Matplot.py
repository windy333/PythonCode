# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年10月11日
"""
# 绘图测试
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
y1 = np.sin(2 * x) / x;
y2 = np.sin(3 * x) / x;
y3 = np.sin(4 * x) / x;
plt.plot(x, y1, 'k--')
plt.plot(x, y2, 'k--')
plt.plot(x, y3, 'y')
plt.title(r'多个序列生成的图形', fontname='Kaiti', fontsize=20)
plt.xlabel('横轴:时间', fontname='Kaiti', fontsize=20)
plt.ylabel('纵轴：振幅', fontname='Kaiti', fontsize=20)
# plt.annotate('y3=sin(4*x)/x',xy=(0,4.5),xytext=(1,4.25),arrowprops=dict(facecolor='black',shrink=1,width=0.1))
# 指定箭头的位置和信息
# plt.text(0,4.25,'y3')    #在指定位置添加文本
# plt.axis([-10,10,-1,4])  #限制x和y的范围
plt.grid(True)  # 添加网格线

plt.show()
