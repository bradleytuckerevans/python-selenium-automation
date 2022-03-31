
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

@given('Open Amazon Hoodie product page')
def open_hoodie(context):
    context.driver.get('https://www.amazon.com/gp/product/B074TBCSC8')

@when('Search for {keyword}')
def search_product(context, keyword):
    context.app.header.search_product(keyword)
    context.app.header.click_search()


@when('Hover over Language options')
def hover_lang_options(context):
    context.app.header.hovers_lang_options()

@when('Select department by alias {alias}')
def select_department(context, alias):
    context.app.header.select_department(alias)
#new by me

@when('Select Pet Supplies department')
def select_pet(context):
    context.app.header.select_pet()

@when('Hover over New Arrivals')
def hover_new_arrivals(context):
    context.app.search_results_page.hover_new_arrivals()
#end
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

@then('Verify Spanish option present')
def verify_spanish_lang_present(context):
    context.app.header.verify_spanish_lang_present()

@then('Verify Deals are Present')
def verify_pop_window(context):
    context.app.search_results_page.verify_pop_window()