import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator


#Plot per paper VLDB tesi. Confronto performance imputazioni tra baseline e STR1

df=pd.read_csv("DataV2.csv", sep=';')

#----------------------------------------------------------------------------------------

dftelemetry=df.loc[df['dataset'] == 'Telemetry' ]

dftelemetrySTR1=dftelemetry.loc[dftelemetry['algoritmo'] == 'STR1' ]
dftelemetryBaseline=dftelemetry.loc[dftelemetry['algoritmo'] == 'Baseline' ]

dftelemetrySTR1V1=dftelemetrySTR1.loc[dftelemetry['version'] == 1 ]
dftelemetrySTR1V2=dftelemetrySTR1.loc[dftelemetry['version'] == 2 ]
dftelemetrySTR1V3=dftelemetrySTR1.loc[dftelemetry['version'] == 3 ]
dftelemetrySTR1V4=dftelemetrySTR1.loc[dftelemetry['version'] == 4 ]
dftelemetrySTR1V5=dftelemetrySTR1.loc[dftelemetry['version'] == 5 ]
dftelemetryBaselineV1=dftelemetryBaseline.loc[dftelemetry['version'] == 1 ]
dftelemetryBaselineV2=dftelemetryBaseline.loc[dftelemetry['version'] == 2 ]
dftelemetryBaselineV3=dftelemetryBaseline.loc[dftelemetry['version'] == 3 ]
dftelemetryBaselineV4=dftelemetryBaseline.loc[dftelemetry['version'] == 4 ]
dftelemetryBaselineV5=dftelemetryBaseline.loc[dftelemetry['version'] == 5 ]


telemetryRecSTR1V1=dftelemetrySTR1V1['recall'].to_numpy().astype(float)/100
telemetryRecSTR1V2=dftelemetrySTR1V2['recall'].to_numpy().astype(float)/100
telemetryRecSTR1V3=dftelemetrySTR1V3['recall'].to_numpy().astype(float)/100
telemetryRecSTR1V4=dftelemetrySTR1V4['recall'].to_numpy().astype(float)/100
telemetryRecSTR1V5=dftelemetrySTR1V5['recall'].to_numpy().astype(float)/100
telemetryPreSTR1V1=dftelemetrySTR1V1['precision'].to_numpy().astype(float)/100
telemetryPreSTR1V2=dftelemetrySTR1V2['precision'].to_numpy().astype(float)/100
telemetryPreSTR1V3=dftelemetrySTR1V3['precision'].to_numpy().astype(float)/100
telemetryPreSTR1V4=dftelemetrySTR1V4['precision'].to_numpy().astype(float)/100
telemetryPreSTR1V5=dftelemetrySTR1V5['precision'].to_numpy().astype(float)/100

telemetryRecBaselineV1=dftelemetryBaselineV1['recall'].to_numpy().astype(float)/100
telemetryRecBaselineV2=dftelemetryBaselineV2['recall'].to_numpy().astype(float)/100
telemetryRecBaselineV3=dftelemetryBaselineV3['recall'].to_numpy().astype(float)/100
telemetryRecBaselineV4=dftelemetryBaselineV4['recall'].to_numpy().astype(float)/100
telemetryRecBaselineV5=dftelemetryBaselineV5['recall'].to_numpy().astype(float)/100
telemetryPreBaselineV1=dftelemetryBaselineV1['precision'].to_numpy().astype(float)/100
telemetryPreBaselineV2=dftelemetryBaselineV2['precision'].to_numpy().astype(float)/100
telemetryPreBaselineV3=dftelemetryBaselineV3['precision'].to_numpy().astype(float)/100
telemetryPreBaselineV4=dftelemetryBaselineV4['precision'].to_numpy().astype(float)/100
telemetryPreBaselineV5=dftelemetryBaselineV5['precision'].to_numpy().astype(float)/100

