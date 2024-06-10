# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年10月11日
"""
# 绘制饼图
import matplotlib.pyplot as plt
import matplotlib

matplotlib.rcParams['font.family'] = 'Fangsong'
matplotlib.rcParams['font.size'] = '12'
plt.figure('cxk', (7, 7))
labels = ['六分水', '三分田', '一分田']
sizes = [6, 3, 1]
colors = ['blue', 'yellowgreen', 'lightskyblue']
explode = [0.05, 0, 0]
plt.pie(sizes, explode=explode, labels=labels, colors=colors, labeldistance=1.1, autopct='%4.2f%%', shadow=
True, startangle=90, pctdistance=0.5)
plt.legend(loc='best')

plt.show()
