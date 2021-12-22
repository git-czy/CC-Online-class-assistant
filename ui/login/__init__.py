# -*- coding: utf-8 -*-
# File: __init__.py.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/22 17:21
import time

from PyQt5 import QtGui

from PIL import Image

from selenium.webdriver import Chrome

from .login import UiLogin

code_id = 'numVerCode'
screen_cut_path = '../../img/screen.png'
code_cut_path = '../../img/code.png'


async def set_code(dr: Chrome, ui: UiLogin):
    dr.refresh()
    await getcode(dr)
    jpg = QtGui.QPixmap('img/code.png')
    ui.codeimg.setPixmap(jpg)


async def getcode(dr):  # 获取验证码
    time.sleep(1)
    dr.save_screenshot(screen_cut_path)
    code = dr.find_element_by_id(code_id)
    left = int(code.location['x'])
    top = int(code.location['y'])
    right = int(code.location['x'] + code.size['width'])
    bottom = int(code.location['y'] + code.size['height'])
    code_img = Image.open(screen_cut_path)
    code_img = code_img.crop((left, top, right, bottom))
    code_img.save(code_cut_path)
