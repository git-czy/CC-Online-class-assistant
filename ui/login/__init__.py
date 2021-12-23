# -*- coding: utf-8 -*-
# File: __init__.py.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/22 17:21
import time
from asyncio import run

from PyQt5 import QtGui

# from PIL import Image

# from selenium.webdriver import Chrome

from chome.login_cookie import get_num_code, get_route_cookie, route_cookie
from ui.main import UiMain

from .login import UiLogin

# code_id = 'numVerCode'
# screen_cut_path = '../../img/screen.png'
code_cut_path = 'img/code.png'


async def set_code(ui: UiLogin = UiLogin):
    """
    初始化时设置验证码
    :param ui: 登录界面
    """
    # cookie = await get_route_cookie()
    get_num_code(route_cookie)
    jpg = QtGui.QPixmap(code_cut_path)
    ui.codeimg.setPixmap(jpg)


def refresh_code(ui: UiLogin = UiLogin):
    get_num_code(route_cookie)


async def set_user_data(ui: UiLogin = UiLogin):
    """
    初始化时设置用户信息
    :param ui: 登录界面
    """
    # 设置账号
    ui.Number.setText("15528510258")
    # 设置密码
    ui.Password.setText("ccc51521")
    # 设置无窗口模式
    ui.iswindow.setChecked(True)
    # 设置记住密码
    ui.isremember.setChecked(True)


def login_click(ui_login: UiLogin, ui_main: UiMain):
    account = ui_login.Number.text()
    password = ui_login.Password.text()
    code = ui_login.code.text()
    r_pwd = ui_login.isremember.isChecked()
    show_window = ui_login.iswindow.isChecked()
    course = ui_login.CourseCheck.currentText()

    print(account)
    print(password)

# async def getcode(dr):  # 获取验证码
#     time.sleep(1)
#     dr.save_screenshot(screen_cut_path)
#     code = dr.find_element_by_id(code_id)
#     left = int(code.location['x'])
#     top = int(code.location['y'])
#     right = int(code.location['x'] + code.size['width'])
#     bottom = int(code.location['y'] + code.size['height'])
#     code_img = Image.open(screen_cut_path)
#     code_img = code_img.crop((left, top, right, bottom))
#     code_img.save(code_cut_path)
