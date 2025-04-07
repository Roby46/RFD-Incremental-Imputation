import pandas as pd


def ordina_csv(file_input, file_output):
    # Legge il CSV
    df = pd.read_csv(file_input, sep=';')

    # Ordina per dataset, algoritmo, MV e version
    df_sorted = df.sort_values(by=['dataset', 'algoritmo', 'MV', 'version'])

    # Salva il CSV ordinato
    df_sorted.to_csv(file_output, sep=';', index=False)

    print(f"File ordinato salvato come {file_output}")


# Esempio di utilizzo
ordina_csv('ALL_Results_v3.csv', 'ALL_Results_v3_sorted.csv')
