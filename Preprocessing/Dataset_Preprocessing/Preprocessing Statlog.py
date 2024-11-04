import pandas as pd

df=pd.read_csv("../../Datasets/Original_Datasets/Statlog.csv", sep=',')

print(df)

# #
filename=f"../../Datasets/Preprocessed_Datasets/Statlog_{len(df)}.csv"
df.to_csv(filename, sep=';', index=None)
# #
# # print(df)
