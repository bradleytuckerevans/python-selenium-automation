from selenium.webdriver.common.by import By
from behave import given, when, then

bestsellers_links = (By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a')

#@given('Open Amazon BestSellers')
#def open_amazon_best(context):
 #   context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

#@then ('User can click through top links and verify correct')
#def verify_bestsellers_links(context, expected_amount):
 #   expected_amount = int(expected_amount)
  #  links_amount = len(context.driver.find_elements(*bestsellers_links))
   # print(links_amount)
    #assert links_amount == expected_amount, f'Expected {expected_amount} links but got {links_amount}'



