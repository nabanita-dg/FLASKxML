from flask import Blueprint, render_template

app_knn=Blueprint("knn_bp",__name__,template_folder="templates", static_folder='static')

@app_knn.route("/")
def index():
    return render_template("knn_index.html")