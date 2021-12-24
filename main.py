# -*- coding: utf-8 -*-
# File: main.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/22 16:50
import asyncio
import sys
from asyncio import run

from PyQt5.QtWidgets import QMessageBox

from chome import init_chrome
from chome import get_route_cookie
from ui import init_ui


async def main():
    inited = await init_chrome()
    get = await get_route_cookie()
    app, ui_login = await init_ui()
    reply = None
    if not get:
        reply = QMessageBox.information(ui_login, '提示', '请检查您的网络后重启程序！', QMessageBox.Yes)
    if inited:
        ui_login.show()
    else:
        reply = QMessageBox.information(ui_login, '提示', 'chrome浏览器初始化失败！', QMessageBox.Yes)
    if reply:
        sys.exit()
    sys.exit(app.exec_())


if __name__ == '__main__':
    run(main())
