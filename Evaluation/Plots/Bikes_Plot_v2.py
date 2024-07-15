import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

df=pd.read_csv("../ALL_Results_v2.csv", sep=';')

df_bikes_4100_=df.loc[df['dataset'] == 'bikes_4100' ]


df_bikes_4100_Pipeline=df_bikes_4100_.loc[df_bikes_4100_['algoritmo'] == 'Pipeline' ]
df_bikes_4100_Baseline=df_bikes_4100_.loc[df_bikes_4100_['algoritmo'] == 'Baseline' ]
df_bikes_4100_Baseline20=df_bikes_4100_.loc[df_bikes_4100_['algoritmo'] == 'Baseline20' ]
df_bikes_4100_PipelineNoRev=df_bikes_4100_.loc[df_bikes_4100_['algoritmo'] == 'Pipeline_noRev' ]
df_bikes_4100_Hybrid=df_bikes_4100_.loc[df_bikes_4100_['algoritmo'] == 'Hybrid' ]



df_bikes_4100_PipelineV1=df_bikes_4100_Pipeline.loc[df_bikes_4100_Pipeline['version'] == 1 ]
df_bikes_4100_PipelineV2=df_bikes_4100_Pipeline.loc[df_bikes_4100_Pipeline['version'] == 2 ]
df_bikes_4100_PipelineV3=df_bikes_4100_Pipeline.loc[df_bikes_4100_Pipeline['version'] == 3 ]
df_bikes_4100_PipelineV4=df_bikes_4100_Pipeline.loc[df_bikes_4100_Pipeline['version'] == 4 ]
df_bikes_4100_PipelineV5=df_bikes_4100_Pipeline.loc[df_bikes_4100_Pipeline['version'] == 5 ]

df_bikes_4100_BaselineV1=df_bikes_4100_Baseline.loc[df_bikes_4100_Baseline['version'] == 1 ]
df_bikes_4100_BaselineV2=df_bikes_4100_Baseline.loc[df_bikes_4100_Baseline['version'] == 2 ]
df_bikes_4100_BaselineV3=df_bikes_4100_Baseline.loc[df_bikes_4100_Baseline['version'] == 3 ]
df_bikes_4100_BaselineV4=df_bikes_4100_Baseline.loc[df_bikes_4100_Baseline['version'] == 4 ]
df_bikes_4100_BaselineV5=df_bikes_4100_Baseline.loc[df_bikes_4100_Baseline['version'] == 5 ]

df_bikes_4100_Baseline20V1=df_bikes_4100_Baseline20.loc[df_bikes_4100_Baseline20['version'] == 1 ]
df_bikes_4100_Baseline20V2=df_bikes_4100_Baseline20.loc[df_bikes_4100_Baseline20['version'] == 2 ]
df_bikes_4100_Baseline20V3=df_bikes_4100_Baseline20.loc[df_bikes_4100_Baseline20['version'] == 3 ]
df_bikes_4100_Baseline20V4=df_bikes_4100_Baseline20.loc[df_bikes_4100_Baseline20['version'] == 4 ]
df_bikes_4100_Baseline20V5=df_bikes_4100_Baseline20.loc[df_bikes_4100_Baseline20['version'] == 5 ]

df_bikes_4100_PipelineNoRevV1=df_bikes_4100_PipelineNoRev.loc[df_bikes_4100_PipelineNoRev['version'] == 1 ]
df_bikes_4100_PipelineNoRevV2=df_bikes_4100_PipelineNoRev.loc[df_bikes_4100_PipelineNoRev['version'] == 2 ]
df_bikes_4100_PipelineNoRevV3=df_bikes_4100_PipelineNoRev.loc[df_bikes_4100_PipelineNoRev['version'] == 3 ]
df_bikes_4100_PipelineNoRevV4=df_bikes_4100_PipelineNoRev.loc[df_bikes_4100_PipelineNoRev['version'] == 4 ]
df_bikes_4100_PipelineNoRevV5=df_bikes_4100_PipelineNoRev.loc[df_bikes_4100_PipelineNoRev['version'] == 5 ]

