# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年10月11日
"""
# 构建笛卡尔坐标系
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
y = np.sin(2 * x) / x
plt.plot(x, y, 'k')
plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi], [r'$-2\pi$', r'$-\pi$', r'$0$', r'$+\pi$', r'$2\pi$'])
plt.yticks([-1, 0, 1, 2, 3])
ax = plt.gca()
ax.spines['right'].set_color('none')  # 设置上和右边框
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')  # 将底边框设置为x轴
ax.spines['bottom'].set_position(('data', 0))  # 移动底边框

ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.show()
