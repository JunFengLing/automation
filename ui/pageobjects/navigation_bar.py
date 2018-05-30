import time

from pageobjects import base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class NavigationBar(base_page.BasePage):

    @property
    def nav_current_product_btn(self):
        return self.driver.find_element(By.ID, 'nav_currentproduct_button')

    @property
    def nav_product_switcher_arrow_btn(self):
        return self.driver.find_element(By.ID, 'nav_productswitcher_arrowbutton')

    @property
    def nav_application_menu_btn(self):
        return self.driver.find_element(By.ID, 'nav_applicationmenu')

    @property
    def sign_out_btn(self):
        return self.driver.find_element(By.ID, 'SignOut')

    def product_switcher(self, product):
        return self.driver.find_element(By.CSS_SELECTOR, '#nav_productswitcher_menu a[data-value=%s]' % product)

    def sign_out(self):
        self.nav_application_menu_btn.click()
        # time.sleep(3)
        WebDriverWait(driver=self.driver, timeout=60).until(EC.element_to_be_clickable((By.ID, 'SignOut')))
        self.sign_out_btn.click()
        self.wait_for_page_ready()
