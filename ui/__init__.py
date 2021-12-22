# -*- coding: utf-8 -*-
# File: __init__.py.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/22 16:41
import sys

from PyQt5.QtWidgets import QApplication

from ui.login import UiLogin


async def init_ui():
    """
    初始化ui界面并返回 ui对象和全局app对象
    :return:
    """
    app = QApplication(sys.argv)
    login_ui = UiLogin()
    return app, login_ui


def hide_piece(piece, show):
    """
    隐藏控件
    :param piece: ui控件
    :param show: True or False
    """
    piece.setVisible(show)
