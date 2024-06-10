import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

# 读取数据
df = pd.read_csv('data3.csv')

# 设置中文字体，解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 构建顾客标签

# 1. 总消费金额
df['TotalAmount'] = df['Quantity'] * df['Price']
customer_total_amount = df.groupby('CustomerID')['TotalAmount'].sum()
# 2. 平均订单金额
customer_avg_order_amount = df.groupby('CustomerID')['TotalAmount'].mean()
# 3. 购买频率（订单次数）
customer_order_count = df.groupby('CustomerID')['EventID'].count()
# 4. 最常购买的商品
customer_favorite_product = df.groupby(['CustomerID', 'Product'])['Quantity'].sum().reset_index()
customer_favorite_product = customer_favorite_product.loc[customer_favorite_product.groupby('CustomerID')['Quantity'].idxmax()]

# 合并标签数据
customer_profile = pd.DataFrame({
    'TotalAmount': customer_total_amount,
    'AvgOrderAmount': customer_avg_order_amount,
    'OrderCount': customer_order_count
}).reset_index()

customer_profile = customer_profile.merge(customer_favorite_product[['CustomerID', 'Product']], on='CustomerID')
customer_profile.rename(columns={'Product': 'FavoriteProduct'}, inplace=True)

# 创建标签
def create_labels(row):
    if (row['TotalAmount'] >= customer_profile['TotalAmount'].quantile(0.8) and
        row['AvgOrderAmount'] >= customer_profile['AvgOrderAmount'].quantile(0.5) and
        row['OrderCount'] >= customer_profile['OrderCount'].quantile(0.6)):
        return 'High Value'
    elif (row['TotalAmount'] <= customer_profile['TotalAmount'].quantile(0.2) and
          row['AvgOrderAmount'] <= customer_profile['AvgOrderAmount'].quantile(0.5) and
          row['OrderCount'] <= customer_profile['OrderCount'].quantile(0.4)):
        return 'Low Value'
    else:
        return 'Middle Value'
customer_profile['CustomerValue'] = customer_profile.apply(create_labels, axis=1)

print(customer_profile.head()) # 查看前5行数据

# 可视化顾客画像
plt.figure(figsize=(12, 6))
sns.countplot(data=customer_profile, x='CustomerValue', palette='viridis')
plt.title('不同价值客户数量')
plt.xlabel('客户价值')
plt.ylabel('数量')
plt.show()

# 1. 总消费金额分布
plt.figure(figsize=(12, 6))
sns.histplot(customer_profile['TotalAmount'], bins=50, kde=True, color='blue')
plt.title('客户总消费金额频率')
plt.xlabel('总消费金额')
plt.ylabel('频率')
plt.show()

# 2. 平均订单金额分布
plt.figure(figsize=(12, 6))
sns.histplot(customer_profile['AvgOrderAmount'], bins=50, kde=True, color='green')
plt.title('客户平均消费额频率')
plt.xlabel('平均消费额')
plt.ylabel('频率')
plt.show()

# 3. 订单次数分布
plt.figure(figsize=(12, 6))
sns.histplot(customer_profile['OrderCount'], bins=50, kde=True, color='red')
plt.title('客户订单次数频率')
plt.xlabel('订单数')
plt.ylabel('频率')
plt.show()

# 导出数据到CSV文件
#customer_profile.to_csv('customer_value.csv', index=False)

