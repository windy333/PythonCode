# 多变量房价预测问题

import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv("../data/data1.csv",names=["square","bedrooms","price"])
df1.head()

# 绘制3D散点图
fig = plt.figure()
# 创建一个Axes3D object
ax = plt.axes(projection="3d")
# 设置三个坐标的名称
ax.set_xlabel("square")
ax.set_ylabel("bedrooms")
ax.set_zlabel("price")
# 绘制3D散点图
ax.scatter3D(df1["square"],df1["bedrooms"],df1["price"],c=df1["price"],cmap="Greens")
plt.show()


# 数据归一化处理
# 然而房屋面积和卧室数量这两个变量（特征）在数值上差了1000倍。
# 在这种情况下，通常先进行特征缩放，再开始训练，可以加速模型收敛。

# 定义归一化函数
def normalize_feature(df):
    return df.apply(lambda column:(column-column.mean()) / column.std())

# 重新查看数据
df = normalize_feature(df1)
df.head()

# 重新展示数据
ax = plt.axes(projection="3d")
ax.set_xlabel("square")
ax.set_ylabel("bedrooms")
ax.set_zlabel("price")
ax.scatter3D(df["square"],df["bedrooms"],df["price"],c=df["price"],cmap="Reds")
plt.show()