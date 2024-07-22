import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

df=pd.read_csv("../ALL_Results_v2.csv", sep=';')

df_NBA_3200_=df.loc[df['dataset'] == 'NBA_3200' ]


df_NBA_3200_Pipeline=df_NBA_3200_.loc[df_NBA_3200_['algoritmo'] == 'Pipeline' ]
#df_NBA_3200_Baseline=df_NBA_3200_.loc[df_NBA_3200_['algoritmo'] == 'Baseline' ]
df_NBA_3200_Baseline20=df_NBA_3200_.loc[df_NBA_3200_['algoritmo'] == 'Baseline20' ]
df_NBA_3200_PipelineNoRev=df_NBA_3200_.loc[df_NBA_3200_['algoritmo'] == 'Pipeline_noRev' ]
df_NBA_3200_Hybrid=df_NBA_3200_.loc[df_NBA_3200_['algoritmo'] == 'Hybrid' ]


df_NBA_3200_PipelineV1=df_NBA_3200_Pipeline.loc[df_NBA_3200_Pipeline['version'] == 1 ]
df_NBA_3200_PipelineV2=df_NBA_3200_Pipeline.loc[df_NBA_3200_Pipeline['version'] == 2 ]
df_NBA_3200_PipelineV3=df_NBA_3200_Pipeline.loc[df_NBA_3200_Pipeline['version'] == 3 ]
df_NBA_3200_PipelineV4=df_NBA_3200_Pipeline.loc[df_NBA_3200_Pipeline['version'] == 4 ]
df_NBA_3200_PipelineV5=df_NBA_3200_Pipeline.loc[df_NBA_3200_Pipeline['version'] == 5 ]

# df_NBA_3200_BaselineV1=df_NBA_3200_Baseline.loc[df_NBA_3200_Baseline['version'] == 1 ]
# df_NBA_3200_BaselineV2=df_NBA_3200_Baseline.loc[df_NBA_3200_Baseline['version'] == 2 ]
# df_NBA_3200_BaselineV3=df_NBA_3200_Baseline.loc[df_NBA_3200_Baseline['version'] == 3 ]
# df_NBA_3200_BaselineV4=df_NBA_3200_Baseline.loc[df_NBA_3200_Baseline['version'] == 4 ]
# df_NBA_3200_BaselineV5=df_NBA_3200_Baseline.loc[df_NBA_3200_Baseline['version'] == 5 ]

df_NBA_3200_Baseline20V1=df_NBA_3200_Baseline20.loc[df_NBA_3200_Baseline20['version'] == 1 ]
df_NBA_3200_Baseline20V2=df_NBA_3200_Baseline20.loc[df_NBA_3200_Baseline20['version'] == 2 ]
df_NBA_3200_Baseline20V3=df_NBA_3200_Baseline20.loc[df_NBA_3200_Baseline20['version'] == 3 ]
df_NBA_3200_Baseline20V4=df_NBA_3200_Baseline20.loc[df_NBA_3200_Baseline20['version'] == 4 ]
df_NBA_3200_Baseline20V5=df_NBA_3200_Baseline20.loc[df_NBA_3200_Baseline20['version'] == 5 ]

df_NBA_3200_PipelineNoRevV1=df_NBA_3200_PipelineNoRev.loc[df_NBA_3200_PipelineNoRev['version'] == 1 ]
df_NBA_3200_PipelineNoRevV2=df_NBA_3200_PipelineNoRev.loc[df_NBA_3200_PipelineNoRev['version'] == 2 ]
df_NBA_3200_PipelineNoRevV3=df_NBA_3200_PipelineNoRev.loc[df_NBA_3200_PipelineNoRev['version'] == 3 ]
df_NBA_3200_PipelineNoRevV4=df_NBA_3200_PipelineNoRev.loc[df_NBA_3200_PipelineNoRev['version'] == 4 ]
df_NBA_3200_PipelineNoRevV5=df_NBA_3200_PipelineNoRev.loc[df_NBA_3200_PipelineNoRev['version'] == 5 ]

