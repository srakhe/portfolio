from flask import Flask, render_template, request, url_for, redirect
from web.utils.portfolio import Portfolio

app = Flask(__name__)
portfolio = Portfolio(url="https://gitconnected.com/v1/portfolio/srakhe")


@app.route("/")
def index():
    basic_info = portfolio.get_basic_info()
    params = {
        "basic": basic_info
    }
    return render_template("index.html", params=params)


@app.route("/about/")
def about():
    basic_info = portfolio.get_basic_info()
    params = {
        "basic": basic_info
    }
    return render_template("about.html", params=params)


@app.route("/projects/")
def projects():
    basic_info = portfolio.get_basic_info()
    projects_info = portfolio.get_projects()
    params = {
        "basic": basic_info,
        "projects": projects_info
    }
    return render_template("projects.html", params=params)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
