import os
import pandas as pd

# Percorso della cartella contenente i CSV
cartella_csv = 'C:/Users\gianp\Desktop\Codes\github\RFD-Incremental-Imputation/risultati_test_discovery\incremental/police_FD'

# Scorri tutti i file nella cartella
for nome_file in os.listdir(cartella_csv):
    if nome_file.endswith('.csv'):
        percorso_file = os.path.join(cartella_csv, nome_file)

        # Leggi il file CSV con pandas
        df = pd.read_csv(percorso_file, sep=';', dtype=str)

        # Verifica se l'ultima colonna è tutta vuota
        if df.columns[-1] and df[df.columns[-1]].isna().all():
            df = df.iloc[:, :-1]  # Rimuove l'ultima colonna

        # Sovrascrive il file originale
        df.to_csv(percorso_file, sep=';', index=False)

print("Pulizia completata.")
