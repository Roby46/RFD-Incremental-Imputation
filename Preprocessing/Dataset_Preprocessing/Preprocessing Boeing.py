import pandas as pd

df=pd.read_csv("../../Datasets/Original_Datasets/Boeing.csv", sep=',')

print(df)
#Remove the specified columns from the DataFrame
#List of columns to eliminate
columns_to_delete = ["Unfilled Orders"]

df = df.drop(columns=columns_to_delete, errors="ignore")
df=df.dropna()
df = df.drop(df.index[-1])

print(df["Customer Name"].nunique())
print(df)

# Campioniamo il DataFrame in modo da avere al massimo 4 righe per ogni tipo di cliente
max_rows_per_customer = 4
sampled_df = df.groupby('Customer Name').head(max_rows_per_customer)

# Visualizziamo il DataFrame campionato
print("\nDataFrame campionato:")
print(sampled_df)


# Mischiamo (shuffle) le righe del DataFrame campionato
shuffled_df = sampled_df.sample(frac=1).reset_index(drop=True)

# Visualizziamo il DataFrame campionato e mischiato
print("\nDataFrame campionato e mischiato:")
print(shuffled_df)

#
def clean_data(text):
    text = str(text)  # Assicurati che il valore sia una stringa
    text = text.replace('""', '')  # Rimuove i doppi apici doppi
    text = text.replace(',', '')   # Rimuove le virgole
    text = text.replace('"', '')   # Rimuove i doppi apici singoli
    return text

# Applica la funzione di pulizia a tutte le colonne di tipo object (stringa)
for col in shuffled_df.select_dtypes(include='object').columns:
    shuffled_df[col] = shuffled_df[col].apply(clean_data)
#
#
# print(df.columns.tolist())
#
# print(df)
# #
# rows=3200
shuffled_df.columns = shuffled_df.columns.str.replace(' ', '_')

def remove_non_ascii(text):
    return ''.join(c for c in text if ord(c) < 128)

# Applica la funzione a tutte le stringhe nel DataFrame
shuffled_df = shuffled_df.applymap(lambda x: remove_non_ascii(x) if isinstance(x, str) else x)

print(shuffled_df)
# #
filename=f"../../Datasets/Preprocessed_Datasets/Boeing_{len(shuffled_df)}.csv"
shuffled_df.to_csv(filename, sep=';', index=None, encoding='ascii')
# #
# # print(df)
