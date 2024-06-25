import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("../../Datasets/Original_Datasets/bikes.csv")

df.sample(8)
print(df)

#Dropping null values
df.dropna(inplace=True)

#Removing values where price==0
#Because price can't be 0
df = df[df['price']>0]


df['model_name'] = df['model_name'].str.replace('Royal Enfield','Royal-Enfield')
df['company'] = df['model_name'].apply(lambda x:" ".join(x.split()[0:1]))
freq_company = df['company'].value_counts()[df['company'].value_counts()>=25].index.tolist()
df = df[df['company'].isin(freq_company)]
print(df)
df['model'] = df['model_name'].apply(lambda x:" ".join(x.split()[1:2]))
#Taking model which appeared in data 10 or more times
freq_model = df['model'].value_counts()[df['model'].value_counts()>=10].index.tolist()
df = df[df['model'].isin(freq_model)]

print(df)


df['kms_driven'] = df['kms_driven'].str.replace('Km','')

#Removing rows containing Mileage in kms_driven
df = df[df['kms_driven'].apply(lambda x : True if x.find("Mil") == -1 else False)]

df = df[df['kms_driven'] != 'Yes ']
#Converting the str values to int type
df['kms_driven'] = df['kms_driven'].astype(int)

df.owner.unique()
#Extracting the first word
#This gives the number in str type (like second,third)
#They can be converted easily into numeric data
df['owner'] = df['owner'].apply(lambda x:" ".join(x.split()[0:1]))
#Removing (\n,kmpl,KMPL etc) to get the numeric data
df['mileage'] = df['mileage'].str.replace("\n",'')
df['mileage'] = df['mileage'].str.replace("kmpl",'')
df['mileage'] = df['mileage'].str.replace("KMPL",'')
df = df[df['mileage'] != ' Liquid Cooled']
df = df[df['mileage'] != ' ']

#Taking mean of the values given in a range (eg. 45-60 kmpl)
#If splitting gives 2 str then we convert them into int and take their mean
#If splitting gives 1 str then it used as it is after conversion

df['mileage'] = df['mileage'].apply(lambda x : float(x) if len(x.split("-")) == 1  else  (int(x.split("-")[0]) + int(x.split("-")[1])) /2 )

df['power'] = df['power'].astype("str")
df['power'] = df['power'].apply(lambda x : x.upper().replace("BHP",'').strip())

# Handling 29.9 hp / 22 kW type data
df['power']  = df['power'].apply(lambda x : x if x.find("HP") == -1 else str(float(x[:x.find("HP")-1])))
#1 kw = 1.34hp
df['power'] = df['power'].apply(lambda x : x if x.find("KW") == -1 else str(float(x[:x.find("KW")-1])*1.34))
#1 ps = 0.98592 hp
df['power'] = df['power'].apply(lambda x : x if x.find("PS") == -1 else str(float(x[:x.find("PS")-1])*0.98592))

df['power'] = df['power'].astype(float)
#Taking figure upto 2 decimal palces
df['power'] = round(df['power'],2)


freq_location = df['location'].value_counts()[df['location'].value_counts()>=10].index.tolist()
df = df[df['location'].isin(freq_location)]
df = df.drop(['model_name'],axis=1)


print(df)

df.to_csv(f"../../Datasets/Preprocessed_Datasets/bikes_{len(df)}.csv", index=None, sep=';')