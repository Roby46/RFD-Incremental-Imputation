import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

df=pd.read_csv("../ALL_Results_v2.csv", sep=';')

df_restaurant_=df.loc[df['dataset'] == 'restaurant' ]


df_restaurant_Pipeline=df_restaurant_.loc[df_restaurant_['algoritmo'] == 'Pipeline' ]
#df_restaurant_Baseline=df_restaurant_.loc[df_restaurant_['algoritmo'] == 'Baseline' ]
df_restaurant_Baseline20=df_restaurant_.loc[df_restaurant_['algoritmo'] == 'Baseline20' ]
df_restaurant_PipelineNoRev=df_restaurant_.loc[df_restaurant_['algoritmo'] == 'Pipeline_noRev' ]
df_restaurant_Hybrid=df_restaurant_.loc[df_restaurant_['algoritmo'] == 'Hybrid' ]


df_restaurant_PipelineV1=df_restaurant_Pipeline.loc[df_restaurant_Pipeline['version'] == 1 ]
df_restaurant_PipelineV2=df_restaurant_Pipeline.loc[df_restaurant_Pipeline['version'] == 2 ]
df_restaurant_PipelineV3=df_restaurant_Pipeline.loc[df_restaurant_Pipeline['version'] == 3 ]
df_restaurant_PipelineV4=df_restaurant_Pipeline.loc[df_restaurant_Pipeline['version'] == 4 ]
df_restaurant_PipelineV5=df_restaurant_Pipeline.loc[df_restaurant_Pipeline['version'] == 5 ]

# df_restaurant_BaselineV1=df_restaurant_Baseline.loc[df_restaurant_Baseline['version'] == 1 ]
# df_restaurant_BaselineV2=df_restaurant_Baseline.loc[df_restaurant_Baseline['version'] == 2 ]
# df_restaurant_BaselineV3=df_restaurant_Baseline.loc[df_restaurant_Baseline['version'] == 3 ]
# df_restaurant_BaselineV4=df_restaurant_Baseline.loc[df_restaurant_Baseline['version'] == 4 ]
# df_restaurant_BaselineV5=df_restaurant_Baseline.loc[df_restaurant_Baseline['version'] == 5 ]

df_restaurant_Baseline20V1=df_restaurant_Baseline20.loc[df_restaurant_Baseline20['version'] == 1 ]
df_restaurant_Baseline20V2=df_restaurant_Baseline20.loc[df_restaurant_Baseline20['version'] == 2 ]
df_restaurant_Baseline20V3=df_restaurant_Baseline20.loc[df_restaurant_Baseline20['version'] == 3 ]
df_restaurant_Baseline20V4=df_restaurant_Baseline20.loc[df_restaurant_Baseline20['version'] == 4 ]
df_restaurant_Baseline20V5=df_restaurant_Baseline20.loc[df_restaurant_Baseline20['version'] == 5 ]

df_restaurant_PipelineNoRevV1=df_restaurant_PipelineNoRev.loc[df_restaurant_PipelineNoRev['version'] == 1 ]
df_restaurant_PipelineNoRevV2=df_restaurant_PipelineNoRev.loc[df_restaurant_PipelineNoRev['version'] == 2 ]
df_restaurant_PipelineNoRevV3=df_restaurant_PipelineNoRev.loc[df_restaurant_PipelineNoRev['version'] == 3 ]
df_restaurant_PipelineNoRevV4=df_restaurant_PipelineNoRev.loc[df_restaurant_PipelineNoRev['version'] == 4 ]
df_restaurant_PipelineNoRevV5=df_restaurant_PipelineNoRev.loc[df_restaurant_PipelineNoRev['version'] == 5 ]

