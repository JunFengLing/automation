from pageobjects import base_page
from selenium.webdriver.common.by import By


class LoginPage(base_page.BasePage):

    @property
    def user_id_input(self):
        return self.driver.find_element(By.ID, 'userid')

    @property
    def password_input(self):
        return self.driver.find_element(By.ID, 'password')

    @property
    def sign_in_submit_btn(self):
        return self.driver.find_element(By.ID, 'signInSbmtBtn')

    def login(self, user_id, password):
        self.user_id_input.send_keys(user_id)
        self.password_input.send_keys(password)
        self.sign_in_submit_btn.click()
        self.wait_for_page_ready()

