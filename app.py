from flask import Flask, render_template, url_for, redirect, send_from_directory, request
from utils.portfolio import Portfolio
from utils.custom import CustomUtils

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


@app.route("/blog/", defaults={'tag': None}, methods=['GET', 'POST'])
@app.route("/blog/<tag>/", methods=['GET', 'POST'])
def blog(tag):
    if request.method == "GET":
        basic_info = portfolio.get_basic_info()
        tags_list = utils.get_tags()
        if tag:
            blogs_list = utils.get_blog_posts(for_tag=tag)
        else:
            blogs_list = utils.get_blog_posts()
        params = {
            "basic": basic_info,
            "tags_list": tags_list,
            "blogs_list": blogs_list
        }
        return render_template("blog.html", params=params)
    if request.method == "POST":
        tag_name = request.form.get("tag_name")
        return redirect(url_for("blog", tag=tag_name))


@app.route("/view/<filename>")
def view(filename):
    basic_info = portfolio.get_basic_info()
    blog_data = utils.get_blog_data(file_name=filename)
    params = {
        "basic": basic_info,
        "blog_data": blog_data
    }
    return render_template("view.html", params=params)


@app.route("/refresh/")
def refresh():
    portfolio.refresh()
    return redirect(url_for("index"))


@app.route("/download/<path:filename>/")
def download(filename):
    resume_url = utils.get_file_url()
    return send_from_directory(directory=resume_url, path=filename, mimetype='application/pdf')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
