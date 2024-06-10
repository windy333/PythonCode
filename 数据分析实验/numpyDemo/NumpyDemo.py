# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年10月12日
"""
import numpy as np

# np.array(object,dtype=None)    object指定生成数组的数据序列，可以是列表，元组
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [2, 3, 5]])
c = np.array(((1, 2, 3), (3, 2, 3)))
d = np.array([(1, 2, 3), (2, 2, 3)])

a = np.ones(shape=(2, 3), dtype=complex)
b = np.zeros_like(c)
c = np.empty(shape=(3, 3), dtype=float)

A = np.arange(1, 10).reshape(3, 3)
B = np.arange(1, 100, 33)

# linspace()返回一个等差数列
# logspace()返回一个等比数列,base参数是幂的底数，默认10.0;base**start,base**stop
np.linspace(1, 10, 3, dtype=float)
np.logspace(1, 3, 3, base=2)

# 单位矩阵,eye为可变
np.eye(3, k=0, dtype=int)
np.identity(3, dtype=int)

np.full((2, 3), 10)
np.full_like(a, 6)

# ndarray对象的属性
# a.T:返回数组的转置
# a.size:返回数组元素的个数
# a.ndim:返回数组的维度
# a.shape:返回数组的型
# a.flat:返回数组的迭代器
