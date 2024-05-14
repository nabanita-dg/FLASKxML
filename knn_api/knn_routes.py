from flask import Blueprint

app_knn=Blueprint("knn_bp",__name__,template_folder="templates")

@app_knn.route("/")
def index():
    return "<h1>KNN Application</h1>"