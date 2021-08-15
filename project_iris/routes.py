from project_iris import app_iris 
from flask import render_template

@app_iris.route("/")
@app_iris.route("/index")
def index():
    return render_template("index.html")