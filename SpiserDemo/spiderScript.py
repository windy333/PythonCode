'''
暂停开发
'''

import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

'''
不建议使用此程序
不支持爬取反爬网站和加了防盗链的图片
'''

# 配置Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')  # 如果不需要浏览器界面可以启用无头模式

# 指定ChromeDriver的路径
driver_path = 'C://Program Files//Google//Chrome//Application//chromedriver//chromedriver.exe'

# 创建WebDriver实例
driver = webdriver.Chrome(executable_path=driver_path, options=options)

def down_scrpit(target_url):
    # 访问目标网站
    driver.get(target_url)

    # 等待页面加载完成（根据需要调整等待条件和时间）
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'img')))

    # 获取所有图片元素
    image_elements = driver.find_elements(By.TAG_NAME, 'img')

    # 创建一个文件夹来保存下载的图片
    image_folder = 'script'
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)

    # 下载图片
    for i, image_element in enumerate(image_elements):
        # 获取图片的URL
        image_url = image_element.get_attribute('src')
        # 只下载http开头的图片链接
        if image_url.startswith('http'):
            try:

                # 发送HTTP GET请求下载图片
                response = requests.get(image_url)
                # 确保请求成功
                if response.status_code == 200:
                    # 保存图片到文件
                    image_path = os.path.join(image_folder, f'image_{i}.jpg')
                    with open(image_path, 'wb') as file:
                        file.write(response.content)
                    print(f"下载图片完成")

            except Exception as e:
                print(f'Failed to download image {image_url}: {e}')


if __name__=="__main__":
    inputUrl=input("请输入URL：")
    down_scrpit(inputUrl)
    # 关闭WebDriver
    driver.quit()

