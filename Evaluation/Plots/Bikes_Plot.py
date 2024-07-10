import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

df=pd.read_csv("../ALL_Results.csv", sep=';')



df_EV_Vehicles_=df.loc[df['dataset'] == 'bikes_4100' ]

df_EV_Vehicles_Pipeline=df_EV_Vehicles_.loc[df_EV_Vehicles_['algoritmo'] == 'Pipeline' ]
#df_EV_Vehicles_Baseline=df_EV_Vehicles_.loc[df_EV_Vehicles_['algoritmo'] == 'Baseline' ]
df_EV_Vehicles_Baseline20=df_EV_Vehicles_.loc[df_EV_Vehicles_['algoritmo'] == 'Baseline20' ]
#df_EV_Vehicles_PipelineNoRev=df_EV_Vehicles_.loc[df_EV_Vehicles_['algoritmo'] == 'Pipeline_noRev' ]
#df_EV_Vehicles_Hybrid=df_EV_Vehicles_.loc[df_EV_Vehicles_['algoritmo'] == 'Hybrid' ]



df_EV_Vehicles_PipelineV1=df_EV_Vehicles_Pipeline.loc[df_EV_Vehicles_Pipeline['version'] == 1 ]
df_EV_Vehicles_PipelineV2=df_EV_Vehicles_Pipeline.loc[df_EV_Vehicles_Pipeline['version'] == 2 ]
df_EV_Vehicles_PipelineV3=df_EV_Vehicles_Pipeline.loc[df_EV_Vehicles_Pipeline['version'] == 3 ]
df_EV_Vehicles_PipelineV4=df_EV_Vehicles_Pipeline.loc[df_EV_Vehicles_Pipeline['version'] == 4 ]
df_EV_Vehicles_PipelineV5=df_EV_Vehicles_Pipeline.loc[df_EV_Vehicles_Pipeline['version'] == 5 ]

# df_EV_Vehicles_BaselineV1=df_EV_Vehicles_Baseline.loc[df_EV_Vehicles_Baseline['version'] == 1 ]
# df_EV_Vehicles_BaselineV2=df_EV_Vehicles_Baseline.loc[df_EV_Vehicles_Baseline['version'] == 2 ]
# df_EV_Vehicles_BaselineV3=df_EV_Vehicles_Baseline.loc[df_EV_Vehicles_Baseline['version'] == 3 ]
# df_EV_Vehicles_BaselineV4=df_EV_Vehicles_Baseline.loc[df_EV_Vehicles_Baseline['version'] == 4 ]
# df_EV_Vehicles_BaselineV5=df_EV_Vehicles_Baseline.loc[df_EV_Vehicles_Baseline['version'] == 5 ]
#
df_EV_Vehicles_Baseline20V1=df_EV_Vehicles_Baseline20.loc[df_EV_Vehicles_Baseline20['version'] == 1 ]
df_EV_Vehicles_Baseline20V2=df_EV_Vehicles_Baseline20.loc[df_EV_Vehicles_Baseline20['version'] == 2 ]
df_EV_Vehicles_Baseline20V3=df_EV_Vehicles_Baseline20.loc[df_EV_Vehicles_Baseline20['version'] == 3 ]
df_EV_Vehicles_Baseline20V4=df_EV_Vehicles_Baseline20.loc[df_EV_Vehicles_Baseline20['version'] == 4 ]
df_EV_Vehicles_Baseline20V5=df_EV_Vehicles_Baseline20.loc[df_EV_Vehicles_Baseline20['version'] == 5 ]
#
# df_EV_Vehicles_PipelineNoRevV1=df_EV_Vehicles_PipelineNoRev.loc[df_EV_Vehicles_PipelineNoRev['version'] == 1 ]
# df_EV_Vehicles_PipelineNoRevV2=df_EV_Vehicles_PipelineNoRev.loc[df_EV_Vehicles_PipelineNoRev['version'] == 2 ]
# df_EV_Vehicles_PipelineNoRevV3=df_EV_Vehicles_PipelineNoRev.loc[df_EV_Vehicles_PipelineNoRev['version'] == 3 ]
# df_EV_Vehicles_PipelineNoRevV4=df_EV_Vehicles_PipelineNoRev.loc[df_EV_Vehicles_PipelineNoRev['version'] == 4 ]
# df_EV_Vehicles_PipelineNoRevV5=df_EV_Vehicles_PipelineNoRev.loc[df_EV_Vehicles_PipelineNoRev['version'] == 5 ]
#
# df_EV_Vehicles_HybridV1=df_EV_Vehicles_Hybrid.loc[df_EV_Vehicles_Hybrid['version'] == 1 ]
# df_EV_Vehicles_HybridV2=df_EV_Vehicles_Hybrid.loc[df_EV_Vehicles_Hybrid['version'] == 2 ]
# df_EV_Vehicles_HybridV3=df_EV_Vehicles_Hybrid.loc[df_EV_Vehicles_Hybrid['version'] == 3 ]
# df_EV_Vehicles_HybridV4=df_EV_Vehicles_Hybrid.loc[df_EV_Vehicles_Hybrid['version'] == 4 ]
# df_EV_Vehicles_HybridV5=df_EV_Vehicles_Hybrid.loc[df_EV_Vehicles_Hybrid['version'] == 5 ]