arrays = [telemetryRecSTR1V1, telemetryRecSTR1V2, telemetryRecSTR1V3, telemetryRecSTR1V4, telemetryRecSTR1V5]
telemetryRecSTR1 = np.mean(arrays, axis=0)
arrays = [telemetryPreSTR1V1, telemetryPreSTR1V2, telemetryPreSTR1V3, telemetryPreSTR1V4, telemetryPreSTR1V5]
telemetryPreSTR1 = np.mean(arrays, axis=0)
arrays = [telemetryRecBaselineV1, telemetryRecBaselineV2, telemetryRecBaselineV3, telemetryRecBaselineV4, telemetryRecBaselineV5]
telemetryRecBaseline = np.mean(arrays, axis=0)
arrays = [telemetryPreBaselineV1, telemetryPreBaselineV2, telemetryPreBaselineV3, telemetryPreBaselineV4, telemetryPreBaselineV5]
telemetryPreBaseline = np.mean(arrays, axis=0)

telemetryF1Baseline = 2 * (telemetryPreBaseline * telemetryRecBaseline) / (telemetryPreBaseline + telemetryRecBaseline)
telemetryF1STR1 = 2 * (telemetryPreSTR1 * telemetryRecSTR1) / (telemetryPreSTR1 + telemetryRecSTR1)

#----------------------------------------------------------------------------------------

dfcars=df.loc[df['dataset'] == 'Cars' ]

dfcarsSTR1=dfcars.loc[dfcars['algoritmo'] == 'STR1' ]
dfcarsBaseline=dfcars.loc[dfcars['algoritmo'] == 'Baseline' ]

dfcarsSTR1V1=dfcarsSTR1.loc[dfcars['version'] == 1 ]
dfcarsSTR1V2=dfcarsSTR1.loc[dfcars['version'] == 2 ]
dfcarsSTR1V3=dfcarsSTR1.loc[dfcars['version'] == 3 ]
dfcarsSTR1V4=dfcarsSTR1.loc[dfcars['version'] == 4 ]
dfcarsSTR1V5=dfcarsSTR1.loc[dfcars['version'] == 5 ]
dfcarsBaselineV1=dfcarsBaseline.loc[dfcars['version'] == 1 ]
dfcarsBaselineV2=dfcarsBaseline.loc[dfcars['version'] == 2 ]
dfcarsBaselineV3=dfcarsBaseline.loc[dfcars['version'] == 3 ]
dfcarsBaselineV4=dfcarsBaseline.loc[dfcars['version'] == 4 ]
dfcarsBaselineV5=dfcarsBaseline.loc[dfcars['version'] == 5 ]



carsRecSTR1V1=dfcarsSTR1V1['recall'].to_numpy().astype(float)/100
carsRecSTR1V2=dfcarsSTR1V2['recall'].to_numpy().astype(float)/100
carsRecSTR1V3=dfcarsSTR1V3['recall'].to_numpy().astype(float)/100
carsRecSTR1V4=dfcarsSTR1V4['recall'].to_numpy().astype(float)/100
carsRecSTR1V5=dfcarsSTR1V5['recall'].to_numpy().astype(float)/100
carsPreSTR1V1=dfcarsSTR1V1['precision'].to_numpy().astype(float)/100
carsPreSTR1V2=dfcarsSTR1V2['precision'].to_numpy().astype(float)/100
carsPreSTR1V3=dfcarsSTR1V3['precision'].to_numpy().astype(float)/100
carsPreSTR1V4=dfcarsSTR1V4['precision'].to_numpy().astype(float)/100
carsPreSTR1V5=dfcarsSTR1V5['precision'].to_numpy().astype(float)/100

carsRecBaselineV1=dfcarsBaselineV1['recall'].to_numpy().astype(float)/100
carsRecBaselineV2=dfcarsBaselineV2['recall'].to_numpy().astype(float)/100
carsRecBaselineV3=dfcarsBaselineV3['recall'].to_numpy().astype(float)/100
carsRecBaselineV4=dfcarsBaselineV4['recall'].to_numpy().astype(float)/100
carsRecBaselineV5=dfcarsBaselineV5['recall'].to_numpy().astype(float)/100
carsPreBaselineV1=dfcarsBaselineV1['precision'].to_numpy().astype(float)/100
carsPreBaselineV2=dfcarsBaselineV2['precision'].to_numpy().astype(float)/100
carsPreBaselineV3=dfcarsBaselineV3['precision'].to_numpy().astype(float)/100
carsPreBaselineV4=dfcarsBaselineV4['precision'].to_numpy().astype(float)/100
carsPreBaselineV5=dfcarsBaselineV5['precision'].to_numpy().astype(float)/100

