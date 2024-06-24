import random
import pandas as pd
import os
import numpy as np
import warnings
import csv

warnings.simplefilter(action='ignore', category=FutureWarning)

def is_row_in_file(file_path, row_data, delimiter=';'):
    # Verifica se il file esiste
    if not os.path.exists(file_path):
        return False

    with open(file_path, 'r', newline='') as file:
        for line in file:
            # Rimuove i caratteri di nuova linea dalla fine della riga e confronta
            if line.strip() == delimiter.join(row_data):
                return True
    return False

def write_unique_row_to_csv(file_path, row_data, delimiter=';'):
    # Controlla se la riga esiste già nel file
    if not is_row_in_file(file_path, row_data, delimiter):
        # Scrivi la riga nel file se non esiste
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=delimiter)
            writer.writerow(row_data)

def determine_column_type(col):
    if col.dtype == 'bool':
        return 'B'
    elif col.dtype == 'object' and col.str.len().max() == 1:
        return 'C'
    else:
        return 'D'

# Function to check if the CSV file exists
def is_file_exist(file_path):
    return os.path.exists(file_path)

# Function to write a row to the CSV file
def write_row_to_csv(file_path, row_data):
    mode = 'a' if is_file_exist(file_path) else 'w'
    with open(file_path, mode, newline='') as file:
        writer = csv.writer(file, delimiter=';')
        # Write the data row
        writer.writerow(row_data)

#Percentages of MVs to inject
percentages=[1,2,3,4,5,10,20,30,40,50]

column_types=[""]
#percentages=[1]
#dataset="restaurant"

#Dataset details
dataset="NBA_7836"
delimiter = ';'
path_file = f'../../Datasets/Preprocessed_Datasets/{dataset}.csv'
#Iterations number (We tested 5 different version for each configuration)
#iterations = [1,2,3,4,5]
iterations = [1,2,3,4,5]
#MV Symbol
null_value = '?'

df=pd.read_csv(path_file, sep=delimiter)
totalValues=len(df.columns.tolist())*len(df)
# Get Column Types
column_types = [determine_column_type(df[col]) for col in df.columns]
print(df)
print("Rows: ", len(df))
print("Columns", len(df.columns.tolist()))
colonne=df.columns.tolist()
print(colonne)
for iteration in iterations:
    print("Generating version",iteration,"of the configurations")
    for p in percentages:
        print("Percentage:", p)
        df = pd.read_csv(path_file, sep=delimiter)
        MV_number = round(totalValues * (p / 100))
        setted_MVs = 0

        missing_dataset_name=f'{dataset}_{MV_number}_{iteration}'

        # Write an entry in the ColumnTypes file (needed for the imputation process)
        column_types_data = column_types + [missing_dataset_name]
        column_types_output_path=f'../../Preprocessing/ColumnTypes/ColumnTypes.csv'
        write_unique_row_to_csv(column_types_output_path, column_types_data)

        # Write an entry in the Header file (needed for the imputation process)
        header_data=colonne + [missing_dataset_name]
        header_output_path = f'../../Preprocessing/Headers/Headers.csv'
        write_unique_row_to_csv(header_output_path, header_data)

        #Path to the file that will contain the correct values for each injected MVs
        path_initial_tuples_output= f'../../Preprocessing/Initial_Tuples/{dataset}/{missing_dataset_name}.csv'

        directory = os.path.dirname(path_initial_tuples_output)
        # Create directory if not existent
        if not os.path.exists(directory):
            os.makedirs(directory)

        while setted_MVs < MV_number:
            riga = random.randint(0, len(df) - 1)
            colonna = random.randint(0, len(df.columns.tolist())- 1)
            if df.iloc[riga, colonna] != null_value:

                raw_data=[riga+1, df.columns.tolist()[colonna],df.iloc[riga, colonna]]
                write_row_to_csv(path_initial_tuples_output, raw_data)

                df.iloc[riga, colonna] = null_value
                setted_MVs= setted_MVs + 1
                #print("Placing null value in", df.columns.tolist()[colonna], "at row", riga+1)

        count_question_marks = (df == "?").sum().sum()
        print(count_question_marks, "MVs were injected")
        path_file_output= f'../../Datasets/Missing_Datasets/{dataset}/{missing_dataset_name}.csv'

        # Estrai il percorso della directory dalla stringa del percorso del file
        directory = os.path.dirname(path_file_output)

        # Crea la directory se non esiste
        if not os.path.exists(directory):
            os.makedirs(directory)

        df.to_csv(path_file_output, index=None, sep=";", header=False)