EV_VehiclesRecPipelineV1=df_EV_Vehicles_PipelineV1['recall'].to_numpy().astype(float)
EV_VehiclesRecPipelineV2=df_EV_Vehicles_PipelineV2['recall'].to_numpy().astype(float)
EV_VehiclesRecPipelineV3=df_EV_Vehicles_PipelineV3['recall'].to_numpy().astype(float)
EV_VehiclesRecPipelineV4=df_EV_Vehicles_PipelineV4['recall'].to_numpy().astype(float)
EV_VehiclesRecPipelineV5=df_EV_Vehicles_PipelineV5['recall'].to_numpy().astype(float)
EV_VehiclesPrePipelineV1=df_EV_Vehicles_PipelineV1['precision'].to_numpy().astype(float)
EV_VehiclesPrePipelineV2=df_EV_Vehicles_PipelineV2['precision'].to_numpy().astype(float)
EV_VehiclesPrePipelineV3=df_EV_Vehicles_PipelineV3['precision'].to_numpy().astype(float)
EV_VehiclesPrePipelineV4=df_EV_Vehicles_PipelineV4['precision'].to_numpy().astype(float)
EV_VehiclesPrePipelineV5=df_EV_Vehicles_PipelineV5['precision'].to_numpy().astype(float)

# EV_VehiclesRecPipelineNoRevV1=df_EV_Vehicles_PipelineNoRevV1['recall'].to_numpy().astype(float)
# EV_VehiclesRecPipelineNoRevV2=df_EV_Vehicles_PipelineNoRevV2['recall'].to_numpy().astype(float)
# EV_VehiclesRecPipelineNoRevV3=df_EV_Vehicles_PipelineNoRevV3['recall'].to_numpy().astype(float)
# EV_VehiclesRecPipelineNoRevV4=df_EV_Vehicles_PipelineNoRevV4['recall'].to_numpy().astype(float)
# EV_VehiclesRecPipelineNoRevV5=df_EV_Vehicles_PipelineNoRevV5['recall'].to_numpy().astype(float)
# EV_VehiclesPrePipelineNoRevV1=df_EV_Vehicles_PipelineNoRevV1['precision'].to_numpy().astype(float)
# EV_VehiclesPrePipelineNoRevV2=df_EV_Vehicles_PipelineNoRevV2['precision'].to_numpy().astype(float)
# EV_VehiclesPrePipelineNoRevV3=df_EV_Vehicles_PipelineNoRevV3['precision'].to_numpy().astype(float)
# EV_VehiclesPrePipelineNoRevV4=df_EV_Vehicles_PipelineNoRevV4['precision'].to_numpy().astype(float)
# EV_VehiclesPrePipelineNoRevV5=df_EV_Vehicles_PipelineNoRevV5['precision'].to_numpy().astype(float)



