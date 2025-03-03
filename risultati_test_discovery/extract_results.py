import json

datasets_incremental = {"actorfilms_4000": {"280":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "560":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "840":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "1120":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "1400":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "2800":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "5600":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "8400":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "11200":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "14000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                },
            "Boeing_1485":{"148":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "297":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "446":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "594":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "742":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "1485":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "2970":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "4455":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "5940":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "7425":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                           },
            "EV_Vehicles_4000":{"400":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "800":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "1200":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "1600":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "2000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "4000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "8000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "12000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "16000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "20000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                },
            "F1_REBUILT_5000":{"350":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "700":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "1050":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "1400":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "1750":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "3500":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "7000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "10500":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "14000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "17500":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                               },
            "Med_Ch_2500":{"300":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "600":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "900":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "1200":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "1500":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "3000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "6000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "9000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "12000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "15000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                           },
            "MotoGP_REBUILT_3000": {"360":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "720":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "1080":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "1440":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "1800":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "3600":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "7200":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "10800":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "14400":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "18000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                    },
            "NBA_3200": {"384":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "768":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "1152":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "1536":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "1920":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "3840":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "7680":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "11520":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "15360":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "19200":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                         },
            "superstore_4500": {"495":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "990":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "1485":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "1980":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "2475":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "4950":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "9900":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "14850":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "19800":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "24750":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                },
            "US_Presidents_3754": {"375":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "751":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "1126":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "1502":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "1877":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "3754":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "7508":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "11262":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "15016":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "18770":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                   }
            }
datasets_baseline = {"actorfilms_4000": {"280":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "560":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "840":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "1120":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "1400":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "2800":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "5600":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "8400":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "11200":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "14000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                },
            "Boeing_1485":{"148":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "297":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "446":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "594":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "742":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "1485":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "2970":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "4455":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "5940":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "7425":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                           },
            "EV_Vehicles_4000":{"400":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "800":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "1200":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "1600":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "2000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "4000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "8000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "12000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "16000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "20000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                },
            "F1_REBUILT_5000":{"350":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "700":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "1050":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "1400":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "1750":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "3500":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "7000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "10500":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "14000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                               "17500":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                               },
            "Med_Ch_2500":{"300":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "600":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "900":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "1200":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "1500":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "3000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "6000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "9000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "12000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "15000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                           },
            "MotoGP_REBUILT_3000": {"360":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "720":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "1080":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "1440":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "1800":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "3600":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "7200":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "10800":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "14400":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                    "18000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                    },
            "NBA_3200": {"384":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "768":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "1152":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "1536":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "1920":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "3840":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "7680":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "11520":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "15360":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                         "19200":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                         },
            "superstore_4500": {"495":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "990":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "1485":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "1980":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "2475":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "4950":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "9900":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "14850":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "19800":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                "24750":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                },
            "US_Presidents_3754": {"375":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "751":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "1126":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "1502":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "1877":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "3754":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "7508":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "11262":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "15016":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "18770":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                   }
            }


for ds in datasets_incremental.keys():
    print(ds)
    for versione in datasets_incremental[ds].keys():
        for i in range(1,6):
            # Leggi il JSON da un file
            with open(f'./ris_incremental/{ds}/analisi_{ds}_{versione}_{i}.json', 'r') as file:
                data = json.load(file)
            # Estrazione dei singoli valori
            datasets_incremental[ds][versione]["new"].append(data["new"])
            datasets_incremental[ds][versione]["found"].append(data["Found"])
            datasets_incremental[ds][versione]["not"].append(data["notFound"])
            datasets_incremental[ds][versione]["gen"].append(data["generalized"])
            datasets_incremental[ds][versione]["spec"].append(data["specialized"])

            with open(f'./ris_baseline//{ds}/analisi_{ds}_{versione}_{i}.json', 'r') as file:
                data2 = json.load(file)
            # Estrazione dei singoli valori
            datasets_baseline[ds][versione]["new"].append(data2["new"])
            datasets_baseline[ds][versione]["found"].append(data2["Found"])
            datasets_baseline[ds][versione]["not"].append(data2["notFound"])
            datasets_baseline[ds][versione]["gen"].append(data2["generalized"])
            datasets_baseline[ds][versione]["spec"].append(data2["specialized"])

with open(f"./ris_baseline/results_baseline.json", "w") as outfile:
    json.dump(datasets_baseline, outfile)

with open(f"./ris_incremental/results_incremental.json", "w") as outfile2:
    json.dump(datasets_incremental, outfile2)