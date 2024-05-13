from project_iris import app_iris

if __name__=='__main__':
    app_iris.debug = True
    app_iris.run(host = '0.0.0.0', port = 8000)