import json

datasets_incremental = {
            "actorfilms_4000": {"280":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
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
            "Boeing_898":{"90":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "180":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "269":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "359":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "449":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "898":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "1796":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "2694":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "3592":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "4490":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
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
                                   },
            "cars": {"37": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                     "73": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                     "110": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                     "146": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                     "183": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                     "365": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                     "731": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                     "1096": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                     "1462": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                     "1827": {"new": [], "found": [], "not": [], "gen": [], "spec": []}
                     },
            "police": {"198": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                       "397": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                       "595": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                       "793": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                       "992": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                       "1984": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                       "3967": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                       "5951": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                       "7934": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                       "9918": {"new": [], "found": [], "not": [], "gen": [], "spec": []}
                       },
            "restaurant": {"52": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                           "104": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                           "156": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                           "207": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                           "259": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                           "518": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                           "1037": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                           "1555": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                           "2074": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                           "2592": {"new": [], "found": [], "not": [], "gen": [], "spec": []}
                           },
            "IoT_Telemetry3000": {"240": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "480": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "720": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "960": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "1200": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "2400": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "4800": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "7200": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "9600": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "12000": {"new": [], "found": [], "not": [], "gen": [], "spec": []}
                                  },
            "Air_9000": {"1170": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "2340": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "3510": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "4680": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "5850": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "11700": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "23400": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "35100": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "46800": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "58500": {"new": [], "found": [], "not": [], "gen": [], "spec": []}
                                  },
            "Cats_1071": {"107": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "214": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "321": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "428": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "536": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "1071": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "2142": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "3213": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "4284": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                                  "5355": {"new": [], "found": [], "not": [], "gen": [], "spec": []}
                                }
            }
datasets_baseline = {
            "actorfilms_4000": {"280":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
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
            "Boeing_898":{"90":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "180":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "269":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "359":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "449":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "898":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "1796":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "2694":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "3592":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                           "4490":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
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
                                   },
            "cars": {"37":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "73":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "110":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "146":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "183":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "365":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "731":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "1096":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "1462":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "1827":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                   },
            "police": {"198":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "397":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "595":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "793":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "992":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "1984":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "3967":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "5951":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "7934":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "9918":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                   },
            "restaurant": {"52":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "104":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "156":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "207":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "259":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "518":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "1037":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "1555":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "2074":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "2592":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                   },
            "IoT_Telemetry3000": {"240":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "480":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "720":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "960":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "1200":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "2400":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "4800":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "7200":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "9600":{"new":[],"found":[],"not":[],"gen":[],"spec":[]},
                                   "12000":{"new":[],"found":[],"not":[],"gen":[],"spec":[]}
                                   },
            "Air_9000": {"1170": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                         "2340": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                         "3510": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                         "4680": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                         "5850": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                         "11700": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                         "23400": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                         "35100": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                         "46800": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                         "58500": {"new": [], "found": [], "not": [], "gen": [], "spec": []}
                         },
            "Cats_1071": {"107": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                          "214": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                          "321": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                          "428": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                          "536": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                          "1071": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                          "2142": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                          "3213": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                          "4284": {"new": [], "found": [], "not": [], "gen": [], "spec": []},
                          "5355": {"new": [], "found": [], "not": [], "gen": [], "spec": []}
                          }
            }

datasets_incremental2 = {
            "actorfilms_4000": {"280":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "560":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "840":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "1120":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "1400":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "2800":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "5600":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "8400":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "11200":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "14000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                                },
            "Boeing_898":{"90":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "180":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "269":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "359":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "449":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "898":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "1796":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "2694":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "3592":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "4490":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                           },
            "EV_Vehicles_4000":{"400":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "800":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "1200":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "1600":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "2000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "4000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "8000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "12000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "16000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "20000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                                },
            "F1_REBUILT_5000":{"350":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "700":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "1050":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "1400":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "1750":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "3500":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "7000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "10500":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "14000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "17500":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                               },
            "Med_Ch_2500":{"300":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "600":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "900":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "1200":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "1500":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "3000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "6000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "9000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "12000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "15000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                           },
            "MotoGP_REBUILT_3000": {"360":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "720":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "1080":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "1440":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "1800":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "3600":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "7200":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "10800":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "14400":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "18000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                                    },
            "NBA_3200": {"384":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "768":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "1152":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "1536":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "1920":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "3840":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "7680":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "11520":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "15360":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "19200":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                         },
            "superstore_4500": {"495":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "990":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "1485":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "1980":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "2475":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "4950":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "9900":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "14850":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "19800":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "24750":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                                },
            "US_Presidents_3754": {"375":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "751":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "1126":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "1502":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "1877":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "3754":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "7508":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "11262":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "15016":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "18770":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                                   },
            "cars": {"37": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "73": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "110": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "146": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "183": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "365": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "731": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1096": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1462": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1827": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                     },
            "police": {"198": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "397": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "595": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "793": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "992": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "1984": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "3967": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "5951": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "7934": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "9918": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                       },
            "restaurant": {"52": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "104": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "156": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "207": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "259": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "518": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1037": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1555": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2074": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2592": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                           },
            "IoT_Telemetry3000": {"240": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "480": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "720": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "960": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "1200": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "2400": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "4800": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "7200": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "9600": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "12000": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                                  },
            "Air_9000": {"1170": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "2340": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "3510": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "4680": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "5850": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "11700": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "23400": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "35100": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "46800": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "58500": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                         },
            "Cats_1071": {"107": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "214": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "321": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "428": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "536": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "1071": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "2142": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "3213": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "4284": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "5355": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                  }
            }
datasets_baseline2 = {
            "actorfilms_4000": {"280":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "560":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "840":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "1120":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "1400":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "2800":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "5600":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "8400":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "11200":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "14000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                                },
            "Boeing_898": {"90": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "180": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "269": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "359": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "449": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "898": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1796": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2694": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "3592": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "4490": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                           },
            "EV_Vehicles_4000":{"400":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "800":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "1200":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "1600":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "2000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "4000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "8000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "12000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "16000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "20000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                                },
            "F1_REBUILT_5000":{"350":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "700":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "1050":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "1400":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "1750":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "3500":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "7000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "10500":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "14000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                               "17500":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                               },
            "Med_Ch_2500":{"300":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "600":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "900":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "1200":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "1500":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "3000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "6000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "9000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "12000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "15000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                           },
            "MotoGP_REBUILT_3000": {"360":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "720":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "1080":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "1440":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "1800":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "3600":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "7200":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "10800":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "14400":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                    "18000":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                                    },
            "NBA_3200": {"384":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "768":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "1152":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "1536":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "1920":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "3840":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "7680":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "11520":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "15360":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                         "19200":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                         },
            "superstore_4500": {"495":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "990":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "1485":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "1980":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "2475":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "4950":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "9900":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "14850":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "19800":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                "24750":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                                },
            "US_Presidents_3754": {"375":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "751":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "1126":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "1502":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "1877":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "3754":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "7508":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "11262":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "15016":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                                   "18770":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                                   },
            "cars": {"37": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "73": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "110": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "146": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "183": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "365": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "731": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1096": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1462": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1827": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                     },
            "police": {"198": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "397": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "595": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "793": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "992": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "1984": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "3967": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "5951": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "7934": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "9918": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                       },
            "restaurant": {"52": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "104": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "156": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "207": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "259": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "518": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1037": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1555": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2074": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2592": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                           },
            "IoT_Telemetry3000": {"240": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "480": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "720": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "960": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "1200": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "2400": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "4800": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "7200": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "9600": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                                  "12000": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                                  },
            "Air_9000": {"1170": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "2340": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "3510": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "4680": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "5850": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "11700": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "23400": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "35100": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "46800": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                         "58500": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                         },
            "Cats_1071": {"107": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "214": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "321": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "428": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "536": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "1071": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "2142": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "3213": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "4284": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                          "5355": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                  }
            }

datasets_incremental_mnar = {
            "Boeing_898_MNAR":{"90":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "180":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "269":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "359":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "449":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "898":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "1796":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "2694":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "3592":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "4490":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                           },
            "cars_MNAR": {"37": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "73": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "110": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "146": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "183": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "365": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "731": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1096": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1462": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1827": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                     },
            "police_MNAR": {"198": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "397": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "595": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "793": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "992": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "1984": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "3967": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "5951": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "7934": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "9918": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                       },
            "restaurant_MNAR": {"52": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "104": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "156": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "207": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "259": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "518": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1037": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1555": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2074": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2592": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                           }
            }
datasets_baseline_mnar = {
            "Boeing_898_MNAR":{"90":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "180":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "269":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "359":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "449":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "898":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "1796":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "2694":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "3592":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "4490":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                           },
            "cars_MNAR": {"37": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "73": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "110": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "146": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "183": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "365": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "731": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1096": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1462": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1827": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                     },
            "police_MNAR": {"198": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "397": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "595": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "793": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "992": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "1984": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "3967": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "5951": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "7934": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "9918": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                       },
            "restaurant_MNAR": {"52": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "104": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "156": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "207": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "259": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "518": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1037": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1555": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2074": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2592": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                           }
            }

datasets_incremental_mbuv = {
            "Boeing_898_MBUV":{"90":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "180":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "269":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "359":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "449":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "898":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "1796":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "2694":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "3592":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "4490":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                           },
            "cars_MBUV": {"37": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "73": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "110": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "146": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "183": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "365": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "731": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1096": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1462": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1827": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                     },
            "police_MBUV": {"198": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "397": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "595": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "793": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "992": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "1984": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "3967": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "5951": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "7934": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "9918": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                       },
            "restaurant_MBUV": {"52": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "104": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "156": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "207": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "259": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "518": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1037": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1555": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2074": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2592": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                           }
            }
datasets_baseline_mbuv = {
            "Boeing_898_MBUV":{"90":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "180":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "269":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "359":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "449":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "898":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "1796":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "2694":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "3592":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "4490":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                           },
            "cars_MBUV": {"37": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "73": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "110": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "146": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "183": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "365": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "731": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1096": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1462": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1827": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                     },
            "police_MBUV": {"198": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "397": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "595": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "793": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "992": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "1984": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "3967": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "5951": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "7934": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "9918": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                       },
            "restaurant_MBUV": {"52": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "104": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "156": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "207": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "259": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "518": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1037": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1555": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2074": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2592": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                           }
            }

datasets_incremental_fd = {
            "Boeing_898_FD":{"90":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "180":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "269":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "359":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "449":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "898":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "1796":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "2694":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "3592":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "4490":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                           },
            "cars_FD": {"37": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "73": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "110": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "146": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "183": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "365": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "731": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1096": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1462": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1827": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                     },
            "police_FD": {"198": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "397": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "595": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "793": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "992": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "1984": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "3967": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "5951": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "7934": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "9918": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                       },
            "restaurant_FD": {"52": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "104": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "156": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "207": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "259": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "518": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1037": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1555": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2074": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2592": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                           }
            }
datasets_baseline_fd = {
            "Boeing_898_FD":{"90":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "180":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "269":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "359":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "449":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "898":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "1796":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "2694":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "3592":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]},
                           "4490":{"new":[],"found":[],"not":[],"gen":[],"spec":[],"oracolo":[],"test":[]}
                           },
            "cars_FD": {"37": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "73": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "110": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "146": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "183": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "365": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "731": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1096": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1462": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                     "1827": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                     },
            "police_FD": {"198": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "397": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "595": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "793": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "992": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "1984": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "3967": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "5951": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "7934": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                       "9918": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                       },
            "restaurant_FD": {"52": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "104": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "156": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "207": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "259": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "518": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1037": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "1555": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2074": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]},
                           "2592": {"new": [], "found": [], "not": [], "gen": [], "spec": [],"oracolo":[],"test":[]}
                           }
            }


def extract_for_plot():
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



    dict_finale = {"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"9":[],"10":[]}
    for ds in datasets_baseline.keys():
        print(ds)
        count = 1
        for perc in datasets_baseline[ds].keys():
            valori_da_mediare = datasets_baseline[ds][perc]
            array_medie = []
            array_medie.append(round(sum(datasets_baseline[ds][perc]["found"]) / len(datasets_baseline[ds][perc]["found"]),2))
            array_medie.append(round(sum(datasets_baseline[ds][perc]["not"]) / len(datasets_baseline[ds][perc]["not"]),2))
            array_medie.append(round(sum(datasets_baseline[ds][perc]["gen"]) / len(datasets_baseline[ds][perc]["gen"]),2))
            array_medie.append(round(sum(datasets_baseline[ds][perc]["spec"]) / len(datasets_baseline[ds][perc]["spec"]),2))
            array_medie.append(round(sum(datasets_baseline[ds][perc]["new"]) / len(datasets_baseline[ds][perc]["new"]),2))
            dict_finale[str(count)].append(array_medie)
            count += 1

    with open(f"./ris_baseline/medie_baseline.json", "w") as outfile:
        json.dump(dict_finale, outfile)


    dict_finale = {"1":[],"2":[],"3":[],"4":[],"5":[],"6":[],"7":[],"8":[],"9":[],"10":[]}
    for ds in datasets_incremental.keys():
        count = 1
        for perc in datasets_incremental[ds].keys():
            valori_da_mediare = datasets_incremental[ds][perc]
            array_medie = []
            array_medie.append(round(sum(datasets_incremental[ds][perc]["found"]) / len(datasets_incremental[ds][perc]["found"]),2))
            array_medie.append(round(sum(datasets_incremental[ds][perc]["not"]) / len(datasets_incremental[ds][perc]["not"]),2))
            array_medie.append(round(sum(datasets_incremental[ds][perc]["gen"]) / len(datasets_incremental[ds][perc]["gen"]),2))
            array_medie.append(round(sum(datasets_incremental[ds][perc]["spec"]) / len(datasets_incremental[ds][perc]["spec"]),2))
            array_medie.append(round(sum(datasets_incremental[ds][perc]["new"]) / len(datasets_incremental[ds][perc]["new"]),2))
            dict_finale[str(count)].append(array_medie)
            count += 1

    with open(f"./ris_incremental/medie_incremental.json", "w") as outfile:
        json.dump(dict_finale, outfile)

def extract_for_metrics():
    for ds in datasets_incremental_fd.keys():
        print(ds)
        for versione in datasets_incremental_fd[ds].keys():
            for i in range(1, 6):
                # Leggi il JSON da un file
                with open(f'./ris_incremental/{ds}/count_{ds}_{versione}_{i}.json', 'r') as file:
                    data = json.load(file)
                # Estrazione dei singoli valori
                print(f'./ris_incremental/{ds}/count_{ds}_{versione}_{i}')
                datasets_incremental_fd[ds][versione]["new"].append(data["new"])
                datasets_incremental_fd[ds][versione]["found"].append(data["Found"])
                datasets_incremental_fd[ds][versione]["not"].append(data["notFound"])
                datasets_incremental_fd[ds][versione]["gen"].append(data["generalized"])
                datasets_incremental_fd[ds][versione]["spec"].append(data["specialized"])
                datasets_incremental_fd[ds][versione]["oracolo"].append(data["oracolo"])
                datasets_incremental_fd[ds][versione]["test"].append(data["test"])

                with open(f'./ris_baseline//{ds}/count_{ds}_{versione}_{i}.json', 'r') as file:
                    data2 = json.load(file)
                # Estrazione dei singoli valori
                datasets_baseline_fd[ds][versione]["new"].append(data2["new"])
                datasets_baseline_fd[ds][versione]["found"].append(data2["Found"])
                datasets_baseline_fd[ds][versione]["not"].append(data2["notFound"])
                datasets_baseline_fd[ds][versione]["gen"].append(data2["generalized"])
                datasets_baseline_fd[ds][versione]["spec"].append(data2["specialized"])
                datasets_baseline_fd[ds][versione]["oracolo"].append(data["oracolo"])
                datasets_baseline_fd[ds][versione]["test"].append(data["test"])

    with open(f"./ris_baseline/results_metrics_baseline_fd.json", "w") as outfile:
        json.dump(datasets_baseline_fd, outfile)

    with open(f"./ris_incremental/results_metrics_incremental_fd.json", "w") as outfile2:
        json.dump(datasets_incremental_fd, outfile2)

    dict_finale = {"1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [], "10": []}
    for ds in datasets_baseline_fd.keys():
        print(ds)
        count = 1
        for perc in datasets_baseline_fd[ds].keys():
            valori_da_mediare = datasets_baseline_fd[ds][perc]
            array_medie = []
            array_medie.append(
                round(sum(datasets_baseline_fd[ds][perc]["found"]) / len(datasets_baseline_fd[ds][perc]["found"]), 2))
            array_medie.append(
                round(sum(datasets_baseline_fd[ds][perc]["not"]) / len(datasets_baseline_fd[ds][perc]["not"]), 2))
            array_medie.append(
                round(sum(datasets_baseline_fd[ds][perc]["gen"]) / len(datasets_baseline_fd[ds][perc]["gen"]), 2))
            array_medie.append(
                round(sum(datasets_baseline_fd[ds][perc]["spec"]) / len(datasets_baseline_fd[ds][perc]["spec"]), 2))
            array_medie.append(
                round(sum(datasets_baseline_fd[ds][perc]["new"]) / len(datasets_baseline_fd[ds][perc]["new"]), 2))
            array_medie.append(
                round(sum(datasets_baseline_fd[ds][perc]["oracolo"]) / len(datasets_baseline_fd[ds][perc]["oracolo"]), 2))
            array_medie.append(
                round(sum(datasets_baseline_fd[ds][perc]["test"]) / len(datasets_baseline_fd[ds][perc]["test"]), 2))
            dict_finale[str(count)].append(array_medie)
            count += 1

    with open(f"./ris_baseline/medie_metrics_baseline_fd.json", "w") as outfile:
        json.dump(dict_finale, outfile)

    dict_finale = {"1": [], "2": [], "3": [], "4": [], "5": [], "6": [], "7": [], "8": [], "9": [], "10": []}
    for ds in datasets_incremental_fd.keys():
        count = 1
        for perc in datasets_incremental_fd[ds].keys():
            print(perc)
            valori_da_mediare = datasets_incremental_fd[ds][perc]
            array_medie = []
            array_medie.append(
                round(sum(datasets_incremental_fd[ds][perc]["found"]) / len(datasets_incremental_fd[ds][perc]["found"]), 2))
            array_medie.append(
                round(sum(datasets_incremental_fd[ds][perc]["not"]) / len(datasets_incremental_fd[ds][perc]["not"]), 2))
            array_medie.append(
                round(sum(datasets_incremental_fd[ds][perc]["gen"]) / len(datasets_incremental_fd[ds][perc]["gen"]), 2))
            array_medie.append(
                round(sum(datasets_incremental_fd[ds][perc]["spec"]) / len(datasets_incremental_fd[ds][perc]["spec"]), 2))
            array_medie.append(
                round(sum(datasets_incremental_fd[ds][perc]["new"]) / len(datasets_incremental_fd[ds][perc]["new"]), 2))
            array_medie.append(
                round(sum(datasets_incremental_fd[ds][perc]["oracolo"]) / len(datasets_incremental_fd[ds][perc]["oracolo"]), 2))
            array_medie.append(
                round(sum(datasets_incremental_fd[ds][perc]["test"]) / len(datasets_incremental_fd[ds][perc]["test"]), 2))
            dict_finale[str(count)].append(array_medie)
            count += 1

    with open(f"./ris_incremental/metrics_medie_incremental_fd.json", "w") as outfile:
        json.dump(dict_finale, outfile)

extract_for_plot()
extract_for_metrics()    #ogni key è un missing rate, ed in ognuno di essi ci sono tanti array quanti sono i dataset