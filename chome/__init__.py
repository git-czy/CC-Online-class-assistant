# -*- coding: utf-8 -*-
# File: __init__.py.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/22 17:04
import os

from PyQt5.QtWidgets import QMessageBox

from .login import *
from .driver import *

import chromedriver_autoinstaller as dr_auto


async def init_chrome(ui_login):
    """
    初始化chrome，检测chrome和driver的安装情况
    :param ui_login:ui
    :return: bool
    """
    try:

        chrome_version = await check_chrome()

        if chrome_version:
            major_version = dr_auto.utils.get_major_version(chrome_version)
            if not os.path.exists(os.path.join(os.getcwd(), major_version)):
                QMessageBox.information(ui_login, '提示', '即将加载程序请耐心等待！', QMessageBox.Yes)
                ui_login.splash.show()
                flag = await check_chrome_driver(chrome_version)
                ui_login.splash.close()
            else:
                flag = await check_chrome_driver(chrome_version)
            return flag
        return False
    except Exception as e:
        print(e)
        # todo 日志纪录


def load_chrome():
    web = WebDriver()
    dr = web()
    dr.get('https://i.mooc.chaoxing.com/space/')
    for cookie in login_cookies.login_cookie_list:
        dr.add_cookie(cookie)
    dr.get('https://i.mooc.chaoxing.com/space/')

    return dr
