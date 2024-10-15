import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

df=pd.read_csv("../ALL_Results_v2.csv", sep=';')

df_superstore_4500_=df.loc[df['dataset'] == 'superstore_4500' ]


df_superstore_4500_Pipeline=df_superstore_4500_.loc[df_superstore_4500_['algoritmo'] == 'Pipeline' ]
#df_superstore_4500_Baseline=df_superstore_4500_.loc[df_superstore_4500_['algoritmo'] == 'Baseline' ]
df_superstore_4500_Baseline20=df_superstore_4500_.loc[df_superstore_4500_['algoritmo'] == 'Baseline20' ]
df_superstore_4500_PipelineNoRev=df_superstore_4500_.loc[df_superstore_4500_['algoritmo'] == 'Pipeline_noRev' ]
df_superstore_4500_Hybrid=df_superstore_4500_.loc[df_superstore_4500_['algoritmo'] == 'Hybrid' ]


df_superstore_4500_PipelineV1=df_superstore_4500_Pipeline.loc[df_superstore_4500_Pipeline['version'] == 1 ]
df_superstore_4500_PipelineV2=df_superstore_4500_Pipeline.loc[df_superstore_4500_Pipeline['version'] == 2 ]
df_superstore_4500_PipelineV3=df_superstore_4500_Pipeline.loc[df_superstore_4500_Pipeline['version'] == 3 ]
df_superstore_4500_PipelineV4=df_superstore_4500_Pipeline.loc[df_superstore_4500_Pipeline['version'] == 4 ]
df_superstore_4500_PipelineV5=df_superstore_4500_Pipeline.loc[df_superstore_4500_Pipeline['version'] == 5 ]

# df_superstore_4500_BaselineV1=df_superstore_4500_Baseline.loc[df_superstore_4500_Baseline['version'] == 1 ]
# df_superstore_4500_BaselineV2=df_superstore_4500_Baseline.loc[df_superstore_4500_Baseline['version'] == 2 ]
# df_superstore_4500_BaselineV3=df_superstore_4500_Baseline.loc[df_superstore_4500_Baseline['version'] == 3 ]
# df_superstore_4500_BaselineV4=df_superstore_4500_Baseline.loc[df_superstore_4500_Baseline['version'] == 4 ]
# df_superstore_4500_BaselineV5=df_superstore_4500_Baseline.loc[df_superstore_4500_Baseline['version'] == 5 ]

df_superstore_4500_Baseline20V1=df_superstore_4500_Baseline20.loc[df_superstore_4500_Baseline20['version'] == 1 ]
df_superstore_4500_Baseline20V2=df_superstore_4500_Baseline20.loc[df_superstore_4500_Baseline20['version'] == 2 ]
df_superstore_4500_Baseline20V3=df_superstore_4500_Baseline20.loc[df_superstore_4500_Baseline20['version'] == 3 ]
df_superstore_4500_Baseline20V4=df_superstore_4500_Baseline20.loc[df_superstore_4500_Baseline20['version'] == 4 ]
df_superstore_4500_Baseline20V5=df_superstore_4500_Baseline20.loc[df_superstore_4500_Baseline20['version'] == 5 ]

