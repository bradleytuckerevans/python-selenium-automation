from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

TABS_BENEFITS = (By.XPATH, '//div[@class="card-deck"]//div[contains(@class, "content-type-external")]')

@given('Open DTN Tabs')
def open_tabs(context):
    context.driver.get('https://www.dtn.com/refined-fuels/terminal-operator/tabs/')

@then('Verify user can see {expected_amount} tabs add ons')
def verify_tabs_benefits(context, expected_amount):
    benefits_amount = len(context.driver.find_elements(*TABS_BENEFITS))
    assert benefits_amount == int(expected_amount), f'Expected {expected_amount} benefits, but got {benefits_amount}'