from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.amazon.com/gp/help/customer/'))

@then('User can close new window')
def close_privacy(context):
    context.driver.close()
    current_window = context.driver.window_handles
    print('\nCurrent:', current_window)
