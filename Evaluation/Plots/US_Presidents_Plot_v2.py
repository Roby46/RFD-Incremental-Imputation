import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

df=pd.read_csv("../ALL_Results_v2.csv", sep=';')

df_US_Presidents_3754_=df.loc[df['dataset'] == 'US_Presidents_3754' ]


df_US_Presidents_3754_Pipeline=df_US_Presidents_3754_.loc[df_US_Presidents_3754_['algoritmo'] == 'Pipeline' ]
#df_US_Presidents_3754_Baseline=df_US_Presidents_3754_.loc[df_US_Presidents_3754_['algoritmo'] == 'Baseline' ]
df_US_Presidents_3754_Baseline20=df_US_Presidents_3754_.loc[df_US_Presidents_3754_['algoritmo'] == 'Baseline20' ]
df_US_Presidents_3754_PipelineNoRev=df_US_Presidents_3754_.loc[df_US_Presidents_3754_['algoritmo'] == 'Pipeline_noRev' ]
df_US_Presidents_3754_Hybrid=df_US_Presidents_3754_.loc[df_US_Presidents_3754_['algoritmo'] == 'Hybrid' ]


df_US_Presidents_3754_PipelineV1=df_US_Presidents_3754_Pipeline.loc[df_US_Presidents_3754_Pipeline['version'] == 1 ]
df_US_Presidents_3754_PipelineV2=df_US_Presidents_3754_Pipeline.loc[df_US_Presidents_3754_Pipeline['version'] == 2 ]
df_US_Presidents_3754_PipelineV3=df_US_Presidents_3754_Pipeline.loc[df_US_Presidents_3754_Pipeline['version'] == 3 ]
df_US_Presidents_3754_PipelineV4=df_US_Presidents_3754_Pipeline.loc[df_US_Presidents_3754_Pipeline['version'] == 4 ]
df_US_Presidents_3754_PipelineV5=df_US_Presidents_3754_Pipeline.loc[df_US_Presidents_3754_Pipeline['version'] == 5 ]

# df_US_Presidents_3754_BaselineV1=df_US_Presidents_3754_Baseline.loc[df_US_Presidents_3754_Baseline['version'] == 1 ]
# df_US_Presidents_3754_BaselineV2=df_US_Presidents_3754_Baseline.loc[df_US_Presidents_3754_Baseline['version'] == 2 ]
# df_US_Presidents_3754_BaselineV3=df_US_Presidents_3754_Baseline.loc[df_US_Presidents_3754_Baseline['version'] == 3 ]
# df_US_Presidents_3754_BaselineV4=df_US_Presidents_3754_Baseline.loc[df_US_Presidents_3754_Baseline['version'] == 4 ]
# df_US_Presidents_3754_BaselineV5=df_US_Presidents_3754_Baseline.loc[df_US_Presidents_3754_Baseline['version'] == 5 ]

df_US_Presidents_3754_Baseline20V1=df_US_Presidents_3754_Baseline20.loc[df_US_Presidents_3754_Baseline20['version'] == 1 ]
df_US_Presidents_3754_Baseline20V2=df_US_Presidents_3754_Baseline20.loc[df_US_Presidents_3754_Baseline20['version'] == 2 ]
df_US_Presidents_3754_Baseline20V3=df_US_Presidents_3754_Baseline20.loc[df_US_Presidents_3754_Baseline20['version'] == 3 ]
df_US_Presidents_3754_Baseline20V4=df_US_Presidents_3754_Baseline20.loc[df_US_Presidents_3754_Baseline20['version'] == 4 ]
df_US_Presidents_3754_Baseline20V5=df_US_Presidents_3754_Baseline20.loc[df_US_Presidents_3754_Baseline20['version'] == 5 ]

