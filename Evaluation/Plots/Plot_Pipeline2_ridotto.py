import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def load_rmse_data(filepath, selected_datasets, dataset_name_map,metrica):
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
                rmse_values = df_algorithm[metrica].tolist()
                rmse_results[algorithm] = rmse_values

            datasets[mapped_name] = rmse_results
        else:
            print(f"Warning: Il dataset '{dataset_name}' non è presente nel file CSV.")

    return datasets

def plot_rmse_results(datasets,metrica,tipologia,ncols=2):
    num_datasets = len(datasets)
    r1 = np.arange(10)  # Indici per le percentuali di valori mancanti

    # Calcolo del numero di righe necessarie
    nrows = (num_datasets + ncols - 1) // ncols  # Formula per arrotondare verso l'alto

    #fig, axs = plt.subplots(nrows, ncols, figsize=(13, 6), sharey=True, sharex=True)
    fig, axs = plt.subplots(nrows, ncols, figsize=(7, 1.4), sharey=True, sharex=True)
    # Modifica degli spazi orizzontali e verticali
    fig.subplots_adjust(hspace=0.20, wspace=0.04)  # Riduci hspace e wspace

    # Appiattire gli assi se nrows > 1
    axs = axs.flatten() if nrows > 1 else axs

    for i, (dataset_name, results) in enumerate(datasets.items()):
        # Plottare RMSE per ogni algoritmo in un singolo grafico
        for algorithm, rmse_means in results.items():
            print(algorithm, rmse_means)
            if 'pipeline' in algorithm:
                axs[i].plot(r1, rmse_means, marker="o", markersize=3.5, color="#ff0000", zorder=2, label='PipelineNoRev')
            elif 'baseline' in algorithm:  # Altri algoritmi, se ce ne sono
                axs[i].plot(r1, rmse_means, marker="x", markersize=5, color="#00748f", zorder=3, label='Pipeline')

        axs[i].set_xticks(r1)
        axs[i].set_xticklabels(["1", "2", "3", "4", "5", "10", "20", "30", "40", "50"])
        axs[i].set_title(f'{dataset_name}', fontsize=10)
        axs[i].tick_params(axis='x', which='major', labelsize=6)
        axs[i].tick_params(axis='y', which='major', labelsize=8)
        axs[i].minorticks_on()
        axs[i].grid(which='major', linestyle='-', linewidth='0.5', color='gray', alpha=0.52)
        axs[i].grid(which='minor', linewidth='0.5', linestyle='dotted', color='gray', alpha=0.4)
        axs[i].xaxis.set_minor_locator(MultipleLocator(1))
        axs[i].yaxis.set_minor_locator(MultipleLocator(0.05))
        axs[i].set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])

        # Imposta l'etichetta RMSE solo per il primo subplot di ogni riga
        if i % ncols == 0:
            axs[i].set_ylabel("Divergence", rotation='vertical')

        # Imposta l'etichetta "Missing Rate" solo per l'ultima riga
        if i >= (nrows - 1) * ncols:
            axs[i].set_xlabel('Missing Rate')

    # Gestire grafici vuoti se non ci sono abbastanza dataset
    for j in range(i + 1, nrows * ncols):
        axs[j].axis('off')  # Nascondere gli assi vuoti

    handles = [
        plt.Line2D([0], [0], color='#ff0000', linestyle='-', label='Discovery Pipeline', marker="o", markersize=6),
        plt.Line2D([0], [0], color='#00748f', linestyle='-', label='Baseline', marker="x", markersize=9)
    ]

    fig.legend(handles=handles, loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1.23), shadow=True, fontsize=7)

    plt.savefig(f"{metrica}_results_{tipologia}_{thr}.pdf", bbox_inches='tight')
    plt.show()

