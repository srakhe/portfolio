import requests
from datetime import datetime


class Github:

    def __init__(self):
        self.latest_update_url = "https://api.github.com/repos/srakhe/portfolio/deployments/586524427/statuses"

    def get_last_update(self):
        resp = requests.get(self.latest_update_url).json()[0]
        latest_date = resp.get("updated_at")
        if latest_date:
            latest_date = datetime.strptime(latest_date, "%Y-%m-%dT%H:%M:%SZ")
            latest_date = latest_date.strftime("%A, %d-%B-%Y")
            print(latest_date)
        else:
            latest_date = "Error"
        return latest_date
