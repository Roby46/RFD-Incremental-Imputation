import pandas as pd
import numpy as np

# Carica il dataset
df = pd.read_csv("../../Datasets/Original_Datasets/S4-ADL5.csv", sep=";")
print(df)
# Numero di righe da campionare
rows = 2400
df = df.sample(rows)

# Seleziona 15 colonne casuali
df = df.sample(n=15, axis=1)

# Salva il nuovo file
filename = f"../../Datasets/Preprocessed_Datasets/S4-ADL5_{rows}.csv"
df.to_csv(filename, sep=';', index=None)

print(df)
