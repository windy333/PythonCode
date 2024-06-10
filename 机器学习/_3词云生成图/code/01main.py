# _*_ coding:utf-8 _*_

# 进行英文词云生成
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 打开文本
text = open('../source/constitution.txt').read()
# 生成对象
wc = WordCloud().generate(text)

# 显示词云
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存到文件
wc.to_file('../create_images//wordcloud1.png')



