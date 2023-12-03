import os
from bs4 import BeautifulSoup


def get_each_blog_content(html_data):
    bs_obj = BeautifulSoup(html_data, "html.parser")
    tag = bs_obj.find("div", {"id": "tag"}).text
    title = bs_obj.find("h1", {"id": "title"}).text
    summary = bs_obj.find("p", {"id": "summary"}).text
    content = bs_obj.find("div", {"id": "content"})
    return tag, title, summary, content


class BlogUtils:

    def __init__(self, root_path):
        self.root_path = root_path

    def get_file_url(self):
        filepath = os.path.join(self.root_path, "data")
        return filepath

    def get_tags(self):
        blog_posts = self.get_blog_posts(for_tag=None)
        tags_list = [each_item.get("tag") for each_item in blog_posts]
        tags_list = list(set(tags_list))
        return tags_list

    def get_blog_posts(self, for_tag=None):
        dir_path = os.path.join(self.root_path, "docs", "blogs")
        i = 0
        blogs_list = []
        for each_file in os.listdir(dir_path):
            each_path = os.path.join(dir_path, each_file)
            i += 1
            with open(each_path, "r", encoding="utf8") as blogFile:
                html_data = blogFile.read()
                tag, title, summary, content = get_each_blog_content(html_data=html_data)
                url = f"/view/{each_file.split('.')[0]}"
                data = {
                    "id": i,
                    "tag": tag,
                    "title": title,
                    "summary": summary,
                    "content": content,
                    "url": url
                }
                if for_tag:
                    if tag == for_tag:
                        blogs_list.append(data)
                else:
                    blogs_list.append(data)
        return blogs_list

    def get_blog_data(self, file_name):
        file_path = os.path.join(self.root_path, "docs", "blogs", f"{file_name}.html")
        with open(file_path, "r+", encoding="utf8") as blogFile:
            html_data = blogFile.read()
            tag, title, summary, content = get_each_blog_content(html_data=html_data)
            data = {
                "tag": tag,
                "title": title,
                "summary": summary,
                "content": content
            }
        return data
