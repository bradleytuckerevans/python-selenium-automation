from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.ui import Select

class Header(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    FLAG = (By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us')
    SPANISH_LANG = (By.CSS_SELECTOR, '[href="#switch-lang=es_US"]')
    SELECT_DEPARTMENT = (By.ID, 'searchDropdownBox')
    SELECT_PET = (By.ID, 'searchDropdownBox')

    def search_product(self, keyword):
        self.input_text(keyword, *self.SEARCH_INPUT)

    def click_search(self):
        self.click(*self.SEARCH_BTN)

    def hovers_lang_options(self):
        flag = self.find_element(*self.FLAG)
        actions = ActionChains(self.driver)
        actions.move_to_element(flag)
        actions.perform()

    def select_department(self, alias: str):
        select_department = self.find_element(*self.SELECT_DEPARTMENT)
        select = Select(select_department)
        select.select_by_value(f'search-alias={alias}')
 # my code

    def select_pet(self):
        select_pet = self.find_element(*self.SELECT_PET)
        select = Select(select_pet)
        select.select_by_value('search-alias=pets')



    def verify_spanish_lang_present(self):
        self.wait_for_element_appear(*self.SPANISH_LANG)

