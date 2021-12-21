import requests as re
import unittest


class Endpoints(unittest.TestCase):
    def test_google(self):
        url:str = 'https://www.google.com'
        self.get_endpoint = re.get(url).status_code
        self.assertEqual(self.get_endpoint,200)
        
    if __name__ == '__main__':
        unittest.main()