df_NBA_3200_HybridV1=df_NBA_3200_Hybrid.loc[df_NBA_3200_Hybrid['version'] == 1 ]
df_NBA_3200_HybridV2=df_NBA_3200_Hybrid.loc[df_NBA_3200_Hybrid['version'] == 2 ]
df_NBA_3200_HybridV3=df_NBA_3200_Hybrid.loc[df_NBA_3200_Hybrid['version'] == 3 ]
df_NBA_3200_HybridV4=df_NBA_3200_Hybrid.loc[df_NBA_3200_Hybrid['version'] == 4 ]
df_NBA_3200_HybridV5=df_NBA_3200_Hybrid.loc[df_NBA_3200_Hybrid['version'] == 5 ]

NBA_3200RecPipelineNoRevV1=df_NBA_3200_PipelineNoRevV1['recall'].to_numpy().astype(float)
NBA_3200RecPipelineNoRevV2=df_NBA_3200_PipelineNoRevV2['recall'].to_numpy().astype(float)
NBA_3200RecPipelineNoRevV3=df_NBA_3200_PipelineNoRevV3['recall'].to_numpy().astype(float)
NBA_3200RecPipelineNoRevV4=df_NBA_3200_PipelineNoRevV4['recall'].to_numpy().astype(float)
NBA_3200RecPipelineNoRevV5=df_NBA_3200_PipelineNoRevV5['recall'].to_numpy().astype(float)
NBA_3200PrePipelineNoRevV1=df_NBA_3200_PipelineNoRevV1['precision'].to_numpy().astype(float)
NBA_3200PrePipelineNoRevV2=df_NBA_3200_PipelineNoRevV2['precision'].to_numpy().astype(float)
NBA_3200PrePipelineNoRevV3=df_NBA_3200_PipelineNoRevV3['precision'].to_numpy().astype(float)
NBA_3200PrePipelineNoRevV4=df_NBA_3200_PipelineNoRevV4['precision'].to_numpy().astype(float)
NBA_3200PrePipelineNoRevV5=df_NBA_3200_PipelineNoRevV5['precision'].to_numpy().astype(float)
NBA_3200RMSEPipelineNoRevV1=df_NBA_3200_PipelineNoRevV1['rmse'].to_numpy().astype(float)
NBA_3200RMSEPipelineNoRevV2=df_NBA_3200_PipelineNoRevV2['rmse'].to_numpy().astype(float)
NBA_3200RMSEPipelineNoRevV3=df_NBA_3200_PipelineNoRevV3['rmse'].to_numpy().astype(float)
NBA_3200RMSEPipelineNoRevV4=df_NBA_3200_PipelineNoRevV4['rmse'].to_numpy().astype(float)
NBA_3200RMSEPipelineNoRevV5=df_NBA_3200_PipelineNoRevV5['rmse'].to_numpy().astype(float)



NBA_3200RecPipelineV1=df_NBA_3200_PipelineV1['recall'].to_numpy().astype(float)
NBA_3200RecPipelineV2=df_NBA_3200_PipelineV2['recall'].to_numpy().astype(float)
NBA_3200RecPipelineV3=df_NBA_3200_PipelineV3['recall'].to_numpy().astype(float)
NBA_3200RecPipelineV4=df_NBA_3200_PipelineV4['recall'].to_numpy().astype(float)
NBA_3200RecPipelineV5=df_NBA_3200_PipelineV5['recall'].to_numpy().astype(float)
NBA_3200PrePipelineV1=df_NBA_3200_PipelineV1['precision'].to_numpy().astype(float)
NBA_3200PrePipelineV2=df_NBA_3200_PipelineV2['precision'].to_numpy().astype(float)
NBA_3200PrePipelineV3=df_NBA_3200_PipelineV3['precision'].to_numpy().astype(float)
NBA_3200PrePipelineV4=df_NBA_3200_PipelineV4['precision'].to_numpy().astype(float)
NBA_3200PrePipelineV5=df_NBA_3200_PipelineV5['precision'].to_numpy().astype(float)
NBA_3200RMSEPipelineV1=df_NBA_3200_PipelineV1['rmse'].to_numpy().astype(float)
NBA_3200RMSEPipelineV2=df_NBA_3200_PipelineV2['rmse'].to_numpy().astype(float)
NBA_3200RMSEPipelineV3=df_NBA_3200_PipelineV3['rmse'].to_numpy().astype(float)
NBA_3200RMSEPipelineV4=df_NBA_3200_PipelineV4['rmse'].to_numpy().astype(float)
NBA_3200RMSEPipelineV5=df_NBA_3200_PipelineV5['rmse'].to_numpy().astype(float)

