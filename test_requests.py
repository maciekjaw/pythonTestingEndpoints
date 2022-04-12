import requests as re
import unittest
import pytest
import mathlib

class Endpoints(unittest.TestCase):
    def test_google(self):
        url:str = 'https://www.google.com'
        self.get_endpoint = re.get(url).status_code
        self.assertEqual(self.get_endpoint,200)
        
    if __name__ == '__main__':
        unittest.main()

def capital_case(x):
    return x.capitalize()

def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'

