import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

df=pd.read_csv("../ALL_Results_v2.csv", sep=';')

df_Boeing_1485_=df.loc[df['dataset'] == 'Boeing_1485' ]


df_Boeing_1485_Pipeline=df_Boeing_1485_.loc[df_Boeing_1485_['algoritmo'] == 'Pipeline' ]
#df_Boeing_1485_Baseline=df_Boeing_1485_.loc[df_Boeing_1485_['algoritmo'] == 'Baseline' ]
df_Boeing_1485_Baseline20=df_Boeing_1485_.loc[df_Boeing_1485_['algoritmo'] == 'Baseline20' ]
#df_Boeing_1485_PipelineNoRev=df_Boeing_1485_.loc[df_Boeing_1485_['algoritmo'] == 'Pipeline_noRev' ]
#df_Boeing_1485_Hybrid=df_Boeing_1485_.loc[df_Boeing_1485_['algoritmo'] == 'Hybrid' ]


df_Boeing_1485_PipelineV1=df_Boeing_1485_Pipeline.loc[df_Boeing_1485_Pipeline['version'] == 1 ]
df_Boeing_1485_PipelineV2=df_Boeing_1485_Pipeline.loc[df_Boeing_1485_Pipeline['version'] == 2 ]
df_Boeing_1485_PipelineV3=df_Boeing_1485_Pipeline.loc[df_Boeing_1485_Pipeline['version'] == 3 ]
df_Boeing_1485_PipelineV4=df_Boeing_1485_Pipeline.loc[df_Boeing_1485_Pipeline['version'] == 4 ]
df_Boeing_1485_PipelineV5=df_Boeing_1485_Pipeline.loc[df_Boeing_1485_Pipeline['version'] == 5 ]

# df_Boeing_1485_BaselineV1=df_Boeing_1485_Baseline.loc[df_Boeing_1485_Baseline['version'] == 1 ]
# df_Boeing_1485_BaselineV2=df_Boeing_1485_Baseline.loc[df_Boeing_1485_Baseline['version'] == 2 ]
# df_Boeing_1485_BaselineV3=df_Boeing_1485_Baseline.loc[df_Boeing_1485_Baseline['version'] == 3 ]
# df_Boeing_1485_BaselineV4=df_Boeing_1485_Baseline.loc[df_Boeing_1485_Baseline['version'] == 4 ]
# df_Boeing_1485_BaselineV5=df_Boeing_1485_Baseline.loc[df_Boeing_1485_Baseline['version'] == 5 ]

df_Boeing_1485_Baseline20V1=df_Boeing_1485_Baseline20.loc[df_Boeing_1485_Baseline20['version'] == 1 ]
df_Boeing_1485_Baseline20V2=df_Boeing_1485_Baseline20.loc[df_Boeing_1485_Baseline20['version'] == 2 ]
df_Boeing_1485_Baseline20V3=df_Boeing_1485_Baseline20.loc[df_Boeing_1485_Baseline20['version'] == 3 ]
df_Boeing_1485_Baseline20V4=df_Boeing_1485_Baseline20.loc[df_Boeing_1485_Baseline20['version'] == 4 ]
df_Boeing_1485_Baseline20V5=df_Boeing_1485_Baseline20.loc[df_Boeing_1485_Baseline20['version'] == 5 ]

