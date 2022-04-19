import requests


class Portfolio:

    def __init__(self, url):
        self.url = url
        self.data = requests.get(self.url).json()

    def get_basic_info(self):
        data = self.data.get("basics")
        return_dict = {
            "image": data.get("image"),
            "name": data.get("name"),
            "label": data.get("label"),
            "summary": data.get("summary"),
            "github": next((link["url"] for link in data.get("profiles") if link["network"] == "GitHub"), None),
            "linkedin": next((link["url"] for link in data.get("profiles") if link["network"] == "LinkedIn"), None)
        }
        return return_dict