#df_superstore_4500_PipelineNoRevV1=df_superstore_4500_PipelineNoRev.loc[df_superstore_4500_PipelineNoRev['version'] == 1 ]
#df_superstore_4500_PipelineNoRevV2=df_superstore_4500_PipelineNoRev.loc[df_superstore_4500_PipelineNoRev['version'] == 2 ]
#df_superstore_4500_PipelineNoRevV3=df_superstore_4500_PipelineNoRev.loc[df_superstore_4500_PipelineNoRev['version'] == 3 ]
#df_superstore_4500_PipelineNoRevV4=df_superstore_4500_PipelineNoRev.loc[df_superstore_4500_PipelineNoRev['version'] == 4 ]
#df_superstore_4500_PipelineNoRevV5=df_superstore_4500_PipelineNoRev.loc[df_superstore_4500_PipelineNoRev['version'] == 5 ]
#
#df_superstore_4500_HybridV1=df_superstore_4500_Hybrid.loc[df_superstore_4500_Hybrid['version'] == 1 ]
#df_superstore_4500_HybridV2=df_superstore_4500_Hybrid.loc[df_superstore_4500_Hybrid['version'] == 2 ]
#df_superstore_4500_HybridV3=df_superstore_4500_Hybrid.loc[df_superstore_4500_Hybrid['version'] == 3 ]
#df_superstore_4500_HybridV4=df_superstore_4500_Hybrid.loc[df_superstore_4500_Hybrid['version'] == 4 ]
#df_superstore_4500_HybridV5=df_superstore_4500_Hybrid.loc[df_superstore_4500_Hybrid['version'] == 5 ]

#superstore_4500RecPipelineNoRevV1=df_superstore_4500_PipelineNoRevV1['recall'].to_numpy().astype(float)
#superstore_4500RecPipelineNoRevV2=df_superstore_4500_PipelineNoRevV2['recall'].to_numpy().astype(float)
#superstore_4500RecPipelineNoRevV3=df_superstore_4500_PipelineNoRevV3['recall'].to_numpy().astype(float)
#superstore_4500RecPipelineNoRevV4=df_superstore_4500_PipelineNoRevV4['recall'].to_numpy().astype(float)
#superstore_4500RecPipelineNoRevV5=df_superstore_4500_PipelineNoRevV5['recall'].to_numpy().astype(float)
#superstore_4500PrePipelineNoRevV1=df_superstore_4500_PipelineNoRevV1['precision'].to_numpy().astype(float)
#superstore_4500PrePipelineNoRevV2=df_superstore_4500_PipelineNoRevV2['precision'].to_numpy().astype(float)
#superstore_4500PrePipelineNoRevV3=df_superstore_4500_PipelineNoRevV3['precision'].to_numpy().astype(float)
#superstore_4500PrePipelineNoRevV4=df_superstore_4500_PipelineNoRevV4['precision'].to_numpy().astype(float)
#superstore_4500PrePipelineNoRevV5=df_superstore_4500_PipelineNoRevV5['precision'].to_numpy().astype(float)
#superstore_4500RMSEPipelineNoRevV1=df_superstore_4500_PipelineNoRevV1['rmse'].to_numpy().astype(float)
#superstore_4500RMSEPipelineNoRevV2=df_superstore_4500_PipelineNoRevV2['rmse'].to_numpy().astype(float)
#superstore_4500RMSEPipelineNoRevV3=df_superstore_4500_PipelineNoRevV3['rmse'].to_numpy().astype(float)
#superstore_4500RMSEPipelineNoRevV4=df_superstore_4500_PipelineNoRevV4['rmse'].to_numpy().astype(float)
#superstore_4500RMSEPipelineNoRevV5=df_superstore_4500_PipelineNoRevV5['rmse'].to_numpy().astype(float)



superstore_4500RecPipelineV1=df_superstore_4500_PipelineV1['recall'].to_numpy().astype(float)
superstore_4500RecPipelineV2=df_superstore_4500_PipelineV2['recall'].to_numpy().astype(float)
superstore_4500RecPipelineV3=df_superstore_4500_PipelineV3['recall'].to_numpy().astype(float)
superstore_4500RecPipelineV4=df_superstore_4500_PipelineV4['recall'].to_numpy().astype(float)
superstore_4500RecPipelineV5=df_superstore_4500_PipelineV5['recall'].to_numpy().astype(float)
superstore_4500PrePipelineV1=df_superstore_4500_PipelineV1['precision'].to_numpy().astype(float)
superstore_4500PrePipelineV2=df_superstore_4500_PipelineV2['precision'].to_numpy().astype(float)
superstore_4500PrePipelineV3=df_superstore_4500_PipelineV3['precision'].to_numpy().astype(float)
superstore_4500PrePipelineV4=df_superstore_4500_PipelineV4['precision'].to_numpy().astype(float)
superstore_4500PrePipelineV5=df_superstore_4500_PipelineV5['precision'].to_numpy().astype(float)
superstore_4500RMSEPipelineV1=df_superstore_4500_PipelineV1['rmse'].to_numpy().astype(float)
superstore_4500RMSEPipelineV2=df_superstore_4500_PipelineV2['rmse'].to_numpy().astype(float)
superstore_4500RMSEPipelineV3=df_superstore_4500_PipelineV3['rmse'].to_numpy().astype(float)
superstore_4500RMSEPipelineV4=df_superstore_4500_PipelineV4['rmse'].to_numpy().astype(float)
superstore_4500RMSEPipelineV5=df_superstore_4500_PipelineV5['rmse'].to_numpy().astype(float)

