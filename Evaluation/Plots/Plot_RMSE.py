import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def load_rmse_data(filepath, selected_datasets):
    df = pd.read_csv(filepath, sep=';')
    datasets = {}

    for dataset_name in selected_datasets:
        if dataset_name in df['dataset'].unique():
            df_dataset = df[df['dataset'] == dataset_name]
            rmse_results = {}
            algorithms = df_dataset['algoritmo'].unique()

            for algorithm in algorithms:
                df_algorithm = df_dataset[df_dataset['algoritmo'] == algorithm]
                rmse_means = []
                mv_percentages = df_algorithm['MV'].unique()

                # Calcolare la media RMSE per ciascuna percentuale di valori mancanti
                for mv in sorted(mv_percentages):
                    rmse_mean = df_algorithm[df_algorithm['MV'] == mv]['rmse'].mean()
                    rmse_means.append(rmse_mean)

                rmse_results[algorithm] = rmse_means

            datasets[dataset_name] = rmse_results
        else:
            print(f"Warning: Il dataset '{dataset_name}' non è presente nel file CSV.")

    return datasets


def plot_rmse_results(datasets, ncols=2):
    num_datasets = len(datasets)
    r1 = np.arange(10)  # Indici per le percentuali di valori mancanti

    # Calcolo del numero di righe necessarie
    nrows = (num_datasets + ncols - 1) // ncols  # Formula per arrotondare verso l'alto

    fig, axs = plt.subplots(nrows, ncols, figsize=(13, 6), sharey=True, sharex=True)  # Aggiunto sharex=True

    # Modifica degli spazi orizzontali e verticali
    fig.subplots_adjust(hspace=0.20, wspace=0.04)  # Riduci hspace e wspace

    # Appiattire gli assi se nrows > 1
    axs = axs.flatten() if nrows > 1 else axs

    for i, (dataset_name, results) in enumerate(datasets.items()):
        # Plottare RMSE per ogni algoritmo in un singolo grafico
        for algorithm, rmse_means in results.items():
            print(algorithm, rmse_means)
            if 'Pipeline_noRev' in algorithm:
                axs[i].plot(r1, rmse_means, marker="o", markersize=5, color="#FFA600", zorder=2, label='PipelineNoRev')
            elif 'Baseline20' in algorithm:
                axs[i].plot(r1, rmse_means, marker="2", markersize=10, color="#00748f", zorder=2, label='Baseline20')
            elif 'Hybrid' in algorithm:
                axs[i].plot(r1, rmse_means, marker="2", markersize=10, color="#61a44f", zorder=3, linestyle='dashdot', label='Hybrid')
            elif 'Pipeline' in algorithm:  # Altri algoritmi, se ce ne sono
                axs[i].plot(r1, rmse_means, marker="x", markersize=8, color="#ff0000", zorder=3, label='Pipeline')

        axs[i].set_xticks(r1)
        axs[i].set_xticklabels(["1", "2", "3", "4", "5", "10", "20", "30", "40", "50"])
        axs[i].set_title(f'{dataset_name}', fontsize=10)
        axs[i].tick_params(axis='x', which='major', labelsize=8)
        axs[i].tick_params(axis='y', which='major', labelsize=11)
        axs[i].minorticks_on()
        axs[i].grid(which='major', linestyle='-', linewidth='0.5', color='gray', alpha=0.52)
        axs[i].grid(which='minor', linewidth='0.5', linestyle='dotted', color='gray', alpha=0.4)
        axs[i].xaxis.set_minor_locator(MultipleLocator(1))
        axs[i].yaxis.set_minor_locator(MultipleLocator(0.05))
        axs[i].set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])

        # Imposta l'etichetta RMSE solo per il primo subplot di ogni riga
        if i % ncols == 0:
            axs[i].set_ylabel('RMSE', rotation='vertical')

        # Imposta l'etichetta "Missing Rate" solo per l'ultima riga
        if i >= (nrows - 1) * ncols:
            axs[i].set_xlabel('Missing Rate')

    # Gestire grafici vuoti se non ci sono abbastanza dataset
    for j in range(i + 1, nrows * ncols):
        axs[j].axis('off')  # Nascondere gli assi vuoti

    handles = [
        plt.Line2D([0], [0], color='#ff0000', linestyle='-', label='Pipeline', marker="x", markersize=10),
        plt.Line2D([0], [0], color='#FFA600', linestyle='-', label='PipelineNoRev', marker="o"),
        plt.Line2D([0], [0], color='#61a44f', linestyle='dashdot', label='Hybrid', marker="2", markersize=10),
        plt.Line2D([0], [0], color='#00748f', linestyle='-', label='Baseline20', marker="2", markersize=12)
    ]

    fig.legend(handles=handles, loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1), shadow=True)

    plt.savefig("rmse_results.pdf", bbox_inches='tight')
    plt.show()


# Esempio di utilizzo
filepath = '../ALL_Results_v2.csv'  # Modifica con il percorso del tuo CSV
selected_datasets = ['Boeing_898', 'actorfilms_4000', 'restaurant', 'NBA_3200', 'EV_Vehicles_4000', 'US_Presidents_3754', 'cars', "superstore_4500", "police"]  # Aggiungi altri dataset qui
datasets = load_rmse_data(filepath, selected_datasets)  # Carica i dati RMSE
print(datasets)
plot_rmse_results(datasets, ncols=3)  # Mostra i risultati, specificando il numero di colonne
