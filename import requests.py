import requests as re


get_endpoint = re.get('https://www.google.com').status_code
assert get_endpoint == 200