arrays = [carsRecSTR1V1, carsRecSTR1V2, carsRecSTR1V3, carsRecSTR1V4, carsRecSTR1V5]
carsRecSTR1 = np.mean(arrays, axis=0)
arrays = [carsPreSTR1V1, carsPreSTR1V2, carsPreSTR1V3, carsPreSTR1V4, carsPreSTR1V5]
carsPreSTR1 = np.mean(arrays, axis=0)
arrays = [carsRecBaselineV1, carsRecBaselineV2, carsRecBaselineV3, carsRecBaselineV4, carsRecBaselineV5]
carsRecBaseline = np.mean(arrays, axis=0)
arrays = [carsPreBaselineV1, carsPreBaselineV2, carsPreBaselineV3, carsPreBaselineV4, carsPreBaselineV5]
carsPreBaseline = np.mean(arrays, axis=0)

carsF1Baseline = 2 * (carsPreBaseline * carsRecBaseline) / (carsPreBaseline + carsRecBaseline)
carsF1STR1 = 2 * (carsPreSTR1 * carsRecSTR1) / (carsPreSTR1 + carsRecSTR1)


print(carsPreSTR1)
print(carsRecSTR1)
print(carsF1STR1)
print("---------")
print(carsPreBaseline)
print(carsRecBaseline)
print(carsF1Baseline)


#----------------------------------------------------------------------------------------

dfRestaurant=df.loc[df['dataset'] == 'Restaurant' ]

dfRestaurantSTR1=dfRestaurant.loc[dfRestaurant['algoritmo'] == 'STR1' ]
dfRestaurantBaseline=dfRestaurant.loc[dfRestaurant['algoritmo'] == 'Baseline' ]

dfRestaurantSTR1V1=dfRestaurantSTR1.loc[dfRestaurant['version'] == 1 ]
dfRestaurantSTR1V2=dfRestaurantSTR1.loc[dfRestaurant['version'] == 2 ]
dfRestaurantSTR1V3=dfRestaurantSTR1.loc[dfRestaurant['version'] == 3 ]
dfRestaurantSTR1V4=dfRestaurantSTR1.loc[dfRestaurant['version'] == 4 ]
dfRestaurantSTR1V5=dfRestaurantSTR1.loc[dfRestaurant['version'] == 5 ]
dfRestaurantBaselineV1=dfRestaurantBaseline.loc[dfRestaurant['version'] == 1 ]
dfRestaurantBaselineV2=dfRestaurantBaseline.loc[dfRestaurant['version'] == 2 ]
dfRestaurantBaselineV3=dfRestaurantBaseline.loc[dfRestaurant['version'] == 3 ]
dfRestaurantBaselineV4=dfRestaurantBaseline.loc[dfRestaurant['version'] == 4 ]
dfRestaurantBaselineV5=dfRestaurantBaseline.loc[dfRestaurant['version'] == 5 ]



RestaurantRecSTR1V1=dfRestaurantSTR1V1['recall'].to_numpy().astype(float)/100
RestaurantRecSTR1V2=dfRestaurantSTR1V2['recall'].to_numpy().astype(float)/100
RestaurantRecSTR1V3=dfRestaurantSTR1V3['recall'].to_numpy().astype(float)/100
RestaurantRecSTR1V4=dfRestaurantSTR1V4['recall'].to_numpy().astype(float)/100
RestaurantRecSTR1V5=dfRestaurantSTR1V5['recall'].to_numpy().astype(float)/100
RestaurantPreSTR1V1=dfRestaurantSTR1V1['precision'].to_numpy().astype(float)/100
RestaurantPreSTR1V2=dfRestaurantSTR1V2['precision'].to_numpy().astype(float)/100
RestaurantPreSTR1V3=dfRestaurantSTR1V3['precision'].to_numpy().astype(float)/100
RestaurantPreSTR1V4=dfRestaurantSTR1V4['precision'].to_numpy().astype(float)/100
RestaurantPreSTR1V5=dfRestaurantSTR1V5['precision'].to_numpy().astype(float)/100

