import pandas as pd
import xml.etree.ElementTree as ET
import os
import csv
import numpy as np
import math

xml_file = 'XML Files/Statlog_similarity_rules.xml'
# Carica il file XML
tree = ET.parse(xml_file)
root = tree.getroot()


def computeRMSE(raw_rmse_data, string_cols):
    total_error = 0
    count = 0

    for col in raw_rmse_data:
        for original, imputed in raw_rmse_data[col]:
            if col in string_cols:
                # Confronto per stringhe
                error = 1 if original != imputed else 0
            else:
                # Confronto per numeri
                original = float(original)
                imputed = float(imputed)
                error = (original - imputed) ** 2
            # if(error>0):
            #     print(original,imputed)
            total_error += error
            count += 1

    rmse = math.sqrt(total_error / count)
    print("RMSE:", rmse)
    return rmse


def parse_similarity_rules(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    similarity_dict = {}

    for attr in root.findall('attr'):
        if attr.get('type') == 'noexpr':
            for values in attr.findall('values'):
                # Prendi il primo valore come rappresentante della classe di equivalenza
                representative_value = values[0].text
                for value in values:
                    similarity_dict[value.text] = representative_value

    #print(similarity_dict)
    return similarity_dict

def column_distance(col1, col2):
    distances = []
    for val1, val2 in zip(col1, col2):
        if pd.isna(val1) or pd.isna(val2):
            distances.append(1)
        elif isinstance(val1, str) and isinstance(val2, str):
            distances.append(0 if val1 == val2 else 1)
        else:
            distances.append(abs(val1 - val2))
    return np.mean(distances)
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

    # Copiare il dataframe per evitare modifiche sull'originale
    df_normalized = df.copy()

    for col in min_max_values:
        col_min = min_max_values[col]['min']
        col_max = min_max_values[col]['max']

        # Normalizzare solo i valori validi (non "?" e non NaN)
        df_normalized[col] = df[col].apply(
            lambda x: round((float(x) - col_min) / (col_max - col_min), 3) if x != '?' else x
        )

    return df_normalized

def get_headers(header_file, dataset_name):
    with open(header_file, 'r') as file:
        for line in file:
            headers = line.strip().split(';')
            if headers[-1] == dataset_name:
                return headers[:-1]
    return []

def process_dataset(dataset_path, results_path, header_file, dataset_name, full_dataset_path,xml_file):

    # Ottieni gli header dal file delle intestazioni
    headers = get_headers(header_file, dataset_name)

    # Leggi il dataset con valori mancanti usando gli header ottenuti
    df_missing = pd.read_csv(dataset_path, delimiter=';', names=headers)
    original_missing_dataset=df_missing.copy()

    #print(df_missing)

    # Leggi il file dei risultati dell'imputation
    imputation_results = pd.read_csv(results_path, delimiter=';')

    #print(imputation_results)

    count_question_marks = (df_missing == "?").sum().sum()
    print(count_question_marks, "MVs Originali")


    full_dataset=pd.read_csv(full_dataset_path,sep=';')
    string_columns = full_dataset.select_dtypes(include=['object']).columns

    raw_rmse_data={}

    # Scorri il file dei risultati e riempi i valori mancanti nel dataset
    for index, row in imputation_results.iterrows():
        row_index = row['riga']
        column_name = row['nome attributo']
        value_to_impute = row['valore imputato']
        if (df_missing.at[row_index-1, column_name]=='?'):
            if value_to_impute != '?':
                df_missing.at[row_index-1, column_name] = value_to_impute
                if column_name not in raw_rmse_data:
                    raw_rmse_data[column_name] = []
                raw_rmse_data[column_name].append((full_dataset.at[row_index-1, column_name],value_to_impute))
        else:
            print("!!!Qualcosa non va!!!")

    # Caricare le regole di similarità dal file XML
    similarity_dict = parse_similarity_rules(xml_file)
    # Identificare le colonne stringa

    for col in string_columns:
            df_missing[col] = df_missing[col].apply(
                lambda x: similarity_dict.get(x, x) if x != "?" else x
            )
            full_dataset[col] = full_dataset[col].apply(
                lambda x: similarity_dict.get(x, x) if x != "?" else x
            )

    print("Valori stringa normalizzati")
    #count_question_marks = (df_missing == "?").sum().sum()
    #print(count_question_marks, "MVs dopo Norm")

    print("Normalizzazione dataset originale")
    df_normalized, min_max_values = normalize_dataframe(full_dataset)

    imputed_df_normalized=normalize_new_dataframe(df_missing,min_max_values)
    original_missing_dataset=normalize_new_dataframe(original_missing_dataset,min_max_values)

    # print("Dataset Imputato Finale")
    # print(imputed_df_normalized)
    # print("Dataset Completo Finale")
    # print(df_normalized)


    norm_rmse_data={}

    # Scorri il file dei risultati e riempi i valori mancanti nel dataset
    for index, row in imputation_results.iterrows():
        row_index = row['riga']
        column_name = row['nome attributo']
        value_to_impute = row['valore imputato']

        if value_to_impute != '?':
            if column_name not in norm_rmse_data:
                norm_rmse_data[column_name] = []
            norm_rmse_data[column_name].append((df_normalized.at[row_index-1, column_name],imputed_df_normalized.at[row_index-1, column_name]))

    #print(norm_rmse_data)
    rmse=computeRMSE(norm_rmse_data,string_columns)

    # Sostituiamo i missing values "?" con NaN
    imputed_df_normalized.replace('?', np.nan, inplace=True)
    original_missing_dataset.replace('?', np.nan, inplace=True)

    # Calcoliamo la similarità per ogni colonna
    similarities = {}
    for column in df_normalized.columns:
        dist = column_distance(df_normalized[column], imputed_df_normalized[column])
        similarities[column] = 1 - dist

    # Calcoliamo la similarità totale del dataset
    total_similarity = np.mean(list(similarities.values()))
    #print(similarities)
    print("Similarità tra dataset completo e quello con imputato:",total_similarity)


    # Calcoliamo la similarità per ogni colonna
    similarities = {}
    for column in df_normalized.columns:
        dist = column_distance(df_normalized[column], original_missing_dataset[column])
        similarities[column] = 1 - dist

    # Calcoliamo la similarità totale del dataset
    total_similarity = np.mean(list(similarities.values()))
    #print(similarities)
    print("Similarità tra dataset completo e quello con missing value:",total_similarity)


    return rmse


def is_row_in_file(file_path, row_data, delimiter=';'):
    # Verifica se il file esiste
    if not os.path.exists(file_path):
        return False

    with open(file_path, 'r', newline='') as file:
        for line in file:
            # Rimuove i caratteri di nuova linea dalla fine della riga e confronta
            if line.strip() == delimiter.join(map(str, row_data)):
                return True
    return False

def write_unique_row_to_csv(file_path, row_data, delimiter=';'):
    # Controlla se la riga esiste già nel file
    if not is_row_in_file(file_path, row_data, delimiter):
        # Scrivi la riga nel file se non esiste
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=delimiter)
            writer.writerow(row_data)

