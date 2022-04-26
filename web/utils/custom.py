import os


class CustomUtils:

    def __init__(self, root_path):
        self.root_path = root_path

    def get_file_url(self):
        filepath = os.path.join(self.root_path, "data")
        return filepath
