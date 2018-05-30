from pageobjects import login_page, navigation_bar, search_page, result_page


class PageCache(object):

    def __init__(self, driver):
        self.login_page = login_page.LoginPage(driver)
        self.navigation_bar = navigation_bar.NavigationBar(driver)
        self.search_page = search_page.SearchPage(driver)
        self.result_page = result_page.ResultPage(driver)