df_restaurant_HybridV1=df_restaurant_Hybrid.loc[df_restaurant_Hybrid['version'] == 1 ]
df_restaurant_HybridV2=df_restaurant_Hybrid.loc[df_restaurant_Hybrid['version'] == 2 ]
df_restaurant_HybridV3=df_restaurant_Hybrid.loc[df_restaurant_Hybrid['version'] == 3 ]
df_restaurant_HybridV4=df_restaurant_Hybrid.loc[df_restaurant_Hybrid['version'] == 4 ]
df_restaurant_HybridV5=df_restaurant_Hybrid.loc[df_restaurant_Hybrid['version'] == 5 ]

restaurantRecPipelineNoRevV1=df_restaurant_PipelineNoRevV1['recall'].to_numpy().astype(float)
restaurantRecPipelineNoRevV2=df_restaurant_PipelineNoRevV2['recall'].to_numpy().astype(float)
restaurantRecPipelineNoRevV3=df_restaurant_PipelineNoRevV3['recall'].to_numpy().astype(float)
restaurantRecPipelineNoRevV4=df_restaurant_PipelineNoRevV4['recall'].to_numpy().astype(float)
restaurantRecPipelineNoRevV5=df_restaurant_PipelineNoRevV5['recall'].to_numpy().astype(float)
restaurantPrePipelineNoRevV1=df_restaurant_PipelineNoRevV1['precision'].to_numpy().astype(float)
restaurantPrePipelineNoRevV2=df_restaurant_PipelineNoRevV2['precision'].to_numpy().astype(float)
restaurantPrePipelineNoRevV3=df_restaurant_PipelineNoRevV3['precision'].to_numpy().astype(float)
restaurantPrePipelineNoRevV4=df_restaurant_PipelineNoRevV4['precision'].to_numpy().astype(float)
restaurantPrePipelineNoRevV5=df_restaurant_PipelineNoRevV5['precision'].to_numpy().astype(float)
restaurantRMSEPipelineNoRevV1=df_restaurant_PipelineNoRevV1['rmse'].to_numpy().astype(float)
restaurantRMSEPipelineNoRevV2=df_restaurant_PipelineNoRevV2['rmse'].to_numpy().astype(float)
restaurantRMSEPipelineNoRevV3=df_restaurant_PipelineNoRevV3['rmse'].to_numpy().astype(float)
restaurantRMSEPipelineNoRevV4=df_restaurant_PipelineNoRevV4['rmse'].to_numpy().astype(float)
restaurantRMSEPipelineNoRevV5=df_restaurant_PipelineNoRevV5['rmse'].to_numpy().astype(float)



restaurantRecPipelineV1=df_restaurant_PipelineV1['recall'].to_numpy().astype(float)
restaurantRecPipelineV2=df_restaurant_PipelineV2['recall'].to_numpy().astype(float)
restaurantRecPipelineV3=df_restaurant_PipelineV3['recall'].to_numpy().astype(float)
restaurantRecPipelineV4=df_restaurant_PipelineV4['recall'].to_numpy().astype(float)
restaurantRecPipelineV5=df_restaurant_PipelineV5['recall'].to_numpy().astype(float)
restaurantPrePipelineV1=df_restaurant_PipelineV1['precision'].to_numpy().astype(float)
restaurantPrePipelineV2=df_restaurant_PipelineV2['precision'].to_numpy().astype(float)
restaurantPrePipelineV3=df_restaurant_PipelineV3['precision'].to_numpy().astype(float)
restaurantPrePipelineV4=df_restaurant_PipelineV4['precision'].to_numpy().astype(float)
restaurantPrePipelineV5=df_restaurant_PipelineV5['precision'].to_numpy().astype(float)
restaurantRMSEPipelineV1=df_restaurant_PipelineV1['rmse'].to_numpy().astype(float)
restaurantRMSEPipelineV2=df_restaurant_PipelineV2['rmse'].to_numpy().astype(float)
restaurantRMSEPipelineV3=df_restaurant_PipelineV3['rmse'].to_numpy().astype(float)
restaurantRMSEPipelineV4=df_restaurant_PipelineV4['rmse'].to_numpy().astype(float)
restaurantRMSEPipelineV5=df_restaurant_PipelineV5['rmse'].to_numpy().astype(float)