#df_US_Presidents_3754_PipelineNoRevV1=df_US_Presidents_3754_PipelineNoRev.loc[df_US_Presidents_3754_PipelineNoRev['version'] == 1 ]
#df_US_Presidents_3754_PipelineNoRevV2=df_US_Presidents_3754_PipelineNoRev.loc[df_US_Presidents_3754_PipelineNoRev['version'] == 2 ]
#df_US_Presidents_3754_PipelineNoRevV3=df_US_Presidents_3754_PipelineNoRev.loc[df_US_Presidents_3754_PipelineNoRev['version'] == 3 ]
#df_US_Presidents_3754_PipelineNoRevV4=df_US_Presidents_3754_PipelineNoRev.loc[df_US_Presidents_3754_PipelineNoRev['version'] == 4 ]
#df_US_Presidents_3754_PipelineNoRevV5=df_US_Presidents_3754_PipelineNoRev.loc[df_US_Presidents_3754_PipelineNoRev['version'] == 5 ]
#
#df_US_Presidents_3754_HybridV1=df_US_Presidents_3754_Hybrid.loc[df_US_Presidents_3754_Hybrid['version'] == 1 ]
#df_US_Presidents_3754_HybridV2=df_US_Presidents_3754_Hybrid.loc[df_US_Presidents_3754_Hybrid['version'] == 2 ]
#df_US_Presidents_3754_HybridV3=df_US_Presidents_3754_Hybrid.loc[df_US_Presidents_3754_Hybrid['version'] == 3 ]
#df_US_Presidents_3754_HybridV4=df_US_Presidents_3754_Hybrid.loc[df_US_Presidents_3754_Hybrid['version'] == 4 ]
#df_US_Presidents_3754_HybridV5=df_US_Presidents_3754_Hybrid.loc[df_US_Presidents_3754_Hybrid['version'] == 5 ]

#US_Presidents_3754RecPipelineNoRevV1=df_US_Presidents_3754_PipelineNoRevV1['recall'].to_numpy().astype(float)
#US_Presidents_3754RecPipelineNoRevV2=df_US_Presidents_3754_PipelineNoRevV2['recall'].to_numpy().astype(float)
#US_Presidents_3754RecPipelineNoRevV3=df_US_Presidents_3754_PipelineNoRevV3['recall'].to_numpy().astype(float)
#US_Presidents_3754RecPipelineNoRevV4=df_US_Presidents_3754_PipelineNoRevV4['recall'].to_numpy().astype(float)
#US_Presidents_3754RecPipelineNoRevV5=df_US_Presidents_3754_PipelineNoRevV5['recall'].to_numpy().astype(float)
#US_Presidents_3754PrePipelineNoRevV1=df_US_Presidents_3754_PipelineNoRevV1['precision'].to_numpy().astype(float)
#US_Presidents_3754PrePipelineNoRevV2=df_US_Presidents_3754_PipelineNoRevV2['precision'].to_numpy().astype(float)
#US_Presidents_3754PrePipelineNoRevV3=df_US_Presidents_3754_PipelineNoRevV3['precision'].to_numpy().astype(float)
#US_Presidents_3754PrePipelineNoRevV4=df_US_Presidents_3754_PipelineNoRevV4['precision'].to_numpy().astype(float)
#US_Presidents_3754PrePipelineNoRevV5=df_US_Presidents_3754_PipelineNoRevV5['precision'].to_numpy().astype(float)
#US_Presidents_3754RMSEPipelineNoRevV1=df_US_Presidents_3754_PipelineNoRevV1['rmse'].to_numpy().astype(float)
#US_Presidents_3754RMSEPipelineNoRevV2=df_US_Presidents_3754_PipelineNoRevV2['rmse'].to_numpy().astype(float)
#US_Presidents_3754RMSEPipelineNoRevV3=df_US_Presidents_3754_PipelineNoRevV3['rmse'].to_numpy().astype(float)
#US_Presidents_3754RMSEPipelineNoRevV4=df_US_Presidents_3754_PipelineNoRevV4['rmse'].to_numpy().astype(float)
#US_Presidents_3754RMSEPipelineNoRevV5=df_US_Presidents_3754_PipelineNoRevV5['rmse'].to_numpy().astype(float)



