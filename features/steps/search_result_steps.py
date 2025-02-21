from selenium.webdriver.common.by import By
from behave import given, when, then

RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//div{@data-component-type='s-search-result']//a[//span@class='a-price")

@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE)


@then('Verify search results are shown for {expected_result}')
def verify_result(context, expected_result):
    context.app.search_results_page.verify_search_result(expected_result)

@then('Verify {department} department is selected')
def verify_department(context, department):
    context.app.search_results_page.verify_correct_department(department)

@then('Verify Pet Supplies department is correct')
def verify_pet(context):
    context.app.search_results_page.verify_pet_department()