#
# restaurantRecBaselineV1=df_restaurant_BaselineV1['recall'].to_numpy().astype(float)
# restaurantRecBaselineV2=df_restaurant_BaselineV2['recall'].to_numpy().astype(float)
# restaurantRecBaselineV3=df_restaurant_BaselineV3['recall'].to_numpy().astype(float)
# restaurantRecBaselineV4=df_restaurant_BaselineV4['recall'].to_numpy().astype(float)
# restaurantRecBaselineV5=df_restaurant_BaselineV5['recall'].to_numpy().astype(float)
# restaurantPreBaselineV1=df_restaurant_BaselineV1['precision'].to_numpy().astype(float)
# restaurantPreBaselineV2=df_restaurant_BaselineV2['precision'].to_numpy().astype(float)
# restaurantPreBaselineV3=df_restaurant_BaselineV3['precision'].to_numpy().astype(float)
# restaurantPreBaselineV4=df_restaurant_BaselineV4['precision'].to_numpy().astype(float)
# restaurantPreBaselineV5=df_restaurant_BaselineV5['precision'].to_numpy().astype(float)
# restaurantRMSEBaselineV1=df_restaurant_BaselineV1['rmse'].to_numpy().astype(float)
# restaurantRMSEBaselineV2=df_restaurant_BaselineV2['rmse'].to_numpy().astype(float)
# restaurantRMSEBaselineV3=df_restaurant_BaselineV3['rmse'].to_numpy().astype(float)
# restaurantRMSEBaselineV4=df_restaurant_BaselineV4['rmse'].to_numpy().astype(float)
# restaurantRMSEBaselineV5=df_restaurant_BaselineV5['rmse'].to_numpy().astype(float)

restaurantRecBaseline20V1=df_restaurant_Baseline20V1['recall'].to_numpy().astype(float)
restaurantRecBaseline20V2=df_restaurant_Baseline20V2['recall'].to_numpy().astype(float)
restaurantRecBaseline20V3=df_restaurant_Baseline20V3['recall'].to_numpy().astype(float)
restaurantRecBaseline20V4=df_restaurant_Baseline20V4['recall'].to_numpy().astype(float)
restaurantRecBaseline20V5=df_restaurant_Baseline20V5['recall'].to_numpy().astype(float)
restaurantPreBaseline20V1=df_restaurant_Baseline20V1['precision'].to_numpy().astype(float)
restaurantPreBaseline20V2=df_restaurant_Baseline20V2['precision'].to_numpy().astype(float)
restaurantPreBaseline20V3=df_restaurant_Baseline20V3['precision'].to_numpy().astype(float)
restaurantPreBaseline20V4=df_restaurant_Baseline20V4['precision'].to_numpy().astype(float)
restaurantPreBaseline20V5=df_restaurant_Baseline20V5['precision'].to_numpy().astype(float)
restaurantRMSEBaseline20V1=df_restaurant_Baseline20V1['rmse'].to_numpy().astype(float)
restaurantRMSEBaseline20V2=df_restaurant_Baseline20V2['rmse'].to_numpy().astype(float)
restaurantRMSEBaseline20V3=df_restaurant_Baseline20V3['rmse'].to_numpy().astype(float)
restaurantRMSEBaseline20V4=df_restaurant_Baseline20V4['rmse'].to_numpy().astype(float)
restaurantRMSEBaseline20V5=df_restaurant_Baseline20V5['rmse'].to_numpy().astype(float)
#
restaurantRecHybridV1=df_restaurant_HybridV1['recall'].to_numpy().astype(float)
restaurantRecHybridV2=df_restaurant_HybridV2['recall'].to_numpy().astype(float)
restaurantRecHybridV3=df_restaurant_HybridV3['recall'].to_numpy().astype(float)
restaurantRecHybridV4=df_restaurant_HybridV4['recall'].to_numpy().astype(float)
restaurantRecHybridV5=df_restaurant_HybridV5['recall'].to_numpy().astype(float)
restaurantPreHybridV1=df_restaurant_HybridV1['precision'].to_numpy().astype(float)
restaurantPreHybridV2=df_restaurant_HybridV2['precision'].to_numpy().astype(float)
restaurantPreHybridV3=df_restaurant_HybridV3['precision'].to_numpy().astype(float)
restaurantPreHybridV4=df_restaurant_HybridV4['precision'].to_numpy().astype(float)
restaurantPreHybridV5=df_restaurant_HybridV5['precision'].to_numpy().astype(float)
restaurantRMSEHybridV1=df_restaurant_HybridV1['rmse'].to_numpy().astype(float)
restaurantRMSEHybridV2=df_restaurant_HybridV2['rmse'].to_numpy().astype(float)
restaurantRMSEHybridV3=df_restaurant_HybridV3['rmse'].to_numpy().astype(float)
restaurantRMSEHybridV4=df_restaurant_HybridV4['rmse'].to_numpy().astype(float)
restaurantRMSEHybridV5=df_restaurant_HybridV5['rmse'].to_numpy().astype(float)

