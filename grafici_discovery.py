import numpy as np
import matplotlib.pyplot as plt
from nltk.sem.chat80 import borders

# Dati di esempio: 4 gruppi, con una barra multi-segmento e una barra unica per ogni gruppo
groups = ['NBA','Cars','Actor','Admissions','Police','Callout','Restaurant','Boeing','Telemetry']

# Valori per la barra con 4 segmenti (prima barra in ogni gruppo)
values1 = np.array([[20, 10, 30, 10],
                    [30, 20, 10, 20],
                    [10, 40, 20, 30],
                    [40, 30, 20, 10],
                    [40, 30, 20, 10],
                    [40, 30, 20, 10],
                    [40, 30, 20, 10],
                    [40, 30, 20, 10],
                    [40, 30, 20, 10]])

# Valori per la barra unica (seconda barra in ogni gruppo)
values2 = np.array([7, 8, 6, 9,4,5,6,7,2])  # singolo segmento per ogni gruppo

# Colori per i segmenti della barra multi-segmento
colors = ['#003049', '#d62828', '#f77f00', '#fcbf49']  # Aggiungi i tuoi codici colore qui

# Settaggi per il grafico
fig, ax = plt.subplots(figsize=(10, 6))  # Dimensione del grafico aumentata per migliore visibilità

bar_width1 = 0.08       # larghezza per la barra multi-segmento
bar_width2 = 0.02      # larghezza per la barra singola
space_between_bars = 0.05  # spazio tra le barre all'interno di un gruppo (stessa coppia)
group_spacing = 0.2    # riduce lo spazio tra i gruppi
indices = np.arange(len(groups)) * group_spacing  # posizioni lungo l'asse y, gruppi più vicini

# Prima barra orizzontale (più grande e multi-segmento)
labels_segmenti = ["RFDs Found", "RFDs not found","Generalizations","Specialization"]
for i in range(values1.shape[1]):  # 4 segmenti
    if i == 0:
        ax.barh(indices + bar_width2/2 + space_between_bars, values1[:, i], height=bar_width1,
                color=colors[i], label=labels_segmenti[i], edgecolor='black', linewidth=1, zorder=2)
    else:
        ax.barh(indices + bar_width2/2 + space_between_bars, values1[:, i], height=bar_width1,
                color=colors[i], left=np.sum(values1[:, :i], axis=1),
                label=labels_segmenti[i], edgecolor='black', linewidth=1, zorder=2)

# Seconda barra orizzontale (più piccola e singolo segmento)
ax.barh(indices - bar_width2/2, values2, height=bar_width2, color='#ffd3b3',
        label='New RFDs', edgecolor='black', linewidth=1, zorder=2)

#b24885 similvioletto
#ffa561 similarancio
#ffd3b3 rosato

# Aggiungi etichette e legenda
ax.set_xlabel('Percentage')
#ax.set_title('Grouped Stacked Horizontal Bar Chart (Multi-segment & Single Segment)')
# Calcola il centro delle barre per ciascun gruppo
center_positions = indices + (bar_width1 + bar_width2) / 2

# Imposta le etichette con le nuove posizioni
ax.set_yticks(center_positions)
ax.set_yticklabels(groups, rotation=0)

ax.set_xlim(0, 100)  # Imposta l'asse x da 0 a 100

# Imposta i tick principali sull'asse x con intervallo di 10
ax.set_xticks(np.arange(0, 101, 10))

# Aggiungi minor ticks sull'asse x
ax.minorticks_on()

# Aggiungi grid con linee tratteggiate e sotto le barre
ax.grid(True, which='both', axis='x', linestyle='--', linewidth=0.5, zorder=-1)


# Migliora l'aspetto delle griglie minori
ax.tick_params(axis='x', which='minor', length=4)

# Mostra la legenda
legend = ax.legend(loc='lower center', bbox_to_anchor=(0.5,1.005), ncol=5, frameon=True)
# Personalizza il bordo (opzionale)
legend.get_frame().set_edgecolor('grey')  # Colore del bordo
legend.get_frame().set_linewidth(0.5)       # Spessore del bordo

# Migliora il layout per evitare sovrapposizioni
plt.tight_layout()

# Mostra il grafico
plt.show()