US_Presidents_3754RecPipelineV1=df_US_Presidents_3754_PipelineV1['recall'].to_numpy().astype(float)
US_Presidents_3754RecPipelineV2=df_US_Presidents_3754_PipelineV2['recall'].to_numpy().astype(float)
US_Presidents_3754RecPipelineV3=df_US_Presidents_3754_PipelineV3['recall'].to_numpy().astype(float)
US_Presidents_3754RecPipelineV4=df_US_Presidents_3754_PipelineV4['recall'].to_numpy().astype(float)
US_Presidents_3754RecPipelineV5=df_US_Presidents_3754_PipelineV5['recall'].to_numpy().astype(float)
US_Presidents_3754PrePipelineV1=df_US_Presidents_3754_PipelineV1['precision'].to_numpy().astype(float)
US_Presidents_3754PrePipelineV2=df_US_Presidents_3754_PipelineV2['precision'].to_numpy().astype(float)
US_Presidents_3754PrePipelineV3=df_US_Presidents_3754_PipelineV3['precision'].to_numpy().astype(float)
US_Presidents_3754PrePipelineV4=df_US_Presidents_3754_PipelineV4['precision'].to_numpy().astype(float)
US_Presidents_3754PrePipelineV5=df_US_Presidents_3754_PipelineV5['precision'].to_numpy().astype(float)
US_Presidents_3754RMSEPipelineV1=df_US_Presidents_3754_PipelineV1['rmse'].to_numpy().astype(float)
US_Presidents_3754RMSEPipelineV2=df_US_Presidents_3754_PipelineV2['rmse'].to_numpy().astype(float)
US_Presidents_3754RMSEPipelineV3=df_US_Presidents_3754_PipelineV3['rmse'].to_numpy().astype(float)
US_Presidents_3754RMSEPipelineV4=df_US_Presidents_3754_PipelineV4['rmse'].to_numpy().astype(float)
US_Presidents_3754RMSEPipelineV5=df_US_Presidents_3754_PipelineV5['rmse'].to_numpy().astype(float)

#
# US_Presidents_3754RecBaselineV1=df_US_Presidents_3754_BaselineV1['recall'].to_numpy().astype(float)
# US_Presidents_3754RecBaselineV2=df_US_Presidents_3754_BaselineV2['recall'].to_numpy().astype(float)
# US_Presidents_3754RecBaselineV3=df_US_Presidents_3754_BaselineV3['recall'].to_numpy().astype(float)
# US_Presidents_3754RecBaselineV4=df_US_Presidents_3754_BaselineV4['recall'].to_numpy().astype(float)
# US_Presidents_3754RecBaselineV5=df_US_Presidents_3754_BaselineV5['recall'].to_numpy().astype(float)
# US_Presidents_3754PreBaselineV1=df_US_Presidents_3754_BaselineV1['precision'].to_numpy().astype(float)
# US_Presidents_3754PreBaselineV2=df_US_Presidents_3754_BaselineV2['precision'].to_numpy().astype(float)
# US_Presidents_3754PreBaselineV3=df_US_Presidents_3754_BaselineV3['precision'].to_numpy().astype(float)
# US_Presidents_3754PreBaselineV4=df_US_Presidents_3754_BaselineV4['precision'].to_numpy().astype(float)
# US_Presidents_3754PreBaselineV5=df_US_Presidents_3754_BaselineV5['precision'].to_numpy().astype(float)
# US_Presidents_3754RMSEBaselineV1=df_US_Presidents_3754_BaselineV1['rmse'].to_numpy().astype(float)
# US_Presidents_3754RMSEBaselineV2=df_US_Presidents_3754_BaselineV2['rmse'].to_numpy().astype(float)
# US_Presidents_3754RMSEBaselineV3=df_US_Presidents_3754_BaselineV3['rmse'].to_numpy().astype(float)
# US_Presidents_3754RMSEBaselineV4=df_US_Presidents_3754_BaselineV4['rmse'].to_numpy().astype(float)
# US_Presidents_3754RMSEBaselineV5=df_US_Presidents_3754_BaselineV5['rmse'].to_numpy().astype(float)