#
# NBA_3200RecBaselineV1=df_NBA_3200_BaselineV1['recall'].to_numpy().astype(float)
# NBA_3200RecBaselineV2=df_NBA_3200_BaselineV2['recall'].to_numpy().astype(float)
# NBA_3200RecBaselineV3=df_NBA_3200_BaselineV3['recall'].to_numpy().astype(float)
# NBA_3200RecBaselineV4=df_NBA_3200_BaselineV4['recall'].to_numpy().astype(float)
# NBA_3200RecBaselineV5=df_NBA_3200_BaselineV5['recall'].to_numpy().astype(float)
# NBA_3200PreBaselineV1=df_NBA_3200_BaselineV1['precision'].to_numpy().astype(float)
# NBA_3200PreBaselineV2=df_NBA_3200_BaselineV2['precision'].to_numpy().astype(float)
# NBA_3200PreBaselineV3=df_NBA_3200_BaselineV3['precision'].to_numpy().astype(float)
# NBA_3200PreBaselineV4=df_NBA_3200_BaselineV4['precision'].to_numpy().astype(float)
# NBA_3200PreBaselineV5=df_NBA_3200_BaselineV5['precision'].to_numpy().astype(float)
# NBA_3200RMSEBaselineV1=df_NBA_3200_BaselineV1['rmse'].to_numpy().astype(float)
# NBA_3200RMSEBaselineV2=df_NBA_3200_BaselineV2['rmse'].to_numpy().astype(float)
# NBA_3200RMSEBaselineV3=df_NBA_3200_BaselineV3['rmse'].to_numpy().astype(float)
# NBA_3200RMSEBaselineV4=df_NBA_3200_BaselineV4['rmse'].to_numpy().astype(float)
# NBA_3200RMSEBaselineV5=df_NBA_3200_BaselineV5['rmse'].to_numpy().astype(float)

