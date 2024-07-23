import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

df=pd.read_csv("../ALL_Results_v2.csv", sep=';')

df_Boeing_898_=df.loc[df['dataset'] == 'Boeing_898' ]


df_Boeing_898_Pipeline=df_Boeing_898_.loc[df_Boeing_898_['algoritmo'] == 'Pipeline' ]
#df_Boeing_898_Baseline=df_Boeing_898_.loc[df_Boeing_898_['algoritmo'] == 'Baseline' ]
df_Boeing_898_Baseline20=df_Boeing_898_.loc[df_Boeing_898_['algoritmo'] == 'Baseline20' ]
#df_Boeing_898_PipelineNoRev=df_Boeing_898_.loc[df_Boeing_898_['algoritmo'] == 'Pipeline_noRev' ]
#df_Boeing_898_Hybrid=df_Boeing_898_.loc[df_Boeing_898_['algoritmo'] == 'Hybrid' ]


df_Boeing_898_PipelineV1=df_Boeing_898_Pipeline.loc[df_Boeing_898_Pipeline['version'] == 1 ]
df_Boeing_898_PipelineV2=df_Boeing_898_Pipeline.loc[df_Boeing_898_Pipeline['version'] == 2 ]
df_Boeing_898_PipelineV3=df_Boeing_898_Pipeline.loc[df_Boeing_898_Pipeline['version'] == 3 ]
df_Boeing_898_PipelineV4=df_Boeing_898_Pipeline.loc[df_Boeing_898_Pipeline['version'] == 4 ]
df_Boeing_898_PipelineV5=df_Boeing_898_Pipeline.loc[df_Boeing_898_Pipeline['version'] == 5 ]

# df_Boeing_898_BaselineV1=df_Boeing_898_Baseline.loc[df_Boeing_898_Baseline['version'] == 1 ]
# df_Boeing_898_BaselineV2=df_Boeing_898_Baseline.loc[df_Boeing_898_Baseline['version'] == 2 ]
# df_Boeing_898_BaselineV3=df_Boeing_898_Baseline.loc[df_Boeing_898_Baseline['version'] == 3 ]
# df_Boeing_898_BaselineV4=df_Boeing_898_Baseline.loc[df_Boeing_898_Baseline['version'] == 4 ]
# df_Boeing_898_BaselineV5=df_Boeing_898_Baseline.loc[df_Boeing_898_Baseline['version'] == 5 ]

df_Boeing_898_Baseline20V1=df_Boeing_898_Baseline20.loc[df_Boeing_898_Baseline20['version'] == 1 ]
df_Boeing_898_Baseline20V2=df_Boeing_898_Baseline20.loc[df_Boeing_898_Baseline20['version'] == 2 ]
df_Boeing_898_Baseline20V3=df_Boeing_898_Baseline20.loc[df_Boeing_898_Baseline20['version'] == 3 ]
df_Boeing_898_Baseline20V4=df_Boeing_898_Baseline20.loc[df_Boeing_898_Baseline20['version'] == 4 ]
df_Boeing_898_Baseline20V5=df_Boeing_898_Baseline20.loc[df_Boeing_898_Baseline20['version'] == 5 ]

# df_Boeing_898_PipelineNoRevV1=df_Boeing_898_PipelineNoRev.loc[df_Boeing_898_PipelineNoRev['version'] == 1 ]
# df_Boeing_898_PipelineNoRevV2=df_Boeing_898_PipelineNoRev.loc[df_Boeing_898_PipelineNoRev['version'] == 2 ]
# df_Boeing_898_PipelineNoRevV3=df_Boeing_898_PipelineNoRev.loc[df_Boeing_898_PipelineNoRev['version'] == 3 ]
# df_Boeing_898_PipelineNoRevV4=df_Boeing_898_PipelineNoRev.loc[df_Boeing_898_PipelineNoRev['version'] == 4 ]
# df_Boeing_898_PipelineNoRevV5=df_Boeing_898_PipelineNoRev.loc[df_Boeing_898_PipelineNoRev['version'] == 5 ]
#
# df_Boeing_898_HybridV1=df_Boeing_898_Hybrid.loc[df_Boeing_898_Hybrid['version'] == 1 ]
# df_Boeing_898_HybridV2=df_Boeing_898_Hybrid.loc[df_Boeing_898_Hybrid['version'] == 2 ]
# df_Boeing_898_HybridV3=df_Boeing_898_Hybrid.loc[df_Boeing_898_Hybrid['version'] == 3 ]
# df_Boeing_898_HybridV4=df_Boeing_898_Hybrid.loc[df_Boeing_898_Hybrid['version'] == 4 ]
# df_Boeing_898_HybridV5=df_Boeing_898_Hybrid.loc[df_Boeing_898_Hybrid['version'] == 5 ]

