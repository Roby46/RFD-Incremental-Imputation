import numpy as np
import matplotlib.pyplot as plt
import json
from matplotlib.patches import Patch

versione_plot = "incremental"

with open(f"./risultati_test_discovery/ris_{versione_plot}/medie_{versione_plot}.json", "r") as outfile:
    data = json.load(outfile)


# Dataset (gruppi)
groups = ['Cars ($ID$ $1$)','Restaurant ($ID$ $2$)','Boeing ($ID$ $3$)','Cats ($ID$ $4$)','Police ($ID$ $5$)','IoT_Telemetry ($ID$ $6$)','Actors ($ID$ $7$)',
          'Medical Charges ($ID$ $8$)','F1 ($ID$ $9$)','MotoGP ($ID$ $10$)','US Presidents ($ID$ $11$)','NBA ($ID$ $12$)','EV Vehicles ($ID$ $13$)','Superstore ($ID$ $14$)','Air Quality ($ID$ $15$)']

# Percentuali (asse y)
missing_values_rates = [str(r) for r in [1, 2, 3, 4, 5, 10, 20, 30, 40, 50] if str(r) in data]

# Colori
labels_segmenti = ["RFDs Found", "Specialization", "Generalizations", "RFDs not found"]
#colors = [  '#00687a','#5ea4ae', '#00BEBE','#7DD6D6']
colors = ["#566285", "#47BBFF", "#9BDAFF", "#E6EFF4"]
# Layout subplot
#fig, axes = plt.subplots(3, 5, figsize=(18, 9), constrained_layout=True, sharex=True)
fig, axes = plt.subplots(3, 5, figsize=(18, 9), constrained_layout=True, sharex=True)
axes = axes.flatten()

# Dimensioni barre
bar_width1 = 0.07  # più larga (segmentata)
bar_width2 = 0.07  # più stretta ("New RFDs")
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
            #color='#f4a67e',
            color = '#f4a67e',
            edgecolor='black',
            label='New RFDs' if idx == 0 else "",
            zorder=2)

    # Asse Y (percentuali)
    ax.set_yticks(y_indices)
    # Mostra le etichette solo nella prima colonna (idx % 5 == 0)
    if idx % 5 == 0:
        ax.set_yticklabels([f'{r}' for r in missing_values_rates], fontsize=12)
    else:
        ax.set_yticklabels([])

    ax.invert_yaxis()  # Scala Y: 1% in alto, 50% in basso
    ax.set_xlim(0, 100)
    ax.set_xticks(np.arange(0, 101, 10))
    ax.set_title(group, fontsize=12)
    ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5, zorder=0)
    ax.tick_params(axis='x', labelsize=10)

# Legenda globale
legend_elements = [
    Patch(facecolor='#566285', edgecolor='black', label="RFDs Found"),
    Patch(facecolor='#47BBFF', edgecolor='black', label="Specializations"),
    Patch(facecolor='#9BDAFF', edgecolor='black', label="Generalizations"),
    Patch(facecolor='#E6EFF4', edgecolor='black', label="RFDs not found"),
    Patch(facecolor='#f4a67e', edgecolor='black', label="New RFDs")
]

# Etichetta asse X comune (in basso al centro)
fig.text(0.5, -0.02, 'Percentage of RFDs (%)', ha='center', fontsize=14)

# Etichetta asse Y comune (verticale, al centro sinistra)
fig.text(-0.01, 0.5, 'Missing Rate (%)', va='center', rotation='vertical', fontsize=14)

fig.legend(handles=legend_elements, loc='upper center',bbox_to_anchor=(0.5, 1.05), fontsize=12, ncol=5,shadow=True)

plt.savefig(f'./discovery_results_{versione_plot}.pdf', bbox_inches='tight')
#plt.savefig(f'ALT2.pdf', bbox_inches='tight')
plt.show()