df_bikes_4100_HybridV1=df_bikes_4100_Hybrid.loc[df_bikes_4100_Hybrid['version'] == 1 ]
df_bikes_4100_HybridV2=df_bikes_4100_Hybrid.loc[df_bikes_4100_Hybrid['version'] == 2 ]
df_bikes_4100_HybridV3=df_bikes_4100_Hybrid.loc[df_bikes_4100_Hybrid['version'] == 3 ]
df_bikes_4100_HybridV4=df_bikes_4100_Hybrid.loc[df_bikes_4100_Hybrid['version'] == 4 ]
df_bikes_4100_HybridV5=df_bikes_4100_Hybrid.loc[df_bikes_4100_Hybrid['version'] == 5 ]

bikes_4100RecPipelineNoRevV1=df_bikes_4100_PipelineNoRevV1['recall'].to_numpy().astype(float)
bikes_4100RecPipelineNoRevV2=df_bikes_4100_PipelineNoRevV2['recall'].to_numpy().astype(float)
bikes_4100RecPipelineNoRevV3=df_bikes_4100_PipelineNoRevV3['recall'].to_numpy().astype(float)
bikes_4100RecPipelineNoRevV4=df_bikes_4100_PipelineNoRevV4['recall'].to_numpy().astype(float)
bikes_4100RecPipelineNoRevV5=df_bikes_4100_PipelineNoRevV5['recall'].to_numpy().astype(float)
bikes_4100PrePipelineNoRevV1=df_bikes_4100_PipelineNoRevV1['precision'].to_numpy().astype(float)
bikes_4100PrePipelineNoRevV2=df_bikes_4100_PipelineNoRevV2['precision'].to_numpy().astype(float)
bikes_4100PrePipelineNoRevV3=df_bikes_4100_PipelineNoRevV3['precision'].to_numpy().astype(float)
bikes_4100PrePipelineNoRevV4=df_bikes_4100_PipelineNoRevV4['precision'].to_numpy().astype(float)
bikes_4100PrePipelineNoRevV5=df_bikes_4100_PipelineNoRevV5['precision'].to_numpy().astype(float)
bikes_4100RMSEPipelineNoRevV1=df_bikes_4100_PipelineNoRevV1['rmse'].to_numpy().astype(float)
bikes_4100RMSEPipelineNoRevV2=df_bikes_4100_PipelineNoRevV2['rmse'].to_numpy().astype(float)
bikes_4100RMSEPipelineNoRevV3=df_bikes_4100_PipelineNoRevV3['rmse'].to_numpy().astype(float)
bikes_4100RMSEPipelineNoRevV4=df_bikes_4100_PipelineNoRevV4['rmse'].to_numpy().astype(float)
bikes_4100RMSEPipelineNoRevV5=df_bikes_4100_PipelineNoRevV5['rmse'].to_numpy().astype(float)



