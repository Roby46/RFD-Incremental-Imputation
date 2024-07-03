import pandas as pd
import numpy as np

df=pd.read_csv("../../Datasets/Original_Datasets/cacao.csv")
rows=4000

print(df)

df.columns = ['Company',"Bean_Origin","REF","R_Date","Cocoa","C_Location","Rating","Bean_Type","Broad_Origin"]
df=df.dropna()

#List of columns to eliminate
columns_to_delete = ["Bean_Type"]

#Remove the specified columns from the DataFrame
df = df.drop(columns=columns_to_delete, errors="ignore")

print(df)


# # Sostituire '?' con np.nan
# df.replace('?', np.nan, inplace=True)
# df=df.dropna()
# print(df)

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

filename=f"../../Datasets/Preprocessed_Datasets/cacao_{len(df)}.csv"
df.to_csv(filename, sep=';', index=None)
