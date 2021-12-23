# -*- coding: utf-8 -*-
# File: login_cookie.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/23 16:31
import time

import requests

from chome.agent import user_agent

route_cookie_url = "https://passport2.chaoxing.com/login?fid=&refer="
code_num_url = "https://passport2.chaoxing.com/num/code?"
code_img_save_path = "img/code.png"
login_url = "https://passport2.chaoxing.com/login?refer=http://i.mooc.chaoxing.com"

route_cookie = ''


async def get_route_cookie():
    """
    获取学习通登录页面cookie，后面调用登录接口，以及验证码接口 需要此cookie
    此cookie随会话结束失效
    在gui程序关闭前确保此cookie一致
    :return: cookie
    """
    global route_cookie
    res = requests.get(url=route_cookie_url)
    cookies = res.cookies
    # cookie_dict = {}
    cookie_str = ''

    for cookie in cookies:
        # cookie_dict[cookie.name] = cookie.value
        cookie_str += f'{cookie.name}={cookie.value}; '
    route_cookie = cookie_str


def get_num_code(cookie: str) -> None:
    """
    获取学习通验证码
    """
    time_now = time.time()
    time_stamp_ms = int(round(time_now * 1000))
    headers = {
        "Cookie": cookie
    }
    res = requests.get(url=f"{code_num_url}{time_stamp_ms}", headers=headers)
    img_content = res.content
    with open(code_img_save_path, 'wb') as f:
        f.write(img_content)


def get_login_cookie(cookie: str, fid: str = '-1', code: str = '', ):
    """
    获取登录成功cookie
    :param cookie: 会话cookie
    :param fid: 机构
    :param code: 验证码
    :return: cookie
    """
    # cookie = get_route_cookie()
    # get_num_code(cookie)
    # code = input('code:')
    form_data = f"refer_0x001=http%253A%252F%252Fi.mooc.chaoxing.com&pid=-1&pidName=&fid={fid}&allowJoin=0&isCheckNumCode=1&f=0&productid=&t=true&uname=MTU1Mjg1MTAyNTg%3D&password=Y2NjNTE1MjE%3D&numcode={code}&verCode="
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
        'Cookie': cookie,  # todo 本次登录持久化route——cookie
        'Origin': 'http://passport2.chaoxing.com',
        'Referer': 'http://passport2.chaoxing.com/login?fid=&refer=',
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': user_agent
    }
    try:
        res = requests.post(url=login_url, data=form_data, headers=headers)
        cookies = res.history[0].cookies
        # cookie_dict = {}
        cookie_str = ''

        for cookie in cookies:
            # cookie_dict[cookie.name] = cookie.value
            cookie_str += f'{cookie.name}={cookie.value}; '
        print(cookie_str)
        return cookie_str
    except Exception as e:
        print(e.args)
