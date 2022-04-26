import requests


class Portfolio:

    def __init__(self, url):
        self.url = url
        self.data = requests.get(self.url).json()

    def refresh(self):
        self.data = requests.get(self.url).json()

    def get_basic_info(self):
        data = self.data.get("basics")
        return_dict = {
            "image": data.get("image"),
            "name": data.get("name"),
            "title": data.get("headline"),
            "label": data.get("label"),
            "summary": data.get("summary"),
            "github": next((link["url"] for link in data.get("profiles") if link["network"] == "GitHub"), None),
            "linkedin": next((link["url"] for link in data.get("profiles") if link["network"] == "LinkedIn"), None)
        }
        return return_dict

    def get_projects(self):
        data = self.data.get("projects")
        projects = []
        for project in data:
            each_pr = {
                "name": project["name"],
                "url": project["githubUrl"],
                "summary": project["summary"],
                "languages": ",".join(project["languages"])
            }
            projects.append(each_pr)
        return projects

    def get_about_info(self):
        return_about = {}
        interests = self.data.get("interests")
        languages = self.data.get("languages")
        skills = self.data.get("skills")

        return_interests = []
        if interests:
            for each_dict in interests:
                return_interests.append(each_dict.get("name"))

        return_languages = []
        if languages:
            for each_dict in languages:
                return_languages.append(each_dict.get("language"))

        return_skills = []
        if skills:
            for each_dict in skills:
                return_skills.append(each_dict.get("name"))

        return_about["interests"] = ", ".join(return_interests)
        return_about["languages"] = ", ".join(return_languages)
        return_about["skills"] = ", ".join(return_skills)
        return return_about
