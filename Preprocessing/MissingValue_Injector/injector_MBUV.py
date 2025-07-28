import random
import pandas as pd
import os
import numpy as np
import warnings
import csv

# Suppress future warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Checks whether a given row (as a string joined by the delimiter) is already in the file.
def is_row_in_file(file_path, row_data, delimiter=';'):
    if not os.path.exists(file_path):
        return False
    with open(file_path, 'r', newline='') as file:
        for line in file:
            if line.strip() == delimiter.join(row_data):
                return True
    return False

# Writes a unique row to CSV (does not duplicate if already present).
def write_unique_row_to_csv(file_path, row_data, delimiter=';'):
    if not is_row_in_file(file_path, row_data, delimiter):
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file, delimiter=delimiter)
            writer.writerow(row_data)

# Determines a column type: 'B' for bool, 'C' for character (if max string length is 1), or 'D' for others.
def determine_column_type(col):
    if col.dtype == 'bool':
        return 'B'
    elif col.dtype == 'object' and col.str.len().max() == 1:
        return 'C'
    else:
        return 'D'

def is_file_exist(file_path):
    return os.path.exists(file_path)

def write_row_to_csv(file_path, row_data):
    mode = 'a' if is_file_exist(file_path) else 'w'
    with open(file_path, mode, newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(row_data)

# Configuration parameters:
percentages = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
dataset = "police_MBUV"
delimiter = ';'
path_file = f'../../Datasets/Preprocessed_Datasets/{dataset}.csv'
iterations = [1, 2, 3, 4, 5]
null_value = '?'

print(path_file)

# Read the original (clean) dataset once to determine column types and total data size.
df_original = pd.read_csv(path_file, sep=delimiter)
totalValues = len(df_original.columns.tolist()) * len(df_original)
print(len(df_original))
print(totalValues)
column_types = [determine_column_type(df_original[col]) for col in df_original.columns]

# Loop over iterations and missing percentages.
for iteration in iterations:
    for p in percentages:
        # Reload the clean dataset for each new missingness injection experiment.
        df = pd.read_csv(path_file, sep=delimiter)

        # Calculate total missing values to inject globally.
        MV_number = round(totalValues * (p / 100))

        # Construct a unique identifier for this missing dataset.
        missing_dataset_name = f'{dataset}_{MV_number}_{iteration}'

        # Log column types and header information, appended with the dataset id.
        column_types_data = column_types + [missing_dataset_name]
        column_types_output_path = f'../../Preprocessing/ColumnTypes/ColumnTypes.csv'
        write_unique_row_to_csv(column_types_output_path, column_types_data)

        header_data = df.columns.tolist() + [missing_dataset_name]
        header_output_path = f'../../Preprocessing/Headers/Headers.csv'
        write_unique_row_to_csv(header_output_path, header_data)

        # Prepare the support file where the original values (to be replaced) are stored.
        path_initial_tuples_output = f'../../Preprocessing/Initial_Tuples/{dataset}/{missing_dataset_name}.csv'
        directory = os.path.dirname(path_initial_tuples_output)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Distribute the global MV_number randomly among the columns using a multinomial.
        n_cols = len(df.columns)
        missing_distribution = np.random.multinomial(MV_number, np.ones(n_cols) / n_cols)

        # For each column, inject missing values using the MBUV approach.
        for idx, col in enumerate(df.columns):
            missing_for_col = int(missing_distribution[idx])
            if missing_for_col <= 0:
                continue

            eligible_rows = [r for r in range(len(df)) if df.iloc[r, idx] != null_value]

            if len(eligible_rows) < missing_for_col:
                missing_for_col = len(eligible_rows)

            fake_feature = np.random.normal(loc=0, scale=1, size=len(df))
            eligible_with_fake = [(r, fake_feature[r]) for r in eligible_rows]
            eligible_sorted = sorted(eligible_with_fake, key=lambda x: x[1])

            m_low = missing_for_col // 2
            m_high = missing_for_col - m_low

            chosen_rows = [x[0] for x in eligible_sorted[:m_low]]
            if m_high > 0:
                chosen_rows += [x[0] for x in eligible_sorted[-m_high:]]

            for r in chosen_rows:
                original_value = df.iloc[r, idx]
                raw_data = [r + 1, col, original_value]
                write_row_to_csv(path_initial_tuples_output, raw_data)
                df.iloc[r, idx] = null_value

        count_question_marks = (df == null_value).sum().sum()
        print(count_question_marks, "MVs were injected")

        path_file_output = f'../../Datasets/Missing_Datasets/{dataset}/{missing_dataset_name}.csv'
        directory = os.path.dirname(path_file_output)
        if not os.path.exists(directory):
            os.makedirs(directory)
        df.to_csv(path_file_output, index=False, sep=delimiter, header=False)
