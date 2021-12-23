# -*- coding: utf-8 -*-
# File: webdriver.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/22 17:05
import chromedriver_autoinstaller
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

chromedriver_autoinstaller.install(cwd=True)


class WebDriver(object):
    options = Options()
    default_options = ['--headless']

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def _init_options(self, options: list = None):
        if options:
            for option in options:
                self.options.add_argument(option)
        for option in self.default_options:
            self.options.add_argument(option)

        dr = Chrome(options=self.options)
        return dr

    def __call__(self, *args, **kwargs):
        options = kwargs.pop('options', None)
        dr = self._init_options(options)
        return dr


if __name__ == '__main__':
    dr = WebDriver().__call__()
    dr.get("https://www.baidu.com/")
    assert "百度" in dr.title
    dr.close()
    dr.quit()
