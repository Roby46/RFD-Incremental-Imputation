import numpy as np
import matplotlib.pyplot as plt
import json
from matplotlib.patches import Patch

versione_plot = "baseline"

with open(f"./risultati_test_discovery/ris_{versione_plot}/medie_{versione_plot}.json", "r") as outfile:
    data = json.load(outfile)

# Dataset (gruppi)
groups = ['actor', 'boeing', 'vehicles', 'f1', 'med', 'motogp', 'nba', 'superstore', 'president', 'cars',
          'police', 'restaurant', 'IoT_Telemetry', 'Air_9000', 'Cats_1071']

# Percentuali (asse y)
missing_values_rates = [str(r) for r in [1, 2, 3, 4, 5, 10, 20, 30, 40, 50] if str(r) in data]

# Colori
labels_segmenti = ["RFDs Found", "Specialization", "Generalizations", "RFDs not found"]
colors = ['#003049', '#2c5980', '#6c88a6', '#acc2d9']

# Layout subplot
fig, axes = plt.subplots(3, 5, figsize=(18, 10), constrained_layout=True)
axes = axes.flatten()

# Dimensioni barre
bar_width1 = 0.07  # più larga (segmentata)
bar_width2 = 0.05  # più stretta ("New RFDs")
#space_between_bars = 0.01

for idx, (ax, group) in enumerate(zip(axes, groups)):
    # Prepara i dati per il dataset corrente
    values1 = []
    values2 = []
    for rate in missing_values_rates:
        all_vals = data[rate][idx]
        print(f"{group} ({rate}%):", all_vals)
        values1.append([all_vals[0], all_vals[3], all_vals[2], all_vals[1]])
        values2.append(all_vals[4])

    values1 = np.array(values1)
    values2 = np.array(values2)

    y_indices = np.arange(len(missing_values_rates)) * 0.2

    # --- Prima barra segmentata (sopra) ---
    for i in range(values1.shape[1]):
        left = np.sum(values1[:, :i], axis=1) if i > 0 else None
        ax.barh(y_indices - bar_width2 / 2,  # più in alto
                values1[:, i],
                height=bar_width1,
                left=left,
                color=colors[i],
                edgecolor='black',
                label=labels_segmenti[i] if idx == 0 else "",
                zorder=2)

    # --- Seconda barra "New RFDs" (sotto) ---
    ax.barh(y_indices + bar_width1 / 2,
            values2,
            height=bar_width2,
            color='#ffd3b3',
            edgecolor='black',
            label='New RFDs' if idx == 0 else "",
            zorder=2)

    # Asse Y (percentuali)
    ax.set_yticks(y_indices)
    # Mostra le etichette solo nella prima colonna (idx % 5 == 0)
    if idx % 5 == 0:
        ax.set_yticklabels([f'{r}%' for r in missing_values_rates], fontsize=8)
    else:
        ax.set_yticklabels([])

    ax.invert_yaxis()  # Scala Y: 1% in alto, 50% in basso
    ax.set_xlim(0, 100)
    ax.set_xticks(np.arange(0, 101, 20))
    ax.set_title(group, fontsize=9)
    ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5, zorder=0)
    ax.tick_params(axis='x', labelsize=7)

# Legenda globale
legend_elements = [
    Patch(facecolor='#003049', edgecolor='black', label="RFDs Found"),
    Patch(facecolor='#2c5980', edgecolor='black', label="Specialization"),
    Patch(facecolor='#6c88a6', edgecolor='black', label="Generalizations"),
    Patch(facecolor='#acc2d9', edgecolor='black', label="RFDs not found"),
    Patch(facecolor='#ffd3b3', edgecolor='black', label="New RFDs")
]

fig.legend(handles=legend_elements, loc='upper center',bbox_to_anchor=(0.5, 1.03), fontsize=8, ncol=5,shadow=True)

#plt.savefig(f'./results_discovery_per_dataset_{versione_plot}_sfumato.pdf', bbox_inches='tight')
plt.show()
