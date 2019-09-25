from selenium.common.exceptions import WebDriverException, TimeoutException, \
    StaleElementReferenceException
import traceback
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

''' Web common functions'''

def go_to_url(context, url):
    """ launch application"""
    try:
        context.driver.implicitly_wait(20)
        context.driver.get(url.strip())
        pass
    except WebDriverException:
        traceback.print_exc()


def enter_text_in_element(context, locator, data):
    try:
        element = WebDriverWait(context.driver,
                                20).until(expected_conditions.presence_of_element_located(locator))
        if not element == False:
            element.clear()
            element.send_keys(data)
            pass
    except(TimeoutException, StaleElementReferenceException):
        traceback.print_exc()


def click_element(context, locator):
    try:
        element = WebDriverWait(context.driver,
                                20).until(expected_conditions.element_to_be_clickable(locator))
        if not element == False:
            element.click()
            pass
    except(TimeoutException, StaleElementReferenceException):
        traceback.print_exc()
