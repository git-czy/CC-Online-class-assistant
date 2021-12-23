# -*- coding: utf-8 -*-
# File: test2.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/23 16:28
import requests

res = requests.get(url="https://passport2.chaoxing.com/login?fid=&refer=")

cookies = res.cookies
cookie_dict = {}
cookie_str = ''

for cookie in cookies:
    cookie_dict[cookie.name] = cookie.value
    cookie_str += f'{cookie.name}={cookie.value}; '

print(cookie_str)