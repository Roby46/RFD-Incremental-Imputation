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


# Generates a set of inviolable (protected) row indices.
# Selects n indices randomly from the first half and n from the second half.
def generate_inviolable_indices(df_length, n):
    first_half = random.sample(range(0, df_length // 2), n)
    second_half = random.sample(range(df_length // 2, df_length), n)
    return set(first_half + second_half)


# Configuration parameters:
percentages = [1, 2, 3, 4, 5, 10, 20, 30, 40, 50]
dataset = "police_MBUV"
delimiter = ';'
path_file = f'../../Datasets/Preprocessed_Datasets/{dataset}.csv'
iterations = [1, 2, 3, 4, 5]
null_value = '?'
n_inviolable_rows = 4  # Number of rows to remain complete in each half

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

        # Generate the inviolable (protected) row indices.
        inviolable_indices = generate_inviolable_indices(len(df), n_inviolable_rows)

        # Distribute the global MV_number randomly among the columns using a multinomial.
        n_cols = len(df.columns)
        # missing_distribution is an array with missing counts for each column summing to MV_number.
        missing_distribution = np.random.multinomial(MV_number, np.ones(n_cols) / n_cols)

        # For each column, inject missing values using the MBUV approach.
        for idx, col in enumerate(df.columns):
            missing_for_col = int(missing_distribution[idx])
            if missing_for_col <= 0:
                continue  # Skip if this column does not get any missing values.

            # Identify eligible rows (those that are not in inviolable_indices and where the cell is not already missing).
            eligible_rows = [r for r in range(len(df)) if r not in inviolable_indices and df.iloc[r, idx] != null_value]

            # In case the eligible count is lower than desired missing count, adjust accordingly.
            if len(eligible_rows) < missing_for_col:
                missing_for_col = len(eligible_rows)

            # Generate a "fake" feature for the column using a normal distribution.
            # This feature is used to rank the rows by extreme values.
            fake_feature = np.random.normal(loc=0, scale=1, size=len(df))

            # Create a list of tuples (row_index, fake_value) only for eligible rows.
            eligible_with_fake = [(r, fake_feature[r]) for r in eligible_rows]

            # Sort eligible rows by the fake value.
            eligible_sorted = sorted(eligible_with_fake, key=lambda x: x[1])

            # Split missing values into two groups:
            # half for the lowest values and half for the highest values.
            m_low = missing_for_col // 2
            m_high = missing_for_col - m_low

            # Select the rows based on the extreme (lowest and highest) fake values.
            chosen_rows = [x[0] for x in eligible_sorted[:m_low]]
            if m_high > 0:
                chosen_rows += [x[0] for x in eligible_sorted[-m_high:]]

            # For each selected row, record the original value and set the cell to the null_value.
            for r in chosen_rows:
                original_value = df.iloc[r, idx]
                # Notice that in the support file, rows are recorded with 1-based indexing.
                raw_data = [r + 1, col, original_value]
                write_row_to_csv(path_initial_tuples_output, raw_data)
                df.iloc[r, idx] = null_value

        # Count the injected missing values in the dataset.
        count_question_marks = (df == null_value).sum().sum()
        print(count_question_marks, "MVs were injected")

        # Write the resulting dataset (with missing values) without headers.
        path_file_output = f'../../Datasets/Missing_Datasets/{dataset}/{missing_dataset_name}.csv'
        directory = os.path.dirname(path_file_output)
        if not os.path.exists(directory):
            os.makedirs(directory)
        df.to_csv(path_file_output, index=False, sep=delimiter, header=False)
