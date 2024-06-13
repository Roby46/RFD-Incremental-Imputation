import pandas as pd

df=pd.read_csv("../../Datasets/Original_Datasets/EV_Vehicles.csv", sep=',')
rows=4000

print(df)
df=df.dropna()

#List of columns to eliminate
columns_to_delete = ["VIN (1-10)", "Postal Code", "Base MSRP", "DOL Vehicle ID", "Electric Utility", "2020 Census Tract", "Vehicle Location"]

#Remove the specified columns from the DataFrame
df = df.drop(columns=columns_to_delete, errors="ignore")

df=df.sample(rows)
df.columns = df.columns.str.replace(' ', '_')

filename=f"../../Datasets/Preprocessed_Datasets/EV_Vehicles_{rows}.csv"
df.to_csv(filename, sep=';', index=None)

print(df)
