import os
import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
    return result['encoding']

def main():
    folder_path = f'Preprocessed_Datasets/'  # Inserisci il percorso della cartella contenente i CSV
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    for csv_file in csv_files:
        file_path = os.path.join(folder_path, csv_file)
        encoding = detect_encoding(file_path)
        print(f"File: {csv_file}, Encoding: {encoding}")

if __name__ == "__main__":
    main()
