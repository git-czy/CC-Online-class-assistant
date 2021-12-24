# -*- coding: utf-8 -*-
# File: __init__.py.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/22 17:04
from chome.login_cookie import route_cookie, route_cookie, get_route_cookie
from chome.webdriver import WebDriver, check_chrome_driver, check_chrome


async def init_chrome():
    """
    初始化chrome，检测chrome和driver的安装情况
    :return: bool
    """
    try:
        res = await check_chrome()
        if res:
            return await check_chrome_driver(res)
        return False
    except Exception as e:
        print(e)
        # todo 日志纪录
