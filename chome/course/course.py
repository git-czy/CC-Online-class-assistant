from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome

from .utils import wait_dom


def find_courses(dr: Chrome):  # 找课程
    """
    获取课程列表
    """
    try:
        wait_dom(dr, By.ID, "frame_content")

        dr.switch_to.frame('frame_content')

        wait_dom(dr, By.CLASS_NAME, "courselistArea")

        course_name_class = 'color1'

        wait_dom(dr, By.CLASS_NAME, course_name_class)

        course = []
        course_name_elements = dr.find_elements(By.CLASS_NAME, course_name_class)
        for element in course_name_elements:
            course.append({'name': element.text, 'href': element.get_dom_attribute('href')})
        return course

    except Exception as e:
        print(e)
        dr.quit()