US_Presidents_3754RecBaseline20V1=df_US_Presidents_3754_Baseline20V1['recall'].to_numpy().astype(float)
US_Presidents_3754RecBaseline20V2=df_US_Presidents_3754_Baseline20V2['recall'].to_numpy().astype(float)
US_Presidents_3754RecBaseline20V3=df_US_Presidents_3754_Baseline20V3['recall'].to_numpy().astype(float)
US_Presidents_3754RecBaseline20V4=df_US_Presidents_3754_Baseline20V4['recall'].to_numpy().astype(float)
US_Presidents_3754RecBaseline20V5=df_US_Presidents_3754_Baseline20V5['recall'].to_numpy().astype(float)
US_Presidents_3754PreBaseline20V1=df_US_Presidents_3754_Baseline20V1['precision'].to_numpy().astype(float)
US_Presidents_3754PreBaseline20V2=df_US_Presidents_3754_Baseline20V2['precision'].to_numpy().astype(float)
US_Presidents_3754PreBaseline20V3=df_US_Presidents_3754_Baseline20V3['precision'].to_numpy().astype(float)
US_Presidents_3754PreBaseline20V4=df_US_Presidents_3754_Baseline20V4['precision'].to_numpy().astype(float)
US_Presidents_3754PreBaseline20V5=df_US_Presidents_3754_Baseline20V5['precision'].to_numpy().astype(float)
US_Presidents_3754RMSEBaseline20V1=df_US_Presidents_3754_Baseline20V1['rmse'].to_numpy().astype(float)
US_Presidents_3754RMSEBaseline20V2=df_US_Presidents_3754_Baseline20V2['rmse'].to_numpy().astype(float)
US_Presidents_3754RMSEBaseline20V3=df_US_Presidents_3754_Baseline20V3['rmse'].to_numpy().astype(float)
US_Presidents_3754RMSEBaseline20V4=df_US_Presidents_3754_Baseline20V4['rmse'].to_numpy().astype(float)
US_Presidents_3754RMSEBaseline20V5=df_US_Presidents_3754_Baseline20V5['rmse'].to_numpy().astype(float)
#
#US_Presidents_3754RecHybridV1=df_US_Presidents_3754_HybridV1['recall'].to_numpy().astype(float)
#US_Presidents_3754RecHybridV2=df_US_Presidents_3754_HybridV2['recall'].to_numpy().astype(float)
#US_Presidents_3754RecHybridV3=df_US_Presidents_3754_HybridV3['recall'].to_numpy().astype(float)
#US_Presidents_3754RecHybridV4=df_US_Presidents_3754_HybridV4['recall'].to_numpy().astype(float)
#US_Presidents_3754RecHybridV5=df_US_Presidents_3754_HybridV5['recall'].to_numpy().astype(float)
#US_Presidents_3754PreHybridV1=df_US_Presidents_3754_HybridV1['precision'].to_numpy().astype(float)
#US_Presidents_3754PreHybridV2=df_US_Presidents_3754_HybridV2['precision'].to_numpy().astype(float)
#US_Presidents_3754PreHybridV3=df_US_Presidents_3754_HybridV3['precision'].to_numpy().astype(float)
#US_Presidents_3754PreHybridV4=df_US_Presidents_3754_HybridV4['precision'].to_numpy().astype(float)
#US_Presidents_3754PreHybridV5=df_US_Presidents_3754_HybridV5['precision'].to_numpy().astype(float)
#US_Presidents_3754RMSEHybridV1=df_US_Presidents_3754_HybridV1['rmse'].to_numpy().astype(float)
#US_Presidents_3754RMSEHybridV2=df_US_Presidents_3754_HybridV2['rmse'].to_numpy().astype(float)
#US_Presidents_3754RMSEHybridV3=df_US_Presidents_3754_HybridV3['rmse'].to_numpy().astype(float)
#US_Presidents_3754RMSEHybridV4=df_US_Presidents_3754_HybridV4['rmse'].to_numpy().astype(float)
#US_Presidents_3754RMSEHybridV5=df_US_Presidents_3754_HybridV5['rmse'].to_numpy().astype(float)
#
#arrays = [US_Presidents_3754RecPipelineNoRevV1, US_Presidents_3754RecPipelineNoRevV2, US_Presidents_3754RecPipelineNoRevV3, US_Presidents_3754RecPipelineNoRevV4, US_Presidents_3754RecPipelineNoRevV5]
#US_Presidents_3754RecPipelineNoRev = np.mean(arrays, axis=0)
#arrays = [US_Presidents_3754PrePipelineNoRevV1, US_Presidents_3754PrePipelineNoRevV2, US_Presidents_3754PrePipelineNoRevV3, US_Presidents_3754PrePipelineNoRevV4, US_Presidents_3754PrePipelineNoRevV5]
#US_Presidents_3754PrePipelineNoRev = np.mean(arrays, axis=0)
#arrays = [US_Presidents_3754RMSEPipelineNoRevV1, US_Presidents_3754RMSEPipelineNoRevV2, US_Presidents_3754RMSEPipelineNoRevV3, US_Presidents_3754RMSEPipelineNoRevV4, US_Presidents_3754RMSEPipelineNoRevV5]
#US_Presidents_3754RMSEPipelineNoRev = np.mean(arrays, axis=0)
#
# arrays = [US_Presidents_3754RecBaselineV1, US_Presidents_3754RecBaselineV2, US_Presidents_3754RecBaselineV3, US_Presidents_3754RecBaselineV4, US_Presidents_3754RecBaselineV5]
# US_Presidents_3754RecBaseline = np.mean(arrays, axis=0)
# arrays = [US_Presidents_3754PreBaselineV1, US_Presidents_3754PreBaselineV2, US_Presidents_3754PreBaselineV3, US_Presidents_3754PreBaselineV4, US_Presidents_3754PreBaselineV5]
# US_Presidents_3754PreBaseline = np.mean(arrays, axis=0)
# arrays = [US_Presidents_3754RMSEBaselineV1, US_Presidents_3754RMSEBaselineV2, US_Presidents_3754RMSEBaselineV3, US_Presidents_3754RMSEBaselineV4, US_Presidents_3754RMSEBaselineV5]
# US_Presidents_3754RMSEBaseline = np.mean(arrays, axis=0)

