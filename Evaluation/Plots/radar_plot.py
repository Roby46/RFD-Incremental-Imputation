import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def radar_plot_gain(file_csv):
    # Leggi il file CSV
    df = pd.read_csv(file_csv, index_col=0)

    print(df)

    # Assicuriamoci che l'indice siano i missing_rate come stringhe
    df.index = df.index.astype(str)

    # Ordina per i missing rate numerici
    ordered_rates = ['1', '2', '3', '4', '5', '10', '20', '30', '40', '50']
    df = df.loc[ordered_rates]

    # Lista degli approcci da confrontare (escludi 'Pipeline' se presente)
    approcci = [col for col in df.columns if col != 'Pipeline']

    # Valori per ciascun approccio
    values_dict = {alg: df[alg].values for alg in approcci}

    # Angoli per il radar plot
    num_vars = len(ordered_rates)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()
    angles += angles[:1]  # chiudi il cerchio

    # Setup del plot
    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))

    # Stili personalizzati per i 3 approcci
    stili = {
        'Pipeline_noRev': {'color': '#FFA600', 'linestyle': '-', 'marker': 'o', 'markersize': 6},
        'Hybrid': {'color': '#61a44f', 'linestyle': 'dashdot', 'marker': '2', 'markersize': 10},
        'Baseline20': {'color': '#00748f', 'linestyle': '-', 'marker': '2', 'markersize': 12},
    }

    for alg, values in values_dict.items():
        val = values.tolist()
        val += val[:1]  # chiudi il cerchio
        style = stili.get(alg, {'color': 'gray', 'linestyle': '--', 'marker': '.', 'markersize': 6})
        ax.plot(angles, val, label=alg,
                color=style['color'],
                linestyle=style['linestyle'],
                markersize=style['markersize'],
                linewidth=2)
        # Griglia principale tratteggiata
        ax.yaxis.grid(True, linestyle='--', color='gray', alpha=0.7)
        ax.xaxis.grid(True, linestyle='--', color='gray', alpha=0.7)
        ax.fill(angles, val, color=style['color'], alpha=0.1)

    ax.yaxis.set_zorder(10)

    # Settaggi dell'asse
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # Etichette degli assi
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(ordered_rates)

    # Aggiunta griglia e legenda
    ax.set_rlabel_position(0)

    handles = [
        plt.Line2D([0], [0], color='#FFA600', linestyle='-', label='PipelineNoRev'),
        plt.Line2D([0], [0], color='#61a44f', linestyle='dashdot', label='Hybrid', markersize=10),
        plt.Line2D([0], [0], color='#00748f', linestyle='-', label='Baseline20', markersize=12)
    ]

    fig.legend(handles=handles, loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1.0), shadow=True, fontsize=11)


    plt.tight_layout()
    plt.savefig("../output/gain_radar_plot.pdf")
    plt.show()


# Esegui il plot
radar_plot_gain('../output/guadagni_missing_rate.csv')
