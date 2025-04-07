import re
from datetime import datetime

import pandas as pd
import numpy as np
import unidecode

def time_to_seconds(time_str):
    try:
        minutes, seconds = map(int, time_str.split(':'))
        return minutes * 60 + seconds
    except Exception as e:
        return None

# Funzione per convertire la data in formato DD/MM/YY
def convert_date(date_str):
    try:
        return datetime.strptime(date_str, '%d-%b-%y').strftime('%d/%m/%y')
    except Exception as e:
        return None


# Funzione per convertire il prezzo rimuovendo il simbolo del dollaro
def convert_price(price_str):
    try:
        # Rimuove il simbolo "$" e converte in float
        return float(price_str.replace('$', '').strip())
    except Exception as e:
        return None


# Lettura del file originale
df = pd.read_csv("../../Datasets/Original_Datasets/iTunes.csv", sep=',')


print(df)

# Applica le funzioni di conversione
df['Time'] = df['Time'].apply(time_to_seconds)
df['Released'] = df['Released'].apply(convert_date)
df['Price'] = df['Price'].apply(convert_price)


# # Sostituisce i valori mancanti (?) con NaN e rimuove le righe con valori mancanti
df.replace('?', np.nan, inplace=True)
df = df.dropna()

print(df)
#
# # Rimuove le colonne specificate
columns_to_delete = ["id"]
df = df.drop(columns=columns_to_delete, errors="ignore")
#
# # Funzione per pulire i dati rimuovendo virgole, apici e normalizzando i caratteri


def clean_data(text):
    text = str(text)

    # Rimuove tutto ciò che è composto solo da underscore/spazi **all'inizio**
    text = re.sub(r'^[_\s]+', '', text)

    # Rimuove simboli indesiderati
    text = text.replace('""', '')
    text = text.replace(',', '')
    text = text.replace('"', '')
    text = text.replace('\'', '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace('.', ' ')
    text = text.replace('*', '')
    text = text.replace('$', '')
    text = text.replace('&', 'and')
    text = text.replace('-', '')
    text = text.replace('[', '')
    text = text.replace(']', '')
    text = text.replace('?', '')
    text = text.replace('!', '')
    text = text.replace('``', '')
    # Rimpiazza underscore nel resto del testo con spazi
    text = text.replace('_', '')
    text = text.replace(';', '')
    text = text.replace(':', '')


    # Riduce spazi multipli a uno solo
    text = re.sub(r'\s+', ' ', text)

    # Rimuove spazi all’inizio e alla fine
    return text.strip()


# Funzione per rimuovere caratteri non ASCII e sostituirli con underscore
def remove_non_ascii_drastic(text):
   # Rimuove qualsiasi carattere non ASCII o lo sostituisce con '_'
   return ''.join(c if ord(c) < 128 else '' for c in text)

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

print(new_df)

new_df=new_df.sample(3000)
# # Crea un nuovo file CSV ripulito
filename = (f"../../Datasets/Preprocessed_Datasets/iTunes_{len(new_df)}.csv")
new_df.to_csv(filename, sep=';', index=False, encoding="ascii")  # Salva in codifica ASCII
#
print(f"File salvato: {filename}")
#print(new_df)