def plot_rmse_results_mnar(datasets,metrica,tipologia,ncols=2):
    num_datasets = len(datasets)
    r1 = np.arange(10)  # Indici per le percentuali di valori mancanti

    # Calcolo del numero di righe necessarie
    nrows = (num_datasets + ncols - 1) // ncols  # Formula per arrotondare verso l'alto

    #fig, axs = plt.subplots(nrows, ncols, figsize=(13, 6), sharey=True, sharex=True)
    fig, axs = plt.subplots(nrows, ncols, figsize=(7, 3), sharey=True, sharex=True)
    # Modifica degli spazi orizzontali e verticali
    fig.subplots_adjust(hspace=0.25, wspace=0.04)  # Riduci hspace e wspace

    # Appiattire gli assi se nrows > 1
    axs = axs.flatten() if nrows > 1 else axs

    for i, (dataset_name, results) in enumerate(datasets.items()):
        # Plottare RMSE per ogni algoritmo in un singolo grafico
        for algorithm, rmse_means in results.items():
            print(algorithm, rmse_means)
            if 'pipeline' in algorithm:
                axs[i].plot(r1, rmse_means, marker="o", markersize=3.5, color="#ff0000", zorder=2, label='PipelineNoRev')
            elif 'baseline' in algorithm:  # Altri algoritmi, se ce ne sono
                axs[i].plot(r1, rmse_means, marker="x", markersize=5, color="#00748f", zorder=3, label='Pipeline')

        axs[i].set_xticks(r1)
        axs[i].set_xticklabels(["1", "2", "3", "4", "5", "10", "20", "30", "40", "50"])
        axs[i].set_title(f'{dataset_name}', fontsize=10)
        axs[i].tick_params(axis='x', which='major', labelsize=6)
        axs[i].tick_params(axis='y', which='major', labelsize=8)
        axs[i].minorticks_on()
        axs[i].grid(which='major', linestyle='-', linewidth='0.5', color='gray', alpha=0.52)
        axs[i].grid(which='minor', linewidth='0.5', linestyle='dotted', color='gray', alpha=0.4)
        axs[i].xaxis.set_minor_locator(MultipleLocator(1))
        axs[i].yaxis.set_minor_locator(MultipleLocator(0.05))
        axs[i].set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])

        # Imposta l'etichetta RMSE solo per il primo subplot di ogni riga
        if i % ncols == 0:
            axs[i].set_ylabel("Divergence", rotation='vertical')

        # Imposta l'etichetta "Missing Rate" solo per l'ultima riga
        if i >= (nrows - 1) * ncols:
            axs[i].set_xlabel('Missing Rate')

    # Gestire grafici vuoti se non ci sono abbastanza dataset
    for j in range(i + 1, nrows * ncols):
        axs[j].axis('off')  # Nascondere gli assi vuoti

    handles = [
        plt.Line2D([0], [0], color='#ff0000', linestyle='-', label='Discovery Pipeline', marker="o", markersize=6),
        plt.Line2D([0], [0], color='#00748f', linestyle='-', label='Baseline', marker="x", markersize=9)
    ]

    fig.legend(handles=handles, loc='upper center', ncol=4, bbox_to_anchor=(0.5, 1.06), shadow=True, fontsize=7)

    plt.savefig(f"{metrica}_results_{tipologia}_{thr}.pdf", bbox_inches='tight')
    plt.show()

# Esempio di utilizzo
metrica = "metric1"
thr = "0.25"
tipologia = "fd"
filepath = f'../All_Results_{metrica}_{tipologia}_{thr}.csv'  # Modifica con il percorso del tuo CSV
#selected_datasets = ["cars_MNAR","cars_MBUV","restaurant_MNAR","restaurant_MBUV","Boeing_898_MNAR","Boeing_898_MBUV","police_MNAR","police_MBUV"]
selected_datasets = ["cars_FD","restaurant_FD","Boeing_898_FD","police_FD"]


dataset_name_map = {
    'cars': 'Cars ($ID$ $1$)',
    'restaurant': 'Restaurant ($ID$ $2$)',
    'Boeing_898': 'Boeing ($ID$ $3$)',
    'Cats_1071': 'Cats ($ID$ $4$)',
    'police': 'Police ($ID$ $5$)',
    'IoT_Telemetry3000': 'IoT_Telemetry ($ID$ $6$)',
    'actorfilms_4000': 'Actors ($ID$ $7$)',
    'Med_Ch_2500': 'Medical Charges ($ID$ $8$)',
    'F1_REBUILT_5000': 'F1 ($ID$ $9$)',
    'MotoGP_REBUILT_3000': 'MotoGP ($ID$ $10$)',
    'US_Presidents_3754': 'US Presidents ($ID$ $11$)',
    'NBA_3200': 'NBA ($ID$ $12$)',
    'EV_Vehicles_4000': 'EV Vehicles ($ID$ $13$)',
    'superstore_4500': 'Superstore ($ID$ $14$)',
    'Air_9000': 'Air Quality ($ID$ $15$)',
    'cars_MNAR': 'Cars (MNAR)',
    'cars_MBUV': 'Cars (MBUV)',
    'restaurant_MNAR': 'Restaurant (MNAR)',
    'restaurant_MBUV': 'Restaurant (MBUV)',
    'Boeing_898_MNAR': 'Boeing (MNAR)',
    'Boeing_898_MBUV': 'Boeing (MBUV)',
    'police_MNAR': 'Police (MNAR)',
    'police_MBUV': 'Police (MBUV)',
    'cars_FD': 'Cars (FD)',
    'restaurant_FD' : 'Restaurant (FD)',
    'Boeing_898_FD': 'Boeing (FD)',
    'police_FD' : 'Police (FD)'
}


datasets = load_rmse_data(filepath, selected_datasets, dataset_name_map,metrica)  # Carica i dati RMSE
print(datasets)
plot_rmse_results(datasets,metrica,tipologia,ncols=4)  # Mostra i risultati, specificando il numero di colonne
