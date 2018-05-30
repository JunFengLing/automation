from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def wait_for_page_ready(self):
        WebDriverWait(driver=self.driver, timeout=60).until(PageReady("complete"))


class PageReady(object):

    def __init__(self, ready_state):
        self.ready_state = ready_state

    def __call__(self, driver):
        if self.ready_state == driver.execute_script('return document.readyState'):
            print("Page is ready")
            return True
        else:
            print("Page is not ready")
            return False
