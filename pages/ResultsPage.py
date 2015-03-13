from pages.BasePage import BasePage


class ResultsPage(BasePage):
    PRODUCT = "//div[@class = 'g-i-list available clearfix' and contains(., '{0}')]"
    SEARCH_BUTTON = 'btn-link-i'

    def get_product_description(self, name):
        return self.driver.find_element_by_xpath(self.PRODUCT.format(name)).text
