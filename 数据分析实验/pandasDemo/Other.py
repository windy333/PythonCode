'''数据聚合和分组'''

import numpy as np
import pandas as pd
from numpy import random

'''数据分组'''
# （1）按列分组
df = pd.DataFrame({'key1': ['a', 'a', 'b', 'b', 'a'], 'key2': ['one', 'two', 'one', 'two', 'one'],
                   'data1': random.randint(1, 6, 5), 'data2': random.randint(1, 6, 5)})

group = df.groupby('key1')  # 按'key1'进行分组
group.groups  # 如下所示，每个分组都指明了它所包含的行。
# >>{'a': Int64Index([0, 1, 4], dtype='int64'), 'b': Int64Index([2, 3],dtype='int64')}


for x in group:  # 显示分组内容
    print(x)
'''
('a',   key1 key2  data1  data2
0       a     one      4      1
1       a     two      2      4
4       a     one      2      5)
('b',   key1 key2  data1  data2
2       b     one      3      2
3       b     two      2      1)
'''

# 既可依据单个列名'key1'进行为分组，也可依据多个列名进行分组。
group1 = df.groupby(['key1', 'key2'])  # 依据两个列名['key1','key2']进行分组
for x in group1:  # 对数据进行迭代输出
    print(x)
'''
(('a', 'one'),   key1 key2  data1  data2
0    a  one      3      5
4    a  one      5      3)
(('a', 'two'),   key1 key2  data1  data2
1    a  two      1      2)
(('b', 'one'),   key1 key2  data1  data2
2    b  one      5      1)
(('b', 'two'),   key1 key2  data1  data2
3    b  two      5      3)
'''

# （2）通过字典进行分组
people = pd.DataFrame(np.random.rand(5, 5), columns=['a', 'b', 'c', 'd', 'e'],
                      index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])

# 对列名建立字典
mapping = {'a': 'red', 'b': 'red', 'c': 'blue', 'd': 'blue', 'e': 'red'}
by_columns = people.groupby(mapping, axis=1)  # 依据 mapping 进行分组
by_columns.mean()  # 对每行的各个分组求平均值
'''
('blue',       c         d
Joe     0.513818  0.751207
Steve   0.605439  0.714830
Wes     0.036449  0.620290
Jim     0.087106  0.270898
Travis  0.977604  0.600654)
'''

# 显示分组内容
for x in by_columns:
    print(x)
'''
('red',       a         b         e
Joe     0.559900  0.408660  0.250101
Steve   0.316330  0.136214  0.304853
Wes     0.620797  0.766599  0.279603
Jim     0.262222  0.465411  0.666505
Travis  0.754793  0.091721  0.444354)
'''

'''数据聚合'''

# (1)在 DataFrame 对象的行或列上执行聚合操作
df3 = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9], [np.nan, np.nan, np.nan]],
                   columns=['A', 'B', 'C'])

df3.agg(['sum', 'min'])  # 在 df 的各列上执行'sum'和'min'聚合操作
df3.agg({'A': ['sum', 'min'], 'B': ['min', 'max']})  # 在不同列上执行不同的聚合操作
df3.agg("mean", axis=1)  # 在行上执行"mean"操作

dict_data = {'key1': ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd'],
             'key2': ['one', 'two', 'three', 'one', 'two', 'three', 'one', 'two'],
             'data1': np.random.randint(1, 10, 8), 'data2': np.random.randint(1, 10, 8)}
df4 = pd.DataFrame(dict_data)

# (2)_在 df.groupby()所生成的分组上应用 agg()
group5 = df4.groupby('key1')
group5.agg('mean')

# (3)应用 apply()函数执行聚合操作
df4.groupby('key2').apply(sum)
