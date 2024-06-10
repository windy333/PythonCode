import pandas as pd
import numpy as np

# data = pd.read_csv(r'D:\Python\chengji.csv') #读取数据data，下面是数据框架，可以用数据直接建立

data = pd.DataFrame([['ding', 'female', 77, 80, 95, 91.0], ['yan', 'female', 83, 90, 93, 90.0],
                     ['feng', 'female', 85, 90, 92, 91.0], ['wang', 'male', 86, 80, 86, 91.0],
                     ['zhang', 'male', 76, 90, 90, 92.0], ['lu', 'female', 69, 90, 83, 92.0],
                     ['meng', 'male', 79, 90, 86, ], ['fei', 'female', 73, 80, 85, 89.0],
                     ['han', 'male', 80, 80, 93, 88.0]],
                    columns=['name', 'sex', 'C', 'DataBase', 'python', 'Java'])

'''
    name     sex   C  DataBase  python  Java
0   ding  female  77        80      95  91.0
1    yan  female  83        90      93  90.0
2   feng  female  85        90      92  91.0
3   wang    male  86        80      86  91.0
4  zhang    male  76        90      90  92.0
5     lu  female  69        90      83  92.0
6   meng    male  79        90      86   NaN
7    fei  female  73        80      85  89.0
8    han    male  80        80      93  88.0
'''

# 基础语法
data_statistics = data.describe().T  # 产生多个列的汇总统计，T 表示转置
data_statistics['null'] = len(data) - data_statistics['count']  # 统计空值记录
data_max_min = data_statistics[['max', 'min']]  # 获取'max'，'min'两列的内容
data[(data['oracle'] > 85) & (data['Java'] > 90)]  # 选取 oracle 成绩大于 85 且 Java 成绩大于 90 的学生
data.sort_values(['C', 'Java'], ascending=True)  # 按'C'、'Java'进行升序排列
data.groupby('sex').size()  # 按'sex'列分组
data.groupby('sex').count()  # 按'sex'列分组
data.groupby('sex').agg({'C': np.sum})  # 按'sex'列分组并对'C'列求和
data.groupby('sex').agg({'C': np.max})  # 按'sex'列分组并对'C'列取最大值

# 应用 map 函数
sex_mapping = {'female': 1, 'male': 2}
data['sex'] = data['sex'].map(sex_mapping)

# 应用 apply 函数
data['C'] = data['C'].apply(lambda x: x + 10 if x >= 85 else x)
df = data.dropna()  # 删除含有缺失值的行
df1 = data.fillna(0)  # 用 0 填补所有缺失值
df2 = data.fillna(method='ffill')  # 使用前一个观察值填充缺失值
df3 = data.fillna({'Java': int(data['Java'].mean())})  # 使用均值填充指定列的缺失值

# 数据分箱（离散化）
bins = [60, 70, 80, 90, 100]  # 分箱的边界
cats = pd.cut(list(data['C']), bins)  # 使用 cut 函数进行数据分箱
cats  # 显示分箱结果
cats.codes  # 获取分箱编码
cats.categories  # 返回分箱便捷索引
pd.value_counts(cats)  # 统计箱中元素的个数

# 进行带标签的分箱
group_names = ['pass', 'medium', 'good', 'excellent']
cats1 = pd.cut(list(data['C']), bins, labels=group_names)
cats1  # 查看带标签的分箱结果
cats1.get_values()
