# -*- coding: utf-8 -*-
# File: __init__.py.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/22 16:41
import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication

from ui.login import UiLogin, login_click, set_code, set_user_data, refresh_code
from ui.main import UiMain


async def init_ui():
    """
    初始化ui界面并返回 ui对象和全局app对象
    :return:
    """
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    login_ui = UiLogin()
    main_ui = UiMain()
    # 设置账号信息
    await set_user_data(login_ui)
    # 设置验证码
    await set_code(login_ui)

    # 按钮绑定事件
    login_ui.LoginBtn.clicked.connect(lambda: login_click(login_ui, main_ui))
    login_ui.code_re.clicked.connect(lambda: refresh_code(login_ui))

    main_ui.StartBtn.clicked.connect(lambda: main_ui.start())

    return app, login_ui
