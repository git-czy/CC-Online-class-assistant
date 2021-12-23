# -*- coding: utf-8 -*-
# File: main.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/22 16:50
import asyncio
import sys

from chome.login_cookie import get_route_cookie
from ui import init_ui


async def main():
    await get_route_cookie()
    app, login_ui = await init_ui()
    login_ui.show()

    # 登录界面绑定函数

    sys.exit(app.exec_())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
