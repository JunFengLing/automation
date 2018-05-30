from pageobjects import base_page
from selenium.webdriver.common.by import By


class SearchPage(base_page.BasePage):

    @property
    def search_terms_input(self):
        return self.driver.find_element(By.ID, 'searchTerms')

    @property
    def main_search_btn(self):
        return self.driver.find_element(By.ID, 'mainSearch')

    def search(self, term):
        self.search_terms_input.send_keys(term)
        self.main_search_btn.click()
        self.wait_for_page_ready()
