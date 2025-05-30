import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def barplot_guadagni_dataset(file_csv, dataset_labels):
    # Carica il file CSV dei guadagni
    # Carica il file CSV dei guadagni
    df = pd.read_csv(file_csv, index_col=0)

    # Filtra solo gli algoritmi che ci interessano
    approcci = ['Hybrid','Pipeline_noRev', 'Baseline20']
    df = df[approcci]

    # 🔧 Riordina i dataset secondo l'ordine fornito
    df = df.reindex(dataset_labels)

    # Coordinate asse X
    n_dataset = len(df)
    x = np.arange(n_dataset)

    width = 0.25
    offset = [-width, 0, width]

    # Colori coerenti
    stili = {
        'Pipeline_noRev': {'color': '#FFA600'},
        'Hybrid': {'color': '#61a44f'},
        'Baseline20': {'color': '#00748f'}
    }

    fig, ax = plt.subplots(figsize=(8, 2))  # Altezza ridotta

    # Plotta le barre con bordo nero
    for i, alg in enumerate(approcci):
        ax.bar(
            x + offset[i],
            df[alg].values,
            width=width,
            label=alg,
            color=stili[alg]['color'],
            edgecolor='black',
            linewidth=0.7,
            zorder=8
        )

    # Etichette asse x
    ax.set_xticks(x)
    ax.set_xticklabels([str(i + 1) for i in range(n_dataset)], fontsize=11)
    ax.set_xlabel('Dataset $ID$', fontsize=11)
    ax.set_ylabel('RMSE Gain (%)', fontsize=11)

    # Linea dello zero
    ax.axhline(0, color='gray', linewidth=0.8)

    # Griglia e sottogriglia
    ax.grid(which='major', linestyle='-', linewidth=0.5, color='gray', alpha=0.52, zorder=0)
    ax.minorticks_on()
    ax.grid(which='minor', linestyle='dotted', linewidth=0.5, color='gray', alpha=0.4, zorder=0)

    # Legenda con rettangolini colorati
    handles = [
        plt.Rectangle((0, 0), 1, 1, color=stili[alg]['color'], label=alg)
        for alg in approcci
    ]
    fig.legend(
        handles=handles,
        loc='upper center',
        bbox_to_anchor=(0.5, 1.08),
        ncol=3,
        shadow=True,
        frameon=True,
        fontsize=10
    )

    plt.tight_layout(rect=[0, 0, 1, 0.95])  # Lascia spazio sopra per la legenda
    plt.savefig("../output/guadagno_barplot_dataset.pdf", bbox_inches='tight')
    plt.show()

# Dataset già usati
selected_datasets = ['cars', 'restaurant', 'Boeing_898', 'Cats_1071', 'police',
                     'IoT_Telemetry3000', 'actorfilms_4000', "Med_Ch_2500", "F1_REBUILT_5000",
                     "MotoGP_REBUILT_3000", 'US_Presidents_3754', 'NBA_3200', 'EV_Vehicles_4000',
                     "superstore_4500", "Air_9000"]

# Esegui il plot
barplot_guadagni_dataset('../output/guadagni_dataset.csv', selected_datasets)