RestaurantRecBaselineV1=dfRestaurantBaselineV1['recall'].to_numpy().astype(float)/100
RestaurantRecBaselineV2=dfRestaurantBaselineV2['recall'].to_numpy().astype(float)/100
RestaurantRecBaselineV3=dfRestaurantBaselineV3['recall'].to_numpy().astype(float)/100
RestaurantRecBaselineV4=dfRestaurantBaselineV4['recall'].to_numpy().astype(float)/100
RestaurantRecBaselineV5=dfRestaurantBaselineV5['recall'].to_numpy().astype(float)/100
RestaurantPreBaselineV1=dfRestaurantBaselineV1['precision'].to_numpy().astype(float)/100
RestaurantPreBaselineV2=dfRestaurantBaselineV2['precision'].to_numpy().astype(float)/100
RestaurantPreBaselineV3=dfRestaurantBaselineV3['precision'].to_numpy().astype(float)/100
RestaurantPreBaselineV4=dfRestaurantBaselineV4['precision'].to_numpy().astype(float)/100
RestaurantPreBaselineV5=dfRestaurantBaselineV5['precision'].to_numpy().astype(float)/100

arrays = [RestaurantRecSTR1V1, RestaurantRecSTR1V2, RestaurantRecSTR1V3, RestaurantRecSTR1V4, RestaurantRecSTR1V5]
RestaurantRecSTR1 = np.mean(arrays, axis=0)
arrays = [RestaurantPreSTR1V1, RestaurantPreSTR1V2, RestaurantPreSTR1V3, RestaurantPreSTR1V4, RestaurantPreSTR1V5]
RestaurantPreSTR1 = np.mean(arrays, axis=0)
arrays = [RestaurantRecBaselineV1, RestaurantRecBaselineV2, RestaurantRecBaselineV3, RestaurantRecBaselineV4, RestaurantRecBaselineV5]
RestaurantRecBaseline = np.mean(arrays, axis=0)
arrays = [RestaurantPreBaselineV1, RestaurantPreBaselineV2, RestaurantPreBaselineV3, RestaurantPreBaselineV4, RestaurantPreBaselineV5]
RestaurantPreBaseline = np.mean(arrays, axis=0)

RestaurantF1Baseline = 2 * (RestaurantPreBaseline * RestaurantRecBaseline) / (RestaurantPreBaseline + RestaurantRecBaseline)
RestaurantF1STR1 = 2 * (RestaurantPreSTR1 * RestaurantRecSTR1) / (RestaurantPreSTR1 + RestaurantRecSTR1)

#----------------------------------------------------------------------------------------

dfpolice=df.loc[df['dataset'] == 'Police' ]

dfpoliceSTR1=dfpolice.loc[dfpolice['algoritmo'] == 'STR1' ]
dfpoliceBaseline=dfpolice.loc[dfpolice['algoritmo'] == 'Baseline' ]

dfpoliceSTR1V1=dfpoliceSTR1.loc[dfpolice['version'] == 1 ]
dfpoliceSTR1V2=dfpoliceSTR1.loc[dfpolice['version'] == 2 ]
dfpoliceSTR1V3=dfpoliceSTR1.loc[dfpolice['version'] == 3 ]
dfpoliceSTR1V4=dfpoliceSTR1.loc[dfpolice['version'] == 4 ]
dfpoliceSTR1V5=dfpoliceSTR1.loc[dfpolice['version'] == 5 ]
dfpoliceBaselineV1=dfpoliceBaseline.loc[dfpolice['version'] == 1 ]
dfpoliceBaselineV2=dfpoliceBaseline.loc[dfpolice['version'] == 2 ]
dfpoliceBaselineV3=dfpoliceBaseline.loc[dfpolice['version'] == 3 ]
dfpoliceBaselineV4=dfpoliceBaseline.loc[dfpolice['version'] == 4 ]
dfpoliceBaselineV5=dfpoliceBaseline.loc[dfpolice['version'] == 5 ]



