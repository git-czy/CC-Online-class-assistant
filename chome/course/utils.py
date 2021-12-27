from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support import ui
from selenium.webdriver.common.by import By


def wait_dom(driver: Chrome, dom_type, dom, wait_time: int = 5):
    try:
        ui.WebDriverWait(driver, wait_time).until(ec.presence_of_element_located((dom_type, dom)))
    except TimeoutException as e:
        raise e
    else:
        print(123)
    finally:
        print(123)
