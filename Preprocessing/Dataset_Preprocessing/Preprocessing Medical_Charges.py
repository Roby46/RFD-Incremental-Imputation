import pandas as pd
pd.set_option('display.max_columns', None)
# Leggi il file Excel e carica i dati in un DataFrame
df = pd.read_excel("../../Datasets/Original_Datasets/medical_charge_nominal.xlsx", engine='openpyxl')
print(df)

# Split del valore in due colonne: 'codice' e 'descrizione'
df[['codice', 'descrizione']] = df['drg_definition'].astype(str).str.split(' - ', n=1, expand=True)
print(df[['codice', 'descrizione']])

# 2. Eliminare le colonne non necessarie
df.drop(columns=['Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'provider_zip_code','drg_definition'], inplace=True)

# Funzione per convertire il valore o restituire un segnaposto in caso di errore
def extract_first_number(value):
    if isinstance(value, str) and '--' in value:  # Controlla se value è una stringa e contiene '--'
        try:
            return float(value.split('--')[0])  # Split e conversione
        except (ValueError, IndexError):
            return -9999  # Restituisce un segnaposto in caso di errore
    return -9999  # Restituisce un segnaposto se value non è una stringa o non è valido

# Applica la funzione a ciascuna colonna e converte i risultati
for col in ['average_covered_charges', 'average_total_payments', 'average_medicare_payments']:
    if col in df.columns:  # Controlla se la colonna esiste nel DataFrame
        df[col] = df[col].apply(extract_first_number)
    else:
        print(f"Colonna {col} non trovata nel DataFrame.")

# Rimuovi le righe con il segnaposto -9999
df = df[df[['average_covered_charges', 'average_total_payments', 'average_medicare_payments']].ne(-9999).all(axis=1)]

# Reimposta l'indice
df.reset_index(drop=True, inplace=True)

# Visualizza il risultato finale
print(df)

# Funzione per pulire i dati
def clean_data(text):
    text = str(text)  # Assicurati che il valore sia una stringa
    text = text.replace('""', '')  # Rimuove i doppi apici doppi
    text = text.replace(',', '')   # Rimuove le virgole
    text = text.replace('"', '')   # Rimuove i doppi apici singoli
    text = text.replace('/', '')   # Rimuove i caratteri '/'
    return text

# Applica la funzione di pulizia a tutte le colonne di tipo object (stringa)
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].apply(clean_data)

df=df.sample(5000)

# Salva il DataFrame pulito in un file CSV (decommenta per salvare)
df.to_csv(f"../../Datasets/Preprocessed_Datasets/Med_Ch_{len(df)}.csv", sep=';', index=None, encoding='ascii')
