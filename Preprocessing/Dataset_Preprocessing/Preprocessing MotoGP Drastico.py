import pandas as pd
import numpy as np
import unidecode

# Lettura del file originale
df = pd.read_csv("../../Datasets/Original_Datasets/MotoGP.csv", sep=';')

# Sostituisce i valori mancanti (?) con NaN e rimuove le righe con valori mancanti
df.replace('?', np.nan, inplace=True)
df = df.dropna()

# Rimuove le colonne specificate
columns_to_delete = ["speed", "time", "sequence"]
df = df.drop(columns=columns_to_delete, errors="ignore")

# Funzione per pulire i dati rimuovendo virgole, apici e normalizzando i caratteri
def clean_data(text):
    text = str(text)
    text = text.replace('""', '')  # Rimuove i doppi apici doppi
    text = text.replace(',', '')   # Rimuove le virgole
    text = text.replace('"', '')   # Rimuove i doppi apici singoli
    text = text.replace('\'', '')  # Rimuove gli apici singoli
    return text

# Funzione per rimuovere caratteri non ASCII e sostituirli con underscore
def remove_non_ascii_drastic(text):
    # Rimuove qualsiasi carattere non ASCII o lo sostituisce con '_'
    return ''.join(c if ord(c) < 128 else '_' for c in text)

# Applica la funzione per rimuovere accenti e normalizzare ulteriormente (es. da 'è' a 'e')
def normalize_text(text):
    return unidecode.unidecode(text) if isinstance(text, str) else text

# Creiamo un nuovo DataFrame vuoto con le stesse colonne
new_df = pd.DataFrame(columns=df.columns)

# Itera su tutte le righe e colonne del DataFrame originale
for idx, row in df.iterrows():
    new_row = {}
    for col in df.columns:
        value = row[col]
        # Pulizia dei dati per ogni valore
        if isinstance(value, str):  # Se il valore è una stringa, lo puliamo
            value = clean_data(value)
            value = remove_non_ascii_drastic(value)
            value = normalize_text(value)
        # Inserisci il valore pulito nella nuova riga
        new_row[col] = value
    # Aggiungi la nuova riga pulita al nuovo DataFrame
    new_df = new_df.append(new_row, ignore_index=True)

# Solo piloti in top 10
new_df = new_df[new_df['position'].between(1, 10)]

# Crea un nuovo file CSV ripulito
filename = f"../../Datasets/Preprocessed_Datasets/MotoGP_REBUILT_{len(new_df)}.csv"
new_df.to_csv(filename, sep=';', index=False, encoding="ascii")  # Salva in codifica ASCII

print(f"File salvato: {filename}")
print(new_df)
