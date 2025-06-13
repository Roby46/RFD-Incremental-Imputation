import numpy as np
import matplotlib.pyplot as plt
import json
from matplotlib.patches import Patch


versione_plot = "baseline"

with open(f"./risultati_test_discovery/ris_{versione_plot}/medie_{versione_plot}.json", "r") as outfile:
    data = json.load(outfile)

# Definizione dei gruppi
groups = ['actor','boeing','vehicles','f1','med','motogp','nba','superstore','president','cars','police','restaurant','IoT_Telemetry','Air_9000','Cats_1071']

# Percentuali di missing values (le chiavi del JSON)
missing_values_rates = missing_values_rates = [str(r) for r in [1, 2, 3, 4, 5, 10, 20, 30, 40, 50] if str(r) in data]


# Colori e etichette per i segmenti delle barre
colors = ['#003049', '#d62828', '#f77f00', '#fcbf49']
labels_segmenti = ["RFDs Found", "RFDs not found", "Generalizations", "Specialization"]

fig, axes = plt.subplots(2, 5, figsize=(16, 8), constrained_layout=True)
axes = axes.flatten()

for ax, rate in zip(axes, missing_values_rates):
    values = np.array(data[rate])  # Converte i dati della chiave attuale in array NumPy
    values1 = values[:, :4]  # Primi 4 valori per le barre segmentate
    values2 = values[:, 4]   # Ultimo valore per "New RFDs"

    indices = np.arange(len(groups)) * 0.2
    bar_width1 = 0.07
    bar_width2 = 0.05
    space_between_bars = 0.010

    # Creazione delle barre segmentate
    for i in range(values1.shape[1]):
        if i == 0:
            ax.barh(indices + bar_width2 / 2 + space_between_bars, values1[:, i], height=bar_width1,
                    color=colors[i], label=labels_segmenti[i], edgecolor='black', linewidth=1, zorder=2)
        else:
            ax.barh(indices + bar_width2 / 2 + space_between_bars, values1[:, i], height=bar_width1,
                    color=colors[i], left=np.sum(values1[:, :i], axis=1),
                    label=labels_segmenti[i], edgecolor='black', linewidth=1, zorder=2)

    # Barra separata per "New RFDs"
    ax.barh(indices - bar_width2 / 2, values2, height=bar_width2, color='#ffd3b3',
            label='New RFDs', edgecolor='black', linewidth=1, zorder=2)

    # Impostazioni degli assi
    if ax in [axes[0], axes[5]]:  # Solo il primo subplot di ogni riga
        ax.set_yticks(indices)
        ax.set_yticklabels(groups, fontsize=8)
    else:
        ax.set_yticks(indices)
        ax.set_yticklabels([])  # Rimuove le etichette
    ax.set_xlim(0, 100)
    ax.set_xticks(np.arange(0, 101, 10))
    ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5, zorder=-1)
    ax.tick_params(axis='x', labelsize=7)
    ax.set_title(f'Missing Values Rate: {rate}%', fontsize=8)

legend_elements = [
    Patch(facecolor='#003049', edgecolor='black', label="RFDs Found"),
    Patch(facecolor='#d62828', edgecolor='black', label="RFDs not found"),
    Patch(facecolor='#f77f00', edgecolor='black', label="Generalizations"),
    Patch(facecolor='#fcbf49', edgecolor='black', label="Specialization"),
    Patch(facecolor='#ffd3b3', edgecolor='black', label="New RFDs")
]

# Posizionamento della legenda globale al di fuori dei subplot
fig.legend(handles=legend_elements, loc='upper center',bbox_to_anchor=(0.5,1.05), fontsize=8, ncol=5,shadow=True)
plt.savefig(f'./results_discovery_{versione_plot}.pdf', bbox_inches='tight')
plt.show()