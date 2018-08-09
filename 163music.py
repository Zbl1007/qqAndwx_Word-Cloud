##coding=utf-8

import requests
from bs4 import BeautifulSoup

#requests 对象重定义   保持cookies登录状态
requests = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    ,"Referer": "http://music.163.com/"
    }
response = requests.get("http://music.163.com/discover/toplist?id=19723756")


print(response.text)
