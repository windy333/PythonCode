# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年12月28日
"""

import pandas as pd
import numpy as np

data1 = pd.Series([10, 20, 30], index=['a', 'b', 'c'])

# 访问Series对象中的元素
print(data1['a'])  # 输出 10

# 根据条件筛选数据
print(data1[data1 > 10])

# 修改Series对象中的元素
data1['c'] = 100  # 将索引为'c'的元素修改为35
print(data1)

# Series对象进行数学运算
data1 = data1 * 2
print(data1)

'''
a     20
b     40
c    200
dtype: int64
'''

s = pd.Series([1, 3, 5], index=['a', 'b', 'c'])
# shape 属性获取 Series 对象的形状
print(s.shape)

# dtype 属性获取 Series
print(s.dtype)

# values 属性获取 Series 对象的数据数组
s.values  # array([1, 3, 5], dtype=int64)

# index 属性获取 Series 对象的数据数组的索引
s.index  # Index(['a', 'b', 'c'], dtype='object')

# Series 对象本身及索引的 name 属性
s.name = 'data'  # 为 Series 对象 s 命名'data'
s.index.name = 'idx'

'''
idx
a    1
b    3
c    5
Name: data, dtype: int
'''

# Series 对象中数据的修改
s['Python'] = 5

# 通过索引和切片查看 Series 对象的数据
s = pd.Series(data=[1, 2, 3], index=['Java', 'C', 'Python'])
s['C']  # 2
s[1]  # 2

# 通过截取（切片）的方式读取多个元素。
s[0:2]
'''
Java 1
C 2
63
dtype: int64
'''

# Series对象运算
s + 2
s * 2

#  函数运算
s1 = pd.Series([2, 4, 6], index=["a", "b", "c"])
np.sqrt(s1)  # 计算各数据的平方根
np.square(s)  # 计算各数据的平方

s2 = pd.Series([2, 4, 6, 8, 2, 4], index=["a", "b", "c", "d", 'e', 'f'])
s2.unique()  # 返回 s1 包含的不同元素   array([2, 4, 6, 8], dtype=int64)
s2.count()  # 返回 s1 包含的元素个数    6
s2.divide(2)  # 返回 s1 除以 2 的结果
s2.isin([2, 4])  # 判断给定的一列数据[2,4]是否在 s2 中
'''
a True
b True
c False
d False
e True
f True
dtype: bool
'''

s2.drop(labels=['a', 'c', 'f'])  # 删除索引为'a', 'c'，'f'元素，s2不变
'''
b 4
d 8
e 2
dtype: int64
从返回结果可以看出：将剩下的元素作为 Series 对象返回
'''

# Series 对象之间的运算
s1 + s2  # 相同索引值的元素相加,这里重新更新了一次s1和s2
'''
a     4.0
b     8.0
c    12.0
d     NaN
e     NaN
f     NaN
dtype: float64
'''