#
# superstore_4500RecBaselineV1=df_superstore_4500_BaselineV1['recall'].to_numpy().astype(float)
# superstore_4500RecBaselineV2=df_superstore_4500_BaselineV2['recall'].to_numpy().astype(float)
# superstore_4500RecBaselineV3=df_superstore_4500_BaselineV3['recall'].to_numpy().astype(float)
# superstore_4500RecBaselineV4=df_superstore_4500_BaselineV4['recall'].to_numpy().astype(float)
# superstore_4500RecBaselineV5=df_superstore_4500_BaselineV5['recall'].to_numpy().astype(float)
# superstore_4500PreBaselineV1=df_superstore_4500_BaselineV1['precision'].to_numpy().astype(float)
# superstore_4500PreBaselineV2=df_superstore_4500_BaselineV2['precision'].to_numpy().astype(float)
# superstore_4500PreBaselineV3=df_superstore_4500_BaselineV3['precision'].to_numpy().astype(float)
# superstore_4500PreBaselineV4=df_superstore_4500_BaselineV4['precision'].to_numpy().astype(float)
# superstore_4500PreBaselineV5=df_superstore_4500_BaselineV5['precision'].to_numpy().astype(float)
# superstore_4500RMSEBaselineV1=df_superstore_4500_BaselineV1['rmse'].to_numpy().astype(float)
# superstore_4500RMSEBaselineV2=df_superstore_4500_BaselineV2['rmse'].to_numpy().astype(float)
# superstore_4500RMSEBaselineV3=df_superstore_4500_BaselineV3['rmse'].to_numpy().astype(float)
# superstore_4500RMSEBaselineV4=df_superstore_4500_BaselineV4['rmse'].to_numpy().astype(float)
# superstore_4500RMSEBaselineV5=df_superstore_4500_BaselineV5['rmse'].to_numpy().astype(float)

