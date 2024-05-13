from project_iris import app_iris 
from flask import render_template
import pandas as pd
from sklearn.datasets import load_iris

@app_iris.route("/")
@app_iris.route("/index")
def index():
    df=load_iris()
    df_X=df.data
    df_Y=df.target
    feature_names=df.feature_names
    df_iris=pd.DataFrame(df_X, columns=feature_names)
    df_iris_table=df_iris.to_html(header="true", table_id="table")
    #print(df_iris)
    return render_template("index.html",
                           iris_data=df_iris_table)