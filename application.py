
from flask import Flask, render_template
import requests

application = Flask(__name__)


@application.route("/")
def root():
    return render_template("index.html")


@application.route("/hello")
def index():
    return "Hello World from COE Team."

@application.route("/call")
def call():
    url = 'http://internal-alb2-1541729269.ap-south-1.elb.amazonaws.com'
    data = requests.get(url)
    return data.json()

if __name__ == "__main__":
    application.run(host="0.0.0.0",port=8000)
