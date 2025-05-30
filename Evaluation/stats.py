import pandas as pd

def analizza_risultati(file_input, selected_datasets):
    # Legge il CSV
    df = pd.read_csv(file_input, sep=';')

    df = df[df['algoritmo'] != 'Baseline']

    # Filtra i dataset selezionati
    df = df[df['dataset'].isin(selected_datasets)]

    # Mappa i missing_rate all'interno di ogni dataset
    df['missing_rate'] = df.groupby('dataset')['MV'].transform(
        lambda x: x.map({mv: rate for mv, rate in zip(sorted(x.unique()), [1, 2, 3, 4, 5, 10, 20, 30, 40, 50])})
    )

    # Debug check
    print(df[['dataset', 'MV', 'missing_rate']].drop_duplicates().sort_values(['dataset', 'missing_rate']))

    # Calcola RMSE medio per ogni dataset e approccio
    dataset_rmse = df.groupby(['dataset', 'algoritmo'])['rmse'].mean().unstack()
    print("\nRMSE medio per dataset e approccio:")
    print(dataset_rmse)

    # Calcola RMSE medio per ogni approccio su tutti i test
    global_rmse = df.groupby('algoritmo')['rmse'].mean()
    print("\nRMSE medio per approccio:")
    print(global_rmse)

    # Calcola RMSE medio per ogni missing rate e approccio
    rate_rmse = df.groupby(['missing_rate', 'algoritmo'])['rmse'].mean().unstack()
    print("\nRMSE medio per missing rate e approccio:")
    print(rate_rmse)

    # Calcola il guadagno percentuale della Pipeline rispetto agli altri approcci
    def calcola_guadagno(rmse_pipeline, rmse_altro):
        return ((rmse_altro - rmse_pipeline) / rmse_altro) * 100

    guadagni_dataset = dataset_rmse.apply(
        lambda col: calcola_guadagno(dataset_rmse['Pipeline'], col) if col.name != 'Pipeline' else None)
    print("\nGuadagno percentuale della Pipeline per dataset:")
    print(guadagni_dataset)

    guadagni_globali = global_rmse.apply(
        lambda x: calcola_guadagno(global_rmse['Pipeline'], x) if x != global_rmse['Pipeline'] else None)
    print("\nGuadagno percentuale della Pipeline su tutti i test:")
    print(guadagni_globali)

    guadagni_missing_rate = rate_rmse.apply(
        lambda col: calcola_guadagno(rate_rmse['Pipeline'], col) if col.name != 'Pipeline' else None)
    print("\nGuadagno percentuale della Pipeline per ogni missing rate:")
    print(guadagni_missing_rate)

    # Salvataggio dei risultati per i plot
    dataset_rmse.to_csv('output/dataset_rmse.csv')
    global_rmse.to_csv('output/global_rmse.csv')
    rate_rmse.to_csv('output/rate_rmse.csv')
    guadagni_dataset.to_csv('output/guadagni_dataset.csv')
    guadagni_globali.to_csv('output/guadagni_globali.csv')
    guadagni_missing_rate.to_csv('output/guadagni_missing_rate.csv')



# Esempio di utilizzo
selected_datasets = ['cars', 'restaurant', 'Boeing_898', 'Cats_1071', 'police', 'IoT_Telemetry3000', 'actorfilms_4000', "Med_Ch_2500",  "F1_REBUILT_5000", "MotoGP_REBUILT_3000", 'US_Presidents_3754', 'NBA_3200', 'EV_Vehicles_4000', "superstore_4500","Air_9000", 'cars_MNAR', 'cars_MBUV', 'restaurant_MNAR', 'restaurant_MBUV', 'Boeing_898_MNAR', 'Boeing_898_MBUV', 'police_MNAR', 'police_MBUV', 'cars_FD', 'restaurant_FD', 'Boeing_898_FD', 'police_FD']

#selected_datasets = ['cars', 'restaurant', 'Boeing_898', 'Cats_1071', 'police', 'IoT_Telemetry3000', 'actorfilms_4000', "Med_Ch_2500",  "F1_REBUILT_5000", "MotoGP_REBUILT_3000", 'US_Presidents_3754', 'NBA_3200', 'EV_Vehicles_4000', "superstore_4500","Air_9000"] #FIG1
#selected_datasets = ['cars_MNAR', 'cars_MBUV', 'restaurant_MNAR', 'restaurant_MBUV', 'Boeing_898_MNAR', 'Boeing_898_MBUV', 'police_MNAR', 'police_MBUV']
#selected_datasets = ['cars_FD', 'restaurant_FD', 'Boeing_898_FD', 'police_FD']



analizza_risultati('ALL_Results_v3.csv', selected_datasets)