bikes_4100RecPipelineV1=df_bikes_4100_PipelineV1['recall'].to_numpy().astype(float)
bikes_4100RecPipelineV2=df_bikes_4100_PipelineV2['recall'].to_numpy().astype(float)
bikes_4100RecPipelineV3=df_bikes_4100_PipelineV3['recall'].to_numpy().astype(float)
bikes_4100RecPipelineV4=df_bikes_4100_PipelineV4['recall'].to_numpy().astype(float)
bikes_4100RecPipelineV5=df_bikes_4100_PipelineV5['recall'].to_numpy().astype(float)
bikes_4100PrePipelineV1=df_bikes_4100_PipelineV1['precision'].to_numpy().astype(float)
bikes_4100PrePipelineV2=df_bikes_4100_PipelineV2['precision'].to_numpy().astype(float)
bikes_4100PrePipelineV3=df_bikes_4100_PipelineV3['precision'].to_numpy().astype(float)
bikes_4100PrePipelineV4=df_bikes_4100_PipelineV4['precision'].to_numpy().astype(float)
bikes_4100PrePipelineV5=df_bikes_4100_PipelineV5['precision'].to_numpy().astype(float)
bikes_4100RMSEPipelineV1=df_bikes_4100_PipelineV1['rmse'].to_numpy().astype(float)
bikes_4100RMSEPipelineV2=df_bikes_4100_PipelineV2['rmse'].to_numpy().astype(float)
bikes_4100RMSEPipelineV3=df_bikes_4100_PipelineV3['rmse'].to_numpy().astype(float)
bikes_4100RMSEPipelineV4=df_bikes_4100_PipelineV4['rmse'].to_numpy().astype(float)
bikes_4100RMSEPipelineV5=df_bikes_4100_PipelineV5['rmse'].to_numpy().astype(float)


bikes_4100RecBaselineV1=df_bikes_4100_BaselineV1['recall'].to_numpy().astype(float)
bikes_4100RecBaselineV2=df_bikes_4100_BaselineV2['recall'].to_numpy().astype(float)
bikes_4100RecBaselineV3=df_bikes_4100_BaselineV3['recall'].to_numpy().astype(float)
bikes_4100RecBaselineV4=df_bikes_4100_BaselineV4['recall'].to_numpy().astype(float)
bikes_4100RecBaselineV5=df_bikes_4100_BaselineV5['recall'].to_numpy().astype(float)
bikes_4100PreBaselineV1=df_bikes_4100_BaselineV1['precision'].to_numpy().astype(float)
bikes_4100PreBaselineV2=df_bikes_4100_BaselineV2['precision'].to_numpy().astype(float)
bikes_4100PreBaselineV3=df_bikes_4100_BaselineV3['precision'].to_numpy().astype(float)
bikes_4100PreBaselineV4=df_bikes_4100_BaselineV4['precision'].to_numpy().astype(float)
bikes_4100PreBaselineV5=df_bikes_4100_BaselineV5['precision'].to_numpy().astype(float)
bikes_4100RMSEBaselineV1=df_bikes_4100_BaselineV1['rmse'].to_numpy().astype(float)
bikes_4100RMSEBaselineV2=df_bikes_4100_BaselineV2['rmse'].to_numpy().astype(float)
bikes_4100RMSEBaselineV3=df_bikes_4100_BaselineV3['rmse'].to_numpy().astype(float)
bikes_4100RMSEBaselineV4=df_bikes_4100_BaselineV4['rmse'].to_numpy().astype(float)
bikes_4100RMSEBaselineV5=df_bikes_4100_BaselineV5['rmse'].to_numpy().astype(float)

bikes_4100RecBaseline20V1=df_bikes_4100_Baseline20V1['recall'].to_numpy().astype(float)
bikes_4100RecBaseline20V2=df_bikes_4100_Baseline20V2['recall'].to_numpy().astype(float)
bikes_4100RecBaseline20V3=df_bikes_4100_Baseline20V3['recall'].to_numpy().astype(float)
bikes_4100RecBaseline20V4=df_bikes_4100_Baseline20V4['recall'].to_numpy().astype(float)
bikes_4100RecBaseline20V5=df_bikes_4100_Baseline20V5['recall'].to_numpy().astype(float)
bikes_4100PreBaseline20V1=df_bikes_4100_Baseline20V1['precision'].to_numpy().astype(float)
bikes_4100PreBaseline20V2=df_bikes_4100_Baseline20V2['precision'].to_numpy().astype(float)
bikes_4100PreBaseline20V3=df_bikes_4100_Baseline20V3['precision'].to_numpy().astype(float)
bikes_4100PreBaseline20V4=df_bikes_4100_Baseline20V4['precision'].to_numpy().astype(float)
bikes_4100PreBaseline20V5=df_bikes_4100_Baseline20V5['precision'].to_numpy().astype(float)
bikes_4100RMSEBaseline20V1=df_bikes_4100_Baseline20V1['rmse'].to_numpy().astype(float)
bikes_4100RMSEBaseline20V2=df_bikes_4100_Baseline20V2['rmse'].to_numpy().astype(float)
bikes_4100RMSEBaseline20V3=df_bikes_4100_Baseline20V3['rmse'].to_numpy().astype(float)
bikes_4100RMSEBaseline20V4=df_bikes_4100_Baseline20V4['rmse'].to_numpy().astype(float)
bikes_4100RMSEBaseline20V5=df_bikes_4100_Baseline20V5['rmse'].to_numpy().astype(float)

