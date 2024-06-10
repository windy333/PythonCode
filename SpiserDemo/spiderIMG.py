import os
import random
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 能够爬取绝大部分图片，前提是图片的src在img标签内，可以自行改get_img_url()方法获取具体的src种类
# 或者你可以直接输入单张图片的真实URL,不支持API网址调用返回JSON格式
# 无法解决JavaScript加载的动态资源，反爬虫的网站无法爬取也不建议爬取

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.0.0 Safari/537.36',
]

def get_userAgent():
    return random.choice(USER_AGENTS)

# data-src针对视觉中国，无法获取原高清图片且仅是预览图(带水印)
def get_img_url(img_tag):
    return img_tag.get("src") or img_tag.get("data-src") or img_tag.get("data-original") or img_tag.get("file")

def download_images(url):
    headers = {'User-Agent': get_userAgent()}
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(response.text, "html.parser")
    save_dir = "IMG"
    os.makedirs(save_dir, exist_ok=True)

    #寻找img标签，并设置URL集合防止下载重复图片(仅链接不同)
    img_tags = soup.find_all("img")
    downloaded_urls = set()
    count = 1

    #遍历img标签
    for img_tag in img_tags:
        # 尝试获取图片链接
        img_url = get_img_url(img_tag)
        # 跳过SVG图像数据URL
        if not img_url or img_url.startswith('data:image/svg+xml'):
            continue
        #将相对链接转化为绝对链接
        img_url = urljoin(url, img_url)

        #防止下载重复的链接图片
        if img_url in downloaded_urls:
            continue

        try:
            # 根据内容类型确定文件扩展名
            img_data = requests.get(img_url, headers=headers).content

            #这里会下载一些指向html的图片，无用可以删除
            content_type = requests.head(img_url, headers=headers).headers.get('content-type', 'image/jpeg')
            # 只取content-type中'/'之后，';'之前的部分作为文件扩展名
            if '/' in content_type:
                ext = content_type.split('/')[-1]
                if ';' in ext:
                    ext = ext.split(';')[0]
            else:
                ext = 'jpg'  # 如果content-type头部不包含'/', 默认使用'.jpg'扩展名

            img_name = f"{count}.{ext}"
            img_path = os.path.join(save_dir, img_name)

            with open(img_path, "wb") as f:
                f.write(img_data)

            downloaded_urls.add(img_url)
            count += 1
            print(img_url)
            print(f"下载图片 {img_name} 完成")

        except requests.exceptions.RequestException as e:
            print(f"下载图片失败 - {e}")

    print("所有图片下载完成")

if __name__ == "__main__":
    inputUrl = input("请输入要下载图片的网站URL: ")
    download_images(inputUrl)
