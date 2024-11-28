import pandas as pd
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from sklearn.preprocessing import LabelEncoder

# Carica il dataset
df = pd.read_csv("../../Datasets/Original_Datasets/Bank.csv", sep=',')

# Separiamo le feature (X) dalla variabile target (y)
X = df.drop(columns=['Class'])
y = df['Class']

# Codifica le variabili categoriche se ce ne sono (Label Encoding)
X_encoded = X.copy()
for column in X_encoded.select_dtypes(include=['object']).columns:
    X_encoded[column] = LabelEncoder().fit_transform(X_encoded[column])

# Calcoliamo l'informazione mutua tra le feature e la variabile target 'Class'
mi = mutual_info_classif(X_encoded, y)

# Crea un DataFrame con le feature e il loro valore di mutual information
mi_df = pd.DataFrame({
    'Feature': X_encoded.columns,
    'Mutual Information': mi
})

# Ordina per mutual information in ordine decrescente e seleziona le 7 caratteristiche più rilevanti
top_features = mi_df.sort_values(by='Mutual Information', ascending=False).head(7)['Feature']

# Aggiungiamo la colonna 'Class' alle feature selezionate
selected_features = top_features.tolist() + ['Class']

# Creiamo un nuovo DataFrame con solo le feature selezionate
df_selected = df[selected_features]

# Visualizziamo le feature selezionate e il nuovo DataFrame
print("Feature selezionate:", selected_features)

# Ora, selezioniamo 4000 righe per ciascuna delle classi (1 e 2)
df_class_1 = df_selected[df_selected['Class'] == 1].sample(n=2000, random_state=42)
df_class_2 = df_selected[df_selected['Class'] == 2].sample(n=2000, random_state=42)

# Uniamo le due classi per ottenere il dataset finale di 8000 righe
df_final = pd.concat([df_class_1, df_class_2])
# Rinominare tutte le colonne tranne 'Class' con V1, V2, V3, ...
new_column_names = {col: f'V{idx+1}' for idx, col in enumerate(df_final.columns[:-1])}  # Ignora 'Class'
df_final.rename(columns={**new_column_names, 'Class': 'Class'}, inplace=True)

filename=f"../../Datasets/Preprocessed_Datasets/Bank_{len(df_final)}.csv"
df_final.to_csv(filename, sep=';', index=None, encoding='ascii')
print(df_final)