arrays = [US_Presidents_3754RecBaseline20V1, US_Presidents_3754RecBaseline20V2, US_Presidents_3754RecBaseline20V3, US_Presidents_3754RecBaseline20V4, US_Presidents_3754RecBaseline20V5]
US_Presidents_3754RecBaseline20 = np.mean(arrays, axis=0)
arrays = [US_Presidents_3754PreBaseline20V1, US_Presidents_3754PreBaseline20V2, US_Presidents_3754PreBaseline20V3, US_Presidents_3754PreBaseline20V4, US_Presidents_3754PreBaseline20V5]
US_Presidents_3754PreBaseline20 = np.mean(arrays, axis=0)
arrays = [US_Presidents_3754RMSEBaseline20V1, US_Presidents_3754RMSEBaseline20V2, US_Presidents_3754RMSEBaseline20V3, US_Presidents_3754RMSEBaseline20V4, US_Presidents_3754RMSEBaseline20V5]
US_Presidents_3754RMSEBaseline20 = np.mean(arrays, axis=0)

#arrays = [US_Presidents_3754RecHybridV1, US_Presidents_3754RecHybridV2, US_Presidents_3754RecHybridV3, US_Presidents_3754RecHybridV4, US_Presidents_3754RecHybridV5]
#US_Presidents_3754RecHybrid = np.mean(arrays, axis=0)
#arrays = [US_Presidents_3754PreHybridV1, US_Presidents_3754PreHybridV2, US_Presidents_3754PreHybridV3, US_Presidents_3754PreHybridV4, US_Presidents_3754PreHybridV5]
#US_Presidents_3754PreHybrid = np.mean(arrays, axis=0)
#arrays = [US_Presidents_3754RMSEHybridV1, US_Presidents_3754RMSEHybridV2, US_Presidents_3754RMSEHybridV3, US_Presidents_3754RMSEHybridV4, US_Presidents_3754RMSEHybridV5]
#US_Presidents_3754RMSEHybrid = np.mean(arrays, axis=0)
#
arrays = [US_Presidents_3754RecPipelineV1, US_Presidents_3754RecPipelineV2, US_Presidents_3754RecPipelineV3, US_Presidents_3754RecPipelineV4, US_Presidents_3754RecPipelineV5]
US_Presidents_3754RecPipeline = np.mean(arrays, axis=0)
arrays = [US_Presidents_3754PrePipelineV1, US_Presidents_3754PrePipelineV2, US_Presidents_3754PrePipelineV3, US_Presidents_3754PrePipelineV4, US_Presidents_3754PrePipelineV5]
US_Presidents_3754PrePipeline = np.mean(arrays, axis=0)
arrays = [US_Presidents_3754RMSEPipelineV1, US_Presidents_3754RMSEPipelineV2, US_Presidents_3754RMSEPipelineV3, US_Presidents_3754RMSEPipelineV4, US_Presidents_3754RMSEPipelineV5]
US_Presidents_3754RMSEPipeline = np.mean(arrays, axis=0)


