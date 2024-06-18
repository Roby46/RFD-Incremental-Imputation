import pandas as pd
import numpy as np


#The original books dataset contained 55 malformed rows. These were deleted in advance.
df=pd.read_csv("../../Datasets/Original_Datasets/books.csv", sep=';')
rows=10

df.drop(df.columns[len(df.columns)-1], axis=1, inplace=True)
print(df)

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

filename=f"../../Datasets/Preprocessed_Datasets/books_{rows}.csv"
df.to_csv(filename, sep=';', index=None)

print(df)
