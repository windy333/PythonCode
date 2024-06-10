# 单变量房价预测问题

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(context="notebook",style="whitegrid",palette="dark")

# 查看q前5行数据
df0 = pd.read_csv("../data/data0.csv",names=["square","price"])
df0.head()

# seaborn.lmplot()方法专门用于用于线性关系的可视化，适用于回归模型
sns.lmplot(x="square", y="price", data=df0, height=6, aspect=1, fit_reg=True)
plt.show()
df0.info()