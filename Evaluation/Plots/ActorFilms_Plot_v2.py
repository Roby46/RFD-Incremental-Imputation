import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

df=pd.read_csv("../ALL_Results_v2.csv", sep=';')

df_actorfilms_4000_=df.loc[df['dataset'] == 'actorfilms_4000' ]


df_actorfilms_4000_Pipeline=df_actorfilms_4000_.loc[df_actorfilms_4000_['algoritmo'] == 'Pipeline' ]
df_actorfilms_4000_Baseline=df_actorfilms_4000_.loc[df_actorfilms_4000_['algoritmo'] == 'Baseline' ]
df_actorfilms_4000_Baseline20=df_actorfilms_4000_.loc[df_actorfilms_4000_['algoritmo'] == 'Baseline20' ]
df_actorfilms_4000_PipelineNoRev=df_actorfilms_4000_.loc[df_actorfilms_4000_['algoritmo'] == 'Pipeline_noRev' ]
df_actorfilms_4000_Hybrid=df_actorfilms_4000_.loc[df_actorfilms_4000_['algoritmo'] == 'Hybrid' ]



df_actorfilms_4000_PipelineV1=df_actorfilms_4000_Pipeline.loc[df_actorfilms_4000_Pipeline['version'] == 1 ]
df_actorfilms_4000_PipelineV2=df_actorfilms_4000_Pipeline.loc[df_actorfilms_4000_Pipeline['version'] == 2 ]
df_actorfilms_4000_PipelineV3=df_actorfilms_4000_Pipeline.loc[df_actorfilms_4000_Pipeline['version'] == 3 ]
df_actorfilms_4000_PipelineV4=df_actorfilms_4000_Pipeline.loc[df_actorfilms_4000_Pipeline['version'] == 4 ]
df_actorfilms_4000_PipelineV5=df_actorfilms_4000_Pipeline.loc[df_actorfilms_4000_Pipeline['version'] == 5 ]

df_actorfilms_4000_BaselineV1=df_actorfilms_4000_Baseline.loc[df_actorfilms_4000_Baseline['version'] == 1 ]
df_actorfilms_4000_BaselineV2=df_actorfilms_4000_Baseline.loc[df_actorfilms_4000_Baseline['version'] == 2 ]
df_actorfilms_4000_BaselineV3=df_actorfilms_4000_Baseline.loc[df_actorfilms_4000_Baseline['version'] == 3 ]
df_actorfilms_4000_BaselineV4=df_actorfilms_4000_Baseline.loc[df_actorfilms_4000_Baseline['version'] == 4 ]
df_actorfilms_4000_BaselineV5=df_actorfilms_4000_Baseline.loc[df_actorfilms_4000_Baseline['version'] == 5 ]

df_actorfilms_4000_Baseline20V1=df_actorfilms_4000_Baseline20.loc[df_actorfilms_4000_Baseline20['version'] == 1 ]
df_actorfilms_4000_Baseline20V2=df_actorfilms_4000_Baseline20.loc[df_actorfilms_4000_Baseline20['version'] == 2 ]
df_actorfilms_4000_Baseline20V3=df_actorfilms_4000_Baseline20.loc[df_actorfilms_4000_Baseline20['version'] == 3 ]
df_actorfilms_4000_Baseline20V4=df_actorfilms_4000_Baseline20.loc[df_actorfilms_4000_Baseline20['version'] == 4 ]
df_actorfilms_4000_Baseline20V5=df_actorfilms_4000_Baseline20.loc[df_actorfilms_4000_Baseline20['version'] == 5 ]

