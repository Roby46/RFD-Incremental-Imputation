import pandas as pd

df=pd.read_csv("../../Datasets/Original_Datasets/student_habits_performance.csv", sep=',')

print(df)
#Remove the specified columns from the DataFrame
#List of columns to eliminate
columns_to_delete = ["student_id"]
df = df.drop(columns=columns_to_delete, errors="ignore")


df=df.dropna()
df = df.drop(df.index[-1])

print(df)


print(df)
# #
filename=f"../../Datasets/Preprocessed_Datasets/Student_{len(df)}.csv"
df.to_csv(filename, sep=';', index=None, encoding='ascii')
# #
# # print(df)
