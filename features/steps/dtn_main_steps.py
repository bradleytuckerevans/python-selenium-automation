from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

HAM_ICON = (By.CLASS_NAME, 'fa-bars.mega-menu-link')
DTN_SHIPPING_HAMBURGER = (By.XPATH, '//a[contains(@href, "weather")]//img[contains(@src, "shipping-industry")]')
DTN_FOOTER_LINKS = (By.XPATH, '//li[contains(@class, "menu-item menu-item-type-post_type menu-item-object-page menu-item")]')
DTN_TWITTER_FOOTER = (By.ID, 'twitter')

@given('Open DTN')
def open_amazon_webpage(context):
    context.driver.get('https://www.dtn.com')

@given('Store original window')
def store_dtn_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)

@when('Click on Twitter footer link')
def click_dtn_twitter(context):
    context.driver.find_element(*DTN_TWITTER_FOOTER).click()

@when('Switch to the new window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print('\nCurrent:', current_windows)
    context.driver.switch_to.window(current_windows[1])


@when('Click on hamburger link')
def click_on_ham_menu(context):
    context.driver.find_element(*HAM_ICON).click()

@when('Click on Shipping hamburger link')
def click_on_shipping(context):
    context.driver.find_element(*DTN_SHIPPING_HAMBURGER).click()




@then('Verify hamburger menu is present')
def verify_ham_menu(context):
    context.driver.find_element(*HAM_ICON)

@then('Verify {expected_amount} links are present')
def verify_footer_links(context, expected_amount):
    expected_amount = int(expected_amount)

    dtn_links = len(context.driver.find_elements(*DTN_FOOTER_LINKS))

    assert dtn_links == expected_amount, f'Expected {expected_amount} links but got {dtn_links}'


@then('Return to original window')
def switch_original_window(context):
    context.driver.switch_to.window(context.original_window)