df_actorfilms_4000_PipelineNoRevV1=df_actorfilms_4000_PipelineNoRev.loc[df_actorfilms_4000_PipelineNoRev['version'] == 1 ]
df_actorfilms_4000_PipelineNoRevV2=df_actorfilms_4000_PipelineNoRev.loc[df_actorfilms_4000_PipelineNoRev['version'] == 2 ]
df_actorfilms_4000_PipelineNoRevV3=df_actorfilms_4000_PipelineNoRev.loc[df_actorfilms_4000_PipelineNoRev['version'] == 3 ]
df_actorfilms_4000_PipelineNoRevV4=df_actorfilms_4000_PipelineNoRev.loc[df_actorfilms_4000_PipelineNoRev['version'] == 4 ]
df_actorfilms_4000_PipelineNoRevV5=df_actorfilms_4000_PipelineNoRev.loc[df_actorfilms_4000_PipelineNoRev['version'] == 5 ]

df_actorfilms_4000_HybridV1=df_actorfilms_4000_Hybrid.loc[df_actorfilms_4000_Hybrid['version'] == 1 ]
df_actorfilms_4000_HybridV2=df_actorfilms_4000_Hybrid.loc[df_actorfilms_4000_Hybrid['version'] == 2 ]
df_actorfilms_4000_HybridV3=df_actorfilms_4000_Hybrid.loc[df_actorfilms_4000_Hybrid['version'] == 3 ]
df_actorfilms_4000_HybridV4=df_actorfilms_4000_Hybrid.loc[df_actorfilms_4000_Hybrid['version'] == 4 ]
df_actorfilms_4000_HybridV5=df_actorfilms_4000_Hybrid.loc[df_actorfilms_4000_Hybrid['version'] == 5 ]