#US_Presidents_3754F1PipelineNoRev = 2 * (US_Presidents_3754PrePipelineNoRev * US_Presidents_3754RecPipelineNoRev) / (US_Presidents_3754PrePipelineNoRev + US_Presidents_3754RecPipelineNoRev)
# US_Presidents_3754F1Baseline = 2 * (US_Presidents_3754PreBaseline * US_Presidents_3754RecBaseline) / (US_Presidents_3754PreBaseline + US_Presidents_3754RecBaseline)
US_Presidents_3754F1Baseline20 = 2 * (US_Presidents_3754PreBaseline20 * US_Presidents_3754RecBaseline20) / (US_Presidents_3754PreBaseline20 + US_Presidents_3754RecBaseline20)
#US_Presidents_3754F1Hybrid = 2 * (US_Presidents_3754PreHybrid * US_Presidents_3754RecHybrid) / (US_Presidents_3754PreHybrid + US_Presidents_3754RecHybrid)
US_Presidents_3754F1Pipeline = 2 * (US_Presidents_3754PrePipeline * US_Presidents_3754RecPipeline) / (US_Presidents_3754PrePipeline + US_Presidents_3754RecPipeline)


#US_Presidents_3754GMeanPipelineNoRev = np.sqrt(US_Presidents_3754PrePipelineNoRev * US_Presidents_3754RecPipelineNoRev)
#US_Presidents_3754GMeanBaseline = np.sqrt(US_Presidents_3754PreBaseline * US_Presidents_3754RecBaseline)
US_Presidents_3754GMeanBaseline20 = np.sqrt(US_Presidents_3754PreBaseline20 * US_Presidents_3754RecBaseline20)
#US_Presidents_3754GMeanHybrid = np.sqrt(US_Presidents_3754PreHybrid * US_Presidents_3754RecHybrid)
US_Presidents_3754GMeanPipeline = np.sqrt(US_Presidents_3754PrePipeline * US_Presidents_3754RecPipeline)

