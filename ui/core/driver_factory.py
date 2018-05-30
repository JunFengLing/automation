from selenium import webdriver
import os

class DriverFactory(object):

    def __init__(self):
        self.driver = webdriver

    @staticmethod
    def get_chrome_driver():
        # executable_path = "C:\\Users\\daij1\\PycharmProjects\\automation\\drivers\\chromedriver.exe"
        executable_path = "../../drivers/chromedriver.exe"
        driver = webdriver.Chrome(executable_path=executable_path)
        return driver


if __name__ == '__main__':
    # DriverFactory.get_chrome_driver()
    print(os.path)