# Funzione per verificare se due valori sono simili
def are_similar(attribute, value1, value2):
    for attr in root.findall('attr'):
        if attr.get('name') == attribute:
            type_ = attr.get('type')
            if type_ == 'noexpr':
                for values in attr.findall('values'):
                    similar_values = [value.text for value in values.findall('value')]
                    if value1 in similar_values and value2 in similar_values:
                        return True
            elif type_ == 'delta':
                threshold = float(attr.find('value').text)
                diff = abs(float(value1) - float(value2))
                return diff <= threshold
            elif type_ == 'expr':
                import re
                for regex in attr.findall('regex'):
                    pattern_parts = []
                    for elem in regex:
                        if elem.tag == 'same':
                            length = int(elem.get('length'))
                            pattern_parts.append(r'\d{' + str(length) + '}')
                        elif elem.tag == 'fix':
                            pattern_parts.append(re.escape(elem.text))
                        elif elem.tag == 'any':
                            length = int(elem.get('length'))
                            pattern_parts.append(r'.{' + str(length) + '}')
                    pattern = ''.join(pattern_parts)
                    if re.match(pattern, value1) and re.match(pattern, value2):
                        return True
    return False


def analyze_imputation_quality(version, approach, MV, xml_file):
    dataset_name = f"Statlog_270_{MV}_{version}"

    # Esempio di utilizzo
    missing_dataset_path = f'../../Datasets/Missing_Datasets/Statlog_270/{dataset_name}.csv'
    full_dataset_path = f'../../Datasets/Preprocessed_Datasets/Statlog_270.csv'

    results_path = ""
    if (approach == "Baseline"):
        results_path = f'../Imputation_Results/Imputation_Baseline_Results/Statlog_270/{version}/Baseline_{dataset_name}.csv'
    elif (approach == "Pipeline_noRev"):
        results_path = f'../Imputation_Results/Imputation_noRestoring_Results/Statlog_270/{version}/{dataset_name}.csv'
    elif (approach == "Baseline20"):
        results_path = f'../Imputation_Results/Imputation_Baseline_20_Results/Statlog_270/{version}/Baseline_{dataset_name}.csv'
    elif (approach == "Pipeline"):
        results_path = f'../Imputation_Results/Imputation_Pipeline_Results/Statlog_270/{version}/{dataset_name}.csv'
    elif (approach == "Hybrid"):
        results_path = f'../Imputation_Results/Imputation_Hybrid_Results/Statlog_270/{version}/{dataset_name}.csv'

    header_file = f'../../Preprocessing/Headers/Headers.csv'
    rmse=process_dataset(missing_dataset_path, results_path, header_file, dataset_name, full_dataset_path, xml_file)
    return  rmse

