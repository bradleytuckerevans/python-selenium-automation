from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# logo
driver.find_element(By.CSS_SELECTOR, '[href="/ref=ap_frn_logo"]')
#name
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name')
#number/email
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')
#pw
driver.find_element(By.CSS_SELECTOR, 'input#ap_password')
#pw length
driver.find_element(By.CSS_SELECTOR, '.a-alert-content')
#reenter
driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')
#button
driver.find_element(By.CSS_SELECTOR, '#continue')
#cou
driver.find_element(By.CSS_SELECTOR, '[href="/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088"]')
#pn

driver.find_element(By.CSS_SELECTOR, '[href="/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496"]')

#signin
driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')


