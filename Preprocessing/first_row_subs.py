import os
import pandas as pd

# Directory contenente i file CSV
directory = './first_row_invalid'


# Funzione per gestire ogni file CSV
def process_csv_file(file_path):
    # Legge il file CSV
    df = pd.read_csv(file_path, header=None, delimiter=";")

    print(f"\nProcessing file: {file_path}")

    # Trova la prima riga senza valori nulli (senza "?")
    first_non_null_index = None
    for i, row in df.iterrows():
        if '?' not in row.values:
            first_non_null_index = i
            break

    if first_non_null_index is not None:
        # Salva una copia della prima riga
        first_row = df.iloc[0].copy()

        print(f"Scambiando la riga 0 con la riga {first_non_null_index}.")

        # Sostituisci la prima riga con la riga trovata
        df.iloc[0] = df.iloc[first_non_null_index]

        # Sostituisci la riga trovata con la prima riga salvata
        df.iloc[first_non_null_index] = first_row

        print(f"Riga 0 (originariamente): {first_row.values}")
        print(f"Riga {first_non_null_index} (nuova riga 0): {df.iloc[0].values}")
    else:
        print("Non è stata trovata nessuna riga senza valori nulli.")

    # Sovrascrivi il file con le modifiche
    df.to_csv(file_path, header=False, index=False,sep=";")


# Elabora ogni file CSV nella cartella
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        file_path = os.path.join(directory, filename)
        process_csv_file(file_path)

print("Processamento completato!")