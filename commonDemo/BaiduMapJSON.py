# -*- coding:utf-8 -*-
"""
作者：Leon
日期：2023年10月06日
"""

'''百度地图的api测试'''

import requests

host = "https://api.map.baidu.com"  # 服务地址
uri = "/place/v2/search"  # 接口地址
ak = "33333333"  # 修改秘钥

params = {
    "query": "ATM机",
    "tag": "银行",
    "region": "武汉市洪山区",
    "output": "json",
    "ak": ak,

}

response = requests.get(url=host + uri, params=params)
if response:
    print(response.json())
