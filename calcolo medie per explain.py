import re
import numpy as np
from collections import defaultdict
import pandas as pd
import matplotlib.pyplot as plt

def costruzione_file_medie():
    tipo = "baseline"

    # === Definizione gruppi e percentuali ===
    groups = ['actor', 'boeing', 'vehicles', 'f1', 'med', 'motogp', 'nba', 'superstore',
              'president', 'cars', 'police', 'restaurant', 'IoT_Telemetry', 'Air_9000', 'Cats_1071']
    group_index = {name: idx for idx, name in enumerate(groups)}

    # === Parsing del file txt ===
    data = defaultdict(lambda: [None] * len(groups))  # {rate_str: list of length 15}

    with open(f"valori_{tipo}.txt", "r") as f:
        for line in f:
            match = re.match(r"(\w+)\s+\((\d+)%\):\s+\[([^\]]+)\]", line)
            if match:
                dataset = match.group(1)
                rate = match.group(2)
                values = [float(v.strip()) for v in match.group(3).split(',')]
                idx = group_index[dataset]
                data[rate][idx] = values

    # === Lista percentuali ordinate ===
    missing_values_rates = sorted(data.keys(), key=lambda x: int(x))

    # === Calcolo medie ===
    media_per_dataset = {}
    media_per_percentuale = defaultdict(list)

    for idx, group in enumerate(groups):
        valori_dataset = []

        for rate in missing_values_rates:
            valori = data[rate][idx]  # [found, not found, gen, spec, new]
            if valori is not None:
                valori_dataset.append(valori)
                media_per_percentuale[rate].append(valori)

        media_per_dataset[group] = np.round(np.mean(valori_dataset, axis=0),2)

    for rate in media_per_percentuale:
        media_per_percentuale[rate] = np.round(np.mean(media_per_percentuale[rate], axis=0),2)

    # === Output di esempio (facoltativo) ===
    print("Media per dataset:")
    for group, media in media_per_dataset.items():
        print(f"{group}: {media}")

    print("\nMedia per percentuale:")
    for rate, media in media_per_percentuale.items():
        print(f"{rate}%: {media}")

    # Converti dizionario in DataFrame
    df_dataset = pd.DataFrame.from_dict(media_per_dataset, orient='index',
        columns=["RFDs Found", "RFDs Not Found", "Generalizations", "Specializations", "New RFDs"])

    df_dataset.index.name = "Dataset"
    df_dataset.to_csv(f"{tipo}_medie_per_dataset.csv")

    # Converti dizionario in DataFrame
    df_percentuale = pd.DataFrame.from_dict(media_per_percentuale, orient='index',
        columns=["RFDs Found", "RFDs Not Found", "Generalizations", "Specializations", "New RFDs"])

    df_percentuale.index.name = "Missing Rate (%)"
    df_percentuale.to_csv(f"{tipo}_medie_per_percentuale.csv")

def calcolo_differenze():
    df_base = pd.read_csv("baseline_medie_per_dataset.csv")
    df_inc = pd.read_csv("inc_medie_per_dataset.csv")

    notfound_base = df_base["RFDs Not Found"]
    notfound_inc = df_inc["RFDs Not Found"]
    datasets = df_inc["Dataset"]

    dict_finale = {}
    print(notfound_base)
    print(notfound_inc)
    array_percentuali = []
    for i in range(0,len(notfound_base)):
        rapporto = notfound_base[i] - notfound_inc[i]
        percentuale_rapporto = np.round(((rapporto * 100) / notfound_base[i]),2)
        print("Dataset:",datasets[i])
        print("notfound_base[i]:",notfound_base[i])
        print("notfound_inc[i]:",notfound_inc[i])
        print("rapporto:",rapporto)
        print("percentuale rapprto:",percentuale_rapporto)
        print("\n")

        dict_finale.update({datasets[i]:percentuale_rapporto})
        array_percentuali.append(percentuale_rapporto)
    print(array_percentuali)
    print(dict_finale)

    df_base = pd.read_csv("baseline_medie_per_percentuale.csv")
    df_inc = pd.read_csv("inc_medie_per_percentuale.csv")

    notfound_base = df_base["RFDs Not Found"]
    notfound_inc = df_inc["RFDs Not Found"]
    datasets = df_inc["Missing Rate (%)"]

    dict_finale_missing = {}
    #print(notfound_base)
    #print(notfound_inc)
    array_percentuali = []
    for i in range(0, len(notfound_base)):
        rapporto = notfound_base[i] - notfound_inc[i]
        percentuale_rapporto = np.round(((rapporto * 100) / notfound_base[i]), 2)
        #print("Dataset:", datasets[i])
        #print("notfound_base[i]:", notfound_base[i])
        #print("notfound_inc[i]:", notfound_inc[i])
        #print("rapporto:", rapporto)
        #print("percentuale rapprto:", percentuale_rapporto)
        #print("\n")

        dict_finale_missing.update({datasets[i]: percentuale_rapporto})
        array_percentuali.append(percentuale_rapporto)
    #print(array_percentuali)
    print(dict_finale_missing)
    return dict_finale,dict_finale_missing