NBA_3200RecBaseline20V1=df_NBA_3200_Baseline20V1['recall'].to_numpy().astype(float)
NBA_3200RecBaseline20V2=df_NBA_3200_Baseline20V2['recall'].to_numpy().astype(float)
NBA_3200RecBaseline20V3=df_NBA_3200_Baseline20V3['recall'].to_numpy().astype(float)
NBA_3200RecBaseline20V4=df_NBA_3200_Baseline20V4['recall'].to_numpy().astype(float)
NBA_3200RecBaseline20V5=df_NBA_3200_Baseline20V5['recall'].to_numpy().astype(float)
NBA_3200PreBaseline20V1=df_NBA_3200_Baseline20V1['precision'].to_numpy().astype(float)
NBA_3200PreBaseline20V2=df_NBA_3200_Baseline20V2['precision'].to_numpy().astype(float)
NBA_3200PreBaseline20V3=df_NBA_3200_Baseline20V3['precision'].to_numpy().astype(float)
NBA_3200PreBaseline20V4=df_NBA_3200_Baseline20V4['precision'].to_numpy().astype(float)
NBA_3200PreBaseline20V5=df_NBA_3200_Baseline20V5['precision'].to_numpy().astype(float)
NBA_3200RMSEBaseline20V1=df_NBA_3200_Baseline20V1['rmse'].to_numpy().astype(float)
NBA_3200RMSEBaseline20V2=df_NBA_3200_Baseline20V2['rmse'].to_numpy().astype(float)
NBA_3200RMSEBaseline20V3=df_NBA_3200_Baseline20V3['rmse'].to_numpy().astype(float)
NBA_3200RMSEBaseline20V4=df_NBA_3200_Baseline20V4['rmse'].to_numpy().astype(float)
NBA_3200RMSEBaseline20V5=df_NBA_3200_Baseline20V5['rmse'].to_numpy().astype(float)
#
NBA_3200RecHybridV1=df_NBA_3200_HybridV1['recall'].to_numpy().astype(float)
NBA_3200RecHybridV2=df_NBA_3200_HybridV2['recall'].to_numpy().astype(float)
NBA_3200RecHybridV3=df_NBA_3200_HybridV3['recall'].to_numpy().astype(float)
NBA_3200RecHybridV4=df_NBA_3200_HybridV4['recall'].to_numpy().astype(float)
NBA_3200RecHybridV5=df_NBA_3200_HybridV5['recall'].to_numpy().astype(float)
NBA_3200PreHybridV1=df_NBA_3200_HybridV1['precision'].to_numpy().astype(float)
NBA_3200PreHybridV2=df_NBA_3200_HybridV2['precision'].to_numpy().astype(float)
NBA_3200PreHybridV3=df_NBA_3200_HybridV3['precision'].to_numpy().astype(float)
NBA_3200PreHybridV4=df_NBA_3200_HybridV4['precision'].to_numpy().astype(float)
NBA_3200PreHybridV5=df_NBA_3200_HybridV5['precision'].to_numpy().astype(float)
NBA_3200RMSEHybridV1=df_NBA_3200_HybridV1['rmse'].to_numpy().astype(float)
NBA_3200RMSEHybridV2=df_NBA_3200_HybridV2['rmse'].to_numpy().astype(float)
NBA_3200RMSEHybridV3=df_NBA_3200_HybridV3['rmse'].to_numpy().astype(float)
NBA_3200RMSEHybridV4=df_NBA_3200_HybridV4['rmse'].to_numpy().astype(float)
NBA_3200RMSEHybridV5=df_NBA_3200_HybridV5['rmse'].to_numpy().astype(float)

arrays = [NBA_3200RecPipelineNoRevV1, NBA_3200RecPipelineNoRevV2, NBA_3200RecPipelineNoRevV3, NBA_3200RecPipelineNoRevV4, NBA_3200RecPipelineNoRevV5]
NBA_3200RecPipelineNoRev = np.mean(arrays, axis=0)
arrays = [NBA_3200PrePipelineNoRevV1, NBA_3200PrePipelineNoRevV2, NBA_3200PrePipelineNoRevV3, NBA_3200PrePipelineNoRevV4, NBA_3200PrePipelineNoRevV5]
NBA_3200PrePipelineNoRev = np.mean(arrays, axis=0)
arrays = [NBA_3200RMSEPipelineNoRevV1, NBA_3200RMSEPipelineNoRevV2, NBA_3200RMSEPipelineNoRevV3, NBA_3200RMSEPipelineNoRevV4, NBA_3200RMSEPipelineNoRevV5]
NBA_3200RMSEPipelineNoRev = np.mean(arrays, axis=0)
#
# arrays = [NBA_3200RecBaselineV1, NBA_3200RecBaselineV2, NBA_3200RecBaselineV3, NBA_3200RecBaselineV4, NBA_3200RecBaselineV5]
# NBA_3200RecBaseline = np.mean(arrays, axis=0)
# arrays = [NBA_3200PreBaselineV1, NBA_3200PreBaselineV2, NBA_3200PreBaselineV3, NBA_3200PreBaselineV4, NBA_3200PreBaselineV5]
# NBA_3200PreBaseline = np.mean(arrays, axis=0)
# arrays = [NBA_3200RMSEBaselineV1, NBA_3200RMSEBaselineV2, NBA_3200RMSEBaselineV3, NBA_3200RMSEBaselineV4, NBA_3200RMSEBaselineV5]
# NBA_3200RMSEBaseline = np.mean(arrays, axis=0)

