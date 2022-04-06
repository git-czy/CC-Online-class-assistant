# -*- coding: utf-8 -*-
# File: __init__.py.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/22 17:21

from PyQt5 import QtGui

from chome import get_login_cookie, get_num_code, load_chrome
from db import DMLSqlite, get_last_login_user
from ui.main import UiMain

from .login import UiLogin

# code_id = 'numVerCode'
# screen_cut_path = '../../img/screen.png'


code_cut_path = 'img/code.png'

zh_error = "账号或密码有误"
code_error = "验证码错误"


def hide_piece(piece, show):
    """
    隐藏控件
    :param piece: ui控件
    :param show: True or False
    """
    piece.setVisible(show)



def show_error(ui, error):
    """
      :param ui:ui
      :param error: 错误信息
    """
    ui.errorinfo.setText(error)
    ui.errorinfo.setStyleSheet("color:red")
    hide_piece(ui.errorinfo, True)


async def set_code(ui: UiLogin = UiLogin):
    """
    初始化时设置验证码
    :param ui: 登录界面
    """
    # cookie = await get_route_cookie()
    get_num_code()
    jpg = QtGui.QPixmap(code_cut_path)
    ui.codeimg.setPixmap(jpg)


def refresh_code(ui: UiLogin = UiLogin):
    get_num_code()
    ui.code.setText('')
    jpg = QtGui.QPixmap(code_cut_path)
    ui.codeimg.setPixmap(jpg)


async def set_user_data(ui: UiLogin):
    """
    初始化时设置用户信息
    :param ui: 登录界面
    """
    user = get_last_login_user()
    if user:
        # 设置账号
        ui.Number.setText(user['number'])

        # 设置密码
        ui.Password.setText(user['password'])
        ui.isremember.setChecked(user['r_pas'] == '1')

        # 设置无窗口模式
        ui.iswindow.setChecked(user['show_window'] == '1')


def login_click(ui_login: UiLogin, ui_main: UiMain):
    number = ui_login.Number.text()
    password = ui_login.Password.text()
    code = ui_login.code.text()
    r_pwd = ui_login.isremember.isChecked()
    show_window = ui_login.iswindow.isChecked()
    course_type = ui_login.CourseCheck.currentText()
    if not number or not password:
        show_error(ui_login, zh_error)
    elif not code:
        show_error(ui_login, code_error)
    else:
        user_obj = {
            "number": number,
            "password": password,
            "r_pas": '1' if r_pwd else '0',
            "show_window": '1' if show_window else '0',
            "course_type": course_type,
            "last": "1"
        }
        with DMLSqlite() as db:
            res = db.insert_or_update_user(**user_obj)
        error = get_login_cookie(code=code, uname=number, password=password)

        if res and not error:
            ui_login.close()
            ui_main.init_chrome()
        else:
            refresh_code(ui_login)
            show_error(ui_login, error)
