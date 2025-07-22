import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

def load_rmse_data(filepath, selected_datasets, dataset_name_map):
    """
    Carica i dati RMSE da un file CSV, applicando una mappatura ai nomi dei dataset.

    Parameters:
    - filepath: path al file CSV
    - selected_datasets: lista dei nomi 'test' dei dataset da includere
    - dataset_name_map: dizionario che mappa i nomi 'test' a quelli effettivi nel CSV

    Returns:
    - Dizionario annidato {nome_dataset_mappato: {algoritmo: [rmse_mean_per_mv]}}
    """
    import pandas as pd

    df = pd.read_csv(filepath, sep=';')

    print(df)

    # Applichiamo la mappatura dei nomi nel DataFrame
    df['dataset'] = df['dataset'].replace(dataset_name_map)

    datasets = {}

    for test_name in selected_datasets:
        mapped_name = dataset_name_map.get(test_name, test_name)  # Usa il nome mappato se esiste

        if mapped_name in df['dataset'].unique():
            df_dataset = df[df['dataset'] == mapped_name]
            rmse_results = {}
            algorithms = df_dataset['algoritmo'].unique()

            for algorithm in algorithms:
                df_algorithm = df_dataset[df_dataset['algoritmo'] == algorithm]
                rmse_means = []
                mv_percentages = sorted(df_algorithm['MV'].unique())

                for mv in mv_percentages:
                    rmse_mean = df_algorithm[df_algorithm['MV'] == mv]['rmse'].mean()
                    rmse_means.append(rmse_mean)

                rmse_results[algorithm] = rmse_means

            datasets[mapped_name] = rmse_results  # Usa il nome 'test' come chiave finale
        else:
            print(f"Warning: Il dataset '{test_name}' (mappato in '{mapped_name}') non è presente nel file CSV.")

    return datasets


def plot_rmse_results(datasets, ncols=2, output_file="output.pdf", x=15, y=7, anchor=1.0,  markers=[5,10,10,8], xticksize=8, yticksize=11, titlesize=10 , hspaces=0.20, wspaces=0.04, legendfont=10):
    num_datasets = len(datasets)
    r1 = np.arange(10)

    # Calcolo righe necessarie
    nrows = (num_datasets + ncols - 1) // ncols  # Formula per arrotondare verso l'alto

    fig, axs = plt.subplots(nrows, ncols, figsize=(x, y), sharey=True, sharex=True) #FIG 1

    # Modifica degli spazi orizzontali e verticali
    fig.subplots_adjust(hspace=hspaces, wspace=wspaces)  # Riduci hspace e wspace

    # Appiattimento gli assi se nrows > 1
    axs = axs.flatten() if nrows > 1 else axs

    for i, (dataset_name, results) in enumerate(datasets.items()):
        for algorithm, rmse_means in results.items():
            print(algorithm, rmse_means)
            if 'Pipeline_noRev' in algorithm:
                axs[i].plot(r1, rmse_means, marker="o", markersize=markers[0], color="#FFA600", zorder=2, label='PipelineNoRev')
            elif 'Baseline20' in algorithm:
                axs[i].plot(r1, rmse_means, marker="2", markersize=markers[1], color="#00748f", zorder=2, label='Baseline20')
            elif 'Hybrid' in algorithm:
                axs[i].plot(r1, rmse_means, marker="2", markersize=markers[2], color="#61a44f", zorder=3, linestyle='dashdot', label='Hybrid')
            elif 'Pipeline' in algorithm:  # Altri algoritmi, se ce ne sono
                axs[i].plot(r1, rmse_means, marker="x", markersize=markers[3], color="#ff0000", zorder=3, label='Pipeline')

        axs[i].set_xticks(r1)
        axs[i].set_xticklabels(["1", "2", "3", "4", "5", "10", "20", "30", "40", "50"])
        axs[i].set_title(f'{dataset_name}', fontsize=titlesize)
        axs[i].tick_params(axis='x', which='major', labelsize=xticksize)
        axs[i].tick_params(axis='y', which='major', labelsize=yticksize)
        axs[i].minorticks_on()
        axs[i].grid(which='major', linestyle='-', linewidth='0.5', color='gray', alpha=0.52)
        axs[i].grid(which='minor', linewidth='0.5', linestyle='dotted', color='gray', alpha=0.4)
        axs[i].xaxis.set_minor_locator(MultipleLocator(1))
        axs[i].yaxis.set_minor_locator(MultipleLocator(0.05))
        axs[i].set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])

        if i % ncols == 0:
            axs[i].set_ylabel('RMSE', rotation='vertical')

        if i >= (nrows - 1) * ncols:
            axs[i].set_xlabel('Missing Rate')

    # Gestione grafici vuoti se non ci sono abbastanza dataset
    for j in range(i + 1, nrows * ncols):
        axs[j].axis('off')  # Nascondere gli assi vuoti

    handles = [
        plt.Line2D([0], [0], color='#ff0000', linestyle='-', label='Pipeline', marker="x", markersize=10),
        plt.Line2D([0], [0], color='#FFA600', linestyle='-', label='PipelineNoRev', marker="o"),
        plt.Line2D([0], [0], color='#61a44f', linestyle='dashdot', label='Hybrid', marker="2", markersize=10),
        plt.Line2D([0], [0], color='#00748f', linestyle='-', label='Baseline20', marker="2", markersize=12)
    ]

    fig.legend(handles=handles, loc='upper center', ncol=4, bbox_to_anchor=(0.5, anchor), shadow=True, fontsize=legendfont)

    plt.savefig(output_file, bbox_inches='tight')
    plt.show()


