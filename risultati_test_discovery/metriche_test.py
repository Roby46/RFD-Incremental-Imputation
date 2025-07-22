import json
import pandas as pd


datasets = [("actorfilms_4000",["280","560","840","1120","1400","2800","5600","8400","11200","14000"]),
            ("Boeing_898",["90","180","269","359","449","898","1796","2694","3592","4490"]),
            ("EV_Vehicles_4000",["400","800","1200","1600","2000","4000","8000","12000","16000","20000"]),
            ("F1_REBUILT_5000",["350","700","1050","1400","1750","3500","7000","10500","14000","17500"]),
            ("Med_Ch_2500",["300","600","900","1200","1500","3000","6000","9000","12000","15000"]),
            ("MotoGP_REBUILT_3000",["360","720","1080","1440","1800","3600","7200","10800","14400","18000"]),
            ("NBA_3200",["384","768","1152","1536","1920","3840","7680","11520","15360","19200"]),
            ("superstore_4500",["495","990","1485","1980","2475","4950","9900","14850","19800","24750"]),
            ("US_Presidents_3754",["375","751","1126","1502","1877","3754","7508","11262","15016","18770"]),
            ("cars",["37","73","110","146","183","365","731","1096","1462","1827"]),
            ("police",["198","397","595","793","992","1984","3967","5951","7934","9918"]),
            ("restaurant",["52","104","156","207","259","518","1037","1555","2074","2592"]),
            ("IoT_Telemetry3000",["240","480","720","960","1200","2400","4800","7200","9600","12000"]),
            ("Air_9000",["1170","2340","3510","4680","5850","11700","23400","35100","46800","58500"]),
            ("Cats_1071",["107","214","321","428","536","1071","2142","3213","4284","5355"])
            ]

datasets_mnar = [("Boeing_898_MNAR",["90","180","269","359","449","898","1796","2694","3592","4490"]),
            ("cars_MNAR",["37","73","110","146","183","365","731","1096","1462","1827"]),
            ("police_MNAR",["198","397","595","793","992","1984","3967","5951","7934","9918"]),
            ("restaurant_MNAR",["52","104","156","207","259","518","1037","1555","2074","2592"])
            ]


datasets_mbuv = [("Boeing_898_MBUV",["90","180","269","359","449","898","1796","2694","3592","4490"]),
            ("cars_MBUV",["37","73","110","146","183","365","731","1096","1462","1827"]),
            ("police_MBUV",["198","397","595","793","992","1984","3967","5951","7934","9918"]),
            ("restaurant_MBUV",["52","104","156","207","259","518","1037","1555","2074","2592"])
            ]


datasets_fd = [("Boeing_898_FD",["90","180","269","359","449","898","1796","2694","3592","4490"]),
            ("cars_FD",["37","73","110","146","183","365","731","1096","1462","1827"]),
            ("police_FD",["198","397","595","793","992","1984","3967","5951","7934","9918"]),
            ("restaurant_FD",["52","104","156","207","259","518","1037","1555","2074","2592"])
            ]


dict_plot_m1 = {"dataset":[],"algoritmo":[],"MV":[],"metric1":[]}
dict_plot_m2 = {"dataset":[],"algoritmo":[],"MV":[],"metric2":[]}

def metric1(spec, gen, nw, nf, oracle, coeff):
    numerator = nf + coeff * spec + coeff * gen + nw
    denominator = oracle + nw
    if denominator == 0:
        return 0
    value = numerator / denominator
    return round(min(value, 1),2)

def metric2(spec, gen, nf, oracle, coeff):
    numerator = nf + coeff * spec + coeff * gen
    denominator = oracle
    if denominator == 0:
        return 0
    value = numerator / denominator
    return round(min(value, 1),2)

def compute_metrics(alg,ds,mr,spec, gen, new, not_found, found,coeff,dataset_type):
    #Numero di RFD dell'oracolo
    num_rfd_oracle=spec+gen+found+not_found

    #Coefficiente per spec e gen (peso dimezzato)
    spec_gen_coeff=coeff
    print(metric1(spec, gen, new, not_found, num_rfd_oracle, spec_gen_coeff))
    print(metric2(spec, gen, not_found, num_rfd_oracle, spec_gen_coeff), "\n")



    dict_plot_m1["dataset"].append(dataset_type[ds][0])
    dict_plot_m2["dataset"].append(dataset_type[ds][0])
    dict_plot_m1["algoritmo"].append(alg)
    dict_plot_m2["algoritmo"].append(alg)
    dict_plot_m1["MV"].append(dataset_type[ds][1][int(mr)-1])
    dict_plot_m2["MV"].append(dataset_type[ds][1][int(mr)-1])
    dict_plot_m1["metric1"].append(metric1(spec,gen,new,not_found,num_rfd_oracle,spec_gen_coeff))
    dict_plot_m2["metric2"].append(metric2(spec,gen,not_found,num_rfd_oracle,spec_gen_coeff))

#specialized=5
#generalized=1
#new=6
#not_found=3
#found=6
coeff = 0.5

