# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年10月06日
"""
'''对图片的更改'''

from PIL import Image, ImageFilter

img = Image.open('./小猫.jpg')
img.show()
print(img.size)
print(img.format)
w, h = img.size

img.thumbnail((w // 2, h // 2))  # 缩放
img.save('thumbnail.jpg', 'JPEG')

# img.transpose().save                               #旋转并保存

img.filter(ImageFilter.DETAIL).save('detail.jpg')  # 滤镜

img2 = Image.new("RGBA", (500, 500), (255, 255, 0))
img2.save("Background.png", "PNG")
img2.paste(img, (50, 50))  # 将图片img粘贴至img2的指定位置
img2.save("NewCat.png")
