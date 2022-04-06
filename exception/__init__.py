# -*- coding: utf-8 -*-
# File: __init__.py.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/27 16:47
import sys
from functools import wraps

from .base import (
    InitChromeFailedException,
    InitInternetFailedException
)


# def exception_handler(exception: BaseException):
#     print(exception.args)
#     print(exception.__context__)
#     print(exception.__traceback__)
#     print(exception.__cause__)
#     print(exception.__traceback__.tb_frame.f_globals['__file__'])
#     print(exception.__traceback__.tb_lineno)
#     print(sys.exc_info())


def exception_handler(function):
    """
    异常处理装饰器
    """

    @wraps(function)
    def inner(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as exception:
            print(exception.args)
            print(exception.__context__)
            print(exception.__traceback__)
            print(exception.__cause__)
            print(exception.__traceback__.tb_frame.f_globals['__file__'])
            print(exception.__traceback__.tb_lineno)
            print(sys.exc_info())

    return inner


if __name__ == '__main__':
    try:
        raise InitInternetFailedException
    except Exception as e:
        exception_handler(e)