bikes_4100RecHybridV1=df_bikes_4100_HybridV1['recall'].to_numpy().astype(float)
bikes_4100RecHybridV2=df_bikes_4100_HybridV2['recall'].to_numpy().astype(float)
bikes_4100RecHybridV3=df_bikes_4100_HybridV3['recall'].to_numpy().astype(float)
bikes_4100RecHybridV4=df_bikes_4100_HybridV4['recall'].to_numpy().astype(float)
bikes_4100RecHybridV5=df_bikes_4100_HybridV5['recall'].to_numpy().astype(float)
bikes_4100PreHybridV1=df_bikes_4100_HybridV1['precision'].to_numpy().astype(float)
bikes_4100PreHybridV2=df_bikes_4100_HybridV2['precision'].to_numpy().astype(float)
bikes_4100PreHybridV3=df_bikes_4100_HybridV3['precision'].to_numpy().astype(float)
bikes_4100PreHybridV4=df_bikes_4100_HybridV4['precision'].to_numpy().astype(float)
bikes_4100PreHybridV5=df_bikes_4100_HybridV5['precision'].to_numpy().astype(float)
bikes_4100RMSEHybridV1=df_bikes_4100_HybridV1['rmse'].to_numpy().astype(float)
bikes_4100RMSEHybridV2=df_bikes_4100_HybridV2['rmse'].to_numpy().astype(float)
bikes_4100RMSEHybridV3=df_bikes_4100_HybridV3['rmse'].to_numpy().astype(float)
bikes_4100RMSEHybridV4=df_bikes_4100_HybridV4['rmse'].to_numpy().astype(float)
bikes_4100RMSEHybridV5=df_bikes_4100_HybridV5['rmse'].to_numpy().astype(float)

arrays = [bikes_4100RecPipelineNoRevV1, bikes_4100RecPipelineNoRevV2, bikes_4100RecPipelineNoRevV3, bikes_4100RecPipelineNoRevV4, bikes_4100RecPipelineNoRevV5]
bikes_4100RecPipelineNoRev = np.mean(arrays, axis=0)
arrays = [bikes_4100PrePipelineNoRevV1, bikes_4100PrePipelineNoRevV2, bikes_4100PrePipelineNoRevV3, bikes_4100PrePipelineNoRevV4, bikes_4100PrePipelineNoRevV5]
bikes_4100PrePipelineNoRev = np.mean(arrays, axis=0)
arrays = [bikes_4100RMSEPipelineNoRevV1, bikes_4100RMSEPipelineNoRevV2, bikes_4100RMSEPipelineNoRevV3, bikes_4100RMSEPipelineNoRevV4, bikes_4100RMSEPipelineNoRevV5]
bikes_4100RMSEPipelineNoRev = np.mean(arrays, axis=0)

