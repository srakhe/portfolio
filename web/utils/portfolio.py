import requests
from pprint import pprint


class Portfolio:

    def __init__(self, url):
        self.url = url
        self.data = requests.get(self.url).json()

    def get_info(self, key):
        # data = self.data.get(key)
        data = self.data
        return data
