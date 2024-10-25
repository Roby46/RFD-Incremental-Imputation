import pandas as pd
import numpy as np


# Example usage
if __name__ == "__main__":
    df = pd.read_csv("../../Datasets/Original_Datasets/Cleveland.csv")
    #df=df.drop(columns=['id'])
    print(df.columns.tolist())
    print(df)
    df.replace('?', np.nan, inplace=True)
    df=df.dropna()


    numeric_cols = df.select_dtypes(include='number')
    # 2. Arrotonda i valori numerici (ad esempio a 2 decimali)
    df[numeric_cols.columns] = numeric_cols.round().astype(int)
    print(df)
    df.to_csv(f"../../Datasets/Preprocessed_Datasets/Cleveland.csv", index=None, sep=";")



    # # Perform feature selection
    # selected_df = entropy_based_feature_selection(df, target_column='Cover_Type', num_features=12)
    #
    # selected_df.to_csv("Red_Covtype.csv" ,index=None)
    #
    # print(selected_df)