policeRecSTR1V1=dfpoliceSTR1V1['recall'].to_numpy().astype(float)/100
policeRecSTR1V2=dfpoliceSTR1V2['recall'].to_numpy().astype(float)/100
policeRecSTR1V3=dfpoliceSTR1V3['recall'].to_numpy().astype(float)/100
policeRecSTR1V4=dfpoliceSTR1V4['recall'].to_numpy().astype(float)/100
policeRecSTR1V5=dfpoliceSTR1V5['recall'].to_numpy().astype(float)/100
policePreSTR1V1=dfpoliceSTR1V1['precision'].to_numpy().astype(float)/100
policePreSTR1V2=dfpoliceSTR1V2['precision'].to_numpy().astype(float)/100
policePreSTR1V3=dfpoliceSTR1V3['precision'].to_numpy().astype(float)/100
policePreSTR1V4=dfpoliceSTR1V4['precision'].to_numpy().astype(float)/100
policePreSTR1V5=dfpoliceSTR1V5['precision'].to_numpy().astype(float)/100

policeRecBaselineV1=dfpoliceBaselineV1['recall'].to_numpy().astype(float)/100
policeRecBaselineV2=dfpoliceBaselineV2['recall'].to_numpy().astype(float)/100
policeRecBaselineV3=dfpoliceBaselineV3['recall'].to_numpy().astype(float)/100
policeRecBaselineV4=dfpoliceBaselineV4['recall'].to_numpy().astype(float)/100
policeRecBaselineV5=dfpoliceBaselineV5['recall'].to_numpy().astype(float)/100
policePreBaselineV1=dfpoliceBaselineV1['precision'].to_numpy().astype(float)/100
policePreBaselineV2=dfpoliceBaselineV2['precision'].to_numpy().astype(float)/100
policePreBaselineV3=dfpoliceBaselineV3['precision'].to_numpy().astype(float)/100
policePreBaselineV4=dfpoliceBaselineV4['precision'].to_numpy().astype(float)/100
policePreBaselineV5=dfpoliceBaselineV5['precision'].to_numpy().astype(float)/100

arrays = [policeRecSTR1V1, policeRecSTR1V2, policeRecSTR1V3, policeRecSTR1V4, policeRecSTR1V5]
policeRecSTR1 = np.mean(arrays, axis=0)
arrays = [policePreSTR1V1, policePreSTR1V2, policePreSTR1V3, policePreSTR1V4, policePreSTR1V5]
policePreSTR1 = np.mean(arrays, axis=0)
arrays = [policeRecBaselineV1, policeRecBaselineV2, policeRecBaselineV3, policeRecBaselineV4, policeRecBaselineV5]
policeRecBaseline = np.mean(arrays, axis=0)
arrays = [policePreBaselineV1, policePreBaselineV2, policePreBaselineV3, policePreBaselineV4, policePreBaselineV5]
policePreBaseline = np.mean(arrays, axis=0)

policeF1Baseline = 2 * (policePreBaseline * policeRecBaseline) / (policePreBaseline + policeRecBaseline)
policeF1STR1 = 2 * (policePreSTR1 * policeRecSTR1) / (policePreSTR1 + policeRecSTR1)

#----------------------------------------------------------------------------------------

dfcallout=df.loc[df['dataset'] == 'Callout' ]

dfcalloutSTR1=dfcallout.loc[dfcallout['algoritmo'] == 'STR1' ]
dfcalloutBaseline=dfcallout.loc[dfcallout['algoritmo'] == 'Baseline' ]

dfcalloutSTR1V1=dfcalloutSTR1.loc[dfcallout['version'] == 1 ]
dfcalloutSTR1V2=dfcalloutSTR1.loc[dfcallout['version'] == 2 ]
dfcalloutSTR1V3=dfcalloutSTR1.loc[dfcallout['version'] == 3 ]
dfcalloutSTR1V4=dfcalloutSTR1.loc[dfcallout['version'] == 4 ]
dfcalloutSTR1V5=dfcalloutSTR1.loc[dfcallout['version'] == 5 ]
dfcalloutBaselineV1=dfcalloutBaseline.loc[dfcallout['version'] == 1 ]
dfcalloutBaselineV2=dfcalloutBaseline.loc[dfcallout['version'] == 2 ]
dfcalloutBaselineV3=dfcalloutBaseline.loc[dfcallout['version'] == 3 ]
dfcalloutBaselineV4=dfcalloutBaseline.loc[dfcallout['version'] == 4 ]
dfcalloutBaselineV5=dfcalloutBaseline.loc[dfcallout['version'] == 5 ]



