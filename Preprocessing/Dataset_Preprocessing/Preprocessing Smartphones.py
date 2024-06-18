import pandas as pd
import numpy as np
import unidecode

df=pd.read_csv("../../Datasets/Original_Datasets/smartphones.csv")

print(df)

df.replace('?', np.nan, inplace=True)
print(df)
#
#List of columns to eliminate
columns_to_delete = ["has_ir_blaster", "fast_charging_available","fast_charging","refresh_rate","num_rear_cameras","num_front_cameras","primary_camera_rear","primary_camera_front","extended_memory_available","extended_upto","resolution_width","resolution_height",
                     "has_5g","has_nfc","battery_capacity","screen_size"]

#Remove the specified columns from the DataFrame
df = df.drop(columns=columns_to_delete, errors="ignore")

df = df[~df.apply(lambda row: row.astype(str).str.contains('nan')).any(axis=1)]


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
df=df.dropna()

filename=f"../../Datasets/Preprocessed_Datasets/smartphones_{len(df)}.csv"
df.to_csv(filename, sep=';', index=None)

print(df)
