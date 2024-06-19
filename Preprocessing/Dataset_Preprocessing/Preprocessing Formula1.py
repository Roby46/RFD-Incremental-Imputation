import pandas as pd
from unidecode import unidecode
df_drivers=pd.read_csv("../../Datasets/Original_Datasets/drivers_updated.csv", sep=',',encoding='utf-8')
df_winners=pd.read_csv("../../Datasets/Original_Datasets/winners.csv", sep=',', encoding='utf-8')
print(df_winners)

df_winners['Driver'] = df_winners['Winner'].str.strip()

#df_winners['Date'] = pd.to_datetime(df_winners['Date']).dt.year


df= pd.merge(df_winners, df_drivers[['Name Code', 'Nationality']], on='Name Code', how='left')

# Normalizziamo i caratteri speciali nei nomi dei piloti
df['Driver'] = df['Driver'].apply(unidecode)
df['Driver'] = df['Driver'].str.replace(r'\s+', ' ', regex=True)


rows=4000

df=df.dropna()

print(df)

#List of columns to eliminate
columns_to_delete = ["Laps", "Time"]

#Remove the specified columns from the DataFrame
df = df.drop(columns=columns_to_delete, errors="ignore")


df=df.sample(rows)
df.columns = df.columns.str.replace(' ', '_')

filename=f"../../Datasets/Preprocessed_Datasets/Formula1_{rows}.csv"
df.to_csv(filename, sep=';', index=None, encoding='utf-8')

print(df)
