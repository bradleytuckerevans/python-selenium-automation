from selenium.webdriver.common.by import By
from behave import given, when, then


TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
HEADER = (By.CSS_SELECTOR, '#zg_banner_text')

@then('User can click through top links and verify correct page opens')
def click_thru_top(context):
    top_links = context.driver.find_elements(*TOP_LINKS)

    for x in range(len(top_links)):
        link_to_click = context.driver.find_elements(*TOP_LINKS)[x]
        link_text = link_to_click.text
        link_to_click.click()
        new_text = context.driver.find_element(*HEADER).text
        assert link_text in new_text, f'Expected {link_text} to be in {new_text}'


@then('User can click through top links and verify correct')
def verify_links_count(context, expected_links):
    actual_links = context.driver.find_elements(*TOP_LINKS)
    assert  len(actual_links) == int(expected_links)