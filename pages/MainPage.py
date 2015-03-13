from pages.BasePage import BasePage


class MainPage(BasePage):
    PAGE_URL = 'http://rozetka.com.ua/'
    SEARCH_FIELD = 'header-search-input-text'
    SEARCH_BUTTON = 'btn-link-i'

    def open(self):
        self.driver.get(self.PAGE_URL)

    def search_for(self, item):
        self.driver.find_element_by_class_name(MainPage.SEARCH_FIELD).send_keys(item)
        self.driver.find_element_by_class_name(MainPage.SEARCH_BUTTON).click()