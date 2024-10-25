import os

# Ottieni il percorso della cartella corrente (dove è salvato lo script)
directory = os.getcwd()

# Scorri tutti i file nella cartella
for filename in os.listdir(directory):
    # Verifica se il file inizia con "Iot_" (con la "t" minuscola)
    if filename.startswith("Iot_") and filename.endswith(".csv"):
        # Nuovo nome del file con "IoT_" (con la "t" maiuscola)
        new_filename = "IoT_" + filename[4:]  # Prende tutto dopo "Iot_"

        # Rinominare il file
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        print(f"Rinominato: {filename} -> {new_filename}")

print("Rinomina completata!")
