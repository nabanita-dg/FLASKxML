import pandas as pd
from sklearn.datasets import load_iris

def iris_process():
    df=load_iris()
    df_X=df.data
    df_Y=df.target
    feature_names=df.feature_names
    df_iris_input=pd.DataFrame(df_X, columns=feature_names)
    df_iris_input_table=df_iris_input.to_html(header="true", table_id="table")

    df_iris_target=pd.DataFrame(df_Y)   
    df_iris_target_table=df_iris_target.to_html(header="false",table_id="table2")

    iris_dict={"iris_input_table":df_iris_input_table,
               "iris_target_table":df_iris_target_table}
    return iris_dict