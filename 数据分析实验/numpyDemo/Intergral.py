# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年12月01日
"""

import sympy as sp

'''求解定积分，与前面Funtion里的求面积类似(利用了数值分析,微分)
    但是没有研究sympy库是怎么具体去实现求解的(通过符号计算的方法来求解定积分)'''
x = sp.symbols('x')
f = x ** 2
a = 0  # 下限
b = 1  # 上限

# 求解定积分
integral = sp.integrate(f, (x, a, b))

# 输出结果
print("定积分的符号表达式：", integral)
print("定积分的数值结果：", integral.evalf())

'''求解二元一次方程'''
from sympy import *

x = Symbol('x')
y = Symbol('y')
print(solve([6 * x + 70 * y - 230, 70 * x + 1286 * y - 1910], [x, y]))
