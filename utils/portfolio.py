import requests
from datetime import datetime
import calendar


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
            if project["end"]["year"] and project["end"]["month"]:
                year = project["end"]["year"]
                month = calendar.month_name[project["end"]["month"]]
            each_pr = {
                "name": project["displayName"],
                "url": project["githubUrl"],
                "summary": project["summary"],
                "languages": ",".join(project["languages"]),
                "date": f"{month},{year}"
            }
            projects.append(each_pr)
        return projects

    def get_about_info(self):
        return_about = {}
        interests = self.data.get("interests")
        languages = self.data.get("languages")
        skills = self.data.get("skills")
        work = self.data.get("work")
        education = self.data.get("education")

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

        return_work = []
        if work:
            for each_dict in work:
                start = datetime.strptime(each_dict.get("startDate").strip(), "%Y-%m-%d")
                end = datetime.strptime(each_dict.get("endDate").strip(), "%Y-%m-%d")
                months_between = (end.year - start.year) * 12 + end.month - start.month + 1
                years_between, months_between = divmod(months_between, 12)
                duration = f"{years_between} Years {months_between} Months"
                return_work.append({
                    "name": each_dict.get("name"),
                    "position": each_dict.get("position"),
                    "start": each_dict.get("startDate"),
                    "end": each_dict.get("endDate"),
                    "duration": duration,
                    "summary": each_dict.get("summary").replace("\n", " <br> "),
                    "url": each_dict.get("url")
                })

        return_education = []
        if education:
            for each_dict in education:
                start = each_dict.get("startDate")
                end = each_dict.get("endDate")
                if start and end:
                    start = datetime.strptime(each_dict.get("startDate").strip(), "%Y-%m-%d")
                    end = datetime.strptime(each_dict.get("endDate").strip(), "%Y-%m-%d")
                    months_between = (end.year - start.year) * 12 + end.month - start.month + 1
                    years_between, months_between = divmod(months_between, 12)
                    duration = f"{years_between} Years {months_between} Months"
                else:
                    duration = f"On-Going"
                return_education.append({
                    "name": each_dict.get("institution"),
                    "study": each_dict.get("studyType") + " in " + each_dict.get("area"),
                    "start": each_dict.get("startDate"),
                    "end": each_dict.get("endDate"),
                    "duration": duration,
                    "summary": each_dict.get("description").replace("\n", " <br> "),
                    "url": each_dict.get("url")
                })

        return_about["interests"] = ", ".join(return_interests)
        return_about["languages"] = ", ".join(return_languages)
        return_about["skills"] = ", ".join(return_skills)
        return_about["work"] = return_work
        return_about["education"] = return_education
        return return_about