arrays = [NBA_3200RecBaseline20V1, NBA_3200RecBaseline20V2, NBA_3200RecBaseline20V3, NBA_3200RecBaseline20V4, NBA_3200RecBaseline20V5]
NBA_3200RecBaseline20 = np.mean(arrays, axis=0)
arrays = [NBA_3200PreBaseline20V1, NBA_3200PreBaseline20V2, NBA_3200PreBaseline20V3, NBA_3200PreBaseline20V4, NBA_3200PreBaseline20V5]
NBA_3200PreBaseline20 = np.mean(arrays, axis=0)
arrays = [NBA_3200RMSEBaseline20V1, NBA_3200RMSEBaseline20V2, NBA_3200RMSEBaseline20V3, NBA_3200RMSEBaseline20V4, NBA_3200RMSEBaseline20V5]
NBA_3200RMSEBaseline20 = np.mean(arrays, axis=0)

arrays = [NBA_3200RecHybridV1, NBA_3200RecHybridV2, NBA_3200RecHybridV3, NBA_3200RecHybridV4, NBA_3200RecHybridV5]
NBA_3200RecHybrid = np.mean(arrays, axis=0)
arrays = [NBA_3200PreHybridV1, NBA_3200PreHybridV2, NBA_3200PreHybridV3, NBA_3200PreHybridV4, NBA_3200PreHybridV5]
NBA_3200PreHybrid = np.mean(arrays, axis=0)
arrays = [NBA_3200RMSEHybridV1, NBA_3200RMSEHybridV2, NBA_3200RMSEHybridV3, NBA_3200RMSEHybridV4, NBA_3200RMSEHybridV5]
NBA_3200RMSEHybrid = np.mean(arrays, axis=0)

arrays = [NBA_3200RecPipelineV1, NBA_3200RecPipelineV2, NBA_3200RecPipelineV3, NBA_3200RecPipelineV4, NBA_3200RecPipelineV5]
NBA_3200RecPipeline = np.mean(arrays, axis=0)
arrays = [NBA_3200PrePipelineV1, NBA_3200PrePipelineV2, NBA_3200PrePipelineV3, NBA_3200PrePipelineV4, NBA_3200PrePipelineV5]
NBA_3200PrePipeline = np.mean(arrays, axis=0)
arrays = [NBA_3200RMSEPipelineV1, NBA_3200RMSEPipelineV2, NBA_3200RMSEPipelineV3, NBA_3200RMSEPipelineV4, NBA_3200RMSEPipelineV5]
NBA_3200RMSEPipeline = np.mean(arrays, axis=0)


NBA_3200F1PipelineNoRev = 2 * (NBA_3200PrePipelineNoRev * NBA_3200RecPipelineNoRev) / (NBA_3200PrePipelineNoRev + NBA_3200RecPipelineNoRev)
# NBA_3200F1Baseline = 2 * (NBA_3200PreBaseline * NBA_3200RecBaseline) / (NBA_3200PreBaseline + NBA_3200RecBaseline)
NBA_3200F1Baseline20 = 2 * (NBA_3200PreBaseline20 * NBA_3200RecBaseline20) / (NBA_3200PreBaseline20 + NBA_3200RecBaseline20)
NBA_3200F1Hybrid = 2 * (NBA_3200PreHybrid * NBA_3200RecHybrid) / (NBA_3200PreHybrid + NBA_3200RecHybrid)
NBA_3200F1Pipeline = 2 * (NBA_3200PrePipeline * NBA_3200RecPipeline) / (NBA_3200PrePipeline + NBA_3200RecPipeline)


