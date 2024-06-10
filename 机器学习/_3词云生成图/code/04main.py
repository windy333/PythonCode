# _*_ coding:utf-8 _*_
# 使用蒙版
from wordcloud import  WordCloud
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba


text = open('../source/xyj.txt',encoding='utf-8').read()

# 中文分词
text = ''.join(jieba.cut(text))
print(text[:100])

# 生成对象
mask = np.array(Image.open("../source/black_mask.png"))
wc = WordCloud(mask=mask,font_path='Hiragino.ttf', width=800, height=600, mode='RGBA', background_color=None).generate(text)

# 显示词云
plt.imshow(wc,interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存到文件
wc.to_file("../create_images/wordcloud4.png")