from pageobjects import base_page
from selenium.webdriver.common.by import By


class ResultPage(base_page.BasePage):

    @property
    def query_for(self):
        return self.driver.find_element(By.CSS_SELECTOR, 'h2 .query')

    @property
    def countries_list(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '.countries-tab .countries li[data-id]')

    @property
    def more_countries_btn(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.countries-tab .countries .more-countries')

    @property
    def more_countries_list(self):
        return self.driver.find_elements(By.CSS_SELECTOR, '.countries-tab .morecountries li')

    @property
    def hlct_list(self):
        return self.driver.find_elements(By.XPATH, '//ul[contains(@class, "content-switcher")]/li[contains(@data-id, "urn:hlct:")]')

    @property
    def countries_text_list(self):
        self.more_countries_btn.click()
        return [item.text for item in self.countries_list] + [item.text for item in self.more_countries_list]

    @property
    def hlct_text_list(self):
        return [item.text for item in self.hlct_list]