calloutRecSTR1V1=dfcalloutSTR1V1['recall'].to_numpy().astype(float)/100
calloutRecSTR1V2=dfcalloutSTR1V2['recall'].to_numpy().astype(float)/100
calloutRecSTR1V3=dfcalloutSTR1V3['recall'].to_numpy().astype(float)/100
calloutRecSTR1V4=dfcalloutSTR1V4['recall'].to_numpy().astype(float)/100
calloutRecSTR1V5=dfcalloutSTR1V5['recall'].to_numpy().astype(float)/100
calloutPreSTR1V1=dfcalloutSTR1V1['precision'].to_numpy().astype(float)/100
calloutPreSTR1V2=dfcalloutSTR1V2['precision'].to_numpy().astype(float)/100
calloutPreSTR1V3=dfcalloutSTR1V3['precision'].to_numpy().astype(float)/100
calloutPreSTR1V4=dfcalloutSTR1V4['precision'].to_numpy().astype(float)/100
calloutPreSTR1V5=dfcalloutSTR1V5['precision'].to_numpy().astype(float)/100

calloutRecBaselineV1=dfcalloutBaselineV1['recall'].to_numpy().astype(float)/100
calloutRecBaselineV2=dfcalloutBaselineV2['recall'].to_numpy().astype(float)/100
calloutRecBaselineV3=dfcalloutBaselineV3['recall'].to_numpy().astype(float)/100
calloutRecBaselineV4=dfcalloutBaselineV4['recall'].to_numpy().astype(float)/100
calloutRecBaselineV5=dfcalloutBaselineV5['recall'].to_numpy().astype(float)/100
calloutPreBaselineV1=dfcalloutBaselineV1['precision'].to_numpy().astype(float)/100
calloutPreBaselineV2=dfcalloutBaselineV2['precision'].to_numpy().astype(float)/100
calloutPreBaselineV3=dfcalloutBaselineV3['precision'].to_numpy().astype(float)/100
calloutPreBaselineV4=dfcalloutBaselineV4['precision'].to_numpy().astype(float)/100
calloutPreBaselineV5=dfcalloutBaselineV5['precision'].to_numpy().astype(float)/100

arrays = [calloutRecSTR1V1, calloutRecSTR1V2, calloutRecSTR1V3, calloutRecSTR1V4, calloutRecSTR1V5]
calloutRecSTR1 = np.mean(arrays, axis=0)
arrays = [calloutPreSTR1V1, calloutPreSTR1V2, calloutPreSTR1V3, calloutPreSTR1V4, calloutPreSTR1V5]
calloutPreSTR1 = np.mean(arrays, axis=0)
arrays = [calloutRecBaselineV1, calloutRecBaselineV2, calloutRecBaselineV3, calloutRecBaselineV4, calloutRecBaselineV5]
calloutRecBaseline = np.mean(arrays, axis=0)
arrays = [calloutPreBaselineV1, calloutPreBaselineV2, calloutPreBaselineV3, calloutPreBaselineV4, calloutPreBaselineV5]
calloutPreBaseline = np.mean(arrays, axis=0)

calloutF1Baseline = 2 * (calloutPreBaseline * calloutRecBaseline) / (calloutPreBaseline + calloutRecBaseline)
calloutF1STR1 = 2 * (calloutPreSTR1 * calloutRecSTR1) / (calloutPreSTR1 + calloutRecSTR1)




r1 = np.arange(10)

fig, axs = plt.subplots(3, 5, figsize=(14,5), sharey=True)
fig.subplots_adjust(hspace=0.1, wspace=0.05)

axs[0, 0].plot(r1, RestaurantRecSTR1, marker="v", markersize=5, color="#F0002B", zorder=3)
axs[0, 0].plot(r1, RestaurantRecBaseline, marker="v", markersize=5, color="#0072B2", zorder=2)   #0072b2

