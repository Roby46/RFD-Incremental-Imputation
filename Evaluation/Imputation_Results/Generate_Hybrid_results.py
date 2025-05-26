import pandas as pd

def update_imputations(row, df2, missing_value):
    if row['valore imputato'] != missing_value:
        match = df2[(df2['riga'] == row['riga']) & (df2['nome attributo'] == row['nome attributo'])]
        if not match.empty and match.iloc[0]['valore imputato'] != missing_value and match.iloc[0]['valore imputato'] != row['valore imputato']:
            row['valore imputato'] = match.iloc[0]['valore imputato']
            #print("Cambiamento effettuato")
    return row

def process_files(dataset, versions, MVs):
    for version in versions:
        for MV in MVs:
            # Load the two CSV files
            file1 = pd.read_csv(f'Imputation_noRestoring_Results/{dataset}/{version}/{dataset}_{MV}_{version}.csv', delimiter=';')
            file2 = pd.read_csv(f'Imputation_Pipeline_Results/{dataset}/{version}/{dataset}_{MV}_{version}.csv', delimiter=';')

            # Update imputations in the first file with those from the second file if different
            result = file1.apply(lambda row: update_imputations(row, file2, '?'), axis=1)

            # Write the final result to a third CSV file
            result.to_csv(f'Imputation_Hybrid_Results/{dataset}/{version}/{dataset}_{MV}_{version}.csv', index=False, sep=";")
            print(f"Processed: {dataset}, Version: {version}, MV: {MV}")

# Specifica le combinazioni di versioni e MV
#dataset = "EV_Vehicles_4000"
#versions = [1,2,3,4,5]  # Lista delle versioni

dataset="police_MNAR"
versions = [1,2,3,4,5]
MVs =  [198, 397, 595, 793, 992, 1984, 3967, 5951, 7934, 9918]

# Esegui il processo per tutte le combinazioni
process_files(dataset, versions, MVs)

# import pandas as pd
#
# dataset="EV_Vehicles_4000"
# version=1
# MV=400
#
# # Load the two CSV files
# file1 = pd.read_csv(f'Imputation_noRestoring_Results/{dataset}/{version}/{dataset}_{MV}_{version}.csv', delimiter=';')
# file2 = pd.read_csv(f'Imputation_Pipeline_Results/{dataset}/{version}/{dataset}_{MV}_{version}.csv', delimiter=';')
#
# # Function to update imputations
# def update_imputations(row, df2, missing_value):
#     if row['valore imputato'] != missing_value:
#         match = df2[(df2['riga'] == row['riga']) & (df2['nome attributo'] == row['nome attributo'])]
#         if not match.empty and match.iloc[0]['valore imputato'] != missing_value and match.iloc[0]['valore imputato'] != row['valore imputato']:
#             row['valore imputato'] = match.iloc[0]['valore imputato']
#             print("Cambiamento effettuato")
#     return row
#
# # Update imputations in the first file with those from the second file if different
# result = file1.apply(lambda row: update_imputations(row, file2, '?'), axis=1)
#
# # Write the final result to a third CSV file
# result.to_csv(f'Imputation_Hybrid_Results/{dataset}/{version}/{dataset}_{MV}_{version}.csv', index=False, sep=";")
