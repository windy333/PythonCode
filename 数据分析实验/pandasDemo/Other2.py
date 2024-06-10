'''数据可视化'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 全局设置默认
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体为SimHei
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

data = {'Month': ['January', 'February', 'March', 'April', 'May'],
        'Sales': [200, 300, 400, 350, 500]}
df = pd.DataFrame(data)

# 画折线图
'''
#为Sales设置索引行Month
df.set_index('Month')['Sales'].plot(kind='line', figsize=[7, 5], legend=True, title='月销售额')
plt.show()
'''

# 画条形图
'''
df.set_index('Month')['Sales'].plot(kind='bar', figsize=[7, 5], legend=False, title='月销售额')
plt.show()
'''

# 画饼图
'''
df.set_index('Month')['Sales'].plot(kind='pie', figsize=[7, 5], legend=True, title='月销售额分布')
plt.show()
'''

# 画散点图
df1 = pd.DataFrame(np.random.rand(50, 2), columns=['A', 'B'])
area = np.pi * (15 * np.random.rand(50)) ** 2  # 设置散点的大小
colors = np.random.rand(50)  # 设置随机颜色

'''
#df1 = pd.DataFrame(np.random.rand(300,2), columns=['A', 'B'])
#df1.plot(kind='scatter', x='A', y='B')
plt.scatter(df1['A'], df1['B'], s=area, c=colors, alpha=0.5)
plt.title('散点图')
plt.show()
'''

# 画直方图
df2 = pd.DataFrame({
    'A': np.random.randn(100),
    'B': np.random.randn(100)
})

'''
df2.plot(kind='hist', alpha=0.5, figsize=[7, 5], title='直方图')
plt.show()
'''

# 画区域图
df3 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
'''
df3.plot(kind='area')  # 生成堆积图
plt.show()
df3.plot(kind ='area',stacked=False) #生成非堆积区域图
plt.show()
'''

# 画箱线图
'''
df4=pd.DataFrame({'a':np.random.randn(1000)+2,'b':np.random.randn(1000)+1,
                  'c':np.random.randn(1000),'d':np.random.randn(1000)-1}, columns=['a', 'b', 'c','d'])
df4.plot(kind="box",title='箱线图')
plt.show()
'''