axs[1, 0].plot(r1, RestaurantPreSTR1, marker="v", markersize=5, color="#F0002B",zorder=3)
axs[1, 0].plot(r1, RestaurantPreBaseline, marker="v", markersize=5, color="#0072B2", zorder=2)

axs[2, 0].plot(r1, RestaurantF1STR1, marker="v", markersize=5, color='#F0002B', zorder=3)
axs[2, 0].plot(r1, RestaurantF1Baseline, marker="v", markersize=5, color="#0072B2", zorder=2)



axs[0, 1].plot(r1, telemetryRecSTR1, marker="v", markersize=5, color="#F0002B", zorder=3)
axs[0, 1].plot(r1, telemetryRecBaseline, marker="v", markersize=5, color="#0072B2", zorder=2)

axs[1, 1].plot(r1, telemetryPreSTR1, marker="v", markersize=5, color="#F0002B", zorder=3)
axs[1, 1].plot(r1, telemetryPreBaseline, marker="v", markersize=5, color="#0072B2", zorder=2)

axs[2, 1].plot(r1, telemetryF1STR1, marker="v", markersize=5, color="#F0002B", zorder=3)
axs[2, 1].plot(r1, telemetryF1Baseline, marker="v", markersize=5, color="#0072B2", zorder=2)



axs[0, 2].plot(r1, carsRecSTR1, marker="v", markersize=5, color="#F0002B", zorder=3)
axs[0, 2].plot(r1, carsRecBaseline, marker="v", markersize=5, color="#0072B2", zorder=2)
axs[0, 2].set_yticks([0,0.25,0.5,0.75,1], labels=["0", "0.25", "0.50", "0.75", "1"])

axs[1, 2].plot(r1, carsPreSTR1, marker="v", markersize=5, color="#F0002B", zorder=3)
axs[1, 2].plot(r1, carsPreBaseline, marker="v", markersize=5, color="#0072B2", zorder=2)

axs[2, 2].plot(r1, carsF1STR1, marker="v", markersize=5, color="#F0002B", zorder=3)
axs[2, 2].plot(r1, carsF1Baseline, marker="v", markersize=5, color="#0072B2", zorder=2)



axs[0, 3].plot(r1, policeRecSTR1, marker="v", markersize=5, color="#F0002B", zorder=3)
axs[0, 3].plot(r1, policeRecBaseline, marker="v", markersize=5, color="#0072B2", zorder=2)

axs[1, 3].plot(r1, policePreSTR1, marker="v", markersize=5, color="#F0002B", zorder=3)
axs[1, 3].plot(r1, policePreBaseline, marker="v", markersize=5, color="#0072B2", zorder=2)

axs[2, 3].plot(r1, policeF1STR1, marker="v", markersize=5, color="#F0002B", zorder=3)
axs[2, 3].plot(r1, policeF1Baseline, marker="v", markersize=5, color="#0072B2", zorder=2)


axs[0, 4].plot(r1, calloutRecSTR1, marker="v", markersize=5, color="#F0002B", zorder=3)
axs[0, 4].plot(r1, calloutRecBaseline, marker="v", markersize=5, color="#0072B2", zorder=2)

axs[1, 4].plot(r1, calloutPreSTR1, marker="v", markersize=5, color="#F0002B", zorder=3)
axs[1, 4].plot(r1, calloutPreBaseline, marker="v", markersize=5, color="#0072B2", zorder=2)

axs[2, 4].plot(r1, calloutF1STR1, marker="v", markersize=5, color="#F0002B", zorder=3)
axs[2, 4].plot(r1, calloutF1Baseline, marker="v", markersize=5, color="#0072B2", zorder=2)



axs[0,0].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[0,0].set_ylabel('Recall', rotation='vertical')
axs[0,0].set_title('Restaurant', fontsize=12)

axs[1,0].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[1,0].set_ylabel('Precision', rotation='vertical')

axs[2,0].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[2,0].set_ylabel('F1-Measure', rotation='vertical')
#axs[2,0].set_title('Missing rate', fontsize=10, y=-0.59)
axs[2,0].set_xlabel('Missing rate')