# df_Boeing_1485_PipelineNoRevV1=df_Boeing_1485_PipelineNoRev.loc[df_Boeing_1485_PipelineNoRev['version'] == 1 ]
# df_Boeing_1485_PipelineNoRevV2=df_Boeing_1485_PipelineNoRev.loc[df_Boeing_1485_PipelineNoRev['version'] == 2 ]
# df_Boeing_1485_PipelineNoRevV3=df_Boeing_1485_PipelineNoRev.loc[df_Boeing_1485_PipelineNoRev['version'] == 3 ]
# df_Boeing_1485_PipelineNoRevV4=df_Boeing_1485_PipelineNoRev.loc[df_Boeing_1485_PipelineNoRev['version'] == 4 ]
# df_Boeing_1485_PipelineNoRevV5=df_Boeing_1485_PipelineNoRev.loc[df_Boeing_1485_PipelineNoRev['version'] == 5 ]
#
# df_Boeing_1485_HybridV1=df_Boeing_1485_Hybrid.loc[df_Boeing_1485_Hybrid['version'] == 1 ]
# df_Boeing_1485_HybridV2=df_Boeing_1485_Hybrid.loc[df_Boeing_1485_Hybrid['version'] == 2 ]
# df_Boeing_1485_HybridV3=df_Boeing_1485_Hybrid.loc[df_Boeing_1485_Hybrid['version'] == 3 ]
# df_Boeing_1485_HybridV4=df_Boeing_1485_Hybrid.loc[df_Boeing_1485_Hybrid['version'] == 4 ]
# df_Boeing_1485_HybridV5=df_Boeing_1485_Hybrid.loc[df_Boeing_1485_Hybrid['version'] == 5 ]

# Boeing_1485RecPipelineNoRevV1=df_Boeing_1485_PipelineNoRevV1['recall'].to_numpy().astype(float)
# Boeing_1485RecPipelineNoRevV2=df_Boeing_1485_PipelineNoRevV2['recall'].to_numpy().astype(float)
# Boeing_1485RecPipelineNoRevV3=df_Boeing_1485_PipelineNoRevV3['recall'].to_numpy().astype(float)
# Boeing_1485RecPipelineNoRevV4=df_Boeing_1485_PipelineNoRevV4['recall'].to_numpy().astype(float)
# Boeing_1485RecPipelineNoRevV5=df_Boeing_1485_PipelineNoRevV5['recall'].to_numpy().astype(float)
# Boeing_1485PrePipelineNoRevV1=df_Boeing_1485_PipelineNoRevV1['precision'].to_numpy().astype(float)
# Boeing_1485PrePipelineNoRevV2=df_Boeing_1485_PipelineNoRevV2['precision'].to_numpy().astype(float)
# Boeing_1485PrePipelineNoRevV3=df_Boeing_1485_PipelineNoRevV3['precision'].to_numpy().astype(float)
# Boeing_1485PrePipelineNoRevV4=df_Boeing_1485_PipelineNoRevV4['precision'].to_numpy().astype(float)
# Boeing_1485PrePipelineNoRevV5=df_Boeing_1485_PipelineNoRevV5['precision'].to_numpy().astype(float)
# Boeing_1485RMSEPipelineNoRevV1=df_Boeing_1485_PipelineNoRevV1['rmse'].to_numpy().astype(float)
# Boeing_1485RMSEPipelineNoRevV2=df_Boeing_1485_PipelineNoRevV2['rmse'].to_numpy().astype(float)
# Boeing_1485RMSEPipelineNoRevV3=df_Boeing_1485_PipelineNoRevV3['rmse'].to_numpy().astype(float)
# Boeing_1485RMSEPipelineNoRevV4=df_Boeing_1485_PipelineNoRevV4['rmse'].to_numpy().astype(float)
# Boeing_1485RMSEPipelineNoRevV5=df_Boeing_1485_PipelineNoRevV5['rmse'].to_numpy().astype(float)



Boeing_1485RecPipelineV1=df_Boeing_1485_PipelineV1['recall'].to_numpy().astype(float)
Boeing_1485RecPipelineV2=df_Boeing_1485_PipelineV2['recall'].to_numpy().astype(float)
Boeing_1485RecPipelineV3=df_Boeing_1485_PipelineV3['recall'].to_numpy().astype(float)
Boeing_1485RecPipelineV4=df_Boeing_1485_PipelineV4['recall'].to_numpy().astype(float)
Boeing_1485RecPipelineV5=df_Boeing_1485_PipelineV5['recall'].to_numpy().astype(float)
Boeing_1485PrePipelineV1=df_Boeing_1485_PipelineV1['precision'].to_numpy().astype(float)
Boeing_1485PrePipelineV2=df_Boeing_1485_PipelineV2['precision'].to_numpy().astype(float)
Boeing_1485PrePipelineV3=df_Boeing_1485_PipelineV3['precision'].to_numpy().astype(float)
Boeing_1485PrePipelineV4=df_Boeing_1485_PipelineV4['precision'].to_numpy().astype(float)
Boeing_1485PrePipelineV5=df_Boeing_1485_PipelineV5['precision'].to_numpy().astype(float)
Boeing_1485RMSEPipelineV1=df_Boeing_1485_PipelineV1['rmse'].to_numpy().astype(float)
Boeing_1485RMSEPipelineV2=df_Boeing_1485_PipelineV2['rmse'].to_numpy().astype(float)
Boeing_1485RMSEPipelineV3=df_Boeing_1485_PipelineV3['rmse'].to_numpy().astype(float)
Boeing_1485RMSEPipelineV4=df_Boeing_1485_PipelineV4['rmse'].to_numpy().astype(float)
Boeing_1485RMSEPipelineV5=df_Boeing_1485_PipelineV5['rmse'].to_numpy().astype(float)