superstore_4500RecBaseline20V1=df_superstore_4500_Baseline20V1['recall'].to_numpy().astype(float)
superstore_4500RecBaseline20V2=df_superstore_4500_Baseline20V2['recall'].to_numpy().astype(float)
superstore_4500RecBaseline20V3=df_superstore_4500_Baseline20V3['recall'].to_numpy().astype(float)
superstore_4500RecBaseline20V4=df_superstore_4500_Baseline20V4['recall'].to_numpy().astype(float)
superstore_4500RecBaseline20V5=df_superstore_4500_Baseline20V5['recall'].to_numpy().astype(float)
superstore_4500PreBaseline20V1=df_superstore_4500_Baseline20V1['precision'].to_numpy().astype(float)
superstore_4500PreBaseline20V2=df_superstore_4500_Baseline20V2['precision'].to_numpy().astype(float)
superstore_4500PreBaseline20V3=df_superstore_4500_Baseline20V3['precision'].to_numpy().astype(float)
superstore_4500PreBaseline20V4=df_superstore_4500_Baseline20V4['precision'].to_numpy().astype(float)
superstore_4500PreBaseline20V5=df_superstore_4500_Baseline20V5['precision'].to_numpy().astype(float)
superstore_4500RMSEBaseline20V1=df_superstore_4500_Baseline20V1['rmse'].to_numpy().astype(float)
superstore_4500RMSEBaseline20V2=df_superstore_4500_Baseline20V2['rmse'].to_numpy().astype(float)
superstore_4500RMSEBaseline20V3=df_superstore_4500_Baseline20V3['rmse'].to_numpy().astype(float)
superstore_4500RMSEBaseline20V4=df_superstore_4500_Baseline20V4['rmse'].to_numpy().astype(float)
superstore_4500RMSEBaseline20V5=df_superstore_4500_Baseline20V5['rmse'].to_numpy().astype(float)
#
#superstore_4500RecHybridV1=df_superstore_4500_HybridV1['recall'].to_numpy().astype(float)
#superstore_4500RecHybridV2=df_superstore_4500_HybridV2['recall'].to_numpy().astype(float)
#superstore_4500RecHybridV3=df_superstore_4500_HybridV3['recall'].to_numpy().astype(float)
#superstore_4500RecHybridV4=df_superstore_4500_HybridV4['recall'].to_numpy().astype(float)
#superstore_4500RecHybridV5=df_superstore_4500_HybridV5['recall'].to_numpy().astype(float)
#superstore_4500PreHybridV1=df_superstore_4500_HybridV1['precision'].to_numpy().astype(float)
#superstore_4500PreHybridV2=df_superstore_4500_HybridV2['precision'].to_numpy().astype(float)
#superstore_4500PreHybridV3=df_superstore_4500_HybridV3['precision'].to_numpy().astype(float)
#superstore_4500PreHybridV4=df_superstore_4500_HybridV4['precision'].to_numpy().astype(float)
#superstore_4500PreHybridV5=df_superstore_4500_HybridV5['precision'].to_numpy().astype(float)
#superstore_4500RMSEHybridV1=df_superstore_4500_HybridV1['rmse'].to_numpy().astype(float)
#superstore_4500RMSEHybridV2=df_superstore_4500_HybridV2['rmse'].to_numpy().astype(float)
#superstore_4500RMSEHybridV3=df_superstore_4500_HybridV3['rmse'].to_numpy().astype(float)
#superstore_4500RMSEHybridV4=df_superstore_4500_HybridV4['rmse'].to_numpy().astype(float)
#superstore_4500RMSEHybridV5=df_superstore_4500_HybridV5['rmse'].to_numpy().astype(float)
#
#arrays = [superstore_4500RecPipelineNoRevV1, superstore_4500RecPipelineNoRevV2, superstore_4500RecPipelineNoRevV3, superstore_4500RecPipelineNoRevV4, superstore_4500RecPipelineNoRevV5]
#superstore_4500RecPipelineNoRev = np.mean(arrays, axis=0)
#arrays = [superstore_4500PrePipelineNoRevV1, superstore_4500PrePipelineNoRevV2, superstore_4500PrePipelineNoRevV3, superstore_4500PrePipelineNoRevV4, superstore_4500PrePipelineNoRevV5]
#superstore_4500PrePipelineNoRev = np.mean(arrays, axis=0)
#arrays = [superstore_4500RMSEPipelineNoRevV1, superstore_4500RMSEPipelineNoRevV2, superstore_4500RMSEPipelineNoRevV3, superstore_4500RMSEPipelineNoRevV4, superstore_4500RMSEPipelineNoRevV5]
#superstore_4500RMSEPipelineNoRev = np.mean(arrays, axis=0)
#
# arrays = [superstore_4500RecBaselineV1, superstore_4500RecBaselineV2, superstore_4500RecBaselineV3, superstore_4500RecBaselineV4, superstore_4500RecBaselineV5]
# superstore_4500RecBaseline = np.mean(arrays, axis=0)
# arrays = [superstore_4500PreBaselineV1, superstore_4500PreBaselineV2, superstore_4500PreBaselineV3, superstore_4500PreBaselineV4, superstore_4500PreBaselineV5]
# superstore_4500PreBaseline = np.mean(arrays, axis=0)
# arrays = [superstore_4500RMSEBaselineV1, superstore_4500RMSEBaselineV2, superstore_4500RMSEBaselineV3, superstore_4500RMSEBaselineV4, superstore_4500RMSEBaselineV5]
# superstore_4500RMSEBaseline = np.mean(arrays, axis=0)