arrays = [bikes_4100RecBaselineV1, bikes_4100RecBaselineV2, bikes_4100RecBaselineV3, bikes_4100RecBaselineV4, bikes_4100RecBaselineV5]
bikes_4100RecBaseline = np.mean(arrays, axis=0)
arrays = [bikes_4100PreBaselineV1, bikes_4100PreBaselineV2, bikes_4100PreBaselineV3, bikes_4100PreBaselineV4, bikes_4100PreBaselineV5]
bikes_4100PreBaseline = np.mean(arrays, axis=0)
arrays = [bikes_4100RMSEBaselineV1, bikes_4100RMSEBaselineV2, bikes_4100RMSEBaselineV3, bikes_4100RMSEBaselineV4, bikes_4100RMSEBaselineV5]
bikes_4100RMSEBaseline = np.mean(arrays, axis=0)

arrays = [bikes_4100RecBaseline20V1, bikes_4100RecBaseline20V2, bikes_4100RecBaseline20V3, bikes_4100RecBaseline20V4, bikes_4100RecBaseline20V5]
bikes_4100RecBaseline20 = np.mean(arrays, axis=0)
arrays = [bikes_4100PreBaseline20V1, bikes_4100PreBaseline20V2, bikes_4100PreBaseline20V3, bikes_4100PreBaseline20V4, bikes_4100PreBaseline20V5]
bikes_4100PreBaseline20 = np.mean(arrays, axis=0)
arrays = [bikes_4100RMSEBaseline20V1, bikes_4100RMSEBaseline20V2, bikes_4100RMSEBaseline20V3, bikes_4100RMSEBaseline20V4, bikes_4100RMSEBaseline20V5]
bikes_4100RMSEBaseline20 = np.mean(arrays, axis=0)

arrays = [bikes_4100RecHybridV1, bikes_4100RecHybridV2, bikes_4100RecHybridV3, bikes_4100RecHybridV4, bikes_4100RecHybridV5]
bikes_4100RecHybrid = np.mean(arrays, axis=0)
arrays = [bikes_4100PreHybridV1, bikes_4100PreHybridV2, bikes_4100PreHybridV3, bikes_4100PreHybridV4, bikes_4100PreHybridV5]
bikes_4100PreHybrid = np.mean(arrays, axis=0)
arrays = [bikes_4100RMSEHybridV1, bikes_4100RMSEHybridV2, bikes_4100RMSEHybridV3, bikes_4100RMSEHybridV4, bikes_4100RMSEHybridV5]
bikes_4100RMSEHybrid = np.mean(arrays, axis=0)

arrays = [bikes_4100RecPipelineV1, bikes_4100RecPipelineV2, bikes_4100RecPipelineV3, bikes_4100RecPipelineV4, bikes_4100RecPipelineV5]
bikes_4100RecPipeline = np.mean(arrays, axis=0)
arrays = [bikes_4100PrePipelineV1, bikes_4100PrePipelineV2, bikes_4100PrePipelineV3, bikes_4100PrePipelineV4, bikes_4100PrePipelineV5]
bikes_4100PrePipeline = np.mean(arrays, axis=0)
arrays = [bikes_4100RMSEPipelineV1, bikes_4100RMSEPipelineV2, bikes_4100RMSEPipelineV3, bikes_4100RMSEPipelineV4, bikes_4100RMSEPipelineV5]
bikes_4100RMSEPipeline = np.mean(arrays, axis=0)


bikes_4100F1PipelineNoRev = 2 * (bikes_4100PrePipelineNoRev * bikes_4100RecPipelineNoRev) / (bikes_4100PrePipelineNoRev + bikes_4100RecPipelineNoRev)
bikes_4100F1Baseline = 2 * (bikes_4100PreBaseline * bikes_4100RecBaseline) / (bikes_4100PreBaseline + bikes_4100RecBaseline)
bikes_4100F1Baseline20 = 2 * (bikes_4100PreBaseline20 * bikes_4100RecBaseline20) / (bikes_4100PreBaseline20 + bikes_4100RecBaseline20)
bikes_4100F1Hybrid = 2 * (bikes_4100PreHybrid * bikes_4100RecHybrid) / (bikes_4100PreHybrid + bikes_4100RecHybrid)
bikes_4100F1Pipeline = 2 * (bikes_4100PrePipeline * bikes_4100RecPipeline) / (bikes_4100PrePipeline + bikes_4100RecPipeline)


