import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# 读取数据
df = pd.read_csv('data.csv')

# 数据预处理
df.dropna(inplace=True) #删除包含缺失值的行
df.drop_duplicates(inplace=True) #删除数据中完全的重复行
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %H:%M', errors='coerce') #转换日期列，处理非法日期
# df = df.dropna(subset=['Date']) #去除转换日期失败的行
df = df[(df['Quantity'] > 0)]  #删除Quantity列值为负数和0的行

# 保存预处理后的数据为data3.csv
# df.to_csv('data3.csv', index=False)

# 设置中文字体，解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 最畅销的商品前10名
top_products = df.groupby('Product')['Quantity'].sum().sort_values(ascending=False).head(10)
print("最畅销的商品前10名：")
print(top_products)
print("\n")

# 购买商品总数最多的顾客前10名
top_customers = df.groupby('CustomerID')['Quantity'].sum().sort_values(ascending=False).head(10)
print("购买商品总数最多的顾客前10名：")
print(top_customers)
print("\n")

# 购买商品总数最多的国家前10名
top_countries = df.groupby('Country')['Quantity'].sum().sort_values(ascending=False).head(10)
print("购买商品总数最多的国家前10名：")
print(top_countries)
print("\n")

# 购买商品的时间段分析
df['Hour'] = df['Date'].dt.hour
time_distribution = df.groupby('Hour')['Quantity'].sum()
print("购买商品的时间段分布：")
print(time_distribution)
print("\n")

# 商品价格的分布分析
price_distribution = df['Price']
print("商品价格分布：")
print(price_distribution.describe())
print("\n")
prices = df['Price']
price_counts = prices.value_counts().sort_index()

# 数据可视化
# 最畅销的商品前10名图表
plt.figure(figsize=(12, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title('最畅销商品TOP10')
plt.xlabel('销售数量')
plt.ylabel('')
plt.subplots_adjust(left=0.22)
plt.show()

# 购买商品总数最多的顾客前10名图表
plt.figure(figsize=(10, 6))
sns.barplot(x=top_customers.index, y=top_customers.values, palette='viridis')
plt.title('购买商品总数顾客TOP10')
plt.xlabel('顾客ID')
plt.ylabel('购买数量')
plt.show()


# 购买商品总数最多的国家前10名图表
plt.figure(figsize=(12, 6))
sns.barplot(x=top_countries.values, y=top_countries.index, palette='viridis')
plt.title('购买商品总数的国家TOP10')
plt.xlabel('购买数量（百万）')
plt.ylabel('国家')
plt.show()

# 购买商品的时间段分布图表
plt.figure(figsize=(12, 6))
sns.lineplot(x=time_distribution.index, y=time_distribution.values, marker='o')
plt.title('购买商品时间段分布图')
plt.xlabel('时间')
plt.ylabel('购买数量')
plt.show()

# 价格频率图
plt.figure(figsize=(12, 6))
sns.lineplot(x=price_counts.index, y=price_counts.values, marker='o')
plt.title('价格频率图')
plt.xlabel('价格')
plt.ylabel('数量频率')
plt.show()



