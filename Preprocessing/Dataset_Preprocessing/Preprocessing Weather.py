import pandas as pd

df=pd.read_csv("../../Datasets/Original_Datasets/Weather.csv", sep=',')
rows=2500

print(df)
df=df.dropna()

def clean_data(text):
    text = str(text)  # Assicurati che il valore sia una stringa
    text = text.replace('""', '')  # Rimuove i doppi apici doppi
    text = text.replace(',', '')   # Rimuove le virgole
    text = text.replace('"', '')   # Rimuove i doppi apici singoli
    return text

# Applica la funzione di pulizia a tutte le colonne di tipo object (stringa)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].apply(clean_data)

df.columns = df.columns.str.replace(' ', '_')

print(df)
#
# #List of columns to eliminate
# columns_to_delete = ["VIN (1-10)", "Postal Code", "Base MSRP", "DOL Vehicle ID", "Electric Utility", "2020 Census Tract", "Vehicle Location"]
#
# #Remove the specified columns from the DataFrame
# df = df.drop(columns=columns_to_delete, errors="ignore")
#
df=df.sample(rows)
#
filename=f"../../Datasets/Preprocessed_Datasets/Weather_{rows}.csv"
df.to_csv(filename, sep=';', index=None)

# print(df)
