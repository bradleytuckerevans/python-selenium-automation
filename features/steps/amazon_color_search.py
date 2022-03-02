from selenium.webdriver.common.by import By
from behave import given, when, then

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')

@given('Open Amazon earphones product page')
def open_amazon_product(context):
    context.driver.get('https://www.amazon.com/Headphones-Bluetooth-Waterproof-Connection-Earphones/dp/B09JWDF2VY')

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection' )

@then('Verify user can click through colors')
def verify_color_clicks(context):
    expected_colors = ['Black', 'Pink', 'Gery']
    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    for color in color_options:
        color.click()
        current_color_name = context.driver.find_element(*CURRENT_COLOR).text
        assert current_color_name in expected_colors, f'Actual {actual_colors} not in expected list {expected_colors}'






















