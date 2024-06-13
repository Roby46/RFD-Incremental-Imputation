import pandas as pd
import numpy as np

df=pd.read_csv("../../Datasets/Original_Datasets/olympics.csv", sep=';')
rows=7500

print(df)
# Sostituire '?' con np.nan
df.replace('?', np.nan, inplace=True)
df=df.dropna()
print(df)
#
#List of columns to eliminate
columns_to_delete = ["ID", "Event"]

#Remove the specified columns from the DataFrame
df = df.drop(columns=columns_to_delete, errors="ignore")

# Funzione per pulire i dati rimuovendo le virgole e i doppi apici
def clean_data(text):
    text = str(text)  # Assicurati che il valore sia una stringa
    text = text.replace('""', '')  # Rimuove i doppi apici doppi
    text = text.replace(',', '')   # Rimuove le virgole
    text = text.replace('"', '')   # Rimuove i doppi apici singoli
    return text

# Applica la funzione di pulizia a tutte le colonne di tipo object (stringa)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].apply(clean_data)

df=df.sample(rows)

filename=f"../../Datasets/Preprocessed_Datasets/Olympics_{rows}.csv"
df.to_csv(filename, sep=';', index=None)

print(df)
