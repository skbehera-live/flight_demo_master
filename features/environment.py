from selenium import webdriver
from selenium.common.exceptions import ScreenshotException
import traceback

from generate_report import generate_html_report


def before_all(context):
    try:
        context.browser = context.config.userdata['browser']
        defpath = context.config.userdata['driver_path']
        browser = context.browser.lower()

        if browser == 'chrome':
            context.driver = webdriver.Chrome(executable_path=defpath)

        elif browser == 'firefox':
            context.driver = webdriver.Firefox(executable_path=defpath)

        elif browser == 'ie':
            context.driver = webdriver.Ie(executable_path=defpath)

        else:
            raise Exception("Browser type '{}' is not supported".format(browser))

        ''' Maximaxize Window'''
        context.driver.maximize_window()

    except Exception as e:
        raise e


def after_all(context):
    context.driver.quit()
    generate_html_report()

def after_step(context, step):
    if step.status == 'failed':
        try:
            context.driver.get_screenshot_as_file("reports/" + context.scenario.name.replace(" ", "_") \
                                                  + "_line_" + str(step.line) + ".png")

        except ScreenshotException:
            traceback.print_exc()
