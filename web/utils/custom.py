import os
import markdown
from bs4 import BeautifulSoup


class CustomUtils:

    def __init__(self, root_path):
        self.root_path = root_path

    def get_file_url(self):
        filepath = os.path.join(self.root_path, "data")
        return filepath

    def get_html_from_md(self, file):
        md_data = file.read()
        html_data = markdown.markdown(md_data)
        return html_data

    def get_each_md_content(self, html_data):
        bs_obj = BeautifulSoup(html_data, "html.parser")
        title = bs_obj.find("h1").text
        content = ''.join(html_data.splitlines(keepends=True)[1:6])
        return title, content

    def get_blog_posts(self):
        dir_path = os.path.join(self.root_path, "docs", "blogs")
        i = 0
        blogs_list = []
        for each_file in os.listdir(dir_path):
            each_path = os.path.join(dir_path, each_file)
            i += 1
            with open(each_path, "r+") as blogFile:
                html_data = self.get_html_from_md(file=blogFile)
                title, content = self.get_each_md_content(html_data=html_data)
                url = f"/view/{each_file.split('.')[0]}"
                data = {
                    "id": i,
                    "title": title,
                    "content": content,
                    "url": url
                }
                blogs_list.append(data)
        return blogs_list

    def get_blog_data(self, blog_name):
        file_path = os.path.join(self.root_path, "docs", "blogs", f"{blog_name}.md")
        with open(file_path, "r+") as blogFile:
            html_data = self.get_html_from_md(file=blogFile)
            title, content = self.get_each_md_content(html_data=html_data)
            data = {
                "title": title,
                "content": content
            }
        return data