# Boeing_898RecPipelineNoRevV1=df_Boeing_898_PipelineNoRevV1['recall'].to_numpy().astype(float)
# Boeing_898RecPipelineNoRevV2=df_Boeing_898_PipelineNoRevV2['recall'].to_numpy().astype(float)
# Boeing_898RecPipelineNoRevV3=df_Boeing_898_PipelineNoRevV3['recall'].to_numpy().astype(float)
# Boeing_898RecPipelineNoRevV4=df_Boeing_898_PipelineNoRevV4['recall'].to_numpy().astype(float)
# Boeing_898RecPipelineNoRevV5=df_Boeing_898_PipelineNoRevV5['recall'].to_numpy().astype(float)
# Boeing_898PrePipelineNoRevV1=df_Boeing_898_PipelineNoRevV1['precision'].to_numpy().astype(float)
# Boeing_898PrePipelineNoRevV2=df_Boeing_898_PipelineNoRevV2['precision'].to_numpy().astype(float)
# Boeing_898PrePipelineNoRevV3=df_Boeing_898_PipelineNoRevV3['precision'].to_numpy().astype(float)
# Boeing_898PrePipelineNoRevV4=df_Boeing_898_PipelineNoRevV4['precision'].to_numpy().astype(float)
# Boeing_898PrePipelineNoRevV5=df_Boeing_898_PipelineNoRevV5['precision'].to_numpy().astype(float)
# Boeing_898RMSEPipelineNoRevV1=df_Boeing_898_PipelineNoRevV1['rmse'].to_numpy().astype(float)
# Boeing_898RMSEPipelineNoRevV2=df_Boeing_898_PipelineNoRevV2['rmse'].to_numpy().astype(float)
# Boeing_898RMSEPipelineNoRevV3=df_Boeing_898_PipelineNoRevV3['rmse'].to_numpy().astype(float)
# Boeing_898RMSEPipelineNoRevV4=df_Boeing_898_PipelineNoRevV4['rmse'].to_numpy().astype(float)
# Boeing_898RMSEPipelineNoRevV5=df_Boeing_898_PipelineNoRevV5['rmse'].to_numpy().astype(float)



Boeing_898RecPipelineV1=df_Boeing_898_PipelineV1['recall'].to_numpy().astype(float)
Boeing_898RecPipelineV2=df_Boeing_898_PipelineV2['recall'].to_numpy().astype(float)
Boeing_898RecPipelineV3=df_Boeing_898_PipelineV3['recall'].to_numpy().astype(float)
Boeing_898RecPipelineV4=df_Boeing_898_PipelineV4['recall'].to_numpy().astype(float)
Boeing_898RecPipelineV5=df_Boeing_898_PipelineV5['recall'].to_numpy().astype(float)
Boeing_898PrePipelineV1=df_Boeing_898_PipelineV1['precision'].to_numpy().astype(float)
Boeing_898PrePipelineV2=df_Boeing_898_PipelineV2['precision'].to_numpy().astype(float)
Boeing_898PrePipelineV3=df_Boeing_898_PipelineV3['precision'].to_numpy().astype(float)
Boeing_898PrePipelineV4=df_Boeing_898_PipelineV4['precision'].to_numpy().astype(float)
Boeing_898PrePipelineV5=df_Boeing_898_PipelineV5['precision'].to_numpy().astype(float)
Boeing_898RMSEPipelineV1=df_Boeing_898_PipelineV1['rmse'].to_numpy().astype(float)
Boeing_898RMSEPipelineV2=df_Boeing_898_PipelineV2['rmse'].to_numpy().astype(float)
Boeing_898RMSEPipelineV3=df_Boeing_898_PipelineV3['rmse'].to_numpy().astype(float)
Boeing_898RMSEPipelineV4=df_Boeing_898_PipelineV4['rmse'].to_numpy().astype(float)
Boeing_898RMSEPipelineV5=df_Boeing_898_PipelineV5['rmse'].to_numpy().astype(float)