arrays = [superstore_4500RecBaseline20V1, superstore_4500RecBaseline20V2, superstore_4500RecBaseline20V3, superstore_4500RecBaseline20V4, superstore_4500RecBaseline20V5]
superstore_4500RecBaseline20 = np.mean(arrays, axis=0)
arrays = [superstore_4500PreBaseline20V1, superstore_4500PreBaseline20V2, superstore_4500PreBaseline20V3, superstore_4500PreBaseline20V4, superstore_4500PreBaseline20V5]
superstore_4500PreBaseline20 = np.mean(arrays, axis=0)
arrays = [superstore_4500RMSEBaseline20V1, superstore_4500RMSEBaseline20V2, superstore_4500RMSEBaseline20V3, superstore_4500RMSEBaseline20V4, superstore_4500RMSEBaseline20V5]
superstore_4500RMSEBaseline20 = np.mean(arrays, axis=0)

#arrays = [superstore_4500RecHybridV1, superstore_4500RecHybridV2, superstore_4500RecHybridV3, superstore_4500RecHybridV4, superstore_4500RecHybridV5]
#superstore_4500RecHybrid = np.mean(arrays, axis=0)
#arrays = [superstore_4500PreHybridV1, superstore_4500PreHybridV2, superstore_4500PreHybridV3, superstore_4500PreHybridV4, superstore_4500PreHybridV5]
#superstore_4500PreHybrid = np.mean(arrays, axis=0)
#arrays = [superstore_4500RMSEHybridV1, superstore_4500RMSEHybridV2, superstore_4500RMSEHybridV3, superstore_4500RMSEHybridV4, superstore_4500RMSEHybridV5]
#superstore_4500RMSEHybrid = np.mean(arrays, axis=0)
#
arrays = [superstore_4500RecPipelineV1, superstore_4500RecPipelineV2, superstore_4500RecPipelineV3, superstore_4500RecPipelineV4, superstore_4500RecPipelineV5]
superstore_4500RecPipeline = np.mean(arrays, axis=0)
arrays = [superstore_4500PrePipelineV1, superstore_4500PrePipelineV2, superstore_4500PrePipelineV3, superstore_4500PrePipelineV4, superstore_4500PrePipelineV5]
superstore_4500PrePipeline = np.mean(arrays, axis=0)
arrays = [superstore_4500RMSEPipelineV1, superstore_4500RMSEPipelineV2, superstore_4500RMSEPipelineV3, superstore_4500RMSEPipelineV4, superstore_4500RMSEPipelineV5]
superstore_4500RMSEPipeline = np.mean(arrays, axis=0)


#superstore_4500F1PipelineNoRev = 2 * (superstore_4500PrePipelineNoRev * superstore_4500RecPipelineNoRev) / (superstore_4500PrePipelineNoRev + superstore_4500RecPipelineNoRev)
# superstore_4500F1Baseline = 2 * (superstore_4500PreBaseline * superstore_4500RecBaseline) / (superstore_4500PreBaseline + superstore_4500RecBaseline)
superstore_4500F1Baseline20 = 2 * (superstore_4500PreBaseline20 * superstore_4500RecBaseline20) / (superstore_4500PreBaseline20 + superstore_4500RecBaseline20)
#superstore_4500F1Hybrid = 2 * (superstore_4500PreHybrid * superstore_4500RecHybrid) / (superstore_4500PreHybrid + superstore_4500RecHybrid)
superstore_4500F1Pipeline = 2 * (superstore_4500PrePipeline * superstore_4500RecPipeline) / (superstore_4500PrePipeline + superstore_4500RecPipeline)


