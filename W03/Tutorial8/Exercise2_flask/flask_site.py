import json
import requests
from flask import Blueprint, render_template

site = Blueprint("site", __name__)


# Client webpage.
@site.route("/")
def index():
    # Use REST API.
    response = requests.get("http://127.0.0.1:5000/person")
    data = json.loads(response.text)

    return render_template("index.html", people=data)