#
# Boeing_898RecBaselineV1=df_Boeing_898_BaselineV1['recall'].to_numpy().astype(float)
# Boeing_898RecBaselineV2=df_Boeing_898_BaselineV2['recall'].to_numpy().astype(float)
# Boeing_898RecBaselineV3=df_Boeing_898_BaselineV3['recall'].to_numpy().astype(float)
# Boeing_898RecBaselineV4=df_Boeing_898_BaselineV4['recall'].to_numpy().astype(float)
# Boeing_898RecBaselineV5=df_Boeing_898_BaselineV5['recall'].to_numpy().astype(float)
# Boeing_898PreBaselineV1=df_Boeing_898_BaselineV1['precision'].to_numpy().astype(float)
# Boeing_898PreBaselineV2=df_Boeing_898_BaselineV2['precision'].to_numpy().astype(float)
# Boeing_898PreBaselineV3=df_Boeing_898_BaselineV3['precision'].to_numpy().astype(float)
# Boeing_898PreBaselineV4=df_Boeing_898_BaselineV4['precision'].to_numpy().astype(float)
# Boeing_898PreBaselineV5=df_Boeing_898_BaselineV5['precision'].to_numpy().astype(float)
# Boeing_898RMSEBaselineV1=df_Boeing_898_BaselineV1['rmse'].to_numpy().astype(float)
# Boeing_898RMSEBaselineV2=df_Boeing_898_BaselineV2['rmse'].to_numpy().astype(float)
# Boeing_898RMSEBaselineV3=df_Boeing_898_BaselineV3['rmse'].to_numpy().astype(float)
# Boeing_898RMSEBaselineV4=df_Boeing_898_BaselineV4['rmse'].to_numpy().astype(float)
# Boeing_898RMSEBaselineV5=df_Boeing_898_BaselineV5['rmse'].to_numpy().astype(float)