actorfilms_4000RecPipelineNoRevV1=df_actorfilms_4000_PipelineNoRevV1['recall'].to_numpy().astype(float)
actorfilms_4000RecPipelineNoRevV2=df_actorfilms_4000_PipelineNoRevV2['recall'].to_numpy().astype(float)
actorfilms_4000RecPipelineNoRevV3=df_actorfilms_4000_PipelineNoRevV3['recall'].to_numpy().astype(float)
actorfilms_4000RecPipelineNoRevV4=df_actorfilms_4000_PipelineNoRevV4['recall'].to_numpy().astype(float)
actorfilms_4000RecPipelineNoRevV5=df_actorfilms_4000_PipelineNoRevV5['recall'].to_numpy().astype(float)
actorfilms_4000PrePipelineNoRevV1=df_actorfilms_4000_PipelineNoRevV1['precision'].to_numpy().astype(float)
actorfilms_4000PrePipelineNoRevV2=df_actorfilms_4000_PipelineNoRevV2['precision'].to_numpy().astype(float)
actorfilms_4000PrePipelineNoRevV3=df_actorfilms_4000_PipelineNoRevV3['precision'].to_numpy().astype(float)
actorfilms_4000PrePipelineNoRevV4=df_actorfilms_4000_PipelineNoRevV4['precision'].to_numpy().astype(float)
actorfilms_4000PrePipelineNoRevV5=df_actorfilms_4000_PipelineNoRevV5['precision'].to_numpy().astype(float)
actorfilms_4000RMSEPipelineNoRevV1=df_actorfilms_4000_PipelineNoRevV1['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEPipelineNoRevV2=df_actorfilms_4000_PipelineNoRevV2['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEPipelineNoRevV3=df_actorfilms_4000_PipelineNoRevV3['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEPipelineNoRevV4=df_actorfilms_4000_PipelineNoRevV4['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEPipelineNoRevV5=df_actorfilms_4000_PipelineNoRevV5['rmse'].to_numpy().astype(float)



actorfilms_4000RecPipelineV1=df_actorfilms_4000_PipelineV1['recall'].to_numpy().astype(float)
actorfilms_4000RecPipelineV2=df_actorfilms_4000_PipelineV2['recall'].to_numpy().astype(float)
actorfilms_4000RecPipelineV3=df_actorfilms_4000_PipelineV3['recall'].to_numpy().astype(float)
actorfilms_4000RecPipelineV4=df_actorfilms_4000_PipelineV4['recall'].to_numpy().astype(float)
actorfilms_4000RecPipelineV5=df_actorfilms_4000_PipelineV5['recall'].to_numpy().astype(float)
actorfilms_4000PrePipelineV1=df_actorfilms_4000_PipelineV1['precision'].to_numpy().astype(float)
actorfilms_4000PrePipelineV2=df_actorfilms_4000_PipelineV2['precision'].to_numpy().astype(float)
actorfilms_4000PrePipelineV3=df_actorfilms_4000_PipelineV3['precision'].to_numpy().astype(float)
actorfilms_4000PrePipelineV4=df_actorfilms_4000_PipelineV4['precision'].to_numpy().astype(float)
actorfilms_4000PrePipelineV5=df_actorfilms_4000_PipelineV5['precision'].to_numpy().astype(float)
actorfilms_4000RMSEPipelineV1=df_actorfilms_4000_PipelineV1['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEPipelineV2=df_actorfilms_4000_PipelineV2['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEPipelineV3=df_actorfilms_4000_PipelineV3['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEPipelineV4=df_actorfilms_4000_PipelineV4['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEPipelineV5=df_actorfilms_4000_PipelineV5['rmse'].to_numpy().astype(float)


actorfilms_4000RecBaselineV1=df_actorfilms_4000_BaselineV1['recall'].to_numpy().astype(float)
actorfilms_4000RecBaselineV2=df_actorfilms_4000_BaselineV2['recall'].to_numpy().astype(float)
actorfilms_4000RecBaselineV3=df_actorfilms_4000_BaselineV3['recall'].to_numpy().astype(float)
actorfilms_4000RecBaselineV4=df_actorfilms_4000_BaselineV4['recall'].to_numpy().astype(float)
actorfilms_4000RecBaselineV5=df_actorfilms_4000_BaselineV5['recall'].to_numpy().astype(float)
actorfilms_4000PreBaselineV1=df_actorfilms_4000_BaselineV1['precision'].to_numpy().astype(float)
actorfilms_4000PreBaselineV2=df_actorfilms_4000_BaselineV2['precision'].to_numpy().astype(float)
actorfilms_4000PreBaselineV3=df_actorfilms_4000_BaselineV3['precision'].to_numpy().astype(float)
actorfilms_4000PreBaselineV4=df_actorfilms_4000_BaselineV4['precision'].to_numpy().astype(float)
actorfilms_4000PreBaselineV5=df_actorfilms_4000_BaselineV5['precision'].to_numpy().astype(float)
actorfilms_4000RMSEBaselineV1=df_actorfilms_4000_BaselineV1['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEBaselineV2=df_actorfilms_4000_BaselineV2['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEBaselineV3=df_actorfilms_4000_BaselineV3['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEBaselineV4=df_actorfilms_4000_BaselineV4['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEBaselineV5=df_actorfilms_4000_BaselineV5['rmse'].to_numpy().astype(float)

actorfilms_4000RecBaseline20V1=df_actorfilms_4000_Baseline20V1['recall'].to_numpy().astype(float)
actorfilms_4000RecBaseline20V2=df_actorfilms_4000_Baseline20V2['recall'].to_numpy().astype(float)
actorfilms_4000RecBaseline20V3=df_actorfilms_4000_Baseline20V3['recall'].to_numpy().astype(float)
actorfilms_4000RecBaseline20V4=df_actorfilms_4000_Baseline20V4['recall'].to_numpy().astype(float)
actorfilms_4000RecBaseline20V5=df_actorfilms_4000_Baseline20V5['recall'].to_numpy().astype(float)
actorfilms_4000PreBaseline20V1=df_actorfilms_4000_Baseline20V1['precision'].to_numpy().astype(float)
actorfilms_4000PreBaseline20V2=df_actorfilms_4000_Baseline20V2['precision'].to_numpy().astype(float)
actorfilms_4000PreBaseline20V3=df_actorfilms_4000_Baseline20V3['precision'].to_numpy().astype(float)
actorfilms_4000PreBaseline20V4=df_actorfilms_4000_Baseline20V4['precision'].to_numpy().astype(float)
actorfilms_4000PreBaseline20V5=df_actorfilms_4000_Baseline20V5['precision'].to_numpy().astype(float)
actorfilms_4000RMSEBaseline20V1=df_actorfilms_4000_Baseline20V1['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEBaseline20V2=df_actorfilms_4000_Baseline20V2['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEBaseline20V3=df_actorfilms_4000_Baseline20V3['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEBaseline20V4=df_actorfilms_4000_Baseline20V4['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEBaseline20V5=df_actorfilms_4000_Baseline20V5['rmse'].to_numpy().astype(float)

actorfilms_4000RecHybridV1=df_actorfilms_4000_HybridV1['recall'].to_numpy().astype(float)
actorfilms_4000RecHybridV2=df_actorfilms_4000_HybridV2['recall'].to_numpy().astype(float)
actorfilms_4000RecHybridV3=df_actorfilms_4000_HybridV3['recall'].to_numpy().astype(float)
actorfilms_4000RecHybridV4=df_actorfilms_4000_HybridV4['recall'].to_numpy().astype(float)
actorfilms_4000RecHybridV5=df_actorfilms_4000_HybridV5['recall'].to_numpy().astype(float)
actorfilms_4000PreHybridV1=df_actorfilms_4000_HybridV1['precision'].to_numpy().astype(float)
actorfilms_4000PreHybridV2=df_actorfilms_4000_HybridV2['precision'].to_numpy().astype(float)
actorfilms_4000PreHybridV3=df_actorfilms_4000_HybridV3['precision'].to_numpy().astype(float)
actorfilms_4000PreHybridV4=df_actorfilms_4000_HybridV4['precision'].to_numpy().astype(float)
actorfilms_4000PreHybridV5=df_actorfilms_4000_HybridV5['precision'].to_numpy().astype(float)
actorfilms_4000RMSEHybridV1=df_actorfilms_4000_HybridV1['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEHybridV2=df_actorfilms_4000_HybridV2['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEHybridV3=df_actorfilms_4000_HybridV3['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEHybridV4=df_actorfilms_4000_HybridV4['rmse'].to_numpy().astype(float)
actorfilms_4000RMSEHybridV5=df_actorfilms_4000_HybridV5['rmse'].to_numpy().astype(float)

arrays = [actorfilms_4000RecPipelineNoRevV1, actorfilms_4000RecPipelineNoRevV2, actorfilms_4000RecPipelineNoRevV3, actorfilms_4000RecPipelineNoRevV4, actorfilms_4000RecPipelineNoRevV5]
actorfilms_4000RecPipelineNoRev = np.mean(arrays, axis=0)
arrays = [actorfilms_4000PrePipelineNoRevV1, actorfilms_4000PrePipelineNoRevV2, actorfilms_4000PrePipelineNoRevV3, actorfilms_4000PrePipelineNoRevV4, actorfilms_4000PrePipelineNoRevV5]
actorfilms_4000PrePipelineNoRev = np.mean(arrays, axis=0)
arrays = [actorfilms_4000RMSEPipelineNoRevV1, actorfilms_4000RMSEPipelineNoRevV2, actorfilms_4000RMSEPipelineNoRevV3, actorfilms_4000RMSEPipelineNoRevV4, actorfilms_4000RMSEPipelineNoRevV5]
actorfilms_4000RMSEPipelineNoRev = np.mean(arrays, axis=0)

arrays = [actorfilms_4000RecBaselineV1, actorfilms_4000RecBaselineV2, actorfilms_4000RecBaselineV3, actorfilms_4000RecBaselineV4, actorfilms_4000RecBaselineV5]
actorfilms_4000RecBaseline = np.mean(arrays, axis=0)
arrays = [actorfilms_4000PreBaselineV1, actorfilms_4000PreBaselineV2, actorfilms_4000PreBaselineV3, actorfilms_4000PreBaselineV4, actorfilms_4000PreBaselineV5]
actorfilms_4000PreBaseline = np.mean(arrays, axis=0)
arrays = [actorfilms_4000RMSEBaselineV1, actorfilms_4000RMSEBaselineV2, actorfilms_4000RMSEBaselineV3, actorfilms_4000RMSEBaselineV4, actorfilms_4000RMSEBaselineV5]
actorfilms_4000RMSEBaseline = np.mean(arrays, axis=0)

arrays = [actorfilms_4000RecBaseline20V1, actorfilms_4000RecBaseline20V2, actorfilms_4000RecBaseline20V3, actorfilms_4000RecBaseline20V4, actorfilms_4000RecBaseline20V5]
actorfilms_4000RecBaseline20 = np.mean(arrays, axis=0)
arrays = [actorfilms_4000PreBaseline20V1, actorfilms_4000PreBaseline20V2, actorfilms_4000PreBaseline20V3, actorfilms_4000PreBaseline20V4, actorfilms_4000PreBaseline20V5]
actorfilms_4000PreBaseline20 = np.mean(arrays, axis=0)
arrays = [actorfilms_4000RMSEBaseline20V1, actorfilms_4000RMSEBaseline20V2, actorfilms_4000RMSEBaseline20V3, actorfilms_4000RMSEBaseline20V4, actorfilms_4000RMSEBaseline20V5]
actorfilms_4000RMSEBaseline20 = np.mean(arrays, axis=0)

arrays = [actorfilms_4000RecHybridV1, actorfilms_4000RecHybridV2, actorfilms_4000RecHybridV3, actorfilms_4000RecHybridV4, actorfilms_4000RecHybridV5]
actorfilms_4000RecHybrid = np.mean(arrays, axis=0)
arrays = [actorfilms_4000PreHybridV1, actorfilms_4000PreHybridV2, actorfilms_4000PreHybridV3, actorfilms_4000PreHybridV4, actorfilms_4000PreHybridV5]
actorfilms_4000PreHybrid = np.mean(arrays, axis=0)
arrays = [actorfilms_4000RMSEHybridV1, actorfilms_4000RMSEHybridV2, actorfilms_4000RMSEHybridV3, actorfilms_4000RMSEHybridV4, actorfilms_4000RMSEHybridV5]
actorfilms_4000RMSEHybrid = np.mean(arrays, axis=0)

arrays = [actorfilms_4000RecPipelineV1, actorfilms_4000RecPipelineV2, actorfilms_4000RecPipelineV3, actorfilms_4000RecPipelineV4, actorfilms_4000RecPipelineV5]
actorfilms_4000RecPipeline = np.mean(arrays, axis=0)
arrays = [actorfilms_4000PrePipelineV1, actorfilms_4000PrePipelineV2, actorfilms_4000PrePipelineV3, actorfilms_4000PrePipelineV4, actorfilms_4000PrePipelineV5]
actorfilms_4000PrePipeline = np.mean(arrays, axis=0)
arrays = [actorfilms_4000RMSEPipelineV1, actorfilms_4000RMSEPipelineV2, actorfilms_4000RMSEPipelineV3, actorfilms_4000RMSEPipelineV4, actorfilms_4000RMSEPipelineV5]
actorfilms_4000RMSEPipeline = np.mean(arrays, axis=0)


actorfilms_4000F1PipelineNoRev = 2 * (actorfilms_4000PrePipelineNoRev * actorfilms_4000RecPipelineNoRev) / (actorfilms_4000PrePipelineNoRev + actorfilms_4000RecPipelineNoRev)
actorfilms_4000F1Baseline = 2 * (actorfilms_4000PreBaseline * actorfilms_4000RecBaseline) / (actorfilms_4000PreBaseline + actorfilms_4000RecBaseline)
actorfilms_4000F1Baseline20 = 2 * (actorfilms_4000PreBaseline20 * actorfilms_4000RecBaseline20) / (actorfilms_4000PreBaseline20 + actorfilms_4000RecBaseline20)
actorfilms_4000F1Hybrid = 2 * (actorfilms_4000PreHybrid * actorfilms_4000RecHybrid) / (actorfilms_4000PreHybrid + actorfilms_4000RecHybrid)
actorfilms_4000F1Pipeline = 2 * (actorfilms_4000PrePipeline * actorfilms_4000RecPipeline) / (actorfilms_4000PrePipeline + actorfilms_4000RecPipeline)


actorfilms_4000GMeanPipelineNoRev = np.sqrt(actorfilms_4000PrePipelineNoRev * actorfilms_4000RecPipelineNoRev)
#actorfilms_4000GMeanBaseline = np.sqrt(actorfilms_4000PreBaseline * actorfilms_4000RecBaseline)
actorfilms_4000GMeanBaseline20 = np.sqrt(actorfilms_4000PreBaseline20 * actorfilms_4000RecBaseline20)
actorfilms_4000GMeanHybrid = np.sqrt(actorfilms_4000PreHybrid * actorfilms_4000RecHybrid)
actorfilms_4000GMeanPipeline = np.sqrt(actorfilms_4000PrePipeline * actorfilms_4000RecPipeline)

# beta=0.4
# actorfilms_4000F0_5PipelineNoRev = (1 + beta**2) * (actorfilms_4000PrePipelineNoRev * actorfilms_4000RecPipelineNoRev) / ((beta**2 * actorfilms_4000PrePipelineNoRev) + actorfilms_4000RecPipelineNoRev)
# #actorfilms_4000F0_5Baseline = (1 + beta**2) * (actorfilms_4000PreBaseline * actorfilms_4000RecBaseline) / ((beta**2 * actorfilms_4000PreBaseline) + actorfilms_4000RecBaseline)
# actorfilms_4000F0_5Baseline20 = (1 + beta**2) * (actorfilms_4000PreBaseline20 * actorfilms_4000RecBaseline20) / ((beta**2 * actorfilms_4000PreBaseline20) + actorfilms_4000RecBaseline20)
# actorfilms_4000F0_5Hybrid = (1 + beta**2) * (actorfilms_4000PreHybrid * actorfilms_4000RecHybrid) / ((beta**2 * actorfilms_4000PreHybrid) + actorfilms_4000RecHybrid)
# actorfilms_4000F0_5PipelineNoRevNoRev = (1 + beta**2) * (actorfilms_4000PrePipelineNoRevNoRev * actorfilms_4000RecPipelineNoRevNoRev) / ((beta**2 * actorfilms_4000PrePipelineNoRevNoRev) + actorfilms_4000RecPipelineNoRevNoRev)


r1 = np.arange(10)

fig, axs = plt.subplots(5, 1, figsize=(5,9), sharey=True)
fig.subplots_adjust(hspace=0.1, wspace=0.05)

axs[0].plot(r1, actorfilms_4000PrePipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[0].plot(r1, actorfilms_4000PreBaseline,marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[0].plot(r1, actorfilms_4000PreBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[0].plot(r1, actorfilms_4000PrePipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[0].plot(r1, actorfilms_4000PreHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")


axs[1].plot(r1, actorfilms_4000RecPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[1].plot(r1, actorfilms_4000RecBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[1].plot(r1, actorfilms_4000RecBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[1].plot(r1, actorfilms_4000RecPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[1].plot(r1, actorfilms_4000RecHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")





axs[2].plot(r1, actorfilms_4000F1Pipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[2].plot(r1, actorfilms_4000F1Baseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[2].plot(r1, actorfilms_4000F1Baseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[2].plot(r1, actorfilms_4000F1PipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[2].plot(r1, actorfilms_4000F1Hybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[3].plot(r1, actorfilms_4000GMeanPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[3].plot(r1, actorfilms_4000GMeanBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[3].plot(r1, actorfilms_4000GMeanBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[3].plot(r1, actorfilms_4000GMeanPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[3].plot(r1, actorfilms_4000GMeanHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[4].plot(r1, actorfilms_4000RMSEPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[4].plot(r1, actorfilms_4000RMSEBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[4].plot(r1, actorfilms_4000RMSEBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
axs[4].plot(r1, actorfilms_4000RMSEPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
axs[4].plot(r1, actorfilms_4000RMSEHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

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

plt.savefig("actorfilms_4000.pdf", bbox_inches='tight')
plt.show()