bikes_4100GMeanPipelineNoRev = np.sqrt(bikes_4100PrePipelineNoRev * bikes_4100RecPipelineNoRev)
#bikes_4100GMeanBaseline = np.sqrt(bikes_4100PreBaseline * bikes_4100RecBaseline)
bikes_4100GMeanBaseline20 = np.sqrt(bikes_4100PreBaseline20 * bikes_4100RecBaseline20)
bikes_4100GMeanHybrid = np.sqrt(bikes_4100PreHybrid * bikes_4100RecHybrid)
bikes_4100GMeanPipeline = np.sqrt(bikes_4100PrePipeline * bikes_4100RecPipeline)

# beta=0.4
# bikes_4100F0_5PipelineNoRev = (1 + beta**2) * (bikes_4100PrePipelineNoRev * bikes_4100RecPipelineNoRev) / ((beta**2 * bikes_4100PrePipelineNoRev) + bikes_4100RecPipelineNoRev)
# #bikes_4100F0_5Baseline = (1 + beta**2) * (bikes_4100PreBaseline * bikes_4100RecBaseline) / ((beta**2 * bikes_4100PreBaseline) + bikes_4100RecBaseline)
# bikes_4100F0_5Baseline20 = (1 + beta**2) * (bikes_4100PreBaseline20 * bikes_4100RecBaseline20) / ((beta**2 * bikes_4100PreBaseline20) + bikes_4100RecBaseline20)
# bikes_4100F0_5Hybrid = (1 + beta**2) * (bikes_4100PreHybrid * bikes_4100RecHybrid) / ((beta**2 * bikes_4100PreHybrid) + bikes_4100RecHybrid)
# bikes_4100F0_5PipelineNoRevNoRev = (1 + beta**2) * (bikes_4100PrePipelineNoRevNoRev * bikes_4100RecPipelineNoRevNoRev) / ((beta**2 * bikes_4100PrePipelineNoRevNoRev) + bikes_4100RecPipelineNoRevNoRev)


r1 = np.arange(10)

fig, axs = plt.subplots(5, 1, figsize=(5,9), sharey=True)
fig.subplots_adjust(hspace=0.1, wspace=0.05)

axs[0].plot(r1, bikes_4100PrePipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[0].plot(r1, bikes_4100PreBaseline,marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[0].plot(r1, bikes_4100PreBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[0].plot(r1, bikes_4100PrePipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[0].plot(r1, bikes_4100PreHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")


axs[1].plot(r1, bikes_4100RecPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[1].plot(r1, bikes_4100RecBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[1].plot(r1, bikes_4100RecBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[1].plot(r1, bikes_4100RecPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[1].plot(r1, bikes_4100RecHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")





axs[2].plot(r1, bikes_4100F1Pipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[2].plot(r1, bikes_4100F1Baseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[2].plot(r1, bikes_4100F1Baseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[2].plot(r1, bikes_4100F1PipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[2].plot(r1, bikes_4100F1Hybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[3].plot(r1, bikes_4100GMeanPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[3].plot(r1, bikes_4100GMeanBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[3].plot(r1, bikes_4100GMeanBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[3].plot(r1, bikes_4100GMeanPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[3].plot(r1, bikes_4100GMeanHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[4].plot(r1, bikes_4100RMSEPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[4].plot(r1, bikes_4100RMSEBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[4].plot(r1, bikes_4100RMSEBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[4].plot(r1, bikes_4100RMSEPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[4].plot(r1, bikes_4100RMSEHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[0].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[0].set_ylabel('Precision', rotation='vertical')
axs[0].set_title('ActorFilms', fontsize=12)

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

plt.savefig("bikes_4100.pdf", bbox_inches='tight')
plt.show()
