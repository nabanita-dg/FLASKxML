import pandas as pd
from sklearn.datasets import load_iris

def iris_process():
    df=load_iris()
    df_X=df.data
    df_Y=df.target
    feature_names=df.feature_names
    df_iris=pd.DataFrame(df_X, columns=feature_names)
    
    df_iris_table=df_iris.to_html(header="true", table_id="table")
    iris_dict={"iris_input_table":df_iris_table,
               "iris_target_table":df_iris_table}
    return iris_dict