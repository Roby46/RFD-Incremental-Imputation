import pandas as pd

df=pd.read_csv("../../Datasets/Original_Datasets/cat_breeds_clean.csv", sep=';')

print(df)
df=df.dropna()
print(df)

#List of columns to eliminate
columns_to_delete = ["Preferred_food","Latitude","Longitude","Owner_play_time_minutes","Preferred_food","Sleep_time_hours","Eye_colour","Gender"]

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
#
filename=f"../../Datasets/Preprocessed_Datasets/Cats_{len(df)}.csv"
df.to_csv(filename, sep=';', index=None)
#
# print(df)
