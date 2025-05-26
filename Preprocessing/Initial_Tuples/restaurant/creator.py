import os
import shutil

# Cartella corrente (dove si trova lo script e i file)
cartella_corrente = os.path.dirname(os.path.abspath(__file__))

# Cartella padre (dove va creata Boeing_898_FD)
cartella_padre = os.path.dirname(cartella_corrente)

# Nuova cartella
destinazione = os.path.join(cartella_padre, 'restaurant_FD')
os.makedirs(destinazione, exist_ok=True)

prefix_originale = 'restaurant'
prefix_nuovo = 'restaurant_FD'

# Loop sui file nella cartella corrente
for nome_file in os.listdir(cartella_corrente):
    if nome_file.startswith(prefix_originale) and os.path.isfile(os.path.join(cartella_corrente, nome_file)):
        # Ottiene la parte dopo 'Boeing_898'
        parte_restante = nome_file[len(prefix_originale):]
        # Nuovo nome con '_FD' inserito
        nuovo_nome = prefix_nuovo + parte_restante
        # Copia con nuovo nome
        shutil.copy2(
            os.path.join(cartella_corrente, nome_file),
            os.path.join(destinazione, nuovo_nome)
        )
        print(f"Copiato: {nome_file} -> {nuovo_nome}")

print("Fatto tutto 😎")