NBA_3200GMeanPipelineNoRev = np.sqrt(NBA_3200PrePipelineNoRev * NBA_3200RecPipelineNoRev)
#NBA_3200GMeanBaseline = np.sqrt(NBA_3200PreBaseline * NBA_3200RecBaseline)
NBA_3200GMeanBaseline20 = np.sqrt(NBA_3200PreBaseline20 * NBA_3200RecBaseline20)
NBA_3200GMeanHybrid = np.sqrt(NBA_3200PreHybrid * NBA_3200RecHybrid)
NBA_3200GMeanPipeline = np.sqrt(NBA_3200PrePipeline * NBA_3200RecPipeline)

# beta=0.4
# NBA_3200F0_5PipelineNoRev = (1 + beta**2) * (NBA_3200PrePipelineNoRev * NBA_3200RecPipelineNoRev) / ((beta**2 * NBA_3200PrePipelineNoRev) + NBA_3200RecPipelineNoRev)
# NBA_3200F0_5Baseline = (1 + beta**2) * (NBA_3200PreBaseline * NBA_3200RecBaseline) / ((beta**2 * NBA_3200PreBaseline) + NBA_3200RecBaseline)
# NBA_3200F0_5Baseline20 = (1 + beta**2) * (NBA_3200PreBaseline20 * NBA_3200RecBaseline20) / ((beta**2 * NBA_3200PreBaseline20) + NBA_3200RecBaseline20)
# NBA_3200F0_5Hybrid = (1 + beta**2) * (NBA_3200PreHybrid * NBA_3200RecHybrid) / ((beta**2 * NBA_3200PreHybrid) + NBA_3200RecHybrid)
# NBA_3200F0_5PipelineNoRevNoRev = (1 + beta**2) * (NBA_3200PrePipelineNoRevNoRev * NBA_3200RecPipelineNoRevNoRev) / ((beta**2 * NBA_3200PrePipelineNoRevNoRev) + NBA_3200RecPipelineNoRevNoRev)


r1 = np.arange(10)

fig, axs = plt.subplots(5, 1, figsize=(5,9), sharey=True)
fig.subplots_adjust(hspace=0.1, wspace=0.05)

axs[0].plot(r1, NBA_3200PrePipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[0].plot(r1, NBA_3200PreBaseline,marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[0].plot(r1, NBA_3200PreBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[0].plot(r1, NBA_3200PrePipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[0].plot(r1, NBA_3200PreHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")


axs[1].plot(r1, NBA_3200RecPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[1].plot(r1, NBA_3200RecBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[1].plot(r1, NBA_3200RecBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[1].plot(r1, NBA_3200RecPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[1].plot(r1, NBA_3200RecHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")





axs[2].plot(r1, NBA_3200F1Pipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[2].plot(r1, NBA_3200F1Baseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[2].plot(r1, NBA_3200F1Baseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[2].plot(r1, NBA_3200F1PipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[2].plot(r1, NBA_3200F1Hybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[3].plot(r1, NBA_3200GMeanPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[3].plot(r1, NBA_3200GMeanBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[3].plot(r1, NBA_3200GMeanBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[3].plot(r1, NBA_3200GMeanPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[3].plot(r1, NBA_3200GMeanHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[4].plot(r1, NBA_3200RMSEPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[4].plot(r1, NBA_3200RMSEBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[4].plot(r1, NBA_3200RMSEBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[4].plot(r1, NBA_3200RMSEPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[4].plot(r1, NBA_3200RMSEHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[0].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[0].set_ylabel('Precision', rotation='vertical')
axs[0].set_title('NBA', fontsize=12)

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

plt.savefig("NBA_3200.pdf", bbox_inches='tight')
plt.show()
