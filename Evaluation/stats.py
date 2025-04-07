import pandas as pd


def analizza_risultati(file_input, selected_datasets):
    # Legge il CSV
    df = pd.read_csv(file_input, sep=';')

    # Filtra i dataset selezionati
    df = df[df['dataset'].isin(selected_datasets)]

    # Trova i valori unici di MV e assegna i missing rates
    mv_sorted = sorted(df['MV'].unique())
    missing_rates = {mv: rate for mv, rate in zip(mv_sorted, [1, 2, 3, 4, 5, 10, 20, 30, 40, 50])}
    df['missing_rate'] = df['MV'].map(missing_rates)

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

    # Calcola il guadagno percentuale della Pipeline per ogni missing rate
    guadagni_missing_rate = rate_rmse.apply(
        lambda col: calcola_guadagno(rate_rmse['Pipeline'], col) if col.name != 'Pipeline' else None)
    print("\nGuadagno percentuale della Pipeline per ogni missing rate:")
    print(guadagni_missing_rate)


# Esempio di utilizzo
selected_datasets = ['Boeing_898', 'actorfilms_4000', 'restaurant', 'NBA_3200', 'EV_Vehicles_4000',
                     'US_Presidents_3754', 'cars', "superstore_4500", "police", "IoT_Telemetry3000", "F1_REBUILT_5000",
                     "MotoGP_REBUILT_3000", "Med_Ch_2500", "restaurant_MNAR", "cars_MNAR",
                     "Boeing_898_MNAR"]
analizza_risultati('ALL_Results_v3.csv', selected_datasets)