'''
with open(f"./ris_incremental/metrics_medie_incremental_fd.json", "r") as outfile2:
    dict_finale = json.load(outfile2)
    #print(dict_finale)

with open(f"./ris_baseline/medie_metrics_baseline_fd.json", "r") as outfile3:
    dict_finale2 = json.load(outfile3)

for ds in range (0,4):
    print("ds:",ds)
    for mr in dict_finale.keys():
        #print("dataset:",ds)
        #print(mr)
        print("incremental:",dict_finale[mr][ds])
        compute_metrics("pipeline",ds,mr,dict_finale[mr][ds][3],dict_finale[mr][ds][2],dict_finale[mr][ds][4],dict_finale[mr][ds][1],dict_finale[mr][ds][0],coeff,datasets_fd)
        print("baseline:", dict_finale2[mr][ds])
        compute_metrics("baseline",ds,mr,dict_finale2[mr][ds][3], dict_finale2[mr][ds][2], dict_finale2[mr][ds][4], dict_finale2[mr][ds][1],dict_finale2[mr][ds][0],coeff,datasets_fd)


print(dict_plot_m1)
ds1 = pd.DataFrame(dict_plot_m1)
ds1.to_csv(f".\All_Results_metric1_fd_{coeff}.csv",sep=";",index=False)
ds2 = pd.DataFrame(dict_plot_m2)
ds2.to_csv(f".\All_Results_metric2_fd_{coeff}.csv",sep=";",index=False)


dict_plot_m1 = {"dataset":[],"algoritmo":[],"MV":[],"metric1":[]}
dict_plot_m2 = {"dataset":[],"algoritmo":[],"MV":[],"metric2":[]}
with open(f"./ris_incremental/metrics_medie_incremental_mbuv.json", "r") as outfile2:
    dict_finale = json.load(outfile2)
    #print(dict_finale)

with open(f"./ris_baseline/medie_metrics_baseline_mbuv.json", "r") as outfile3:
    dict_finale2 = json.load(outfile3)

for ds in range (0,4):
    print("ds:",ds)
    for mr in dict_finale.keys():
        #print("dataset:",ds)
        #print(mr)
        print("incremental:",dict_finale[mr][ds])
        compute_metrics("pipeline",ds,mr,dict_finale[mr][ds][3],dict_finale[mr][ds][2],dict_finale[mr][ds][4],dict_finale[mr][ds][1],dict_finale[mr][ds][0],coeff,datasets_mbuv)
        print("baseline:", dict_finale2[mr][ds])
        compute_metrics("baseline",ds,mr,dict_finale2[mr][ds][3], dict_finale2[mr][ds][2], dict_finale2[mr][ds][4], dict_finale2[mr][ds][1],dict_finale2[mr][ds][0],coeff,datasets_mbuv)

print(dict_plot_m1)
ds1 = pd.DataFrame(dict_plot_m1)
ds1.to_csv(f".\All_Results_metric1_mbuv_{coeff}.csv",sep=";",index=False)
ds2 = pd.DataFrame(dict_plot_m2)
ds2.to_csv(f".\All_Results_metric2_mbuv_{coeff}.csv",sep=";",index=False)


dict_plot_m1 = {"dataset":[],"algoritmo":[],"MV":[],"metric1":[]}
dict_plot_m2 = {"dataset":[],"algoritmo":[],"MV":[],"metric2":[]}
with open(f"./ris_incremental/metrics_medie_incremental_mnar.json", "r") as outfile2:
    dict_finale = json.load(outfile2)
    #print(dict_finale)

with open(f"./ris_baseline/medie_metrics_baseline_mnar.json", "r") as outfile3:
    dict_finale2 = json.load(outfile3)

for ds in range (0,4):
    print("ds:",ds)
    for mr in dict_finale.keys():
        #print("dataset:",ds)
        #print(mr)
        print("incremental:",dict_finale[mr][ds])
        compute_metrics("pipeline",ds,mr,dict_finale[mr][ds][3],dict_finale[mr][ds][2],dict_finale[mr][ds][4],dict_finale[mr][ds][1],dict_finale[mr][ds][0],coeff,datasets_mnar)
        print("baseline:", dict_finale2[mr][ds])
        compute_metrics("baseline",ds,mr,dict_finale2[mr][ds][3], dict_finale2[mr][ds][2], dict_finale2[mr][ds][4], dict_finale2[mr][ds][1],dict_finale2[mr][ds][0],coeff,datasets_mnar)

print(dict_plot_m1)
ds1 = pd.DataFrame(dict_plot_m1)
ds1.to_csv(f".\All_Results_metric1_mnar_{coeff}.csv",sep=";",index=False)
ds2 = pd.DataFrame(dict_plot_m2)
ds2.to_csv(f".\All_Results_metric2_mnar_{coeff}.csv",sep=";",index=False)
'''

dict_plot_m1 = {"dataset":[],"algoritmo":[],"MV":[],"metric1":[]}
dict_plot_m2 = {"dataset":[],"algoritmo":[],"MV":[],"metric2":[]}


with open(f"./ris_incremental/metrics_medie_incremental.json", "r") as outfile2:
    dict_finale = json.load(outfile2)
    #print(dict_finale)

with open(f"./ris_baseline/medie_metrics_baseline.json", "r") as outfile3:
    dict_finale2 = json.load(outfile3)

for ds in range (0,15):
    print("ds:",ds)
    for mr in dict_finale.keys():
        #print("dataset:",ds)
        #print(mr)
        print("incremental:",dict_finale[mr][ds])
        compute_metrics("pipeline",ds,mr,dict_finale[mr][ds][3],dict_finale[mr][ds][2],dict_finale[mr][ds][4],dict_finale[mr][ds][1],dict_finale[mr][ds][0],coeff,datasets)
        print("baseline:", dict_finale2[mr][ds])
        compute_metrics("baseline",ds,mr,dict_finale2[mr][ds][3], dict_finale2[mr][ds][2], dict_finale2[mr][ds][4], dict_finale2[mr][ds][1],dict_finale2[mr][ds][0],coeff,datasets)

print(dict_plot_m1)
ds1 = pd.DataFrame(dict_plot_m1)
ds1.to_csv(f".\All_Results_metric1_{coeff}.csv",sep=";",index=False)
ds2 = pd.DataFrame(dict_plot_m2)
ds2.to_csv(f".\All_Results_metric2_{coeff}.csv",sep=";",index=False)