arrays = [restaurantRecPipelineNoRevV1, restaurantRecPipelineNoRevV2, restaurantRecPipelineNoRevV3, restaurantRecPipelineNoRevV4, restaurantRecPipelineNoRevV5]
restaurantRecPipelineNoRev = np.mean(arrays, axis=0)
arrays = [restaurantPrePipelineNoRevV1, restaurantPrePipelineNoRevV2, restaurantPrePipelineNoRevV3, restaurantPrePipelineNoRevV4, restaurantPrePipelineNoRevV5]
restaurantPrePipelineNoRev = np.mean(arrays, axis=0)
arrays = [restaurantRMSEPipelineNoRevV1, restaurantRMSEPipelineNoRevV2, restaurantRMSEPipelineNoRevV3, restaurantRMSEPipelineNoRevV4, restaurantRMSEPipelineNoRevV5]
restaurantRMSEPipelineNoRev = np.mean(arrays, axis=0)
#
# arrays = [restaurantRecBaselineV1, restaurantRecBaselineV2, restaurantRecBaselineV3, restaurantRecBaselineV4, restaurantRecBaselineV5]
# restaurantRecBaseline = np.mean(arrays, axis=0)
# arrays = [restaurantPreBaselineV1, restaurantPreBaselineV2, restaurantPreBaselineV3, restaurantPreBaselineV4, restaurantPreBaselineV5]
# restaurantPreBaseline = np.mean(arrays, axis=0)
# arrays = [restaurantRMSEBaselineV1, restaurantRMSEBaselineV2, restaurantRMSEBaselineV3, restaurantRMSEBaselineV4, restaurantRMSEBaselineV5]
# restaurantRMSEBaseline = np.mean(arrays, axis=0)

arrays = [restaurantRecBaseline20V1, restaurantRecBaseline20V2, restaurantRecBaseline20V3, restaurantRecBaseline20V4, restaurantRecBaseline20V5]
restaurantRecBaseline20 = np.mean(arrays, axis=0)
arrays = [restaurantPreBaseline20V1, restaurantPreBaseline20V2, restaurantPreBaseline20V3, restaurantPreBaseline20V4, restaurantPreBaseline20V5]
restaurantPreBaseline20 = np.mean(arrays, axis=0)
arrays = [restaurantRMSEBaseline20V1, restaurantRMSEBaseline20V2, restaurantRMSEBaseline20V3, restaurantRMSEBaseline20V4, restaurantRMSEBaseline20V5]
restaurantRMSEBaseline20 = np.mean(arrays, axis=0)

