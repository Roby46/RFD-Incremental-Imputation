import pandas as pd
import xml.etree.ElementTree as ET

# Carica il file XML
tree = ET.parse(f'XML Files/Telemetry_similarity_rules.xml')
root = tree.getroot()

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
#df=pd.read_csv(r"../Imputation_Results/Imputation_Pipeline_Results/EV_Vehicles/1/EV_Vehicles_4000_12000_1.csv", sep=';')
#df=pd.read_csv(r"../Imputation_Results/Imputation_Baseline_Results/EV_Vehicles/1/Baseline_EV_Vehicles_4000_12000_1.csv", sep=';')
df = pd.read_csv(r"../Imputation_Results/Imputation_noRestoring_Results/EV_Vehicles/2/Baseline_IoT_Telemetry3000_12000_19.csv", sep=';')
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
accuracy = (exact + similar) / tot
print("Accuracy: ", accuracy)
precision = (exact + similar) / (exact + similar + wrong)
print("Precision: ", precision)
