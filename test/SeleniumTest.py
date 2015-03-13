from pages.MainPage import MainPage
from pages.ResultsPage import ResultsPage
from test.BaseSeleniumTest import BaseSeleniumTest


class MyTestCase(BaseSeleniumTest):
    item = "D-Link DIR-826L"

    def test_something(self):
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.search_for(self.item)
        results_page = ResultsPage(self.driver)
        element_text = results_page.get_product_description(self.item)

        self.assertTrue('Есть в наличии' in element_text)
        self.assertTrue('840 грн.' in element_text)





