# -*- coding: utf-8 -*-
# File: webdriver.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/22 17:05
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class WebDriver(object):
    options = Options()
    default_options = ['--headless']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def _init_options(self, options: list):
        for option in options:
            self.options.add_argument(option)
        for option in self.default_options:
            self.options.add_argument(option)

        dr = Chrome(chrome_options=self.options)
        return dr

    def __call__(self, *args, **kwargs):
        options = kwargs.pop('options', None)
        dr = self._init_options(options)
        return dr



