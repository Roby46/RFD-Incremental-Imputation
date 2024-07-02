import pandas as pd
import xml.etree.ElementTree as ET
import os
import csv


# Carica il file XML
tree = ET.parse(f'XML Files/Olympics_similarity_rules.xml')
root = tree.getroot()

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

# Leggi il CSV
version=1
MV=27000

approach="Pipeline"
#approach="Baseline"
#approach="Baseline20"
#approach="Pipeline_noRev"
#approach="Hybrid"

df=""
if(approach=="Baseline"):
    df=pd.read_csv(f"../Imputation_Results/Imputation_Baseline_Results/Olympics_7500/{version}/Baseline_Olympics_7500_{MV}_{version}.csv", sep=';')
elif(approach=="Pipeline_noRev"):
    df = pd.read_csv(f"../Imputation_Results/Imputation_noRestoring_Results/Olympics_7500/{version}/Olympics_7500_{MV}_{version}.csv", sep=';')
elif(approach=="Baseline20"):
    df = pd.read_csv(f"../Imputation_Results/Imputation_Baseline_20_Results/Olympics_7500/{version}/Baseline_Olympics_7500_{MV}_{version}.csv", sep=';')
elif(approach=="Pipeline"):
    df = pd.read_csv(f"../Imputation_Results/Imputation_Pipeline_Results/Olympics_7500/{version}/Olympics_7500_{MV}_{version}.csv", sep=';')
elif(approach=="Hybrid"):
    df = pd.read_csv(f"../Imputation_Results/Imputation_Hybrid_Results/Olympics_7500/{version}/Olympics_7500_{MV}_{version}.csv", sep=';')

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
