import pandas as pd
import xml.etree.ElementTree as ET
import os
import csv
import numpy as np

def normalize_dataframe(df):
    # Creare un dizionario per salvare i minimi e i massimi
    min_max_values = {}

    # Copiare il dataframe per evitare modifiche sull'originale
    df_normalized = df.copy()

    # Identificare le colonne numeriche
    numeric_columns = df.select_dtypes(include=['number']).columns

    for col in numeric_columns:
        # Calcolare il minimo e il massimo per la colonna corrente
        col_min = df[col].min()
        col_max = df[col].max()

        # Salvare i valori minimi e massimi nel dizionario
        min_max_values[col] = {'min': col_min, 'max': col_max}

        # Normalizzare la colonna
        df_normalized[col] = (df[col] - col_min) / (col_max - col_min)
        df_normalized[col] = df_normalized[col].round(3)

    return df_normalized, min_max_values


# Funzione per normalizzare un nuovo DataFrame utilizzando minimi e massimi predefiniti
def normalize_new_dataframe(df, min_max_values):
    df_normalized = df.copy()
    df_normalized = df_normalized.replace('?', np.nan)

    for col in min_max_values:
        col_min = min_max_values[col]['min']
        col_max = min_max_values[col]['max']

        # Evitare la divisione per zero nel caso in cui min e max siano uguali
        if col_max != col_min:
            print(df_normalized[col])
            df_normalized[col] = (df[col] - col_min) / (col_max - col_min)
        else:
            df_normalized[col] = 0  # O qualsiasi altro valore appropriato

    return df_normalized


# Carica il file XML
tree = ET.parse(f'XML Files/Bikes_similarity_rules.xml')
root = tree.getroot()

# Leggi il CSV
version=4
MV=18450

import pandas as pd

def get_headers(header_file, dataset_name):
    with open(header_file, 'r') as file:
        for line in file:
            headers = line.strip().split(';')
            if headers[-1] == dataset_name:
                return headers[:-1]
    return []


def fill_missing_values(dataset_path, results_path, header_file, dataset_name, output_path, full_dataset_path):

    # Ottieni gli header dal file delle intestazioni
    headers = get_headers(header_file, dataset_name)

    # Leggi il dataset con valori mancanti usando gli header ottenuti
    df = pd.read_csv(dataset_path, delimiter=';', names=headers)

    print(df)

    # Leggi il file dei risultati dell'imputation
    results = pd.read_csv(results_path, delimiter=';')

    print(results)

    # Scorri il file dei risultati e riempi i valori mancanti nel dataset
    for index, row in results.iterrows():
        row_index = row['riga']
        column_name = row['nome attributo']
        value_to_impute = row['valore imputato']
        # Controlla se effettivamente c'era un valore mancante
        if (df.at[row_index-1, column_name]=='?'):
            # Se l'algoritmo ha imputato un valore, riempi il valore mancante
            if value_to_impute != '?':
                df.at[row_index-1, column_name] = value_to_impute
        else:
            print(row_index, column_name, value_to_impute)
            print(df.at[row_index -1, column_name])
            print("Qualcosa non va")

    print(df)

    full_dataset=pd.read_csv(full_dataset_path,sep=';')
    df_normalized, min_max_values = normalize_dataframe(full_dataset)

    print(df_normalized)
    print(min_max_values)

    df=normalize_new_dataframe(df, min_max_values)

    print(df)
    # Salva il dataset con i valori imputati
    #df.to_csv(output_path, index=False, sep=';')


# Esempio di utilizzo
dataset_path = f'../../Datasets/Missing_Datasets/EV_Vehicles_4000/EV_Vehicles_4000_4000_1.csv'
full_dataset_path=f'../../Datasets/Preprocessed_Datasets/EV_Vehicles_4000.csv'
results_path = '../Imputation_Results/Imputation_Pipeline_Results/EV_Vehicles_4000/1/EV_Vehicles_4000_4000_1.csv'
output_path = 'path_to_your_output.csv'
dataset_name='EV_Vehicles_4000_4000_1'
header_file= f'../../Preprocessing/Headers/Headers.csv'

fill_missing_values(dataset_path, results_path, header_file, dataset_name, output_path, full_dataset_path)
