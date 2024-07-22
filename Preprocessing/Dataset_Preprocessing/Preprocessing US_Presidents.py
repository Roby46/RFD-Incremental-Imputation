import pandas as pd
import numpy as np
import unidecode

df=pd.read_csv("../../Datasets/Original_Datasets/US_Presidents.csv")

print(df)
# Rimuovi tutte le virgolette doppie e singole
df.replace({'"': '', "'": ''}, regex=True, inplace=True)

columns_to_delete = ["notes"]
df = df.drop(columns=columns_to_delete, errors="ignore")

df=df.dropna()

print(df)

# Funzione per dividere i nomi
def split_name(candidate):
    parts = candidate.split(',')
    if len(parts) == 2:
        return parts[0].strip(), parts[1].strip()
    else:
        return parts[0].strip(), ''


def clean_data(text):
    text = str(text)  # Assicurati che il valore sia una stringa
    text = text.replace('""', '')  # Rimuove i doppi apici doppi
    text = text.replace(',', '')   # Rimuove le virgole
    text = text.replace('"', '')   # Rimuove i doppi apici singoli
    return text




# Applica la funzione di split ai candidati
df[['candidate_last_name', 'candidate_first_name']] = df['candidate'].apply(split_name).apply(pd.Series)

# Riorganizza il DataFrame per visualizzare il risultato
df = df[['year', 'state', 'state_po', 'state_fips', 'state_cen', 'state_ic', 'office', 'candidate_last_name', 'candidate_first_name', 'party_detailed', 'writein', 'candidatevotes', 'totalvotes', 'version', 'party_simplified']]


# Applica la funzione di pulizia a tutte le colonne di tipo object (stringa)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].apply(clean_data)


# Mostra il DataFrame preprocessato
print(df)
print(df.columns)
columns_to_delete = ["writein", "version", "office", "state_ic","state_cen"]
df = df.drop(columns=columns_to_delete, errors="ignore")
print(df)


filename=f"../../Datasets/Preprocessed_Datasets/US_Presidents_{len(df)}.csv"
df.to_csv(filename, sep=';', index=None, encoding="ascii")
