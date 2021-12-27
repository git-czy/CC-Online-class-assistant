# -*- coding: utf-8 -*-
# File: base.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/27 16:47

class CCBaseException(Exception):
    """
    Base异常
    """


class InitInternetFailedException(CCBaseException):
    """
    网络初始化失败异常
    """
    args = "网络初始化失败!"


class InitChromeFailedException(CCBaseException):
    """
    浏览器初始化失败异常
    """
    args = "浏览器初始化失败!"
