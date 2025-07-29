import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def barplot_guadagni_composito(dataset_csv, mr_csv, dataset_labels):
    df_dataset = pd.read_csv(dataset_csv, index_col=0)
    approcci = ['Hybrid','Pipeline_noRev', 'Baseline20']
    df_dataset = df_dataset[approcci]
    df_dataset = df_dataset.reindex(dataset_labels)

    df_mr = pd.read_csv(mr_csv)
    df_mr = df_mr[['missing_rate'] + approcci].dropna()

    fig, axes = plt.subplots(nrows=2, figsize=(8, 3.5), sharex=False)

    stili = {
        'Pipeline_noRev': {'color': '#FFA600'},
        'Hybrid': {'color': '#61a44f'},
        'Baseline20': {'color': '#00748f'}
    }

    width = 0.25
    offset = [-width, 0, width]

    # === Primo subplot ===
    n1 = len(df_dataset)
    x1 = np.arange(n1)
    for i, alg in enumerate(approcci):
        axes[0].bar(
            x1 + offset[i],
            df_dataset[alg].values,
            width=width,
            label=alg,
            color=stili[alg]['color'],
            edgecolor='black',
            linewidth=0.7,
            zorder=8
        )
    axes[0].set_xticks(x1)
    axes[0].set_xticklabels([str(i + 1) for i in range(n1)], fontsize=10)
    axes[0].set_ylabel('RMSE Gain (%)', fontsize=11)
    axes[0].set_xlabel('Dataset $ID$', fontsize=11)
    axes[0].axhline(0, color='gray', linewidth=0.8)
    axes[0].grid(which='major', linestyle='-', linewidth=0.5, color='gray', alpha=0.52, zorder=0)
    axes[0].minorticks_on()
    axes[0].grid(which='minor', linestyle='dotted', linewidth=0.5, color='gray', alpha=0.4, zorder=0)
    axes[0].set_ylim(bottom=-7)

    # === Secondo subplot ===
    x2_valid = np.linspace(0, n1 - 1, len(df_mr))  # 10 punti distribuiti su 15 slot

    for i, alg in enumerate(approcci):
        axes[1].bar(
            x2_valid + offset[i],
            df_mr[alg].values,
            width=width,
            color=stili[alg]['color'],
            edgecolor='black',
            linewidth=0.7,
            zorder=8
        )

    axes[1].set_xticks(x2_valid)
    axes[1].set_xticklabels(df_mr['missing_rate'].astype(str), fontsize=10)
    axes[1].set_ylabel('RMSE Gain (%)', fontsize=11)
    axes[1].set_xlabel('Missing Rate (%)', fontsize=11)
    axes[1].axhline(0, color='gray', linewidth=0.8)
    axes[1].grid(which='major', linestyle='-', linewidth=0.5, color='gray', alpha=0.52, zorder=0)
    axes[1].minorticks_on()
    axes[1].grid(which='minor', linestyle='dotted', linewidth=0.5, color='gray', alpha=0.4, zorder=0)
    axes[1].set_ylim(bottom=-5)
    axes[1].set_yticks([0, 20, 40, 60])

    # === Legenda comune ===
    label_map = {
        'Pipeline_noRev': 'PipelineNoRev',
        'Hybrid': 'Hybrid',
        'Baseline20': 'Baseline'  #
    }

    handles = [
        plt.Rectangle((0, 0), 1, 1, color=stili[alg]['color'], label=label_map[alg])
        for alg in approcci
    ]

    fig.legend(
        handles=handles,
        loc='upper center',
        bbox_to_anchor=(0.5, 1.05),
        ncol=3,
        shadow=True,
        frameon=True,
        fontsize=10
    )

    plt.tight_layout(rect=[0, 0, 1, 0.97])
    plt.savefig("guadagni_barplot_composito.pdf", bbox_inches='tight')
    plt.show()

# === Dataset usati ===
selected_datasets = ['cars', 'restaurant', 'Boeing_898', 'Cats_1071', 'police',
                     'IoT_Telemetry3000', 'actorfilms_4000', "Med_Ch_2500", "F1_REBUILT_5000",
                     "MotoGP_REBUILT_3000", 'US_Presidents_3754', 'NBA_3200', 'EV_Vehicles_4000',
                     "superstore_4500", "Air_9000"]

# === Esegui ===
barplot_guadagni_composito(
    'guadagni_dataset.csv',
    'guadagni_missing_rate.csv',
    selected_datasets
)
