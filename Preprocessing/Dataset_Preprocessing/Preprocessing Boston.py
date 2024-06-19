import pandas as pd
from unidecode import unidecode
df=pd.read_csv("../../Datasets/Original_Datasets/crime.csv", sep=',', encoding='latin1')
df.to_csv("../../Datasets/Preprocessed_Datasets/crimetemp.csv", sep=';', encoding='latin1')
#df_winners=pd.read_csv("../../Datasets/Original_Datasets/winners.csv", sep=',', encoding='utf-8')
print(df)