Boeing_898RecBaseline20V1=df_Boeing_898_Baseline20V1['recall'].to_numpy().astype(float)
Boeing_898RecBaseline20V2=df_Boeing_898_Baseline20V2['recall'].to_numpy().astype(float)
Boeing_898RecBaseline20V3=df_Boeing_898_Baseline20V3['recall'].to_numpy().astype(float)
Boeing_898RecBaseline20V4=df_Boeing_898_Baseline20V4['recall'].to_numpy().astype(float)
Boeing_898RecBaseline20V5=df_Boeing_898_Baseline20V5['recall'].to_numpy().astype(float)
Boeing_898PreBaseline20V1=df_Boeing_898_Baseline20V1['precision'].to_numpy().astype(float)
Boeing_898PreBaseline20V2=df_Boeing_898_Baseline20V2['precision'].to_numpy().astype(float)
Boeing_898PreBaseline20V3=df_Boeing_898_Baseline20V3['precision'].to_numpy().astype(float)
Boeing_898PreBaseline20V4=df_Boeing_898_Baseline20V4['precision'].to_numpy().astype(float)
Boeing_898PreBaseline20V5=df_Boeing_898_Baseline20V5['precision'].to_numpy().astype(float)
Boeing_898RMSEBaseline20V1=df_Boeing_898_Baseline20V1['rmse'].to_numpy().astype(float)
Boeing_898RMSEBaseline20V2=df_Boeing_898_Baseline20V2['rmse'].to_numpy().astype(float)
Boeing_898RMSEBaseline20V3=df_Boeing_898_Baseline20V3['rmse'].to_numpy().astype(float)
Boeing_898RMSEBaseline20V4=df_Boeing_898_Baseline20V4['rmse'].to_numpy().astype(float)
Boeing_898RMSEBaseline20V5=df_Boeing_898_Baseline20V5['rmse'].to_numpy().astype(float)
#
# Boeing_898RecHybridV1=df_Boeing_898_HybridV1['recall'].to_numpy().astype(float)
# Boeing_898RecHybridV2=df_Boeing_898_HybridV2['recall'].to_numpy().astype(float)
# Boeing_898RecHybridV3=df_Boeing_898_HybridV3['recall'].to_numpy().astype(float)
# Boeing_898RecHybridV4=df_Boeing_898_HybridV4['recall'].to_numpy().astype(float)
# Boeing_898RecHybridV5=df_Boeing_898_HybridV5['recall'].to_numpy().astype(float)
# Boeing_898PreHybridV1=df_Boeing_898_HybridV1['precision'].to_numpy().astype(float)
# Boeing_898PreHybridV2=df_Boeing_898_HybridV2['precision'].to_numpy().astype(float)
# Boeing_898PreHybridV3=df_Boeing_898_HybridV3['precision'].to_numpy().astype(float)
# Boeing_898PreHybridV4=df_Boeing_898_HybridV4['precision'].to_numpy().astype(float)
# Boeing_898PreHybridV5=df_Boeing_898_HybridV5['precision'].to_numpy().astype(float)
# Boeing_898RMSEHybridV1=df_Boeing_898_HybridV1['rmse'].to_numpy().astype(float)
# Boeing_898RMSEHybridV2=df_Boeing_898_HybridV2['rmse'].to_numpy().astype(float)
# Boeing_898RMSEHybridV3=df_Boeing_898_HybridV3['rmse'].to_numpy().astype(float)
# Boeing_898RMSEHybridV4=df_Boeing_898_HybridV4['rmse'].to_numpy().astype(float)
# Boeing_898RMSEHybridV5=df_Boeing_898_HybridV5['rmse'].to_numpy().astype(float)

# arrays = [Boeing_898RecPipelineNoRevV1, Boeing_898RecPipelineNoRevV2, Boeing_898RecPipelineNoRevV3, Boeing_898RecPipelineNoRevV4, Boeing_898RecPipelineNoRevV5]
# Boeing_898RecPipelineNoRev = np.mean(arrays, axis=0)
# arrays = [Boeing_898PrePipelineNoRevV1, Boeing_898PrePipelineNoRevV2, Boeing_898PrePipelineNoRevV3, Boeing_898PrePipelineNoRevV4, Boeing_898PrePipelineNoRevV5]
# Boeing_898PrePipelineNoRev = np.mean(arrays, axis=0)
# arrays = [Boeing_898RMSEPipelineNoRevV1, Boeing_898RMSEPipelineNoRevV2, Boeing_898RMSEPipelineNoRevV3, Boeing_898RMSEPipelineNoRevV4, Boeing_898RMSEPipelineNoRevV5]
# Boeing_898RMSEPipelineNoRev = np.mean(arrays, axis=0)
#
# arrays = [Boeing_898RecBaselineV1, Boeing_898RecBaselineV2, Boeing_898RecBaselineV3, Boeing_898RecBaselineV4, Boeing_898RecBaselineV5]
# Boeing_898RecBaseline = np.mean(arrays, axis=0)
# arrays = [Boeing_898PreBaselineV1, Boeing_898PreBaselineV2, Boeing_898PreBaselineV3, Boeing_898PreBaselineV4, Boeing_898PreBaselineV5]
# Boeing_898PreBaseline = np.mean(arrays, axis=0)
# arrays = [Boeing_898RMSEBaselineV1, Boeing_898RMSEBaselineV2, Boeing_898RMSEBaselineV3, Boeing_898RMSEBaselineV4, Boeing_898RMSEBaselineV5]
# Boeing_898RMSEBaseline = np.mean(arrays, axis=0)

