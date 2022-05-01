import os
from bs4 import BeautifulSoup


def get_each_blog_content(html_data):
    bs_obj = BeautifulSoup(html_data, "html.parser")
    title = bs_obj.find("h1", {"id": "title"}).text
    summary = bs_obj.find("p", {"id": "summary"}).text
    content = bs_obj.find("div", {"id": "content"})
    return title, summary, content


class CustomUtils:

    def __init__(self, root_path):
        self.root_path = root_path

    def get_file_url(self):
        filepath = os.path.join(self.root_path, "data")
        return filepath

    def get_blog_posts(self):
        dir_path = os.path.join(self.root_path, "docs", "blogs")
        i = 0
        blogs_list = []
        for each_file in os.listdir(dir_path):
            each_path = os.path.join(dir_path, each_file)
            i += 1
            with open(each_path, "r+", encoding="utf8") as blogFile:
                html_data = blogFile.read()
                title, summary, content = get_each_blog_content(html_data=html_data)
                url = f"/view/{each_file.split('.')[0]}"
                data = {
                    "id": i,
                    "title": title,
                    "summary": summary,
                    "content": content,
                    "url": url
                }
                blogs_list.append(data)
        return blogs_list

    def get_blog_data(self, file_name):
        file_path = os.path.join(self.root_path, "docs", "blogs", f"{file_name}.html")
        with open(file_path, "r+", encoding="utf8") as blogFile:
            html_data = blogFile.read()
            title, summary, content = get_each_blog_content(html_data=html_data)
            data = {
                "title": title,
                "summary": summary,
                "content": content
            }
        return data