# EV_VehiclesRecBaselineV1=df_EV_Vehicles_BaselineV1['recall'].to_numpy().astype(float)
# EV_VehiclesRecBaselineV2=df_EV_Vehicles_BaselineV2['recall'].to_numpy().astype(float)
# EV_VehiclesRecBaselineV3=df_EV_Vehicles_BaselineV3['recall'].to_numpy().astype(float)
# EV_VehiclesRecBaselineV4=df_EV_Vehicles_BaselineV4['recall'].to_numpy().astype(float)
# EV_VehiclesRecBaselineV5=df_EV_Vehicles_BaselineV5['recall'].to_numpy().astype(float)
# EV_VehiclesPreBaselineV1=df_EV_Vehicles_BaselineV1['precision'].to_numpy().astype(float)
# EV_VehiclesPreBaselineV2=df_EV_Vehicles_BaselineV2['precision'].to_numpy().astype(float)
# EV_VehiclesPreBaselineV3=df_EV_Vehicles_BaselineV3['precision'].to_numpy().astype(float)
# EV_VehiclesPreBaselineV4=df_EV_Vehicles_BaselineV4['precision'].to_numpy().astype(float)
# EV_VehiclesPreBaselineV5=df_EV_Vehicles_BaselineV5['precision'].to_numpy().astype(float)
#
#
EV_VehiclesRecBaseline20V1=df_EV_Vehicles_Baseline20V1['recall'].to_numpy().astype(float)
EV_VehiclesRecBaseline20V2=df_EV_Vehicles_Baseline20V2['recall'].to_numpy().astype(float)
EV_VehiclesRecBaseline20V3=df_EV_Vehicles_Baseline20V3['recall'].to_numpy().astype(float)
EV_VehiclesRecBaseline20V4=df_EV_Vehicles_Baseline20V4['recall'].to_numpy().astype(float)
EV_VehiclesRecBaseline20V5=df_EV_Vehicles_Baseline20V5['recall'].to_numpy().astype(float)
EV_VehiclesPreBaseline20V1=df_EV_Vehicles_Baseline20V1['precision'].to_numpy().astype(float)
EV_VehiclesPreBaseline20V2=df_EV_Vehicles_Baseline20V2['precision'].to_numpy().astype(float)
EV_VehiclesPreBaseline20V3=df_EV_Vehicles_Baseline20V3['precision'].to_numpy().astype(float)
EV_VehiclesPreBaseline20V4=df_EV_Vehicles_Baseline20V4['precision'].to_numpy().astype(float)
EV_VehiclesPreBaseline20V5=df_EV_Vehicles_Baseline20V5['precision'].to_numpy().astype(float)

# EV_VehiclesRecHybridV1=df_EV_Vehicles_HybridV1['recall'].to_numpy().astype(float)
# EV_VehiclesRecHybridV2=df_EV_Vehicles_HybridV2['recall'].to_numpy().astype(float)
# EV_VehiclesRecHybridV3=df_EV_Vehicles_HybridV3['recall'].to_numpy().astype(float)
# EV_VehiclesRecHybridV4=df_EV_Vehicles_HybridV4['recall'].to_numpy().astype(float)
# EV_VehiclesRecHybridV5=df_EV_Vehicles_HybridV5['recall'].to_numpy().astype(float)
# EV_VehiclesPreHybridV1=df_EV_Vehicles_HybridV1['precision'].to_numpy().astype(float)
# EV_VehiclesPreHybridV2=df_EV_Vehicles_HybridV2['precision'].to_numpy().astype(float)
# EV_VehiclesPreHybridV3=df_EV_Vehicles_HybridV3['precision'].to_numpy().astype(float)
# EV_VehiclesPreHybridV4=df_EV_Vehicles_HybridV4['precision'].to_numpy().astype(float)
# EV_VehiclesPreHybridV5=df_EV_Vehicles_HybridV5['precision'].to_numpy().astype(float)