#
# Boeing_1485RecBaselineV1=df_Boeing_1485_BaselineV1['recall'].to_numpy().astype(float)
# Boeing_1485RecBaselineV2=df_Boeing_1485_BaselineV2['recall'].to_numpy().astype(float)
# Boeing_1485RecBaselineV3=df_Boeing_1485_BaselineV3['recall'].to_numpy().astype(float)
# Boeing_1485RecBaselineV4=df_Boeing_1485_BaselineV4['recall'].to_numpy().astype(float)
# Boeing_1485RecBaselineV5=df_Boeing_1485_BaselineV5['recall'].to_numpy().astype(float)
# Boeing_1485PreBaselineV1=df_Boeing_1485_BaselineV1['precision'].to_numpy().astype(float)
# Boeing_1485PreBaselineV2=df_Boeing_1485_BaselineV2['precision'].to_numpy().astype(float)
# Boeing_1485PreBaselineV3=df_Boeing_1485_BaselineV3['precision'].to_numpy().astype(float)
# Boeing_1485PreBaselineV4=df_Boeing_1485_BaselineV4['precision'].to_numpy().astype(float)
# Boeing_1485PreBaselineV5=df_Boeing_1485_BaselineV5['precision'].to_numpy().astype(float)
# Boeing_1485RMSEBaselineV1=df_Boeing_1485_BaselineV1['rmse'].to_numpy().astype(float)
# Boeing_1485RMSEBaselineV2=df_Boeing_1485_BaselineV2['rmse'].to_numpy().astype(float)
# Boeing_1485RMSEBaselineV3=df_Boeing_1485_BaselineV3['rmse'].to_numpy().astype(float)
# Boeing_1485RMSEBaselineV4=df_Boeing_1485_BaselineV4['rmse'].to_numpy().astype(float)
# Boeing_1485RMSEBaselineV5=df_Boeing_1485_BaselineV5['rmse'].to_numpy().astype(float)