def radar_plot_builder(dizionario,dizionario_perc):
    '''
    # Ordina i valori
    valori = list(dizionario.values())

    # Imposta i punti
    num_vars = len(valori)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    valori += valori[:1]  # Chiudi il cerchio
    angles += angles[:1]

    # Etichette da 1 a 15
    labels = [f"$ID$ {i}" for i in range(1, 16)]

    # Radar plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # 2. Ingrandisci tick delle etichette angolari (1–15)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels, fontsize=15)  # Aumenta fontsize
    ax.tick_params(axis='x', pad=13)  # Puoi provare valori come 6, 8, 10

    # 3. Etichette radiali (0, 20, ..., 80) SOLO in alto
    ax.set_rlabel_position(0)  # Mostra le etichette radiali in alto (0°)

    # 4. Mostra solo fino a 80 (escludi 100)
    ax.set_yticks([0, 20, 40, 60, 80])
    ax.set_yticklabels(['0', '20', '40', '60', '80'], fontsize=15)

    # 5. Limite asse
    ax.set_ylim(0, 100)

    ax.plot(angles, valori, color='blue', linewidth=2)
    ax.fill(angles, valori, color='skyblue', alpha=0.4)

    # Etichette radiali (1...15)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    # Range asse
    ax.set_ylim(0, 100)

    plt.tight_layout()
    plt.show()

    # Ordina le chiavi
    labels = list(dizionario_perc.keys())
    values = list(dizionario_perc.values())

    # Chiudi il cerchio (aggiungi primo valore e primo angolo)
    values += values[:1]  # Chiude la linea nel radar
    angles = np.linspace(0, 2 * np.pi, len(values), endpoint=True)

    # Crea il radar plot
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # Inizio dall'alto, senso orario
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Imposta le etichette degli assi angolari
    ax.set_xticks(angles[:-1])  # Solo 10 tick
    ax.set_xticklabels([f"${p}\\%$" for p in labels], fontsize=15)
    ax.tick_params(axis='x', pad=6)

    # Etichette radiali solo sopra, senza "100"
    ax.set_rlabel_position(0)
    ax.set_yticks([0, 20, 40, 60, 80])
    ax.set_yticklabels(['0', '20', '40', '60', '80'], fontsize=15)
    ax.set_ylim(0, 100)

    # Disegna radar
    ax.plot(angles, values, color='green', linewidth=2)
    ax.fill(angles, values, color='lightgreen', alpha=0.4)

    plt.tight_layout()
    plt.show()
    '''
    # Crea figura con 2 subplot
    fig, axes = plt.subplots(1, 2, figsize=(14, 6), subplot_kw=dict(polar=True))


    # --- Primo radar plot (15 ID numerati) ---
    valori_1 = list(dizionario.values())
    num_vars_1 = len(valori_1)
    angles_1 = np.linspace(0, 2 * np.pi, num_vars_1, endpoint=False).tolist()
    valori_1 += valori_1[:1]
    angles_1 += angles_1[:1]
    labels_1 = [f"$ID$ {i}" for i in range(1, num_vars_1 + 1)]

    ax1 = axes[0]
    ax1.set_theta_offset(np.pi / 2)
    ax1.set_theta_direction(-1)
    ax1.set_xticks(angles_1[:-1])
    ax1.set_xticklabels(labels_1, fontsize=15)
    ax1.tick_params(axis='x', pad=13)
    ax1.set_rlabel_position(0)
    ax1.set_yticks([0, 20, 40, 60, 80])
    ax1.set_yticklabels(['0', '20', '40', '60', '80'], fontsize=15)
    ax1.set_ylim(0, 100)
    ax1.plot(angles_1, valori_1, color='blue', linewidth=2)
    ax1.fill(angles_1, valori_1, color='skyblue', alpha=0.4)

    # --- Secondo radar plot (percentuali) ---
    labels_2 = list(dizionario_perc.keys())
    valori_2 = list(dizionario_perc.values())
    valori_2 += valori_2[:1]
    angles_2 = np.linspace(0, 2 * np.pi, len(valori_2), endpoint=True)

    ax2 = axes[1]
    ax2.set_theta_offset(np.pi / 2)
    ax2.set_theta_direction(-1)
    ax2.set_xticks(angles_2[:-1])
    ax2.set_xticklabels([f"${p}\\%$" for p in labels_2], fontsize=15)
    ax2.tick_params(axis='x', pad=10)
    ax2.set_rlabel_position(0)
    ax2.set_yticks([0, 20, 40, 60, 80])
    ax2.set_yticklabels(['0', '20', '40', '60', '80'], fontsize=15)
    ax2.set_ylim(0, 100)
    ax2.plot(angles_2, valori_2, color='green', linewidth=2)
    ax2.fill(angles_2, valori_2, color='lightgreen', alpha=0.4)
    plt.subplots_adjust(wspace=0.1)
    # Mostra tutto
    #plt.tight_layout()
    plt.show()

def barplot_missing_rate(dizionario_perc):

    # Ordina per chiave
    labels = list(dizionario_perc.keys())
    values = list(dizionario_perc.values())

    # Plot
    plt.figure(figsize=(8, 5))
    bars = plt.bar([f"{k}%" for k in labels], values, color='lightgreen', edgecolor='green',zorder=2)

    # Aggiungi valori sopra le barre
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, height + 1, f"{height:.1f}", ha='center', va='bottom', fontsize=9)

    # Stile asse y
    plt.ylim(0, 100)
    #plt.ylabel("Media (%)", fontsize=12)
    #plt.xlabel("Percentuale di Missing", fontsize=12)
    #plt.title("Media per Percentuale di Missing", fontsize=14)
    plt.grid(axis='y', linestyle='--', linewidth=0.5,zorder=1)

    plt.tight_layout()
    plt.savefig(f'./notfound_reduction.pdf', bbox_inches='tight')
    plt.show()



dict_for_dataset,dict_for_missing = calcolo_differenze()
#radar_plot_builder(dict_for_dataset,dict_for_missing)
barplot_missing_rate(dict_for_missing)