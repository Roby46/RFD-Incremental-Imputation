import pandas as pd
import numpy as np
import unidecode

# Lettura del file originale
df = pd.read_csv("../../Datasets/Original_Datasets/police_MNAR.csv", sep=';')


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

# Crea una lista per raccogliere le righe pulite
cleaned_rows = []

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
    # Aggiungi la nuova riga pulita alla lista
    cleaned_rows.append(new_row)

# Crea un nuovo DataFrame con le righe pulite
new_df = pd.DataFrame(cleaned_rows)

# Crea un nuovo file CSV ripulito
filename = f"../../Datasets/Preprocessed_Datasets/police_MNAR.csv"
new_df.to_csv(filename, sep=';', index=False, encoding="ascii")  # Salva in codifica ASCII

print(f"File salvato: {filename}")
print(new_df)
