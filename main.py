# -*- coding: utf-8 -*-
# File: main.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/22 16:50
import os
import sys
from asyncio import run
from PyQt5.QtWidgets import QMessageBox

# 自定义package
from chome import (
    init_chrome,
    init_internet
)

from ui import init_ui

from exception import (
    InitChromeFailedException,
    InitInternetFailedException,
    exception_handler
)


@exception_handler
async def main():
    try:
        # 初始化ui
        app, ui_login = await init_ui()
        # 初始化chrome浏览器
        inited_chrome = await init_chrome(ui_login)
        # 初始化网络
        inited_internet = await init_internet()

        if inited_chrome and inited_internet:
            ui_login.show()

        if not inited_internet:
            QMessageBox.information(ui_login, '提示', '请检查您的网络后重启程序！', QMessageBox.Yes)
            raise InitInternetFailedException
        if not inited_chrome:
            QMessageBox.information(ui_login, '提示', 'chrome浏览器初始化失败！请检查chrome浏览器是否安装！', QMessageBox.Yes)
            raise InitChromeFailedException
        sys.exit(app.exec_())
    except Exception as e:
        exception_handler(e)
        sys.exit(-1)


async def init_img_path():
    cwd = os.getcwd()


if __name__ == '__main__':
    run(main())
    # @exception_handler
    # def test():
    #     raise InitInternetFailedException
    # test()
# pyinstaller -F -w -i D:\pythonproject\CC-Online-class-assistant\img\cc.ico main.py