arrays = [restaurantRecHybridV1, restaurantRecHybridV2, restaurantRecHybridV3, restaurantRecHybridV4, restaurantRecHybridV5]
restaurantRecHybrid = np.mean(arrays, axis=0)
arrays = [restaurantPreHybridV1, restaurantPreHybridV2, restaurantPreHybridV3, restaurantPreHybridV4, restaurantPreHybridV5]
restaurantPreHybrid = np.mean(arrays, axis=0)
arrays = [restaurantRMSEHybridV1, restaurantRMSEHybridV2, restaurantRMSEHybridV3, restaurantRMSEHybridV4, restaurantRMSEHybridV5]
restaurantRMSEHybrid = np.mean(arrays, axis=0)

arrays = [restaurantRecPipelineV1, restaurantRecPipelineV2, restaurantRecPipelineV3, restaurantRecPipelineV4, restaurantRecPipelineV5]
restaurantRecPipeline = np.mean(arrays, axis=0)
arrays = [restaurantPrePipelineV1, restaurantPrePipelineV2, restaurantPrePipelineV3, restaurantPrePipelineV4, restaurantPrePipelineV5]
restaurantPrePipeline = np.mean(arrays, axis=0)
arrays = [restaurantRMSEPipelineV1, restaurantRMSEPipelineV2, restaurantRMSEPipelineV3, restaurantRMSEPipelineV4, restaurantRMSEPipelineV5]
restaurantRMSEPipeline = np.mean(arrays, axis=0)


restaurantF1PipelineNoRev = 2 * (restaurantPrePipelineNoRev * restaurantRecPipelineNoRev) / (restaurantPrePipelineNoRev + restaurantRecPipelineNoRev)
# restaurantF1Baseline = 2 * (restaurantPreBaseline * restaurantRecBaseline) / (restaurantPreBaseline + restaurantRecBaseline)
restaurantF1Baseline20 = 2 * (restaurantPreBaseline20 * restaurantRecBaseline20) / (restaurantPreBaseline20 + restaurantRecBaseline20)
restaurantF1Hybrid = 2 * (restaurantPreHybrid * restaurantRecHybrid) / (restaurantPreHybrid + restaurantRecHybrid)
restaurantF1Pipeline = 2 * (restaurantPrePipeline * restaurantRecPipeline) / (restaurantPrePipeline + restaurantRecPipeline)


restaurantGMeanPipelineNoRev = np.sqrt(restaurantPrePipelineNoRev * restaurantRecPipelineNoRev)
#restaurantGMeanBaseline = np.sqrt(restaurantPreBaseline * restaurantRecBaseline)
restaurantGMeanBaseline20 = np.sqrt(restaurantPreBaseline20 * restaurantRecBaseline20)
restaurantGMeanHybrid = np.sqrt(restaurantPreHybrid * restaurantRecHybrid)
restaurantGMeanPipeline = np.sqrt(restaurantPrePipeline * restaurantRecPipeline)

# beta=0.4
# restaurantF0_5PipelineNoRev = (1 + beta**2) * (restaurantPrePipelineNoRev * restaurantRecPipelineNoRev) / ((beta**2 * restaurantPrePipelineNoRev) + restaurantRecPipelineNoRev)
# restaurantF0_5Baseline = (1 + beta**2) * (restaurantPreBaseline * restaurantRecBaseline) / ((beta**2 * restaurantPreBaseline) + restaurantRecBaseline)
# restaurantF0_5Baseline20 = (1 + beta**2) * (restaurantPreBaseline20 * restaurantRecBaseline20) / ((beta**2 * restaurantPreBaseline20) + restaurantRecBaseline20)
# restaurantF0_5Hybrid = (1 + beta**2) * (restaurantPreHybrid * restaurantRecHybrid) / ((beta**2 * restaurantPreHybrid) + restaurantRecHybrid)
# restaurantF0_5PipelineNoRevNoRev = (1 + beta**2) * (restaurantPrePipelineNoRevNoRev * restaurantRecPipelineNoRevNoRev) / ((beta**2 * restaurantPrePipelineNoRevNoRev) + restaurantRecPipelineNoRevNoRev)


r1 = np.arange(10)

fig, axs = plt.subplots(5, 1, figsize=(5,9), sharey=True)
fig.subplots_adjust(hspace=0.1, wspace=0.05)

