from flask import Flask, render_template, request, url_for, redirect
from utils.portfolio import Portfolio

app = Flask(__name__)
port = Portfolio(url="https://gitconnected.com/v1/portfolio/srakhe")


@app.route("/")
def index():
    basic_info = port.get_info(key="basics")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
