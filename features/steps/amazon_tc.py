from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

privacy = (By.XPATH, "//a[@href='https://www.amazon.com/privacy']")


@given('Open Amazon T&C page')
def open_amazon_tc(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@when('Store original window')
def tc_window(context):
    context.original_window = context.driver.current_window_handle
    print(context.original_window)

@when('Click on Amazon Privacy Notice link')
def click_privacy(context):
    context.driver.find_element(*privacy).click()

@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_window = context.driver.window_handles
    print('\nCurrent:', current_window)
    context.driver.switch_to.window(current_window[1])

@then('switch back to original')
def switch_original_window(context):
    context.driver.switch_to.window(context.original_window)