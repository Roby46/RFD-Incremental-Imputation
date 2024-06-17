import chardet

# Apri il file in modalità binaria
with open("../../Datasets/Original_Datasets/olympics.csv", 'rb') as f:
    # Leggi una porzione del file
    rawdata = f.read(10000)
    # Usa chardet per rilevare l'encoding
    result = chardet.detect(rawdata)
    encoding = result['encoding']
    print(f"L'encoding rilevato è: {encoding}")