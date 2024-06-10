import os
import requests
import random
from lxml import etree
import re

# 爬取div标签中的图片，目前最大页数那里可能爬一些网站时会存在只爬一页的情况，默认缺省值设为1
# 图片存放在div标签的网站 https://pic.netbian.top/4kmeinv/index_2.html

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.0.0 Safari/537.36',
]

def get_user_agent():
    return random.choice(USER_AGENTS)

def create_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

def get_image_urls(page_content, image_xpath):
    tree = etree.HTML(page_content)
    image_elements = tree.xpath(image_xpath)
    image_urls = []
    for element in image_elements:
        # 假设element是一个包含style属性的元素
        style = element.get('style')
        if style:
            match = re.search(r'url\((.*?)\)', style)
            if match:
                image_urls.append(match.group(1))
    return image_urls


def download_images(image_urls, headers, folder='DIV'):
    create_directory(folder)
    for url in image_urls:
        image_name = url.split('/')[-1]
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            file_path = os.path.join(folder, image_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
                print(f"{image_name} downloaded.")

def get_next_page_url(current_page_content, next_page_xpath):
    tree = etree.HTML(current_page_content)
    next_page_elements = tree.xpath(next_page_xpath)
    if next_page_elements:
        # 确保我们得到的是一个元素节点
        next_page_element = next_page_elements[0]
        return next_page_element.get('href')
    return None


def crawl_images(url, image_xpath, next_page_xpath, max_pages=None):
    headers = {'User-Agent': get_user_agent()}
    current_url = url
    page_count = 0

    while current_url and (max_pages is None or page_count < max_pages):
        response = requests.get(current_url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to retrieve {current_url}")
            break

        page_content = response.text
        image_urls = get_image_urls(page_content, image_xpath)
        download_images(image_urls, headers)

        next_page_url = get_next_page_url(page_content, next_page_xpath)
        if next_page_url:
            current_url = os.path.join(os.path.dirname(current_url), next_page_url)
        else:
            break

        page_count += 1

if __name__ == "__main__":
    input_url = input("请输入URL：")
    image_xpath = '//ul[@class="clearfix"]/li/a/span/div[@class="pic"]'
    next_page_xpath = '//div[@class="page"]/a[@href and not(contains(text(), "下一页"))]'
    max_pages = int(input("请输入要爬取的最大页数："))
    crawl_images(input_url, image_xpath, next_page_xpath, max_pages)

'''
简化版本
import os.path
import  requests
from lxml import  etree
import  re
if __name__=="__main__":
    url='https://pic.netbian.top/4kdongman/'
    headers={"User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'}
    page_text=requests.get(url=url,headers=headers).text
    #print(page_text)
    tree=etree.HTML(page_text)
    li_list=tree.xpath('//ul[@class="clearfix"]/li')
    #print(li_list)
    if not os.path.exists('./img'):
        os.mkdir('./img')
    for li in li_list:
        img_data=li.xpath('./a/span/div[@class="pic"]/@style')
        img_name=li.xpath('./a/@title')[0]
        #print(img_name)
        img_str= ''.join([item for item in img_data if isinstance(item, str)])#将用xpath获取的列表里面的元素转化为字符串
        img_url=re.search(r'url\((.*?)\)',img_str).group((1))#通过正则表达式提取获取页面中的图片的url
        #print(img_url)
        img_data_2=requests.get(url=img_url,headers=headers).content
        img_path='img/'+img_name+'.jpg'
        with open (img_path,'wb') as fp:
            fp.write(img_data_2)
            print(img_name+"下载完成")
'''
