from behave import given, when, then
from common.webcommon import *
from pages.page_dictionary import LoginPage


@given(u'open the url "{app_url}"')
def open_application(context, app_url):
    go_to_url(context,app_url)


@then(u'validate landing page "{page_title}"')
def verify_page_title(context, page_title):
    try:
        context.driver.implicitly_wait(20)
        actual_page_title = context.driver.title
        assert actual_page_title.strip() == page_title.strip(), \
            "Expected: {}, Actual: {}".format(page_title, actual_page_title)
    except Exception as e:
        raise e


@when(u'login with username "{uname}" and password "{pswd}"')
def login_to_application(context, uname, pswd):
    try:
        login = LoginPage()
        enter_text_in_element(context, login.dictionary['txt_username'], uname)
        enter_text_in_element(context, login.dictionary['txt_password'], pswd)
        click_element(context, login.dictionary['btn_login'])
    except Exception as e:
        raise e
