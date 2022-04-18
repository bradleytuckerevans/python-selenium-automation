from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

@then('Verify Twitter is open')
def verify_twitter_opened(context):
    context.driver.wait.until(EC.url_contains('https://twitter.com/dtn'))

@then('Close Twitter')
def close_twitter(context):
    context.driver.close()
    current_windows = context.driver.window_handles
    print('\nCurrent:', current_windows)
