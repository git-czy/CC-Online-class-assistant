# -*- coding: utf-8 -*-
# File: test.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/23 15:05
import urllib

import requests

# post_data = {
#     "refer_0x001": 'http%3A%2F%2Fi.mooc.chaoxing.com',
#     "pid": -1,
#     "fid": -1,
#     "allowJoin": 0,
#     "isCheckNumCode": 1,
#     "f": 0,
#     "t": 'true',
#     "uname": "MTU1Mjg1MTAyNTg=",
#     "password": "Y2NjNTE1MjE=",
#     "numcode": "5255",
# }
from bs4 import BeautifulSoup

code = "1833"
form_data = f"refer_0x001=http%253A%252F%252Fi.mooc.chaoxing.com&pid=-1&pidName=&fid=2347&allowJoin=0&isCheckNumCode=1&f=0&productid=&t=true&uname=MTU1Mjg1MTAyNTg%3D&password=Y2NjNTE1MjE%3D&numcode={code}&verCode="
form_data = form_data.encode("utf-8")
headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
    'Cache-Control': "max-age=0",
    'Connection': "keep-alive",
    'Content-Length': "195",
    'Content-Type': "application/x-www-form-urlencoded",
    'Host': "passport2.chaoxing.com",
    'cookie': "JSESSIONID=80DA77424FF04B3361031525A78189BF; route=675f734212e82e8a062506a8bb55a65c",
    'Origin': 'http://passport2.chaoxing.com',
    'Referer': 'http://passport2.chaoxing.com/login?fid=&refer=',
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
}
path = "https://passport2.chaoxing.com/login?refer=http://i.mooc.chaoxing.com"

res = requests.post(url=path, data=form_data, headers=headers)

cookies = res.history[0].cookies
cookie_dict = {}
cookie_str = ''

for cookie in cookies:
    cookie_dict[cookie.name] = cookie.value
    cookie_str += f'{cookie.name}={cookie.value}; '

print(cookie_dict)
print(cookie_str)


def get_couress(url, cookie):  # 主函数
    global result_headnum, result_title, result_endnum
    hearders = {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36",
    }
    req = urllib.request.Request(url=url, headers=hearders, method="GET")
    response = urllib.request.urlopen(req)
    # print(response.read().decode("utf-8"))
    html = response.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all('h3', class_="clearfix")
    # print("获取数据")
    result = []

    for link in links:
        for item in link.find_all('span', class_="articlename"):  # title_title查找器
            result_title = item['title']
            if result_title == '阅读' or result_title == '问卷调查':
                continue
            else:
                for item in link.find_all('span', class_="chapterNumber"):  # title_headnum查找器
                    result_headnum = item.get_text()
                for item in link.find_all('span', class_="icon"):
                    result_endnum = item.get_text().replace('\n', '')  # title_num查找器
                    if result_endnum == '2':
                        result_endnum = '未完成'
                    if result_endnum == '':
                        result_endnum = '已完成'
                result.append((result_headnum + ' ', result_title, ' ' + result_endnum))
    print(result)
    return result


url = "https://mooc1-1.chaoxing.com/mycourse/studentcourse?courseId=214694943&clazzid=38195621&enc=a2d4557fa4444e8c33e10556b163141e&cpi=125553139&vc=1"

get_couress(url, cookie_str)
