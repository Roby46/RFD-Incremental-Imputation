import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def load_rmse_data(filepath, selected_datasets, dataset_name_map):
    df = pd.read_csv(filepath, sep=';')
    df['dataset'] = df['dataset'].replace(dataset_name_map)


    datasets = {}

    for dataset_name in selected_datasets:
        mapped_name = dataset_name_map.get(dataset_name, dataset_name)  # Usa il nome mappato se esiste

        if mapped_name in df['dataset'].unique():
            df_dataset = df[df['dataset'] == mapped_name]
            rmse_results = {}
            algorithms = df_dataset['algoritmo'].unique()

            for algorithm in algorithms:
                df_algorithm = df_dataset[df_dataset['algoritmo'] == algorithm].sort_values(by='MV')
                rmse_values = df_algorithm['metric1'].tolist()
                rmse_results[algorithm] = rmse_values

            datasets[mapped_name] = rmse_results
        else:
            print(f"Warning: Il dataset '{dataset_name}' non è presente nel file CSV.")

    return datasets


def plot_rmse_results(datasets, ncols=2):
    num_datasets = len(datasets)
    r1 = np.arange(10)  # Indici per le percentuali di valori mancanti

    # Calcolo del numero di righe necessarie
    nrows = (num_datasets + ncols - 1) // ncols  # Formula per arrotondare verso l'alto

    #fig, axs = plt.subplots(nrows, ncols, figsize=(13, 6), sharey=True, sharex=True)
    fig, axs = plt.subplots(nrows, ncols, figsize=(22, 8), sharey=True, sharex=True)
    # Modifica degli spazi orizzontali e verticali
    fig.subplots_adjust(hspace=0.20, wspace=0.04)  # Riduci hspace e wspace

    # Appiattire gli assi se nrows > 1
    axs = axs.flatten() if nrows > 1 else axs

    for i, (dataset_name, results) in enumerate(datasets.items()):
        # Plottare RMSE per ogni algoritmo in un singolo grafico
        for algorithm, rmse_means in results.items():
            print(algorithm, rmse_means)
            if 'pipeline' in algorithm:
                axs[i].plot(r1, rmse_means, marker="o", markersize=5, color="#ff0000", zorder=2, label='PipelineNoRev')
            elif 'baseline' in algorithm:  # Altri algoritmi, se ce ne sono
                axs[i].plot(r1, rmse_means, marker="x", markersize=8, color="#00748f", zorder=3, label='Pipeline')

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
            axs[i].set_ylabel('metric1', rotation='vertical')

        # Imposta l'etichetta "Missing Rate" solo per l'ultima riga
        if i >= (nrows - 1) * ncols:
            axs[i].set_xlabel('Missing Rate')

    # Gestire grafici vuoti se non ci sono abbastanza dataset
    for j in range(i + 1, nrows * ncols):
        axs[j].axis('off')  # Nascondere gli assi vuoti

    handles = [
        plt.Line2D([0], [0], color='#ff0000', linestyle='-', label='Pipeline', marker="o", markersize=10),
        plt.Line2D([0], [0], color='#00748f', linestyle='-', label='Baseline', marker="x", markersize=12)
    ]

    fig.legend(handles=handles, loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1), shadow=True)

    plt.savefig("metric1_results.pdf", bbox_inches='tight')
    plt.show()


# Esempio di utilizzo
filepath = '../ALL_Results_metric1.csv'  # Modifica con il percorso del tuo CSV
selected_datasets = ['cars', 'restaurant', 'Boeing_898', 'Cats_1071', 'police', 'IoT_Telemetry3000', 'actorfilms_4000', "Med_Ch_2500",  "F1_REBUILT_5000", "MotoGP_REBUILT_3000", 'US_Presidents_3754', 'NBA_3200', 'EV_Vehicles_4000', "superstore_4500","Air_9000"]


dataset_name_map = {
    'cars': 'Cars',
    'restaurant': 'Restaurant',
    'Boeing_898': 'Boeing',
    'Cats_1071': 'Cats',
    'police': 'Police',
    'IoT_Telemetry3000': 'IoT_Telemetry',
    'actorfilms_4000': 'Actors',
    'Med_Ch_2500': 'Medical Charges',
    'F1_REBUILT_5000': 'F1',
    'MotoGP_REBUILT_3000': 'MotoGP',
    'US_Presidents_3754': 'US Presidents',
    'NBA_3200': 'NBA',
    'EV_Vehicles_4000': 'EV Vehicles',
    'superstore_4500': 'Superstore',
    'Air_9000': 'Air Quality',
    'cars_MNAR': 'Cars_MNAR',
    'cars_MBUV': 'Cars_MBUV',
    'restaurant_MNAR': 'restaurant_MNAR',
    'restaurant_MBUV': 'restaurant_MBUV',
    'Boeing_898_MNAR': 'Boeing_MNAR',
    'Boeing_898_MBUV': 'Boeing_MBUV',
    'police_MNAR': 'police_MNAR',
    'police_MBUV': 'police_MBUV'
}


datasets = load_rmse_data(filepath, selected_datasets, dataset_name_map)  # Carica i dati RMSE
print(datasets)
plot_rmse_results(datasets, ncols=4)  # Mostra i risultati, specificando il numero di colonne
