# -*- coding: utf-8 -*-
# File: __init__.py.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/24 13:48
from .core import DMLSqlite


def get_last_login_user():
    """
    获取最后登录用户的信息
    :return: 用户信息
    """
    with DMLSqlite() as db:
        user = db.select_user(last='1')
        return user
