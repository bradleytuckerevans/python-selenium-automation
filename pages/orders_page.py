from selenium.webdriver.common.by import By
from pages.base_page import Page

class OrdersPage(Page):
        ORDERS_BTN = (By.ID, 'nav-orders')

        def click(self):
            self.click(*self.ORDERS_BTN)


