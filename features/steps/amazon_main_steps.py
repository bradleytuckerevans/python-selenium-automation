
from selenium.webdriver.common.by import By
from behave import given, when
from selenium.webdriver.support import expected_conditions as EC

SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
NAV_MENU_ICON = (By.ID, 'nav-hamburger-menu')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem a')
SIGN_IN_POPUP_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip a.nav-action-button')

ORDERS_BTN = (By.ID, 'nav-orders')

@given('Open Amazon')
def open_amazon(context):
    context.app.main_page.open_main()

@when('Search for {keyword}')
def search_product(context, keyword):
    context.app.header.search_product(keyword)
    context.app.header.click_search()



@when('Click on button from SignIn popup')
def click_sign_in_popup(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_POPUP_BTN),
        message='Sign In btn not clickable').click()


@when('Wait for {sec} sec')
def wait(context, sec):
    sleep(int(sec))


@when('Click Amazon Orders link')
def click_orders_link(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(ORDERS_BTN),message='Order btn not clickable').click()