arrays = [Boeing_898RecBaseline20V1, Boeing_898RecBaseline20V2, Boeing_898RecBaseline20V3, Boeing_898RecBaseline20V4, Boeing_898RecBaseline20V5]
Boeing_898RecBaseline20 = np.mean(arrays, axis=0)
arrays = [Boeing_898PreBaseline20V1, Boeing_898PreBaseline20V2, Boeing_898PreBaseline20V3, Boeing_898PreBaseline20V4, Boeing_898PreBaseline20V5]
Boeing_898PreBaseline20 = np.mean(arrays, axis=0)
arrays = [Boeing_898RMSEBaseline20V1, Boeing_898RMSEBaseline20V2, Boeing_898RMSEBaseline20V3, Boeing_898RMSEBaseline20V4, Boeing_898RMSEBaseline20V5]
Boeing_898RMSEBaseline20 = np.mean(arrays, axis=0)

# arrays = [Boeing_898RecHybridV1, Boeing_898RecHybridV2, Boeing_898RecHybridV3, Boeing_898RecHybridV4, Boeing_898RecHybridV5]
# Boeing_898RecHybrid = np.mean(arrays, axis=0)
# arrays = [Boeing_898PreHybridV1, Boeing_898PreHybridV2, Boeing_898PreHybridV3, Boeing_898PreHybridV4, Boeing_898PreHybridV5]
# Boeing_898PreHybrid = np.mean(arrays, axis=0)
# arrays = [Boeing_898RMSEHybridV1, Boeing_898RMSEHybridV2, Boeing_898RMSEHybridV3, Boeing_898RMSEHybridV4, Boeing_898RMSEHybridV5]
# Boeing_898RMSEHybrid = np.mean(arrays, axis=0)

arrays = [Boeing_898RecPipelineV1, Boeing_898RecPipelineV2, Boeing_898RecPipelineV3, Boeing_898RecPipelineV4, Boeing_898RecPipelineV5]
Boeing_898RecPipeline = np.mean(arrays, axis=0)
arrays = [Boeing_898PrePipelineV1, Boeing_898PrePipelineV2, Boeing_898PrePipelineV3, Boeing_898PrePipelineV4, Boeing_898PrePipelineV5]
Boeing_898PrePipeline = np.mean(arrays, axis=0)
arrays = [Boeing_898RMSEPipelineV1, Boeing_898RMSEPipelineV2, Boeing_898RMSEPipelineV3, Boeing_898RMSEPipelineV4, Boeing_898RMSEPipelineV5]
Boeing_898RMSEPipeline = np.mean(arrays, axis=0)


# Boeing_898F1PipelineNoRev = 2 * (Boeing_898PrePipelineNoRev * Boeing_898RecPipelineNoRev) / (Boeing_898PrePipelineNoRev + Boeing_898RecPipelineNoRev)
# Boeing_898F1Baseline = 2 * (Boeing_898PreBaseline * Boeing_898RecBaseline) / (Boeing_898PreBaseline + Boeing_898RecBaseline)
Boeing_898F1Baseline20 = 2 * (Boeing_898PreBaseline20 * Boeing_898RecBaseline20) / (Boeing_898PreBaseline20 + Boeing_898RecBaseline20)
# Boeing_898F1Hybrid = 2 * (Boeing_898PreHybrid * Boeing_898RecHybrid) / (Boeing_898PreHybrid + Boeing_898RecHybrid)
Boeing_898F1Pipeline = 2 * (Boeing_898PrePipeline * Boeing_898RecPipeline) / (Boeing_898PrePipeline + Boeing_898RecPipeline)


#Boeing_898GMeanPipelineNoRev = np.sqrt(Boeing_898PrePipelineNoRev * Boeing_898RecPipelineNoRev)
#Boeing_898GMeanBaseline = np.sqrt(Boeing_898PreBaseline * Boeing_898RecBaseline)
Boeing_898GMeanBaseline20 = np.sqrt(Boeing_898PreBaseline20 * Boeing_898RecBaseline20)
#Boeing_898GMeanHybrid = np.sqrt(Boeing_898PreHybrid * Boeing_898RecHybrid)
Boeing_898GMeanPipeline = np.sqrt(Boeing_898PrePipeline * Boeing_898RecPipeline)

