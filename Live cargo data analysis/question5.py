import pandas as pd
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 读取数据
df = pd.read_csv('data.csv')

# 数据预处理
df.dropna(inplace=True) # 删除包含缺失值的行
df.drop_duplicates(inplace=True) # 删除数据中完全的重复行
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y %H:%M', errors='coerce') # 转换日期列，处理非法日期
df = df[(df['Quantity'] > 0)]  # 删除Quantity列值为负数和0的行

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

# 计算每个群体的客户数量
segment_counts = rfm['Segment'].value_counts().reset_index()
segment_counts.columns = ['Segment', 'Count']

# 代金券设计
voucher_design = {
    'High Value': 100,  # 高价值客户，代金券100元
    'Low Value': 10,    # 低价值客户，代金券10元
    'Recent': 50,       # 最近有购买行为的客户，代金券50元
    'Frequent': 70,     # 频繁购买的客户，代金券70元
    'Other': 15         # 其他客户（中等价值），代金券15元
}

# 合并客户数量数据
segment_counts['VoucherAmount'] = segment_counts['Segment'].map(voucher_design)

# 总投放金额
total_amount = 1000000  # 100万元

# 每个节日投放金额
amount_per_event = total_amount / 2  # 50万元

# 计算每个群体在整体客户中的比例
segment_counts['Proportion'] = segment_counts['Count'] / segment_counts['Count'].sum()

# 根据比例分配总投放金额
segment_counts['AllocatedAmount'] = segment_counts['Proportion'] * amount_per_event

# 计算每种类型优惠券的投放数量
segment_counts['VoucherCount'] = segment_counts['AllocatedAmount'] / segment_counts['VoucherAmount']

# 打印结果
print("各群体优惠券投放数量和金额分配：")
print(segment_counts[['Segment', 'Count', 'Proportion', 'AllocatedAmount', 'VoucherAmount', 'VoucherCount']])

# 可视化各群体优惠券投放数量
plt.figure(figsize=(12, 6))
sns.barplot(data=segment_counts, x='Segment', y='VoucherCount', palette='viridis')
plt.title('各群体优惠券投放数量')
plt.xlabel('客户群体')
plt.ylabel('优惠券数量')
plt.show()

# 可视化各群体优惠券分配金额
plt.figure(figsize=(12, 6))
sns.barplot(data=segment_counts, x='Segment', y='AllocatedAmount', palette='viridis')
plt.title('各群体优惠券分配金额')
plt.xlabel('客户群体')
plt.ylabel('分配金额（元）')
plt.show()
