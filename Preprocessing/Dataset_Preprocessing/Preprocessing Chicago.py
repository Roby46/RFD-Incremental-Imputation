import pandas as pd
from unidecode import unidecode
import  numpy as np

df=pd.read_csv("../../Datasets/Original_Datasets/Chicago.csv", sep=',')
rows=5000
print(df)
print(df.columns.tolist())

def clean_data(text):
    text = str(text)  # Assicurati che il valore sia una stringa
    text = text.replace('""', '')  # Rimuove i doppi apici doppi
    text = text.replace(',', '')   # Rimuove le virgole
    text = text.replace('"', '')   # Rimuove i doppi apici singoli

    return text

df['Arrest'] = df['Arrest'].replace({True: 1, False: 0})
df['Domestic'] = df['Domestic'].replace({True: 1, False: 0})
df['Date'] = pd.to_datetime(df['Date'])  # Converte la colonna 'date' in tipo datetime

# Filtra il DataFrame per tenere solo gli eventi del 2017
df = df[df['Date'].dt.year == 2017]

# Remove the first column (unnamed column)
df = df.iloc[:, 1:]

print("DF Convertito e Filtrato\n", df)

#List of columns to eliminate
columns_to_delete = ["ID", "Case Number", "Date", "Beat", "FBI Code", "X Coordinate", "Y Coordinate", "Year", "Updated On", "Latitude", "Longitude", "Location"]

#Remove the specified columns from the DataFrame
df = df.drop(columns=columns_to_delete, errors="ignore")
df=df.dropna()

print(df)

df.replace('?', np.nan, inplace=True)
df=df.dropna()

print(df)

# Applica la funzione di pulizia a tutte le colonne di tipo object (stringa)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].apply(clean_data)

df=df.sample(rows)
df.columns = df.columns.str.replace(' ', '')

print(df)

df.to_csv(f"../../Datasets/Preprocessed_Datasets/Chicago_{rows}.csv", sep=';', index=False)
