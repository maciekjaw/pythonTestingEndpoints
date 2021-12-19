import requests as re
from unittest import TestCase


class Endpoints(TestCase,):
    def test_google(self):
        url:str = 'https://www.google.com'
        self.get_endpoint = re.get(url).status_code
        self.assertEqual(self.get_endpoint,200)
