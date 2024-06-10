import pandas as pd
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 读取数据
df = pd.read_csv('data.csv')

# 数据预处理
df.dropna(inplace=True) #删除包含缺失值的行
df.drop_duplicates(inplace=True) #删除数据中完全的重复行
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %H:%M', errors='coerce') #转换日期列，处理非法日期
# df = df.dropna(subset=['Date']) #去除转换日期失败的行
df = df[(df['Quantity'] > 0)]  #删除Quantity列值为负数和0的行


# 删除无法解析的日期
df = df.dropna(subset=['Date'])

# 计算总消费金额
df['TotalAmount'] = df['Quantity'] * df['Price']

# 设定分析基准日期为数据集中最近的日期
latest_date = df['Date'].max() + dt.timedelta(days=1)

# 构建RFM特征
rfm = df.groupby('CustomerID').agg({
    'Date': lambda x: (latest_date - x.max()).days,
    'EventID': 'count',
    'TotalAmount': 'sum'
})

# 重命名列
rfm.rename(columns={
    'Date': 'Recency',
    'EventID': 'Frequency',
    'TotalAmount': 'Monetary'
}, inplace=True)

# 计算RFM打分
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=range(5, 0, -1))
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=range(1, 6))
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=range(1, 6))

# 计算RFM综合评分
rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)

# 客户细分
def rfm_segment(df):
    if df['R_Score'] in [4, 5] and df['F_Score'] in [4, 5] and df['M_Score'] in [4, 5]:
        return 'High Value'
    elif df['R_Score'] in [1, 2] and df['F_Score'] in [1, 2] and df['M_Score'] in [1, 2]:
        return 'Low Value'
    elif df['R_Score'] in [4, 5] and df['F_Score'] in [1, 2] and df['M_Score'] in [1, 2]:
        return 'Recent'
    elif df['R_Score'] in [1, 2] and df['F_Score'] in [4, 5] and df['M_Score'] in [4, 5]:
        return 'Frequent'
    else:
        return 'Other'

rfm['Segment'] = rfm.apply(rfm_segment, axis=1)

# 代金券设计
voucher_design = {
    'High Value': 100,  # 高价值客户，代金券100元
    'Low Value': 10,    # 低价值客户，代金券10元
    'Recent': 50,       # 最近有购买行为的客户，代金券50元
    'Frequent': 70,     # 频繁购买的客户，代金券70元
    'Other': 15         # 其他客户（中等价值），代金券15元
}

# 为每个客户分配代金券
rfm['Voucher'] = rfm['Segment'].map(voucher_design)


# 开始解决问题四
# 查看各RFM分段的描述性统计
print(rfm.groupby('Segment').agg({
    'Recency': ['mean', 'median', 'std'],
    'Frequency': ['mean', 'median', 'std'],
    'Monetary': ['mean', 'median', 'std']
}))

# 可视化各RFM分段的消费金额分布
plt.figure(figsize=(12, 6))
sns.boxplot(data=rfm, x='Segment', y='Monetary', palette='viridis')
plt.title('各RFM分段的消费金额分布')
plt.xlabel('RFM分段')
plt.ylabel('消费金额')
plt.show()

# 分析各RFM分段的客户数量和平均消费金额
rfm_analysis = rfm.groupby('Segment').agg({
    'Recency': 'count',
    'Monetary': 'mean'
}).rename(columns={'Recency': 'CustomerCount', 'Monetary': 'AvgMonetary'})

print(rfm_analysis)

# 可视化客户数量和平均消费金额
fig, ax1 = plt.subplots(figsize=(12, 6))

color = 'tab:blue'
ax1.set_xlabel('RFM分段')
ax1.set_ylabel('客户数量', color=color)
ax1.bar(rfm_analysis.index, rfm_analysis['CustomerCount'], color=color, alpha=0.6)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'tab:red'
ax2.set_ylabel('平均消费金额', color=color)
ax2.plot(rfm_analysis.index, rfm_analysis['AvgMonetary'], color=color, marker='o')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()
plt.title('各RFM分段的客户数量和平均消费金额')
plt.show()

# 回购率 = 回购客户数量 / 总客户数量
# 模拟回购数据
np.random.seed(42)
df['IsRepeatedPurchase'] = np.random.choice([0, 1], size=len(df), p=[0.7, 0.3])
repeat_purchase = df.groupby('CustomerID')['IsRepeatedPurchase'].max().reset_index()

rfm = rfm.reset_index().merge(repeat_purchase, on='CustomerID', how='left')
rfm['IsRepeatedPurchase'].fillna(0, inplace=True)

repeat_purchase_rate = rfm.groupby('Segment')['IsRepeatedPurchase'].mean()
print(repeat_purchase_rate)

# 可视化回购率
plt.figure(figsize=(12, 6))
sns.barplot(x=repeat_purchase_rate.index, y=repeat_purchase_rate.values, palette='viridis')
plt.title('各RFM分段的客户回购率')
plt.xlabel('RFM分段')
plt.ylabel('回购率')
plt.show()