def checkResults(version, approach, MV,xml_file):
    df = ""
    if (approach == "Baseline"):
        df = pd.read_csv(
            f"../Imputation_Results/Imputation_Baseline_Results/Statlog_270/{version}/Baseline_Statlog_270_{MV}_{version}.csv",
            sep=';')
    elif (approach == "Pipeline_noRev"):
        df = pd.read_csv(
            f"../Imputation_Results/Imputation_noRestoring_Results/Statlog_270/{version}/Statlog_270_{MV}_{version}.csv",
            sep=';')
    elif (approach == "Baseline20"):
        df = pd.read_csv(
            f"../Imputation_Results/Imputation_Baseline_20_Results/Statlog_270/{version}/Baseline_Statlog_270_{MV}_{version}.csv",
            sep=';')
    elif (approach == "Pipeline"):
        df = pd.read_csv(
            f"../Imputation_Results/Imputation_Pipeline_Results/Statlog_270/{version}/Statlog_270_{MV}_{version}.csv",
            sep=';')
    elif (approach == "Hybrid"):
        df = pd.read_csv(
            f"../Imputation_Results/Imputation_Hybrid_Results/Statlog_270/{version}/Statlog_270_{MV}_{version}.csv",
            sep=';')

    df = df.drop(['riga'], axis=1)
    print(df.columns.tolist())

    not_imp = 0
    exact = 0
    similar = 0
    tot = 0

    for index, row in df.iterrows():
        tot += 1
        if row['valore imputato'] == "?":
            not_imp += 1
        elif row['valore imputato'] == row['valore da imputare']:
            exact += 1
        else:
            if are_similar(row['nome attributo'], row['valore da imputare'], row['valore imputato']):
                similar += 1

    print("Non Imputati", not_imp)
    print("Esatti", exact)
    print("Simili", similar)
    print("Esatti+Simili", exact + similar)
    wrong = tot - (not_imp + exact + similar)
    print("Imputazioni totali", exact + similar + wrong)
    print("MV Totali", tot)
    print("Sbagliati", wrong)
    recall = (exact + similar) / tot
    print("Recall: ", recall)
    precision = (exact + similar) / (exact + similar + wrong)
    print("Precision: ", precision)



    rmse=analyze_imputation_quality(version,approach,mv,xml_file)
    all_results_path = f"../ALL_Results_v3.csv"
    row_data = ["Statlog_270"] + [approach] + [MV] + [str(recall)] + [str(precision)] + [str(version)] + [
        str(exact)] + [str(similar)] + [str(wrong)] + [rmse]
    print(row_data)
    write_unique_row_to_csv(all_results_path, row_data)



approaches=["Pipeline_noRev","Hybrid", "Pipeline", "Baseline20"]
#approaches=["Pipeline","Baseline20"]
versions=[1,2,3,4,5]
MVs = [38,76,113,151,189,378,756,1134,1512,1890]

for version in versions:
    for approach in approaches:
        for mv in MVs:
            checkResults(version,approach,mv,xml_file)





