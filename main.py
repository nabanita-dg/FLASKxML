from flask import Flask
from iris_api.routes import app_iris
from knn_api.knn_routes import app_knn

app = Flask(__name__)
app.register_blueprint(app_iris, url_prefix="/iris")
app.register_blueprint(app_knn, url_prefix="/knn")

if __name__=='__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)