axs[0,1].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[0,1].set_title('Telemetry', fontsize=12)
axs[1,1].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[2,1].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
#axs[2,1].set_title('Missing rate', fontsize=10, y=-0.29)
axs[2,1].set_xlabel('Missing rate')


axs[0,2].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[0,2].set_title('Cars', fontsize=12)
axs[1,2].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[2,2].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
#axs[2,2].set_title('Missing rate', fontsize=10, y=-0.29)
axs[2,2].set_xlabel('Missing rate')


axs[0,3].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[0,3].set_title('Police', fontsize=12)
axs[1,3].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[2,3].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
#axs[2,3].set_title('Missing rate', fontsize=10, y=-0.29)
axs[2,3].set_xlabel('Missing rate')


axs[0,4].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[0,4].set_title('Callout', fontsize=12)
axs[1,4].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[2,4].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
#axs[2,4].set_title('Missing rate', fontsize=10, y=-0.29)
axs[2,4].set_xlabel('Missing rate')



axs[0,0].tick_params(axis='x', which='major', labelsize=10)
axs[1,0].tick_params(axis='x', which='major', labelsize=10)
axs[2,0].tick_params(axis='x', which='major', labelsize=10)
axs[0,1].tick_params(axis='x', which='major', labelsize=10)
axs[1,1].tick_params(axis='x', which='major', labelsize=10)
axs[2,1].tick_params(axis='x', which='major', labelsize=10)
axs[0,2].tick_params(axis='x', which='major', labelsize=10)
axs[1,2].tick_params(axis='x', which='major', labelsize=10)
axs[2,2].tick_params(axis='x', which='major', labelsize=10)
axs[0,3].tick_params(axis='x', which='major', labelsize=10)
axs[1,3].tick_params(axis='x', which='major', labelsize=10)
axs[2,3].tick_params(axis='x', which='major', labelsize=10)
axs[0,4].tick_params(axis='x', which='major', labelsize=10)
axs[1,4].tick_params(axis='x', which='major', labelsize=10)
axs[2,4].tick_params(axis='x', which='major', labelsize=10)


axs[0,0].tick_params(axis='y', which='major', labelsize=11)
axs[1,0].tick_params(axis='y', which='major', labelsize=11)
axs[2,0].tick_params(axis='y', which='major', labelsize=11)
axs[0,1].tick_params(axis='y', which='major', labelsize=11)
axs[1,1].tick_params(axis='y', which='major', labelsize=11)
axs[2,1].tick_params(axis='y', which='major', labelsize=11)
axs[0,2].tick_params(axis='y', which='major', labelsize=11)
axs[1,2].tick_params(axis='y', which='major', labelsize=11)
axs[2,2].tick_params(axis='y', which='major', labelsize=11)
axs[0,3].tick_params(axis='y', which='major', labelsize=11)
axs[1,3].tick_params(axis='y', which='major', labelsize=11)
axs[2,3].tick_params(axis='y', which='major', labelsize=11)
axs[0,4].tick_params(axis='y', which='major', labelsize=11)
axs[1,4].tick_params(axis='y', which='major', labelsize=11)
axs[2,4].tick_params(axis='y', which='major', labelsize=11)

for ax in axs.flat:
    ax.label_outer()
    #ax.grid(True, color='#CFCFCF', zorder=1)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='gray', alpha=0.52)
    ax.grid(which='minor', linewidth='0.5',linestyle='dotted', ms=2, color='gray', alpha=0.4)
    ax.xaxis.set_minor_locator(MultipleLocator(1))  # Customize the spacing between minor gridlines on the x-axis
    ax.yaxis.set_minor_locator(MultipleLocator(0.05))  # Customize the spacing between minor gridlines on the y-axis


# Create legend artists for each line
legend_artist1 = plt.Line2D([0], [0], color='#F0002B', linestyle='-', label='Imputation Pipeline')
legend_artist2 = plt.Line2D([0], [0], color='#0072B2', linestyle='-', label='Baseline')

# Add the legend artists to the figure
legend = fig.legend(handles=[legend_artist1, legend_artist2], loc='upper center', ncol=2, bbox_to_anchor=(0.5, 1.015), shadow=True)




plt.savefig("ResultsSTR1Aggregated.pdf", bbox_inches='tight')
plt.show()


