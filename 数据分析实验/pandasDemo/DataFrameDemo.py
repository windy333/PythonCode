# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年12月28日
"""
import pandas as pd
import numpy as np

'''DataFrame对象的创建'''
data = {'course': ['java', 'c', 'python'],
        'scores': [100, 90, 100],
        'grade': ['A', 'B', 'A']}
df1 = pd.DataFrame(data)

df2 = pd.DataFrame(data, columns=['course', 'scores', 'x'], index=['一', '二', '三'])
'''
df2=pd.DataFrame([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 
                 index=['一','二','三','四'],
                 columns=['A','B','C','D'])
'''

# 用字典对象创建
data3 = {"name": {'one': "Jack", 'two': "Mary", 'three': "John", 'four': "Alice"},
         "age": {'one': 10, 'two': 20, 'three': 30, 'four': 40},
         "weight": {'one': 30, 'two': 40, 'three': 50, 'four': 65}}
df3 = pd.DataFrame(data3)

# 用键值为 Series 的字典创建 DataFrame：
data4 = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
         'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df4 = pd.DataFrame(data4)

df = pd.DataFrame({'city': ['上海市', '北京市', '广州市', '深圳市'],
                   'GDP': [13908.57, 12406.8, 9891.48, 9709.02]}, columns=['city', 'GDP'])

'''一些操作'''
df.T  # 转置
df.index  # 查看行索引名
df.columns  # 查看行列引名
df.shape  # 查看 DataFrame 对象的形状
df.values  # 查看 DataFrame 对象的数据

# 获取 DataFrame 对象某列的内容
df['city']
df.GDP

# 获取行内容
df.ix[2]
df.ix[[2, 3]]
df.loc[1]

df.iloc[0:2, :2]  # 获取前 2 行、前 2 列的数据

df.size  # 返回 DataFrame 对象包含的元素个数  8个

# 对行重新索引，然后对列重新索引
df.ix[[3, 2, 1, 0], ['GDP', 'city']]
'''
      GDP  city
3 9709.02 深圳市
2 9891.48 广州市
1 12406.80 北京市
0 13908.57 上海市
'''

'''查看 DataFrame 对象中的元素'''
df['GDP'][1]
df[df.GDP > 10000]  # 指定条件筛选 DataFrame 对象的元素。

# 修改 DataFrame 对象中的元素
df.index.name = 'id'
df.columns.name = 'item'
'''
item  city       GDP
id                 
0     上海市  13908.57
1     北京市  12406.80
2     广州市   9891.48
3     深圳市   9709.02
'''

df['new'] = 10  # 添加新列，并将新列的所有元素都赋值为 10
df['new'] = [11, 12, 13, 14]  # 更新或者直接设置初始值

# 修改单个元素
df['GDP'][3] = 15000  # 会报警告

# 判断
df.isin(['Jack', 30])
df.isin(['上海市'])
'''
item   city    GDP
id                
0      True  False
1     False  False
2     False  False
3     False  False
'''

# 数据筛选
df.head(2)
df.tail(1)
df[2:4]  # 获取索引值为 2-3 的行

# 获取'GDP'列值大于 10000 的行
df[df['GDP'] > 10000]
df.query('GD> 10000')

'''数据预处理'''

# （1）重复行处理
df.duplicated(subset=None, keep='first')
df.index.duplicated(keep='last')  # 作用：根据行索引标记重复行
df.drop_duplicates(subset=None, keep='first', inplace=False)
# df.drop_duplicates('col1') #删除 df.duplicated('col1')标记的重复记录

# （2）缺失值处理
df.fillna('missing')  # 用字符串'missing'填充缺失值
df.fillna(method='ffill')  # ffill：用前一个非缺失值去填充该缺失值

# （3）删除指定的行或列

# （4）删除缺失值
df.dropna()  # 删除含有缺失值的行
df.dropna(how='all')  # 删除全为缺失值的行
df.dropna(thresh=2)  # 删除至少含有两个缺失值的行

df.dropna(subset=['GDP', 'city'])  # 删除时只在'GDP'和'city'列中查看缺失值

# 数据替换
df.replace(0, np.nan)  # 用 np.nan 替换 0
df.replace([0, 1, 2, 3], np.nan)  # 把 df 出现在列表中的元素用np.nan 替换
df.replace([1, 2, 3], [11, 22, 33])  # 1替换为11,2替换为22,3替换为33

'''两个 DataFrame 对象的连接'''

df11 = pd.DataFrame({'key1': ['k1', 'k1', 'k2', 'k3'], 'key2': ['k1', 'k2', 'k1', 'k2'],
                     'A': ['a1', 'a2', 'a3', 'a4'], 'B': ['b1', 'b2', 'b3', 'b4']})
df12 = pd.DataFrame({'key1': ['k1', 'k2', 'k2', 'k3'], 'key2': ['k1', 'k1', 'k1', 'k1'],
                     'C': ['c1', 'c2', 'c3', 'c4'], 'D': ['d1', 'd2', 'd3', 'd4']})

# 类似数据库的左右内外连接
# how 没指定，默认使用 inner，使用'key1', 'key2'作为键进行内连接
df11.merge(df12, on=['key1', 'key2'])  # 只保留两个表中公共部分的信息

# how='left'，只保留 df1 的所有数据
df11.merge(df12, how='left', on=['key1', 'key2'])

# how='right'，只保留 df2 的所有数据
df11.merge(df12, how='right', on=['key1', 'key2'])

# how='outer'，保留 df1 和 df2 的所有数据
df11.merge(df12, how='outer', on=['key1', 'key2'])

# how='inner'内连接，只保留两个表中公共部分的信息
pd.merge(df11, df12, left_on='lkey', right_on='rkey', how='inner')

# pd.merge(df1,df2,on='value') #没用公共部分，返回空 DataFrame对象

# sort='True'表示对合并后的 DataFrame 对象，根据合并关键字按字典顺序对行排序
pd.merge(df11, df12, left_on='lkey', right_on='rkey', how='outer', sort='True')

# ignore_index=True,忽略 df11、df12 的行索引，重新索引
pd.concat([df11, df12], ignore_index=True)

''' 运算 '''
# df1 + df2 作用：将 df1 和 df2 的行名和列名都相同的元素相加，其它位置的元素用NaN 填充
