import pandas as pd
import numpy as np
import unidecode

df=pd.read_csv("../../Datasets/Original_Datasets/MotoGP.csv", sep=';')

print(df)

df.replace('?', np.nan, inplace=True)
df=df.dropna()
print(df)
#
#List of columns to eliminate
columns_to_delete = ["speed", "time", "sequence"]

#Remove the specified columns from the DataFrame
df = df.drop(columns=columns_to_delete, errors="ignore")

# Funzione per pulire i dati rimuovendo le virgole e i doppi apici
def clean_data(text):
    text = str(text)
    text = text.replace('""', '')  # Rimuove i doppi apici doppi
    text = text.replace(',', '')   # Rimuove le virgole
    text = text.replace('"', '')   # Rimuove i doppi apici singoli
    return text

# Applica la funzione di pulizia a tutte le colonne di tipo object (stringa)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].apply(clean_data)

#Solo piloti in top10
df = df[df['position'].between(1, 10)]

filename=f"../../Datasets/Preprocessed_Datasets/MotoGP_{len(df)}.csv"
df.to_csv(filename, sep=';', index=None)

print(df)
