from flask import Flask, redirect, url_for
from iris_api.routes import app_iris
from knn_api.knn_routes import app_knn

app = Flask(__name__)
app.register_blueprint(app_iris, url_prefix="/iris")
app.register_blueprint(app_knn, url_prefix="/knn")

@app.route("/")
def home():
    return redirect(url_for("iris_bp.home"))

if __name__=='__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)