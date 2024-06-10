# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年10月11日
"""
# 在一个窗口创建多个子图
import matplotlib.pyplot as plt
import numpy as np

plt.figure(num='cxk', figsize=(8, 8))
x = np.arange(-5, 5, 0.1)
y1 = x ** 2
y2 = x
plt.subplot(221)
plt.plot(x, y1)
plt.subplot(222)
plt.plot(x, y2)

plt.show()