# beta=0.4
# Boeing_898F0_5PipelineNoRev = (1 + beta**2) * (Boeing_898PrePipelineNoRev * Boeing_898RecPipelineNoRev) / ((beta**2 * Boeing_898PrePipelineNoRev) + Boeing_898RecPipelineNoRev)
# #Boeing_898F0_5Baseline = (1 + beta**2) * (Boeing_898PreBaseline * Boeing_898RecBaseline) / ((beta**2 * Boeing_898PreBaseline) + Boeing_898RecBaseline)
# Boeing_898F0_5Baseline20 = (1 + beta**2) * (Boeing_898PreBaseline20 * Boeing_898RecBaseline20) / ((beta**2 * Boeing_898PreBaseline20) + Boeing_898RecBaseline20)
# Boeing_898F0_5Hybrid = (1 + beta**2) * (Boeing_898PreHybrid * Boeing_898RecHybrid) / ((beta**2 * Boeing_898PreHybrid) + Boeing_898RecHybrid)
# Boeing_898F0_5PipelineNoRevNoRev = (1 + beta**2) * (Boeing_898PrePipelineNoRevNoRev * Boeing_898RecPipelineNoRevNoRev) / ((beta**2 * Boeing_898PrePipelineNoRevNoRev) + Boeing_898RecPipelineNoRevNoRev)


r1 = np.arange(10)

fig, axs = plt.subplots(5, 1, figsize=(5,9), sharey=True)
fig.subplots_adjust(hspace=0.1, wspace=0.05)

axs[0].plot(r1, Boeing_898PrePipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[0].plot(r1, Boeing_898PreBaseline,marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[0].plot(r1, Boeing_898PreBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
# axs[0].plot(r1, Boeing_898PrePipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
# axs[0].plot(r1, Boeing_898PreHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")


axs[1].plot(r1, Boeing_898RecPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[1].plot(r1, Boeing_898RecBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[1].plot(r1, Boeing_898RecBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
# axs[1].plot(r1, Boeing_898RecPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
# axs[1].plot(r1, Boeing_898RecHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")





axs[2].plot(r1, Boeing_898F1Pipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[2].plot(r1, Boeing_898F1Baseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[2].plot(r1, Boeing_898F1Baseline20, marker="2", markersize=10, color="#00748f", zorder=2)
# axs[2].plot(r1, Boeing_898F1PipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
# axs[2].plot(r1, Boeing_898F1Hybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[3].plot(r1, Boeing_898GMeanPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[3].plot(r1, Boeing_898GMeanBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[3].plot(r1, Boeing_898GMeanBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
# axs[3].plot(r1, Boeing_898GMeanPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
# axs[3].plot(r1, Boeing_898GMeanHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[4].plot(r1, Boeing_898RMSEPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[4].plot(r1, Boeing_898RMSEBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[4].plot(r1, Boeing_898RMSEBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
# axs[4].plot(r1, Boeing_898RMSEPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
# axs[4].plot(r1, Boeing_898RMSEHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[0].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[0].set_ylabel('Precision', rotation='vertical')
axs[0].set_title('Boeing_898', fontsize=12)

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
legend_artist2 = plt.Line2D([0], [0], color='#00C3CC', linestyle='-', label='Baseline', marker="+", markersize=10)
legend_artist3 = plt.Line2D([0], [0], color='#FFA600', linestyle='-', label='PipelineNoRev', marker="o")
legend_artist4 = plt.Line2D([0], [0], color='#61a44f', linestyle='dashdot', label='Hybrid', marker="2", markersize=10)
legend_artist5 = plt.Line2D([0], [0], color='#00748f', linestyle='-', label='Baseline20', marker="2", markersize=12)

# Add the legend artists to the figure
legend = fig.legend(handles=[legend_artist1, legend_artist2, legend_artist3, legend_artist4, legend_artist5], loc='upper center', ncol=5, bbox_to_anchor=(0.5, 0.95), shadow=True)

plt.savefig("Boeing_898.pdf", bbox_inches='tight')
plt.show()
