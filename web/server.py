from flask import Flask, render_template, url_for, redirect, send_file
from web.utils.portfolio import Portfolio
from web.utils.custom import CustomUtils

app = Flask(__name__)
portfolio = Portfolio(url="https://gitconnected.com/v1/portfolio/srakhe")
utils = CustomUtils(root_path=app.root_path)


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
    about_info = portfolio.get_about_info()
    params = {
        "basic": basic_info,
        "about": about_info
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


@app.route("/contact/")
def contact():
    basic_info = portfolio.get_basic_info()
    params = {
        "basic": basic_info
    }
    return render_template("contact.html", params=params)


@app.route("/refresh/")
def refresh():
    portfolio.refresh()
    return redirect(url_for("index"))


@app.route("/download/<path:filename>/")
def download(filename):
    resume_url = utils.get_file_url(file_name=filename)
    send_file(resume_url, as_attachment=True)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
