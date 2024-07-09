import pandas as pd

df=pd.read_csv("../../Datasets/Original_Datasets/NBA.csv", sep=',')

print(df)
df=df.dropna()
print(df)

#List of columns to eliminate
columns_to_delete = ["REB","AST","GP","MIN","FGM","FGA","3PM","3PA","FTM","FTA","TOV","PF","ORB","DRB","STL","BLK","birth_month","birth_date","height","weight","draft_round","draft_pick"]
#
#Remove the specified columns from the DataFrame
df = df.drop(columns=columns_to_delete, errors="ignore")

def clean_data(text):
    text = str(text)  # Assicurati che il valore sia una stringa
    text = text.replace('""', '')  # Rimuove i doppi apici doppi
    text = text.replace(',', '')   # Rimuove le virgole
    text = text.replace('"', '')   # Rimuove i doppi apici singoli
    return text

# Applica la funzione di pulizia a tutte le colonne di tipo object (stringa)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].apply(clean_data)


print(df.columns.tolist())

print(df)
#
rows=3200
df=df.sample(rows)
# df.columns = df.columns.str.replace(' ', '_')
#
filename=f"../../Datasets/Preprocessed_Datasets/NBA_{len(df)}.csv"
df.to_csv(filename, sep=';', index=None)
#
# print(df)
