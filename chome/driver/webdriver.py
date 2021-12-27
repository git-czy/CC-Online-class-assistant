# -*- coding: utf-8 -*-
# File: webdriver.py
# @Author: 陈志洋
# @Email:  chenzhiyang@sinontt.com
# @Time: 2021/12/22 17:05
import os
import shutil

import chromedriver_autoinstaller as dr_auto
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


# from selenium.webdriver.common.service import Service


class WebDriver:
    options = Options()
    # default_options = ['--headless']
    default_options = ['blink-settings=imagesEnabled=false']
    driver = None

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def _init_options(self, options: list = None):
        if options:
            for option in options:
                self.options.add_argument(option)
        for option in self.default_options:
            self.options.add_argument(option)

        self.driver = Chrome(options=self.options)

    def __enter__(self):
        self._init_options()
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()
        if isinstance(exc_type, Exception):
            # todo logging
            pass
        return True

    def __call__(self, *args, **kwargs):
        self._init_options()
        return self.driver


async def check_chrome_driver(chrome_version: str) -> bool:
    """
    检测是否安chrome_driver版本是否正确，不正确则自动安装适配的driver
    :return: bool
    """

    # chrome_version = dr_auto.get_chrome_version()  # 谷歌浏览器版本
    major_version = dr_auto.utils.get_major_version(chrome_version)  # 浏览器版本大版本
    # driver_version = dr_auto.utils.get_matched_chromedriver_version(chrome_version)  # 适配浏览器版本的driver
    # major_driver_version = dr_auto.utils.get_major_version(driver_version)  # driver版本大版本

    cwd_path = os.getcwd()
    cwd_file_list = os.listdir(cwd_path)

    for file_name in cwd_file_list:
        if file_name.isdigit() and major_version != file_name:
            shutil.rmtree(os.path.join(cwd_path, file_name))

    dr_auto.install(cwd=True)
    if os.path.exists(os.path.join(cwd_path, major_version)):
        return True

    return False


async def check_chrome():
    """
    检测chrome浏览器是否安装
    :return: bool
    """
    return dr_auto.get_chrome_version()


if __name__ == '__main__':
    res = check_chrome_driver()
    print(res)