Boeing_1485RecBaseline20V1=df_Boeing_1485_Baseline20V1['recall'].to_numpy().astype(float)
Boeing_1485RecBaseline20V2=df_Boeing_1485_Baseline20V2['recall'].to_numpy().astype(float)
Boeing_1485RecBaseline20V3=df_Boeing_1485_Baseline20V3['recall'].to_numpy().astype(float)
Boeing_1485RecBaseline20V4=df_Boeing_1485_Baseline20V4['recall'].to_numpy().astype(float)
Boeing_1485RecBaseline20V5=df_Boeing_1485_Baseline20V5['recall'].to_numpy().astype(float)
Boeing_1485PreBaseline20V1=df_Boeing_1485_Baseline20V1['precision'].to_numpy().astype(float)
Boeing_1485PreBaseline20V2=df_Boeing_1485_Baseline20V2['precision'].to_numpy().astype(float)
Boeing_1485PreBaseline20V3=df_Boeing_1485_Baseline20V3['precision'].to_numpy().astype(float)
Boeing_1485PreBaseline20V4=df_Boeing_1485_Baseline20V4['precision'].to_numpy().astype(float)
Boeing_1485PreBaseline20V5=df_Boeing_1485_Baseline20V5['precision'].to_numpy().astype(float)
Boeing_1485RMSEBaseline20V1=df_Boeing_1485_Baseline20V1['rmse'].to_numpy().astype(float)
Boeing_1485RMSEBaseline20V2=df_Boeing_1485_Baseline20V2['rmse'].to_numpy().astype(float)
Boeing_1485RMSEBaseline20V3=df_Boeing_1485_Baseline20V3['rmse'].to_numpy().astype(float)
Boeing_1485RMSEBaseline20V4=df_Boeing_1485_Baseline20V4['rmse'].to_numpy().astype(float)
Boeing_1485RMSEBaseline20V5=df_Boeing_1485_Baseline20V5['rmse'].to_numpy().astype(float)
#
# Boeing_1485RecHybridV1=df_Boeing_1485_HybridV1['recall'].to_numpy().astype(float)
# Boeing_1485RecHybridV2=df_Boeing_1485_HybridV2['recall'].to_numpy().astype(float)
# Boeing_1485RecHybridV3=df_Boeing_1485_HybridV3['recall'].to_numpy().astype(float)
# Boeing_1485RecHybridV4=df_Boeing_1485_HybridV4['recall'].to_numpy().astype(float)
# Boeing_1485RecHybridV5=df_Boeing_1485_HybridV5['recall'].to_numpy().astype(float)
# Boeing_1485PreHybridV1=df_Boeing_1485_HybridV1['precision'].to_numpy().astype(float)
# Boeing_1485PreHybridV2=df_Boeing_1485_HybridV2['precision'].to_numpy().astype(float)
# Boeing_1485PreHybridV3=df_Boeing_1485_HybridV3['precision'].to_numpy().astype(float)
# Boeing_1485PreHybridV4=df_Boeing_1485_HybridV4['precision'].to_numpy().astype(float)
# Boeing_1485PreHybridV5=df_Boeing_1485_HybridV5['precision'].to_numpy().astype(float)
# Boeing_1485RMSEHybridV1=df_Boeing_1485_HybridV1['rmse'].to_numpy().astype(float)
# Boeing_1485RMSEHybridV2=df_Boeing_1485_HybridV2['rmse'].to_numpy().astype(float)
# Boeing_1485RMSEHybridV3=df_Boeing_1485_HybridV3['rmse'].to_numpy().astype(float)
# Boeing_1485RMSEHybridV4=df_Boeing_1485_HybridV4['rmse'].to_numpy().astype(float)
# Boeing_1485RMSEHybridV5=df_Boeing_1485_HybridV5['rmse'].to_numpy().astype(float)

# arrays = [Boeing_1485RecPipelineNoRevV1, Boeing_1485RecPipelineNoRevV2, Boeing_1485RecPipelineNoRevV3, Boeing_1485RecPipelineNoRevV4, Boeing_1485RecPipelineNoRevV5]
# Boeing_1485RecPipelineNoRev = np.mean(arrays, axis=0)
# arrays = [Boeing_1485PrePipelineNoRevV1, Boeing_1485PrePipelineNoRevV2, Boeing_1485PrePipelineNoRevV3, Boeing_1485PrePipelineNoRevV4, Boeing_1485PrePipelineNoRevV5]
# Boeing_1485PrePipelineNoRev = np.mean(arrays, axis=0)
# arrays = [Boeing_1485RMSEPipelineNoRevV1, Boeing_1485RMSEPipelineNoRevV2, Boeing_1485RMSEPipelineNoRevV3, Boeing_1485RMSEPipelineNoRevV4, Boeing_1485RMSEPipelineNoRevV5]
# Boeing_1485RMSEPipelineNoRev = np.mean(arrays, axis=0)
#
# arrays = [Boeing_1485RecBaselineV1, Boeing_1485RecBaselineV2, Boeing_1485RecBaselineV3, Boeing_1485RecBaselineV4, Boeing_1485RecBaselineV5]
# Boeing_1485RecBaseline = np.mean(arrays, axis=0)
# arrays = [Boeing_1485PreBaselineV1, Boeing_1485PreBaselineV2, Boeing_1485PreBaselineV3, Boeing_1485PreBaselineV4, Boeing_1485PreBaselineV5]
# Boeing_1485PreBaseline = np.mean(arrays, axis=0)
# arrays = [Boeing_1485RMSEBaselineV1, Boeing_1485RMSEBaselineV2, Boeing_1485RMSEBaselineV3, Boeing_1485RMSEBaselineV4, Boeing_1485RMSEBaselineV5]
# Boeing_1485RMSEBaseline = np.mean(arrays, axis=0)