#superstore_4500GMeanPipelineNoRev = np.sqrt(superstore_4500PrePipelineNoRev * superstore_4500RecPipelineNoRev)
#superstore_4500GMeanBaseline = np.sqrt(superstore_4500PreBaseline * superstore_4500RecBaseline)
superstore_4500GMeanBaseline20 = np.sqrt(superstore_4500PreBaseline20 * superstore_4500RecBaseline20)
#superstore_4500GMeanHybrid = np.sqrt(superstore_4500PreHybrid * superstore_4500RecHybrid)
superstore_4500GMeanPipeline = np.sqrt(superstore_4500PrePipeline * superstore_4500RecPipeline)

# beta=0.4
# superstore_4500F0_5PipelineNoRev = (1 + beta**2) * (superstore_4500PrePipelineNoRev * superstore_4500RecPipelineNoRev) / ((beta**2 * superstore_4500PrePipelineNoRev) + superstore_4500RecPipelineNoRev)
# superstore_4500F0_5Baseline = (1 + beta**2) * (superstore_4500PreBaseline * superstore_4500RecBaseline) / ((beta**2 * superstore_4500PreBaseline) + superstore_4500RecBaseline)
# superstore_4500F0_5Baseline20 = (1 + beta**2) * (superstore_4500PreBaseline20 * superstore_4500RecBaseline20) / ((beta**2 * superstore_4500PreBaseline20) + superstore_4500RecBaseline20)
# superstore_4500F0_5Hybrid = (1 + beta**2) * (superstore_4500PreHybrid * superstore_4500RecHybrid) / ((beta**2 * superstore_4500PreHybrid) + superstore_4500RecHybrid)
# superstore_4500F0_5PipelineNoRevNoRev = (1 + beta**2) * (superstore_4500PrePipelineNoRevNoRev * superstore_4500RecPipelineNoRevNoRev) / ((beta**2 * superstore_4500PrePipelineNoRevNoRev) + superstore_4500RecPipelineNoRevNoRev)


r1 = np.arange(10)

fig, axs = plt.subplots(5, 1, figsize=(5,9), sharey=True)
fig.subplots_adjust(hspace=0.1, wspace=0.05)

axs[0].plot(r1, superstore_4500PrePipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[0].plot(r1, superstore_4500PreBaseline,marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[0].plot(r1, superstore_4500PreBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
#axs[0].plot(r1, superstore_4500PrePipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
#axs[0].plot(r1, superstore_4500PreHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")


axs[1].plot(r1, superstore_4500RecPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[1].plot(r1, superstore_4500RecBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[1].plot(r1, superstore_4500RecBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
#axs[1].plot(r1, superstore_4500RecPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
#axs[1].plot(r1, superstore_4500RecHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")





axs[2].plot(r1, superstore_4500F1Pipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[2].plot(r1, superstore_4500F1Baseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[2].plot(r1, superstore_4500F1Baseline20, marker="2", markersize=10, color="#00748f", zorder=2)
#axs[2].plot(r1, superstore_4500F1PipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
#axs[2].plot(r1, superstore_4500F1Hybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[3].plot(r1, superstore_4500GMeanPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[3].plot(r1, superstore_4500GMeanBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[3].plot(r1, superstore_4500GMeanBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
#axs[3].plot(r1, superstore_4500GMeanPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
#axs[3].plot(r1, superstore_4500GMeanHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[4].plot(r1, superstore_4500RMSEPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[4].plot(r1, superstore_4500RMSEBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[4].plot(r1, superstore_4500RMSEBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
#axs[4].plot(r1, superstore_4500RMSEPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
#axs[4].plot(r1, superstore_4500RMSEHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[0].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[0].set_ylabel('Precision', rotation='vertical')
axs[0].set_title('Superstore', fontsize=12)

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

plt.savefig("superstore_4500.pdf", bbox_inches='tight')
plt.show()
