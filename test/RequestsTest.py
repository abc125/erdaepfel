import unittest
import json

import requests


class MyTestCase(unittest.TestCase):
    def test_something(self):
        headers = {'content-type': 'application/x-www-form-urlencoded', 'ajaxAction': 'http://rozetka.com.ua/search/'}
        data = {'text': 'D-Link DIR-826L', 'suggest': '1', 'referrer': 'http://rozetka.com.ua/'}
        r = requests.post('http://rozetka.com.ua/cgi-bin/search-form.php', headers=headers, data=data)
        resp = json.loads(r.text)
        self.assertEqual('available', resp['content']['records'][0]['sell_status'], 'The item is not available')
        self.assertEqual('840грн.', resp['content']['records'][0]['price'].replace("&nbsp;", ""),
                         'Incorrect UAH price')
        self.assertEqual('$70', resp['content']['records'][0]['price_usd'].replace("&nbsp;", ""),
                         'Incorrect USD price')

        if __name__ == '__main__':
            unittest.main()