arrays = [Boeing_1485RecBaseline20V1, Boeing_1485RecBaseline20V2, Boeing_1485RecBaseline20V3, Boeing_1485RecBaseline20V4, Boeing_1485RecBaseline20V5]
Boeing_1485RecBaseline20 = np.mean(arrays, axis=0)
arrays = [Boeing_1485PreBaseline20V1, Boeing_1485PreBaseline20V2, Boeing_1485PreBaseline20V3, Boeing_1485PreBaseline20V4, Boeing_1485PreBaseline20V5]
Boeing_1485PreBaseline20 = np.mean(arrays, axis=0)
arrays = [Boeing_1485RMSEBaseline20V1, Boeing_1485RMSEBaseline20V2, Boeing_1485RMSEBaseline20V3, Boeing_1485RMSEBaseline20V4, Boeing_1485RMSEBaseline20V5]
Boeing_1485RMSEBaseline20 = np.mean(arrays, axis=0)

# arrays = [Boeing_1485RecHybridV1, Boeing_1485RecHybridV2, Boeing_1485RecHybridV3, Boeing_1485RecHybridV4, Boeing_1485RecHybridV5]
# Boeing_1485RecHybrid = np.mean(arrays, axis=0)
# arrays = [Boeing_1485PreHybridV1, Boeing_1485PreHybridV2, Boeing_1485PreHybridV3, Boeing_1485PreHybridV4, Boeing_1485PreHybridV5]
# Boeing_1485PreHybrid = np.mean(arrays, axis=0)
# arrays = [Boeing_1485RMSEHybridV1, Boeing_1485RMSEHybridV2, Boeing_1485RMSEHybridV3, Boeing_1485RMSEHybridV4, Boeing_1485RMSEHybridV5]
# Boeing_1485RMSEHybrid = np.mean(arrays, axis=0)

arrays = [Boeing_1485RecPipelineV1, Boeing_1485RecPipelineV2, Boeing_1485RecPipelineV3, Boeing_1485RecPipelineV4, Boeing_1485RecPipelineV5]
Boeing_1485RecPipeline = np.mean(arrays, axis=0)
arrays = [Boeing_1485PrePipelineV1, Boeing_1485PrePipelineV2, Boeing_1485PrePipelineV3, Boeing_1485PrePipelineV4, Boeing_1485PrePipelineV5]
Boeing_1485PrePipeline = np.mean(arrays, axis=0)
arrays = [Boeing_1485RMSEPipelineV1, Boeing_1485RMSEPipelineV2, Boeing_1485RMSEPipelineV3, Boeing_1485RMSEPipelineV4, Boeing_1485RMSEPipelineV5]
Boeing_1485RMSEPipeline = np.mean(arrays, axis=0)


# Boeing_1485F1PipelineNoRev = 2 * (Boeing_1485PrePipelineNoRev * Boeing_1485RecPipelineNoRev) / (Boeing_1485PrePipelineNoRev + Boeing_1485RecPipelineNoRev)
# Boeing_1485F1Baseline = 2 * (Boeing_1485PreBaseline * Boeing_1485RecBaseline) / (Boeing_1485PreBaseline + Boeing_1485RecBaseline)
Boeing_1485F1Baseline20 = 2 * (Boeing_1485PreBaseline20 * Boeing_1485RecBaseline20) / (Boeing_1485PreBaseline20 + Boeing_1485RecBaseline20)
# Boeing_1485F1Hybrid = 2 * (Boeing_1485PreHybrid * Boeing_1485RecHybrid) / (Boeing_1485PreHybrid + Boeing_1485RecHybrid)
Boeing_1485F1Pipeline = 2 * (Boeing_1485PrePipeline * Boeing_1485RecPipeline) / (Boeing_1485PrePipeline + Boeing_1485RecPipeline)


