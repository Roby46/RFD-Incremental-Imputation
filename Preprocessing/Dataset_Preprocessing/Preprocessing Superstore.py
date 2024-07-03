import pandas as pd
import numpy as np
import unidecode

df=pd.read_csv("../../Datasets/Original_Datasets/Superstore.csv")
rows=4500
print(df)
df = df.applymap(lambda x: x.replace('\xa0', ' ') if isinstance(x, str) else x)
df=df.dropna()

columns_to_delete = ["Row ID","Order ID","Order Date","Ship Date","Postal Code","Category","Country"]


#List of columns to eliminate


#Remove the specified columns from the DataFrame
df = df.drop(columns=columns_to_delete, errors="ignore")

df.columns = df.columns.str.replace(' ', '_')

df["Sales"]=df["Sales"].round(2)
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

print(df)

# Funzione per rimuovere i caratteri non ASCII
def remove_non_ascii(text):
    return ''.join(c for c in text if ord(c) < 128)

# Applica la funzione a tutte le stringhe nel DataFrame
df = df.applymap(lambda x: remove_non_ascii(x) if isinstance(x, str) else x)

df=df.sample(rows)

filename=f"../../Datasets/Preprocessed_Datasets/superstore_{len(df)}.csv"
df.to_csv(filename, sep=';', index=None, encoding="ascii")
