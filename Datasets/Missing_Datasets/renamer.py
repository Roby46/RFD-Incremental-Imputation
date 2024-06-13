import os

def rename_files(folder_path, mapping):
    # Ordina le chiavi del dizionario di mapping in ordine crescente
    keys_sorted = sorted(mapping.keys())

    # Per ogni numero nel mapping, rinomina i file corrispondenti
    for number in keys_sorted:
        new_number = mapping[number]
        for filename in os.listdir(folder_path):
            if filename.endswith(".csv"):
                parts = filename.split("_")
                file_number = int(parts[-1].split(".")[0])
                if file_number == number:
                    new_filename = "_".join(parts[:-1]) + "_" + str(new_number) + ".csv"
                    os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))

cartella = "cars/"
mappatura = {
    1: 1,
    3: 1,
    4: 1,
    16: 2,
    17: 3,
    18: 4,
    19: 5
}
rename_files(cartella, mappatura)