#Boeing_1485GMeanPipelineNoRev = np.sqrt(Boeing_1485PrePipelineNoRev * Boeing_1485RecPipelineNoRev)
#Boeing_1485GMeanBaseline = np.sqrt(Boeing_1485PreBaseline * Boeing_1485RecBaseline)
Boeing_1485GMeanBaseline20 = np.sqrt(Boeing_1485PreBaseline20 * Boeing_1485RecBaseline20)
#Boeing_1485GMeanHybrid = np.sqrt(Boeing_1485PreHybrid * Boeing_1485RecHybrid)
Boeing_1485GMeanPipeline = np.sqrt(Boeing_1485PrePipeline * Boeing_1485RecPipeline)

# beta=0.4
# Boeing_1485F0_5PipelineNoRev = (1 + beta**2) * (Boeing_1485PrePipelineNoRev * Boeing_1485RecPipelineNoRev) / ((beta**2 * Boeing_1485PrePipelineNoRev) + Boeing_1485RecPipelineNoRev)
# #Boeing_1485F0_5Baseline = (1 + beta**2) * (Boeing_1485PreBaseline * Boeing_1485RecBaseline) / ((beta**2 * Boeing_1485PreBaseline) + Boeing_1485RecBaseline)
# Boeing_1485F0_5Baseline20 = (1 + beta**2) * (Boeing_1485PreBaseline20 * Boeing_1485RecBaseline20) / ((beta**2 * Boeing_1485PreBaseline20) + Boeing_1485RecBaseline20)
# Boeing_1485F0_5Hybrid = (1 + beta**2) * (Boeing_1485PreHybrid * Boeing_1485RecHybrid) / ((beta**2 * Boeing_1485PreHybrid) + Boeing_1485RecHybrid)
# Boeing_1485F0_5PipelineNoRevNoRev = (1 + beta**2) * (Boeing_1485PrePipelineNoRevNoRev * Boeing_1485RecPipelineNoRevNoRev) / ((beta**2 * Boeing_1485PrePipelineNoRevNoRev) + Boeing_1485RecPipelineNoRevNoRev)


r1 = np.arange(10)

fig, axs = plt.subplots(5, 1, figsize=(5,9), sharey=True)
fig.subplots_adjust(hspace=0.1, wspace=0.05)

axs[0].plot(r1, Boeing_1485PrePipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[0].plot(r1, Boeing_1485PreBaseline,marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[0].plot(r1, Boeing_1485PreBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
# axs[0].plot(r1, Boeing_1485PrePipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
# axs[0].plot(r1, Boeing_1485PreHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")


axs[1].plot(r1, Boeing_1485RecPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[1].plot(r1, Boeing_1485RecBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[1].plot(r1, Boeing_1485RecBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
# axs[1].plot(r1, Boeing_1485RecPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
# axs[1].plot(r1, Boeing_1485RecHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")





axs[2].plot(r1, Boeing_1485F1Pipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[2].plot(r1, Boeing_1485F1Baseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[2].plot(r1, Boeing_1485F1Baseline20, marker="2", markersize=10, color="#00748f", zorder=2)
# axs[2].plot(r1, Boeing_1485F1PipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
# axs[2].plot(r1, Boeing_1485F1Hybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[3].plot(r1, Boeing_1485GMeanPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[3].plot(r1, Boeing_1485GMeanBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[3].plot(r1, Boeing_1485GMeanBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
# axs[3].plot(r1, Boeing_1485GMeanPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
# axs[3].plot(r1, Boeing_1485GMeanHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[4].plot(r1, Boeing_1485RMSEPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[4].plot(r1, Boeing_1485RMSEBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[4].plot(r1, Boeing_1485RMSEBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
# axs[4].plot(r1, Boeing_1485RMSEPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
# axs[4].plot(r1, Boeing_1485RMSEHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

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

plt.savefig("Boeing_1485.pdf", bbox_inches='tight')
plt.show()
