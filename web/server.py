from flask import Flask, render_template, request, url_for, redirect
from utils.portfolio import Portfolio

app = Flask(__name__)
port = Portfolio(url="https://gitconnected.com/v1/portfolio/srakhe")


@app.route("/")
def index():
    basic_info = port.get_basic_info()
    params = {
        "basic": basic_info
    }
    return render_template("index.html", params=params)


if __name__ == "__main__":
    app.run(debug=True)