filepath = '../ALL_Results_v3.csv'

selected_datasets = ['cars', 'restaurant', 'Boeing_898', 'Cats_1071', 'police', 'IoT_Telemetry3000', 'actorfilms_4000', "Med_Ch_2500",  "F1_REBUILT_5000", "MotoGP_REBUILT_3000", 'US_Presidents_3754', 'NBA_3200', 'EV_Vehicles_4000', "superstore_4500","Air_9000"] #FIG1
#selected_datasets = ['cars_FD', 'restaurant_FD', 'Boeing_898_FD', 'police_FD']

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

datasets = load_rmse_data(filepath, selected_datasets, dataset_name_map)
print("dataset",  datasets)
print(type(datasets))

plot_rmse_results(datasets, ncols=5, output_file="rmse_results.pdf", x=13, y=6, anchor=0.98, markers=[5,10,10,8],
                  xticksize=8, yticksize=11, titlesize=10, hspaces=0.20, wspaces=0.04, legendfont=10) #FIG1



selected_datasets = ['cars_MNAR', 'cars_MBUV', 'restaurant_MNAR', 'restaurant_MBUV', 'Boeing_898_MNAR', 'Boeing_898_MBUV', 'police_MNAR', 'police_MBUV']
datasets = load_rmse_data(filepath, selected_datasets, dataset_name_map)
plot_rmse_results(datasets, ncols=4, output_file="rmse_mnar_mbuv.pdf", x=7,y=3, anchor=1.06,  markers=[2.5,5,5,4],
                  xticksize=6, yticksize=8, titlesize=7, hspaces=0.25, wspaces=0.04, legendfont=7) #FIG2


selected_datasets = ['cars_FD', 'restaurant_FD', 'Boeing_898_FD', 'police_FD']
datasets = load_rmse_data(filepath, selected_datasets, dataset_name_map)
plot_rmse_results(datasets, ncols=4, output_file="rmse_fd.pdf", x=7,y=1.4, anchor=1.21,  markers=[2.5,5,5,4],
                  xticksize=6, yticksize=8, titlesize=7, hspaces=0.20, wspaces=0.04, legendfont=7) #FIG3