arrays = [EV_VehiclesRecPipelineV1, EV_VehiclesRecPipelineV2, EV_VehiclesRecPipelineV3, EV_VehiclesRecPipelineV4, EV_VehiclesRecPipelineV5]
EV_VehiclesRecPipeline = np.mean(arrays, axis=0)
arrays = [EV_VehiclesPrePipelineV1, EV_VehiclesPrePipelineV2, EV_VehiclesPrePipelineV3, EV_VehiclesPrePipelineV4, EV_VehiclesPrePipelineV5]
EV_VehiclesPrePipeline = np.mean(arrays, axis=0)

# arrays = [EV_VehiclesRecBaselineV1, EV_VehiclesRecBaselineV2, EV_VehiclesRecBaselineV3, EV_VehiclesRecBaselineV4, EV_VehiclesRecBaselineV5]
# EV_VehiclesRecBaseline = np.mean(arrays, axis=0)
# arrays = [EV_VehiclesPreBaselineV1, EV_VehiclesPreBaselineV2, EV_VehiclesPreBaselineV3, EV_VehiclesPreBaselineV4, EV_VehiclesPreBaselineV5]
# EV_VehiclesPreBaseline = np.mean(arrays, axis=0)
#
arrays = [EV_VehiclesRecBaseline20V1, EV_VehiclesRecBaseline20V2, EV_VehiclesRecBaseline20V3, EV_VehiclesRecBaseline20V4, EV_VehiclesRecBaseline20V5]
EV_VehiclesRecBaseline20 = np.mean(arrays, axis=0)
arrays = [EV_VehiclesPreBaseline20V1, EV_VehiclesPreBaseline20V2, EV_VehiclesPreBaseline20V3, EV_VehiclesPreBaseline20V4, EV_VehiclesPreBaseline20V5]
EV_VehiclesPreBaseline20 = np.mean(arrays, axis=0)
#
# arrays = [EV_VehiclesRecHybridV1, EV_VehiclesRecHybridV2, EV_VehiclesRecHybridV3, EV_VehiclesRecHybridV4, EV_VehiclesRecHybridV5]
# EV_VehiclesRecHybrid = np.mean(arrays, axis=0)
# arrays = [EV_VehiclesPreHybridV1, EV_VehiclesPreHybridV2, EV_VehiclesPreHybridV3, EV_VehiclesPreHybridV4, EV_VehiclesPreHybridV5]
# EV_VehiclesPreHybrid = np.mean(arrays, axis=0)
#
# arrays = [EV_VehiclesRecPipelineNoRevV1, EV_VehiclesRecPipelineNoRevV2, EV_VehiclesRecPipelineNoRevV3, EV_VehiclesRecPipelineNoRevV4, EV_VehiclesRecPipelineNoRevV5]
# EV_VehiclesRecPipelineNoRev = np.mean(arrays, axis=0)
# arrays = [EV_VehiclesPrePipelineNoRevV1, EV_VehiclesPrePipelineNoRevV2, EV_VehiclesPrePipelineNoRevV3, EV_VehiclesPrePipelineNoRevV4, EV_VehiclesPrePipelineNoRevV5]
# EV_VehiclesPrePipelineNoRev = np.mean(arrays, axis=0)


EV_VehiclesF1Pipeline = 2 * (EV_VehiclesPrePipeline * EV_VehiclesRecPipeline) / (EV_VehiclesPrePipeline + EV_VehiclesRecPipeline)
# EV_VehiclesF1Baseline = 2 * (EV_VehiclesPreBaseline * EV_VehiclesRecBaseline) / (EV_VehiclesPreBaseline + EV_VehiclesRecBaseline)
EV_VehiclesF1Baseline20 = 2 * (EV_VehiclesPreBaseline20 * EV_VehiclesRecBaseline20) / (EV_VehiclesPreBaseline20 + EV_VehiclesRecBaseline20)
# EV_VehiclesF1Hybrid = 2 * (EV_VehiclesPreHybrid * EV_VehiclesRecHybrid) / (EV_VehiclesPreHybrid + EV_VehiclesRecHybrid)
# EV_VehiclesF1PipelineNoRev = 2 * (EV_VehiclesPrePipelineNoRev * EV_VehiclesRecPipelineNoRev) / (EV_VehiclesPrePipelineNoRev + EV_VehiclesRecPipelineNoRev)