# beta=0.4
# US_Presidents_3754F0_5PipelineNoRev = (1 + beta**2) * (US_Presidents_3754PrePipelineNoRev * US_Presidents_3754RecPipelineNoRev) / ((beta**2 * US_Presidents_3754PrePipelineNoRev) + US_Presidents_3754RecPipelineNoRev)
# US_Presidents_3754F0_5Baseline = (1 + beta**2) * (US_Presidents_3754PreBaseline * US_Presidents_3754RecBaseline) / ((beta**2 * US_Presidents_3754PreBaseline) + US_Presidents_3754RecBaseline)
# US_Presidents_3754F0_5Baseline20 = (1 + beta**2) * (US_Presidents_3754PreBaseline20 * US_Presidents_3754RecBaseline20) / ((beta**2 * US_Presidents_3754PreBaseline20) + US_Presidents_3754RecBaseline20)
# US_Presidents_3754F0_5Hybrid = (1 + beta**2) * (US_Presidents_3754PreHybrid * US_Presidents_3754RecHybrid) / ((beta**2 * US_Presidents_3754PreHybrid) + US_Presidents_3754RecHybrid)
# US_Presidents_3754F0_5PipelineNoRevNoRev = (1 + beta**2) * (US_Presidents_3754PrePipelineNoRevNoRev * US_Presidents_3754RecPipelineNoRevNoRev) / ((beta**2 * US_Presidents_3754PrePipelineNoRevNoRev) + US_Presidents_3754RecPipelineNoRevNoRev)


r1 = np.arange(10)

fig, axs = plt.subplots(5, 1, figsize=(5,9), sharey=True)
fig.subplots_adjust(hspace=0.1, wspace=0.05)

axs[0].plot(r1, US_Presidents_3754PrePipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[0].plot(r1, US_Presidents_3754PreBaseline,marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[0].plot(r1, US_Presidents_3754PreBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
#axs[0].plot(r1, US_Presidents_3754PrePipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
#axs[0].plot(r1, US_Presidents_3754PreHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")


axs[1].plot(r1, US_Presidents_3754RecPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[1].plot(r1, US_Presidents_3754RecBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[1].plot(r1, US_Presidents_3754RecBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
#axs[1].plot(r1, US_Presidents_3754RecPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
#axs[1].plot(r1, US_Presidents_3754RecHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")





axs[2].plot(r1, US_Presidents_3754F1Pipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[2].plot(r1, US_Presidents_3754F1Baseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[2].plot(r1, US_Presidents_3754F1Baseline20, marker="2", markersize=10, color="#00748f", zorder=2)
#axs[2].plot(r1, US_Presidents_3754F1PipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
#axs[2].plot(r1, US_Presidents_3754F1Hybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[3].plot(r1, US_Presidents_3754GMeanPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[3].plot(r1, US_Presidents_3754GMeanBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[3].plot(r1, US_Presidents_3754GMeanBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
#axs[3].plot(r1, US_Presidents_3754GMeanPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
#axs[3].plot(r1, US_Presidents_3754GMeanHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[4].plot(r1, US_Presidents_3754RMSEPipeline, marker="x", markersize=8, color="#ff0000",zorder=3)
# axs[4].plot(r1, US_Presidents_3754RMSEBaseline, marker="+", markersize=10, color="#00C3CC", zorder=2)
axs[4].plot(r1, US_Presidents_3754RMSEBaseline20, marker="2", markersize=10, color="#00748f", zorder=2)
#axs[4].plot(r1, US_Presidents_3754RMSEPipelineNoRev, marker="o", markersize=5, color="#FFA600", zorder=2)
#axs[4].plot(r1, US_Presidents_3754RMSEHybrid, marker="2", markersize=10, color="#61a44f",zorder=3,linestyle="dashdot")

axs[0].set_xticks(np.arange(10),["1","2","3","4","5","10","20","30","40","50"])
axs[0].set_ylabel('Precision', rotation='vertical')
axs[0].set_title('US_Presidents', fontsize=12)

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

plt.savefig("US_Presidents_3754.pdf", bbox_inches='tight')
plt.show()
