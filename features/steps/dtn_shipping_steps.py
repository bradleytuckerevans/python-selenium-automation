from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

@then('Verify Shipping page is open')
def verify_shipping_opened(context):
    context.driver.wait.until(EC.url_contains('https://www.dtn.com/weather/shipping/'))

@then('Close Shipping Page')
def close_shipping(context):
    context.driver.close()
    current_windows = context.driver.window_handles
    print('\nCurrent:', current_windows)