r1 = np.arange(10)

fig, axs = plt.subplots(3, 1, figsize=(6,9), sharey=True)
fig.subplots_adjust(hspace=0.1, wspace=0.05)

axs[0].plot(r1, EV_VehiclesPrePipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[0].plot(r1, EV_VehiclesPreBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[0].plot(r1, EV_VehiclesPreBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
# axs[0].plot(r1, EV_VehiclesPrePipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
# axs[0].plot(r1, EV_VehiclesPreHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")


axs[1].plot(r1, EV_VehiclesRecPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[1].plot(r1, EV_VehiclesRecBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[1].plot(r1, EV_VehiclesRecBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
# axs[1].plot(r1, EV_VehiclesRecPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
# axs[1].plot(r1, EV_VehiclesRecHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")





axs[2].plot(r1, EV_VehiclesF1Pipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[2].plot(r1, EV_VehiclesF1Baseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[2].plot(r1, EV_VehiclesF1Baseline20, marker="2", markersize=10, color="#00748f", zorder=2)
# axs[2].plot(r1, EV_VehiclesF1PipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
# axs[2].plot(r1, EV_VehiclesF1Hybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")



axs[0].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[0].set_ylabel('Precision', rotation='vertical')
axs[0].set_title('Bikes', fontsize=12)

axs[1].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[1].set_ylabel('Recall', rotation='vertical')

axs[2].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[2].set_ylabel('F1-Measure', rotation='vertical')
#axs[0].set_title('Missing rate', fontsize=10, y=-0.59)
axs[2].set_xlabel('Missing rate')


axs[0].tick_params(axis='x', which='major', labelsize=10)
axs[1].tick_params(axis='x', which='major', labelsize=10)
axs[2].tick_params(axis='x', which='major', labelsize=10)

axs[0].tick_params(axis='y', which='major', labelsize=11)
axs[1].tick_params(axis='y', which='major', labelsize=11)
axs[2].tick_params(axis='y', which='major', labelsize=11)

for ax in axs.flat:
    ax.label_outer()
    #ax.grid(True, color='#CFCFCF', zorder=1)
    ax.minorticks_on()
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='gray', alpha=0.52)
    ax.grid(which='minor', linewidth='0.5',linestyle='dotted', ms=2, color='gray', alpha=0.4)
    ax.xaxis.set_minor_locator(MultipleLocator(1))  # Customize the spacing between minor gridlines on the x-axis
    ax.yaxis.set_minor_locator(MultipleLocator(0.05))  # Customize the spacing between minor gridlines on the y-axis

# Create legend artists for each line
legend_artist1 = plt.Line2D([0], [0], color='#ff0000', linestyle='-', label='Pipeline', marker="x", markersize=10)
legend_artist2 = plt.Line2D([0], [0], color='#00C3CC', linestyle='-', label='Baseline', marker="+", markersize=10)
legend_artist3 = plt.Line2D([0], [0], color='#FFA600', linestyle='-', label='Pipeline NoRev', marker="o")
legend_artist4 = plt.Line2D([0], [0], color='#61a44f', linestyle='dashdot', label='Hybrid', marker="2", markersize=10)
legend_artist5 = plt.Line2D([0], [0], color='#00748f', linestyle='-', label='Baseline20', marker="2", markersize=12)


# Add the legend artists to the figure
legend = fig.legend(handles=[legend_artist1, legend_artist2, legend_artist3, legend_artist4, legend_artist5], loc='upper center', ncol=5, bbox_to_anchor=(0.5, 0.95), shadow=True)

plt.savefig("Bikes_4100.pdf", bbox_inches='tight')
plt.show()
