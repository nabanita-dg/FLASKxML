from flask import Blueprint, render_template, redirect, url_for
from iris_api.process import iris_process

app_iris = Blueprint("iris_bp", __name__, template_folder="templates", static_folder='static')

@app_iris.route("/")
def home():
    return redirect(url_for("iris_bp.index"))

@app_iris.route("/index")
def index():
    iris_dict=iris_process()
    return render_template("index.html",
                           iris_input_table=iris_dict["iris_input_table"],
                           iris_target_table=iris_dict["iris_target_table"])