axs[0].plot(r1, restaurantPrePipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[0].plot(r1, restaurantPreBaseline,marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[0].plot(r1, restaurantPreBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[0].plot(r1, restaurantPrePipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[0].plot(r1, restaurantPreHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")


axs[1].plot(r1, restaurantRecPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[1].plot(r1, restaurantRecBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[1].plot(r1, restaurantRecBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[1].plot(r1, restaurantRecPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[1].plot(r1, restaurantRecHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")





axs[2].plot(r1, restaurantF1Pipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[2].plot(r1, restaurantF1Baseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[2].plot(r1, restaurantF1Baseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[2].plot(r1, restaurantF1PipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[2].plot(r1, restaurantF1Hybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[3].plot(r1, restaurantGMeanPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[3].plot(r1, restaurantGMeanBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[3].plot(r1, restaurantGMeanBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[3].plot(r1, restaurantGMeanPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[3].plot(r1, restaurantGMeanHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[4].plot(r1, restaurantRMSEPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[4].plot(r1, restaurantRMSEBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[4].plot(r1, restaurantRMSEBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[4].plot(r1, restaurantRMSEPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[4].plot(r1, restaurantRMSEHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[0].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[0].set_ylabel('Precision', rotation='vertical')
axs[0].set_title('Restaurant', fontsize=12)

axs[1].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[1].set_ylabel('Recall', rotation='vertical')

axs[2].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[2].set_ylabel('F1-Score', rotation='vertical')

axs[3].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[3].set_ylabel('G-Mean', rotation='vertical')

axs[4].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[4].set_ylabel('RMSE', rotation='vertical')
axs[4].set_xlabel('Missing rate')


axs[0].tick_params(axis='x', which='major', labelsize=10)
axs[1].tick_params(axis='x', which='major', labelsize=10)
axs[2].tick_params(axis='x', which='major', labelsize=10)
axs[3].tick_params(axis='x', which='major', labelsize=10)
axs[4].tick_params(axis='x', which='major', labelsize=10)

axs[0].tick_params(axis='y', which='major', labelsize=11)
axs[1].tick_params(axis='y', which='major', labelsize=11)
axs[2].tick_params(axis='y', which='major', labelsize=11)
axs[3].tick_params(axis='y', which='major', labelsize=11)
axs[4].tick_params(axis='y', which='major', labelsize=11)

for ax in axs.flat:
    ax.label_outer()
    #ax.grid(True, color='#CFCFCF', zorder=1)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='gray', alpha=0.52)
    ax.grid(which='minor', linewidth='0.5',linestyle='dotted', ms=2, color='gray', alpha=0.4)
    ax.xaxis.set_minor_locator(MultipleLocator(1))  # Customize the spacing between minor gridlines on the x-axis
    ax.yaxis.set_minor_locator(MultipleLocator(0.05))  # Customize the spacing between minor gridlines on the y-axis

# Create legend artists for each line
legend_artist1 = plt.Line2D([0], [0], color='#ff0000', linestyle='-', label='PipelineNoRev', marker="x", markersize=10)
#legend_artist2 = plt.Line2D([0], [0], color='#00C3CC', linestyle='-', label='Baseline', marker="+", markersize=10)
legend_artist3 = plt.Line2D([0], [0], color='#FFA600', linestyle='-', label='PipelineNoRev', marker="o")
legend_artist4 = plt.Line2D([0], [0], color='#61a44f', linestyle='dashdot', label='Hybrid', marker="2", markersize=10)
legend_artist5 = plt.Line2D([0], [0], color='#00748f', linestyle='-', label='Baseline20', marker="2", markersize=12)

# Add the legend artists to the figure
legend = fig.legend(handles=[legend_artist1, legend_artist3, legend_artist4, legend_artist5], loc='upper center', ncol=5, bbox_to_anchor=(0.5, 0.95), shadow=True)

plt.savefig("restaurant.pdf", bbox_inches='tight')
plt.show()
