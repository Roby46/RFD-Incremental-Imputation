import pandas as pd

df=pd.read_csv("../../Datasets/Original_Datasets/Hospital_Staff.csv", sep=',')
rows=6000

print(df)
df=df.dropna()

#List of columns to eliminate
columns_to_delete = ["Begin Date", "End Date"]

#Remove the specified columns from the DataFrame
df = df.drop(columns=columns_to_delete, errors="ignore")

df=df.sample(rows)
df.columns = df.columns.str.replace(' ', '_')

filename=f"../../Datasets/Preprocessed_Datasets/Hospital_Staff_{rows}.csv"
df.to_csv(filename, sep=';', index=None)

print(df)
