# -*- coding: utf-8 -*-
# File: login_cookie.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/23 16:31
import base64
import time

import requests
from bs4 import BeautifulSoup
from chome.agent import user_agent
from exception import exception_handler

route_cookie_url = "https://passport2.chaoxing.com/login?fid=&refer="
code_num_url = "https://passport2.chaoxing.com/num/code?"
code_img_save_path = "img/code.png"
login_url = "https://passport2.chaoxing.com/login?refer=https://i.mooc.chaoxing.com"


class LoginCookie:
    def __init__(self, cookie: str = '', cookie_list: list = None, route_cookie: str = ''):
        self.login_cookie = cookie
        self.login_cookie_list = cookie_list
        self.route_cookie = route_cookie


login_cookies = LoginCookie()


@exception_handler
async def get_route_cookie() -> bool:
    """
    获取学习通登录页面cookie，后面调用登录接口，以及验证码接口 需要此cookie
    此cookie随会话结束失效
    在gui程序关闭前确保此cookie一致
    :return: cookie
    """
    res = requests.get(url=route_cookie_url)
    cookies = res.cookies
    # cookie_dict = {}
    cookie_str = ''

    for cookie in cookies:
        cookie_str += f'{cookie.name}={cookie.value}; '

    setattr(login_cookies, 'route_cookie', cookie_str)
    return True


@exception_handler
def get_num_code() -> None:
    """
    获取学习通验证码
    """
    time_now = time.time()
    time_stamp_ms = int(round(time_now * 1000))
    headers = {
        "Cookie": login_cookies.route_cookie
    }
    res = requests.get(url=f"{code_num_url}{time_stamp_ms}", headers=headers)
    img_content = res.content
    with open(code_img_save_path, 'wb') as f:
        f.write(img_content)


@exception_handler
def get_login_cookie(fid: str = '-1', code: str = '', uname: str = '', password: str = '', ):
    """
    获取登录成功cookie
    :param password: 密码
    :param uname: 用户名
    :param fid: 机构
    :param code: 验证码
    :return: error or None
    """

    # get_route_cookie()
    # get_num_code()
    # code = input('code:')

    uname = base64.encodebytes(uname.encode('utf-8')).decode('utf-8').replace('\n', '')
    password = base64.encodebytes(password.encode('utf-8')).decode('utf-8').replace('\n', '')

    form_data = f"refer_0x001=http%253A%252F%252Fi.mooc.chaoxing.com&pid=-1&pidName=&fid={fid}&allowJoin=0" \
                f"&isCheckNumCode=1&f=0&productid=&t=true&uname={uname}&password={password}&numcode={code}&verCode= "
    form_data = form_data.encode("utf-8")
    headers = {
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
                  "application/signed-exchange;v=b3;q=0.9",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "zh-CN,zh;q=0.9,en;q=0.8",
        'Cache-Control': "max-age=0",
        'Connection': "keep-alive",
        'Content-Length': "195",
        'Content-Type': "application/x-www-form-urlencoded",
        'Host': "passport2.chaoxing.com",
        'Cookie': login_cookies.route_cookie,
        'Origin': 'https://passport2.chaoxing.com',
        'Referer': 'https://passport2.chaoxing.com/login?fid=&refer=',
        'Upgrade-Insecure-Requests': "1",
        'User-Agent': user_agent
    }

    res = requests.post(url=login_url, data=form_data, headers=headers)

    error = check_login_status(res.content)
    if error:
        return error
    cookies = res.history[0].cookies

    cookie_list = []
    cookie_str = ''

    for cookie in cookies:
        cookie_list.append({
            'name': cookie.name,
            'value': cookie.value,
            'domain': cookie.domain,
            'path': cookie.path,
        })
        cookie_str += f'{cookie.name}={cookie.value}; '

    setattr(login_cookies, 'login_cookie', cookie_str)
    setattr(login_cookies, 'login_cookie_list', cookie_list)


@exception_handler
def check_login_status(content: bytes) -> str:
    """
    :param content:bytes流
    :return 错误信息
    """
    soup = BeautifulSoup(content.decode('utf-8'), 'html.parser')
    error_log = soup.find_all('td', id="show_error")[0].text
    if error_log != ' ':
        return error_log
    return ''


if __name__ == '__main__':
    get_login_cookie()
