import csv as csv
import json
import copy
import numpy as np

class RFD():
    def __init__(self, RHS, LHS, label_attributi, thres_attributi, stampaRHS, stampaLHS, found):
        self.RHS = RHS
        self.LHS = LHS
        self.label_attributi = label_attributi
        self.thres_attributi = thres_attributi
        self.stampaRHS = stampaRHS
        self.stampaLHS = stampaLHS
        self.found = found

    # def __str__(self): return ("RHS: " + str(self.RHS) + "  LHS: " + str(self.LHS) + "  label_attributi: " + str(self.label_attributi) + "  thres_attributi: " + str(self.thres_attributi) + "  stampaRHS: " + str(self.stampaRHS) + "  stampaLHS: " + str(self.stampaLHS))
    def __str__(self): return ("RHS: " + str(self.stampaRHS) + "  LHS: " + str(self.stampaLHS))

def readRFDcsv(path):
    LHS = set()
    RFDs = []
    label_attributi = []
    stampaLHS = []
    thres_attributi = np.array([])
    line_count = 0
    with open(path, "r") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if line_count == 0:
                global header
                header = row
                line_count += 1
            else:
                index = 0
                for item in row:
                    if index == 0:
                        RHS = item
                        index += 1
                    else:
                        if item != "?":
                            if header.__getitem__(index) != RHS:
                                single_lhs = (header.__getitem__(index), str(item))
                                LHS.add(single_lhs)
                                label_attributi.append(header.__getitem__(index))
                                thres_attributi = np.append(thres_attributi, float(item))
                                stampaLHS.append(header.__getitem__(index) + "_" + str(item))
                                index += 1
                            else:
                                RHS = (RHS, float(item))
                                stampaRHS = RHS[0] + "_" + str(item)
                                index += 1
                        else:
                            index += 1
                line_count += 1
                dep = RFD(RHS, LHS, label_attributi, thres_attributi, stampaRHS, stampaLHS, False)
                #print(dep)
                RFDs.append(dep)
                label_attributi = []
                thres_attributi = []
                LHS = set()
                stampaLHS = []
    return RFDs

def create_json(oracle, rfdsfile, nomedataset,versione,iteration, tipologia):
    # print("RFD calcolate su dataset completo:")
    print(f"oracolo: {oracle}")
    RFDsfullDS = readRFDcsv(oracle)
    # print("\n\n RFD calcolate su dataset incompleto:")
    RFDstoTest = readRFDcsv(rfdsfile)
    print(f"file da valutare: {rfdsfile}")

    stampe_per_plot = {}
    stampe_per_metriche = {}
    gendiverse = []
    specdiverse = []
    originaliTrovate = 0
    countspec = 0
    coutngen = 0
    countnonTrovate = 0
    countnuove = 0
    RFDspec = []
    RFDgen = []
    RFDtrovate = []
    RFDnuove = []
    RFDnontrovate = []
    global attributes
    RHSoriginali = {
        "name": object,
        "children": []
    }
    LHSoriginali = {
        "name": object,
        "children": []
    }
    stringhe = {
        "name": object,
        "value": 0
    }
    specMap = {
        "name": "specializations",
        "children": []
    }
    genMap = {
        "name": "generalizations",
        "children": []
    }
    newRFDMap = {
        "name": "new RFDs",
        "children": []
    }
    RFDfoundMap = {
        "name": "RFD found",
        "children": []
    }
    notFoundMap = {
        "name": "RFD not found",
        "children": []
    }
    type = [specMap, genMap, newRFDMap, RFDfoundMap, notFoundMap]
    RFDMap = {
        "name": "RFDs",
        "children": type
    }
    # print(RFDMap)

    # creazione dizionario per il file json
    for i in RFDsfullDS:
        for j in RFDstoTest:
            #print(j.RHS[0])
            #print(i.RHS[0])
            if j.RHS[0] == i.RHS[0]:
                #print("j: "+j.RHS[0])
                #print("i: "+i.RHS[0])
                #print("j: " + str(j.RHS[1]))
                #print("i: " + str(i.RHS[1]))
                if j.RHS[1] == i.RHS[1]:
                    #print("j: "+str(j.RHS[1]))
                    #print("i: "+str(i.RHS[1]))
                    if j.label_attributi == i.label_attributi:
                        #print("j label: "+str(j.label_attributi))
                        #print("i label: "+str(i.label_attributi))
                        if np.array_equal(j.thres_attributi, i.thres_attributi):
                            #print("trovata RFD Found")
                            #print("ho trovato una RFD originale")
                            l2 = list(j.stampaLHS)
                            j.found = True
                            i.found = True
                            tmp = {"RHS": j.stampaRHS, "LHS": l2}
                            # print("\t Ho trovato ",tmp)
                            RFDtrovate.append(tmp)
                            originaliTrovate += 1
                            # print("Cerco ", str(j.RHS),"in",RFDfoundMap)
                            arrayTmp = RFDfoundMap["children"]
                            flagtrovato = False
                            if len(arrayTmp) != 0:
                                for z in arrayTmp:
                                    if z["name"] == str(j.stampaRHS):
                                        # print("ho trovato RHS: " + str(j.RHS))
                                        flagtrovato = True

                                        stringhe = {
                                            "name": object,
                                            "value": 0
                                        }
                                        LHSoriginali = {
                                            "name": object,
                                            "children": []
                                        }
                                        LHSoriginali["name"] = str(j.stampaLHS)
                                        stringhe["name"] = i.__str__()
                                        LHSoriginali["children"].append(copy.copy(stringhe))
                                        z["children"].append(copy.copy(LHSoriginali))
                                        break

                                if flagtrovato == False:
                                    # print("non ho trovato RHS che cercavo, allora non esiste e devo crearlo")
                                    RHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }

                                    LHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }

                                    stringhe = {
                                        "name": object,
                                        "value": 0
                                    }
                                    RHSoriginali["name"] = str(j.stampaRHS)
                                    LHSoriginali["name"] = str(j.stampaLHS)
                                    stringhe["name"] = i.__str__()
                                    LHSoriginali["children"].append(copy.copy(stringhe))
                                    RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                    RFDfoundMap["children"].append(copy.copy(RHSoriginali))
                            else:
                                # print("questa è la prima volta")
                                RHSoriginali = {
                                    "name": object,
                                    "children": []
                                }
                                LHSoriginali = {
                                    "name": object,
                                    "children": []
                                }

                                stringhe = {
                                    "name": object,
                                    "value": 0
                                }

                                RHSoriginali["name"] = str(j.stampaRHS)
                                LHSoriginali["name"] = str(j.stampaLHS)
                                stringhe["name"] = i.__str__()
                                LHSoriginali["children"].append(copy.copy(stringhe))
                                RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                RFDfoundMap["children"].append(copy.copy(RHSoriginali))
                            # print(RFDfoundMap)
                        else:
                            differenze_lhs = j.thres_attributi - i.thres_attributi
                            if np.all(differenze_lhs >= 0) and np.any(differenze_lhs > 0):  #caso generalizzazione con lhs più grande
                                #print("trovata generalizzazione su soglie lhs")
                                l2 = list(j.stampaLHS)
                                j.found = True
                                i.found = True
                                tmp = {"RHS": j.stampaRHS, "LHS ": l2}
                                RFDgen.append(tmp)
                                # print("Cerco ", str(j.RHS),"in",RFDfoundMap)
                                arrayTmp = genMap["children"]
                                flagtrovato = False
                                if len(arrayTmp) != 0:
                                    for z in arrayTmp:
                                        if z["name"] == str(j.stampaRHS):
                                            # print("ho trovato RHS: " + str(j.RHS))
                                            flagtrovato = True
                                            lhspresente = False
                                            for t in z["children"]:
                                                # print("sono nel for")
                                                # print(type(t["name"]))
                                                # print("t.name: " + t["name"] + " LHS di j: " + str(j.LHS))
                                                # print(t["name"] == str(j.LHS))

                                                if (t["name"] == str(j.stampaLHS)):
                                                    # print("sono nell'if del for, quindi ho trovato t.name == j.LHS")
                                                    stringhe = {
                                                        "name": object,
                                                        "value": 0
                                                    }
                                                    stringhe["name"] = i.__str__()
                                                    find = False
                                                    for r in gendiverse:
                                                        if (r == i.__str__()):
                                                            find = True
                                                    if (find == False):
                                                        gendiverse.append(i.__str__())
                                                    t["children"].append(copy.copy(stringhe))
                                                    lhspresente = True
                                                    break

                                            if (lhspresente != True):
                                                # print("sono nell'else perchè in confronto è falso")
                                                stringhe = {
                                                    "name": object,
                                                    "value": 0
                                                }
                                                LHSoriginali = {
                                                    "name": object,
                                                    "children": []
                                                }
                                                LHSoriginali["name"] = str(j.stampaLHS)
                                                stringhe["name"] = i.__str__()
                                                find = False
                                                for r in gendiverse:
                                                    if (r == i.__str__()):
                                                        find = True
                                                if (find == False):
                                                    gendiverse.append(i.__str__())
                                                LHSoriginali["children"].append(copy.copy(stringhe))
                                                z["children"].append(copy.copy(LHSoriginali))
                                                # print("[T children]"+t["children"])
                                    if flagtrovato == False:
                                        # print("non ho trovato RHS che cercavo, allora non esiste e devo crearlo")

                                        stringhe = {
                                            "name": object,
                                            "value": 0
                                        }

                                        RHSoriginali = {
                                            "name": object,
                                            "children": []
                                        }

                                        LHSoriginali = {
                                            "name": object,
                                            "children": []
                                        }
                                        RHSoriginali["name"] = str(j.stampaRHS)
                                        LHSoriginali["name"] = str(j.stampaLHS)
                                        stringhe["name"] = i.__str__()
                                        find = False
                                        for r in gendiverse:
                                            if (r == i.__str__()):
                                                find = True
                                        if (find == False):
                                            gendiverse.append(i.__str__())
                                        LHSoriginali["children"].append(copy.copy(stringhe))
                                        RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                        genMap["children"].append(copy.copy(RHSoriginali))
                                else:
                                    # print("questa è la prima volta")

                                    stringhe = {
                                        "name": object,
                                        "value": 0
                                    }

                                    RHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    LHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    RHSoriginali["name"] = str(j.stampaRHS)
                                    LHSoriginali["name"] = str(j.stampaLHS)
                                    stringhe["name"] = i.__str__()
                                    find = False
                                    for r in gendiverse:
                                        if (r == i.__str__()):
                                            find = True
                                    if (find == False):
                                        gendiverse.append(i.__str__())
                                    LHSoriginali["children"].append(copy.copy(stringhe))
                                    RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                    genMap["children"].append(copy.copy(RHSoriginali))
                                # print(genMap)
                            else:
                                if np.all(differenze_lhs <= 0) and np.any(differenze_lhs < 0):
                                    #print("trovata specializzazione su soglie lhs")
                                    l2 = list(j.stampaLHS)
                                    j.found = True
                                    i.found = True
                                    tmp = {"RHS": j.stampaRHS, "LHS": l2}
                                    RFDspec.append(tmp)
                                    # print("Cerco ", str(j.RHS),"in",RFDfoundMap)
                                    arrayTmp = specMap["children"]
                                    flagtrovato = False
                                    if len(arrayTmp) != 0:
                                        for z in arrayTmp:
                                            if z["name"] == str(j.stampaRHS):
                                                # print("[SPEC] ho trovato RHS: " + str(j.RHS) + "---->")
                                                flagtrovato = True
                                                lhspresente = False
                                                for t in z["children"]:
                                                    # print("sono nel for")
                                                    # print(type(t["name"]))
                                                    # print("t.name: " + t["name"] + " LHS di j: " + str(j.LHS))
                                                    # print(t["name"] == str(j.LHS))

                                                    if (t["name"] == str(j.stampaLHS)):
                                                        # print("sono nell'if del for, quindi ho trovato t.name == j.LHS")
                                                        stringhe = {
                                                            "name": object,
                                                            "value": 0
                                                        }
                                                        stringhe["name"] = i.__str__()
                                                        find = False
                                                        for r in specdiverse:
                                                            if (r == i.__str__()):
                                                                find = True
                                                        if (find == False):
                                                            specdiverse.append(i.__str__())
                                                        t["children"].append(copy.copy(stringhe))
                                                        lhspresente = True
                                                        break

                                                if (lhspresente != True):
                                                    # print("sono nell'else perchè in confronto è falso")
                                                    stringhe = {
                                                        "name": object,
                                                        "value": 0
                                                    }
                                                    LHSoriginali = {
                                                        "name": object,
                                                        "children": []
                                                    }
                                                    LHSoriginali["name"] = str(j.stampaLHS)
                                                    stringhe["name"] = i.__str__()
                                                    # print(i.__str__())
                                                    find = False
                                                    for r in specdiverse:
                                                        if (r == i.__str__()):
                                                            find = True
                                                    if (find == False):
                                                        specdiverse.append(i.__str__())
                                                    LHSoriginali["children"].append(copy.copy(stringhe))
                                                    z["children"].append(copy.copy(LHSoriginali))
                                                    # print("[T children]"+t["children"])

                                        if flagtrovato == False:
                                            # print("non ho trovato RHS che cercavo, allora non esiste e devo crearlo")

                                            stringhe = {
                                                "name": object,
                                                "value": 0
                                            }

                                            RHSoriginali = {
                                                "name": object,
                                                "children": []
                                            }

                                            LHSoriginali = {
                                                "name": object,
                                                "children": []
                                            }
                                            RHSoriginali["name"] = str(j.stampaRHS)
                                            LHSoriginali["name"] = str(j.stampaLHS)
                                            stringhe["name"] = i.__str__()
                                            find = False
                                            for r in specdiverse:
                                                if (r == i.__str__()):
                                                    find = True
                                            if (find == False):
                                                specdiverse.append(i.__str__())
                                            LHSoriginali["children"].append(copy.copy(stringhe))
                                            RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                            specMap["children"].append(copy.copy(RHSoriginali))
                                    else:
                                        # print("questa è la prima volta")
                                        # print(specMap["children"])
                                        stringhe = {
                                            "name": object,
                                            "value": 0
                                        }

                                        RHSoriginali = {
                                            "name": object,
                                            "children": []
                                        }
                                        LHSoriginali = {
                                            "name": object,
                                            "children": []
                                        }
                                        RHSoriginali["name"] = str(j.stampaRHS)
                                        LHSoriginali["name"] = str(j.stampaLHS)
                                        stringhe["name"] = i.__str__()
                                        find = False
                                        for r in specdiverse:
                                            if (r == i.__str__()):
                                                find = True
                                        if (find == False):
                                            specdiverse.append(i.__str__())
                                        LHSoriginali["children"].append(copy.copy(stringhe))
                                        RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                        specMap["children"].append(copy.copy(RHSoriginali))
                                        # print(specMap["children"])

                                    # print(specMap)
                    else:
                        if (set(j.label_attributi).issuperset(set(i.label_attributi))):
                            #print("trovata specializzazione classica")
                            l2 = list(j.stampaLHS)
                            j.found = True
                            i.found = True
                            tmp = {"RHS": j.stampaRHS, "LHS": l2}
                            RFDspec.append(tmp)
                            # print("Cerco ", str(j.RHS),"in",RFDfoundMap)
                            arrayTmp = specMap["children"]
                            flagtrovato = False
                            if len(arrayTmp) != 0:
                                for z in arrayTmp:
                                    if z["name"] == str(j.stampaRHS):
                                        # print("[SPEC] ho trovato RHS: " + str(j.RHS) + "---->")
                                        flagtrovato = True
                                        lhspresente = False
                                        for t in z["children"]:
                                            # print("sono nel for")
                                            # print(type(t["name"]))
                                            # print("t.name: " + t["name"] + " LHS di j: " + str(j.LHS))
                                            # print(t["name"] == str(j.LHS))

                                            if (t["name"] == str(j.stampaLHS)):
                                                # print("sono nell'if del for, quindi ho trovato t.name == j.LHS")
                                                stringhe = {
                                                    "name": object,
                                                    "value": 0
                                                }
                                                stringhe["name"] = i.__str__()
                                                find = False
                                                for r in specdiverse:
                                                    if (r == i.__str__()):
                                                        find = True
                                                if (find == False):
                                                    specdiverse.append(i.__str__())
                                                t["children"].append(copy.copy(stringhe))
                                                lhspresente = True
                                                break

                                        if (lhspresente != True):
                                            # print("sono nell'else perchè in confronto è falso")
                                            stringhe = {
                                                "name": object,
                                                "value": 0
                                            }
                                            LHSoriginali = {
                                                "name": object,
                                                "children": []
                                            }
                                            LHSoriginali["name"] = str(j.stampaLHS)
                                            stringhe["name"] = i.__str__()
                                            # print(i.__str__())
                                            find = False
                                            for r in specdiverse:
                                                if (r == i.__str__()):
                                                    find = True
                                            if (find == False):
                                                specdiverse.append(i.__str__())
                                            LHSoriginali["children"].append(copy.copy(stringhe))
                                            z["children"].append(copy.copy(LHSoriginali))
                                            # print("[T children]"+t["children"])

                                if flagtrovato == False:
                                    # print("non ho trovato RHS che cercavo, allora non esiste e devo crearlo")

                                    stringhe = {
                                        "name": object,
                                        "value": 0
                                    }

                                    RHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }

                                    LHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    RHSoriginali["name"] = str(j.stampaRHS)
                                    LHSoriginali["name"] = str(j.stampaLHS)
                                    stringhe["name"] = i.__str__()
                                    find = False
                                    for r in specdiverse:
                                        if (r == i.__str__()):
                                            find = True
                                    if (find == False):
                                        specdiverse.append(i.__str__())
                                    LHSoriginali["children"].append(copy.copy(stringhe))
                                    RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                    specMap["children"].append(copy.copy(RHSoriginali))
                            else:
                                # print("questa è la prima volta")
                                # print(specMap["children"])
                                stringhe = {
                                    "name": object,
                                    "value": 0
                                }

                                RHSoriginali = {
                                    "name": object,
                                    "children": []
                                }
                                LHSoriginali = {
                                    "name": object,
                                    "children": []
                                }
                                RHSoriginali["name"] = str(j.stampaRHS)
                                LHSoriginali["name"] = str(j.stampaLHS)
                                stringhe["name"] = i.__str__()
                                find = False
                                for r in specdiverse:
                                    if (r == i.__str__()):
                                        find = True
                                if (find == False):
                                    specdiverse.append(i.__str__())
                                LHSoriginali["children"].append(copy.copy(stringhe))
                                RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                specMap["children"].append(copy.copy(RHSoriginali))
                                # print(specMap["children"])

                            # print(specMap)
                        elif(set(j.label_attributi).issubset(set(i.label_attributi))):
                            #print("trovata generalizzazione classica")
                            l2 = list(j.stampaLHS)
                            j.found = True
                            i.found = True
                            tmp = {"RHS": j.stampaRHS, "LHS ": l2}
                            RFDgen.append(tmp)
                            # print("Cerco ", str(j.RHS),"in",RFDfoundMap)
                            arrayTmp = genMap["children"]
                            flagtrovato = False
                            if len(arrayTmp) != 0:
                                for z in arrayTmp:
                                    if z["name"] == str(j.stampaRHS):
                                        # print("ho trovato RHS: " + str(j.RHS))
                                        flagtrovato = True
                                        lhspresente = False
                                        for t in z["children"]:
                                            # print("sono nel for")
                                            # print(type(t["name"]))
                                            # print("t.name: " + t["name"] + " LHS di j: " + str(j.LHS))
                                            # print(t["name"] == str(j.LHS))

                                            if (t["name"] == str(j.stampaLHS)):
                                                # print("sono nell'if del for, quindi ho trovato t.name == j.LHS")
                                                stringhe = {
                                                    "name": object,
                                                    "value": 0
                                                }
                                                stringhe["name"] = i.__str__()
                                                find = False
                                                for r in gendiverse:
                                                    if (r == i.__str__()):
                                                        find = True
                                                if (find == False):
                                                    gendiverse.append(i.__str__())
                                                t["children"].append(copy.copy(stringhe))
                                                lhspresente = True
                                                break

                                        if (lhspresente != True):
                                            # print("sono nell'else perchè in confronto è falso")
                                            stringhe = {
                                                "name": object,
                                                "value": 0
                                            }
                                            LHSoriginali = {
                                                "name": object,
                                                "children": []
                                            }
                                            LHSoriginali["name"] = str(j.stampaLHS)
                                            stringhe["name"] = i.__str__()
                                            find = False
                                            for r in gendiverse:
                                                if (r == i.__str__()):
                                                    find = True
                                            if (find == False):
                                                gendiverse.append(i.__str__())
                                            LHSoriginali["children"].append(copy.copy(stringhe))
                                            z["children"].append(copy.copy(LHSoriginali))
                                            # print("[T children]"+t["children"])
                                if flagtrovato == False:
                                    # print("non ho trovato RHS che cercavo, allora non esiste e devo crearlo")

                                    stringhe = {
                                        "name": object,
                                        "value": 0
                                    }

                                    RHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }

                                    LHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    RHSoriginali["name"] = str(j.stampaRHS)
                                    LHSoriginali["name"] = str(j.stampaLHS)
                                    stringhe["name"] = i.__str__()
                                    find = False
                                    for r in gendiverse:
                                        if (r == i.__str__()):
                                            find = True
                                    if (find == False):
                                        gendiverse.append(i.__str__())
                                    LHSoriginali["children"].append(copy.copy(stringhe))
                                    RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                    genMap["children"].append(copy.copy(RHSoriginali))
                            else:
                                # print("questa è la prima volta")

                                stringhe = {
                                    "name": object,
                                    "value": 0
                                }

                                RHSoriginali = {
                                    "name": object,
                                    "children": []
                                }
                                LHSoriginali = {
                                    "name": object,
                                    "children": []
                                }
                                RHSoriginali["name"] = str(j.stampaRHS)
                                LHSoriginali["name"] = str(j.stampaLHS)
                                stringhe["name"] = i.__str__()
                                find = False
                                for r in gendiverse:
                                    if (r == i.__str__()):
                                        find = True
                                if (find == False):
                                    gendiverse.append(i.__str__())
                                LHSoriginali["children"].append(copy.copy(stringhe))
                                RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                genMap["children"].append(copy.copy(RHSoriginali))
                            # print(genMap)
                else:
                    if j.label_attributi == i.label_attributi:
                        if np.array_equal(j.thres_attributi, i.thres_attributi):
                            differenze_rhs = float(j.RHS[1]) - float(i.RHS[1])
                            if differenze_rhs > 0:
                                #print("trovata specializzazione su rhs")
                                l2 = list(j.stampaLHS)
                                j.found = True
                                i.found = True
                                tmp = {"RHS": j.stampaRHS, "LHS": l2}
                                RFDspec.append(tmp)
                                # print("Cerco ", str(j.RHS),"in",RFDfoundMap)
                                arrayTmp = specMap["children"]
                                flagtrovato = False
                                if len(arrayTmp) != 0:
                                    for z in arrayTmp:
                                        if z["name"] == str(j.stampaRHS):
                                            # print("[SPEC] ho trovato RHS: " + str(j.RHS) + "---->")
                                            flagtrovato = True
                                            lhspresente = False
                                            for t in z["children"]:
                                                # print("sono nel for")
                                                # print(type(t["name"]))
                                                # print("t.name: " + t["name"] + " LHS di j: " + str(j.LHS))
                                                # print(t["name"] == str(j.LHS))

                                                if (t["name"] == str(j.stampaLHS)):
                                                    # print("sono nell'if del for, quindi ho trovato t.name == j.LHS")
                                                    stringhe = {
                                                        "name": object,
                                                        "value": 0
                                                    }
                                                    stringhe["name"] = i.__str__()
                                                    find = False
                                                    for r in specdiverse:
                                                        if (r == i.__str__()):
                                                            find = True
                                                    if (find == False):
                                                        specdiverse.append(i.__str__())
                                                    t["children"].append(copy.copy(stringhe))
                                                    lhspresente = True
                                                    break

                                            if (lhspresente != True):
                                                # print("sono nell'else perchè in confronto è falso")
                                                stringhe = {
                                                    "name": object,
                                                    "value": 0
                                                }
                                                LHSoriginali = {
                                                    "name": object,
                                                    "children": []
                                                }
                                                LHSoriginali["name"] = str(j.stampaLHS)
                                                stringhe["name"] = i.__str__()
                                                # print(i.__str__())
                                                find = False
                                                for r in specdiverse:
                                                    if (r == i.__str__()):
                                                        find = True
                                                if (find == False):
                                                    specdiverse.append(i.__str__())
                                                LHSoriginali["children"].append(copy.copy(stringhe))
                                                z["children"].append(copy.copy(LHSoriginali))
                                                # print("[T children]"+t["children"])

                                    if flagtrovato == False:
                                        # print("non ho trovato RHS che cercavo, allora non esiste e devo crearlo")

                                        stringhe = {
                                            "name": object,
                                            "value": 0
                                        }

                                        RHSoriginali = {
                                            "name": object,
                                            "children": []
                                        }

                                        LHSoriginali = {
                                            "name": object,
                                            "children": []
                                        }
                                        RHSoriginali["name"] = str(j.stampaRHS)
                                        LHSoriginali["name"] = str(j.stampaLHS)
                                        stringhe["name"] = i.__str__()
                                        find = False
                                        for r in specdiverse:
                                            if (r == i.__str__()):
                                                find = True
                                        if (find == False):
                                            specdiverse.append(i.__str__())
                                        LHSoriginali["children"].append(copy.copy(stringhe))
                                        RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                        specMap["children"].append(copy.copy(RHSoriginali))
                                else:
                                    # print("questa è la prima volta")
                                    # print(specMap["children"])
                                    stringhe = {
                                        "name": object,
                                        "value": 0
                                    }

                                    RHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    LHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    RHSoriginali["name"] = str(j.stampaRHS)
                                    LHSoriginali["name"] = str(j.stampaLHS)
                                    stringhe["name"] = i.__str__()
                                    find = False
                                    for r in specdiverse:
                                        if (r == i.__str__()):
                                            find = True
                                    if (find == False):
                                        specdiverse.append(i.__str__())
                                    LHSoriginali["children"].append(copy.copy(stringhe))
                                    RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                    specMap["children"].append(copy.copy(RHSoriginali))
                                    # print(specMap["children"])

                                # print(specMap)
                            else:
                                #print("trovata generalizzazione su rhs")
                                l2 = list(j.stampaLHS)
                                j.found = True
                                i.found = True
                                tmp = {"RHS": j.stampaRHS, "LHS ": l2}
                                RFDgen.append(tmp)
                                # print("Cerco ", str(j.RHS),"in",RFDfoundMap)
                                arrayTmp = genMap["children"]
                                flagtrovato = False
                                if len(arrayTmp) != 0:
                                    for z in arrayTmp:
                                        if z["name"] == str(j.stampaRHS):
                                            # print("ho trovato RHS: " + str(j.RHS))
                                            flagtrovato = True
                                            lhspresente = False
                                            for t in z["children"]:
                                                # print("sono nel for")
                                                # print(type(t["name"]))
                                                # print("t.name: " + t["name"] + " LHS di j: " + str(j.LHS))
                                                # print(t["name"] == str(j.LHS))

                                                if (t["name"] == str(j.stampaLHS)):
                                                    # print("sono nell'if del for, quindi ho trovato t.name == j.LHS")
                                                    stringhe = {
                                                        "name": object,
                                                        "value": 0
                                                    }
                                                    stringhe["name"] = i.__str__()
                                                    find = False
                                                    for r in gendiverse:
                                                        if (r == i.__str__()):
                                                            find = True
                                                    if (find == False):
                                                        gendiverse.append(i.__str__())
                                                    t["children"].append(copy.copy(stringhe))
                                                    lhspresente = True
                                                    break

                                            if (lhspresente != True):
                                                # print("sono nell'else perchè in confronto è falso")
                                                stringhe = {
                                                    "name": object,
                                                    "value": 0
                                                }
                                                LHSoriginali = {
                                                    "name": object,
                                                    "children": []
                                                }
                                                LHSoriginali["name"] = str(j.stampaLHS)
                                                stringhe["name"] = i.__str__()
                                                find = False
                                                for r in gendiverse:
                                                    if (r == i.__str__()):
                                                        find = True
                                                if (find == False):
                                                    gendiverse.append(i.__str__())
                                                LHSoriginali["children"].append(copy.copy(stringhe))
                                                z["children"].append(copy.copy(LHSoriginali))
                                                # print("[T children]"+t["children"])
                                    if flagtrovato == False:
                                        # print("non ho trovato RHS che cercavo, allora non esiste e devo crearlo")

                                        stringhe = {
                                            "name": object,
                                            "value": 0
                                        }

                                        RHSoriginali = {
                                            "name": object,
                                            "children": []
                                        }

                                        LHSoriginali = {
                                            "name": object,
                                            "children": []
                                        }
                                        RHSoriginali["name"] = str(j.stampaRHS)
                                        LHSoriginali["name"] = str(j.stampaLHS)
                                        stringhe["name"] = i.__str__()
                                        find = False
                                        for r in gendiverse:
                                            if (r == i.__str__()):
                                                find = True
                                        if (find == False):
                                            gendiverse.append(i.__str__())
                                        LHSoriginali["children"].append(copy.copy(stringhe))
                                        RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                        genMap["children"].append(copy.copy(RHSoriginali))
                                else:
                                    # print("questa è la prima volta")

                                    stringhe = {
                                        "name": object,
                                        "value": 0
                                    }

                                    RHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    LHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    RHSoriginali["name"] = str(j.stampaRHS)
                                    LHSoriginali["name"] = str(j.stampaLHS)
                                    stringhe["name"] = i.__str__()
                                    find = False
                                    for r in gendiverse:
                                        if (r == i.__str__()):
                                            find = True
                                    if (find == False):
                                        gendiverse.append(i.__str__())
                                    LHSoriginali["children"].append(copy.copy(stringhe))
                                    RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                    genMap["children"].append(copy.copy(RHSoriginali))
                                # print(genMap)
                        else:
                            differenze_unificate = j.thres_attributi - i.thres_attributi
                            diff_rhs = float(i.RHS[1]) - float(j.RHS[1])
                            differenze_unificate = np.append(differenze_unificate, diff_rhs)
                            if np.all(differenze_unificate >= 0) and np.any(differenze_unificate > 0):
                                #print("trovata generalizzazione su  rhs e lhs")
                                l2 = list(j.stampaLHS)
                                j.found = True
                                i.found = True
                                tmp = {"RHS": j.stampaRHS, "LHS ": l2}
                                RFDgen.append(tmp)
                                # print("Cerco ", str(j.RHS),"in",RFDfoundMap)
                                arrayTmp = genMap["children"]
                                flagtrovato = False
                                if len(arrayTmp) != 0:
                                    for z in arrayTmp:
                                        if z["name"] == str(j.stampaRHS):
                                            # print("ho trovato RHS: " + str(j.RHS))
                                            flagtrovato = True
                                            lhspresente = False
                                            for t in z["children"]:
                                                # print("sono nel for")
                                                # print(type(t["name"]))
                                                # print("t.name: " + t["name"] + " LHS di j: " + str(j.LHS))
                                                # print(t["name"] == str(j.LHS))

                                                if (t["name"] == str(j.stampaLHS)):
                                                    # print("sono nell'if del for, quindi ho trovato t.name == j.LHS")
                                                    stringhe = {
                                                        "name": object,
                                                        "value": 0
                                                    }
                                                    stringhe["name"] = i.__str__()
                                                    find = False
                                                    for r in gendiverse:
                                                        if (r == i.__str__()):
                                                            find = True
                                                    if (find == False):
                                                        gendiverse.append(i.__str__())
                                                    t["children"].append(copy.copy(stringhe))
                                                    lhspresente = True
                                                    break

                                            if (lhspresente != True):
                                                # print("sono nell'else perchè in confronto è falso")
                                                stringhe = {
                                                    "name": object,
                                                    "value": 0
                                                }
                                                LHSoriginali = {
                                                    "name": object,
                                                    "children": []
                                                }
                                                LHSoriginali["name"] = str(j.stampaLHS)
                                                stringhe["name"] = i.__str__()
                                                find = False
                                                for r in gendiverse:
                                                    if (r == i.__str__()):
                                                        find = True
                                                if (find == False):
                                                    gendiverse.append(i.__str__())
                                                LHSoriginali["children"].append(copy.copy(stringhe))
                                                z["children"].append(copy.copy(LHSoriginali))
                                                # print("[T children]"+t["children"])
                                    if flagtrovato == False:
                                        # print("non ho trovato RHS che cercavo, allora non esiste e devo crearlo")

                                        stringhe = {
                                            "name": object,
                                            "value": 0
                                        }

                                        RHSoriginali = {
                                            "name": object,
                                            "children": []
                                        }

                                        LHSoriginali = {
                                            "name": object,
                                            "children": []
                                        }
                                        RHSoriginali["name"] = str(j.stampaRHS)
                                        LHSoriginali["name"] = str(j.stampaLHS)
                                        stringhe["name"] = i.__str__()
                                        find = False
                                        for r in gendiverse:
                                            if (r == i.__str__()):
                                                find = True
                                        if (find == False):
                                            gendiverse.append(i.__str__())
                                        LHSoriginali["children"].append(copy.copy(stringhe))
                                        RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                        genMap["children"].append(copy.copy(RHSoriginali))
                                else:
                                    # print("questa è la prima volta")

                                    stringhe = {
                                        "name": object,
                                        "value": 0
                                    }

                                    RHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    LHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    RHSoriginali["name"] = str(j.stampaRHS)
                                    LHSoriginali["name"] = str(j.stampaLHS)
                                    stringhe["name"] = i.__str__()
                                    find = False
                                    for r in gendiverse:
                                        if (r == i.__str__()):
                                            find = True
                                    if (find == False):
                                        gendiverse.append(i.__str__())
                                    LHSoriginali["children"].append(copy.copy(stringhe))
                                    RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                    genMap["children"].append(copy.copy(RHSoriginali))
                                # print(genMap)
                            elif np.all(differenze_unificate <= 0) and np.any(differenze_unificate < 0):
                                #print("trovata specializzazione su  rhs e lhs")
                                l2 = list(j.stampaLHS)
                                j.found = True
                                i.found = True
                                tmp = {"RHS": j.stampaRHS, "LHS": l2}
                                RFDspec.append(tmp)
                                # print("Cerco ", str(j.RHS),"in",RFDfoundMap)
                                arrayTmp = specMap["children"]
                                flagtrovato = False
                                if len(arrayTmp) != 0:
                                    for z in arrayTmp:
                                        if z["name"] == str(j.stampaRHS):
                                            # print("[SPEC] ho trovato RHS: " + str(j.RHS) + "---->")
                                            flagtrovato = True
                                            lhspresente = False
                                            for t in z["children"]:
                                                # print("sono nel for")
                                                # print(type(t["name"]))
                                                # print("t.name: " + t["name"] + " LHS di j: " + str(j.LHS))
                                                # print(t["name"] == str(j.LHS))

                                                if (t["name"] == str(j.stampaLHS)):
                                                    # print("sono nell'if del for, quindi ho trovato t.name == j.LHS")
                                                    stringhe = {
                                                        "name": object,
                                                        "value": 0
                                                    }
                                                    stringhe["name"] = i.__str__()
                                                    find = False
                                                    for r in specdiverse:
                                                        if (r == i.__str__()):
                                                            find = True
                                                    if (find == False):
                                                        specdiverse.append(i.__str__())
                                                    t["children"].append(copy.copy(stringhe))
                                                    lhspresente = True
                                                    break

                                            if (lhspresente != True):
                                                # print("sono nell'else perchè in confronto è falso")
                                                stringhe = {
                                                    "name": object,
                                                    "value": 0
                                                }
                                                LHSoriginali = {
                                                    "name": object,
                                                    "children": []
                                                }
                                                LHSoriginali["name"] = str(j.stampaLHS)
                                                stringhe["name"] = i.__str__()
                                                # print(i.__str__())
                                                find = False
                                                for r in specdiverse:
                                                    if (r == i.__str__()):
                                                        find = True
                                                if (find == False):
                                                    specdiverse.append(i.__str__())
                                                LHSoriginali["children"].append(copy.copy(stringhe))
                                                z["children"].append(copy.copy(LHSoriginali))
                                                # print("[T children]"+t["children"])

                                    if flagtrovato == False:
                                        # print("non ho trovato RHS che cercavo, allora non esiste e devo crearlo")

                                        stringhe = {
                                            "name": object,
                                            "value": 0
                                        }

                                        RHSoriginali = {
                                            "name": object,
                                            "children": []
                                        }

                                        LHSoriginali = {
                                            "name": object,
                                            "children": []
                                        }
                                        RHSoriginali["name"] = str(j.stampaRHS)
                                        LHSoriginali["name"] = str(j.stampaLHS)
                                        stringhe["name"] = i.__str__()
                                        find = False
                                        for r in specdiverse:
                                            if (r == i.__str__()):
                                                find = True
                                        if (find == False):
                                            specdiverse.append(i.__str__())
                                        LHSoriginali["children"].append(copy.copy(stringhe))
                                        RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                        specMap["children"].append(copy.copy(RHSoriginali))
                                else:
                                    # print("questa è la prima volta")
                                    # print(specMap["children"])
                                    stringhe = {
                                        "name": object,
                                        "value": 0
                                    }

                                    RHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    LHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    RHSoriginali["name"] = str(j.stampaRHS)
                                    LHSoriginali["name"] = str(j.stampaLHS)
                                    stringhe["name"] = i.__str__()
                                    find = False
                                    for r in specdiverse:
                                        if (r == i.__str__()):
                                            find = True
                                    if (find == False):
                                        specdiverse.append(i.__str__())
                                    LHSoriginali["children"].append(copy.copy(stringhe))
                                    RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                    specMap["children"].append(copy.copy(RHSoriginali))
                                    # print(specMap["children"])

                                # print(specMap)
                    else:
                        if (set(j.label_attributi).issuperset(set(i.label_attributi))):
                            #print("trovata specializzazione classica")
                            l2 = list(j.stampaLHS)
                            j.found = True
                            i.found = True
                            tmp = {"RHS": j.stampaRHS, "LHS": l2}
                            RFDspec.append(tmp)
                            # print("Cerco ", str(j.RHS),"in",RFDfoundMap)
                            arrayTmp = specMap["children"]
                            flagtrovato = False
                            if len(arrayTmp) != 0:
                                for z in arrayTmp:
                                    if z["name"] == str(j.stampaRHS):
                                        # print("[SPEC] ho trovato RHS: " + str(j.RHS) + "---->")
                                        flagtrovato = True
                                        lhspresente = False
                                        for t in z["children"]:
                                            # print("sono nel for")
                                            # print(type(t["name"]))
                                            # print("t.name: " + t["name"] + " LHS di j: " + str(j.LHS))
                                            # print(t["name"] == str(j.LHS))

                                            if (t["name"] == str(j.stampaLHS)):
                                                # print("sono nell'if del for, quindi ho trovato t.name == j.LHS")
                                                stringhe = {
                                                    "name": object,
                                                    "value": 0
                                                }
                                                stringhe["name"] = i.__str__()
                                                find = False
                                                for r in specdiverse:
                                                    if (r == i.__str__()):
                                                        find = True
                                                if (find == False):
                                                    specdiverse.append(i.__str__())
                                                t["children"].append(copy.copy(stringhe))
                                                lhspresente = True
                                                break

                                        if (lhspresente != True):
                                            # print("sono nell'else perchè in confronto è falso")
                                            stringhe = {
                                                "name": object,
                                                "value": 0
                                            }
                                            LHSoriginali = {
                                                "name": object,
                                                "children": []
                                            }
                                            LHSoriginali["name"] = str(j.stampaLHS)
                                            stringhe["name"] = i.__str__()
                                            # print(i.__str__())
                                            find = False
                                            for r in specdiverse:
                                                if (r == i.__str__()):
                                                    find = True
                                            if (find == False):
                                                specdiverse.append(i.__str__())
                                            LHSoriginali["children"].append(copy.copy(stringhe))
                                            z["children"].append(copy.copy(LHSoriginali))
                                            # print("[T children]"+t["children"])

                                if flagtrovato == False:
                                    # print("non ho trovato RHS che cercavo, allora non esiste e devo crearlo")

                                    stringhe = {
                                        "name": object,
                                        "value": 0
                                    }

                                    RHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }

                                    LHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    RHSoriginali["name"] = str(j.stampaRHS)
                                    LHSoriginali["name"] = str(j.stampaLHS)
                                    stringhe["name"] = i.__str__()
                                    find = False
                                    for r in specdiverse:
                                        if (r == i.__str__()):
                                            find = True
                                    if (find == False):
                                        specdiverse.append(i.__str__())
                                    LHSoriginali["children"].append(copy.copy(stringhe))
                                    RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                    specMap["children"].append(copy.copy(RHSoriginali))
                            else:
                                # print("questa è la prima volta")
                                # print(specMap["children"])
                                stringhe = {
                                    "name": object,
                                    "value": 0
                                }

                                RHSoriginali = {
                                    "name": object,
                                    "children": []
                                }
                                LHSoriginali = {
                                    "name": object,
                                    "children": []
                                }
                                RHSoriginali["name"] = str(j.stampaRHS)
                                LHSoriginali["name"] = str(j.stampaLHS)
                                stringhe["name"] = i.__str__()
                                find = False
                                for r in specdiverse:
                                    if (r == i.__str__()):
                                        find = True
                                if (find == False):
                                    specdiverse.append(i.__str__())
                                LHSoriginali["children"].append(copy.copy(stringhe))
                                RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                specMap["children"].append(copy.copy(RHSoriginali))
                                # print(specMap["children"])

                            # print(specMap)
                        elif (set(j.label_attributi).issubset(set(i.label_attributi))):
                            #print("trovata generalizzazione classica")
                            l2 = list(j.stampaLHS)
                            j.found = True
                            i.found = True
                            tmp = {"RHS": j.stampaRHS, "LHS ": l2}
                            RFDgen.append(tmp)
                            # print("Cerco ", str(j.RHS),"in",RFDfoundMap)
                            arrayTmp = genMap["children"]
                            flagtrovato = False
                            if len(arrayTmp) != 0:
                                for z in arrayTmp:
                                    if z["name"] == str(j.stampaRHS):
                                        # print("ho trovato RHS: " + str(j.RHS))
                                        flagtrovato = True
                                        lhspresente = False
                                        for t in z["children"]:
                                            # print("sono nel for")
                                            # print(type(t["name"]))
                                            # print("t.name: " + t["name"] + " LHS di j: " + str(j.LHS))
                                            # print(t["name"] == str(j.LHS))

                                            if (t["name"] == str(j.stampaLHS)):
                                                # print("sono nell'if del for, quindi ho trovato t.name == j.LHS")
                                                stringhe = {
                                                    "name": object,
                                                    "value": 0
                                                }
                                                stringhe["name"] = i.__str__()
                                                find = False
                                                for r in gendiverse:
                                                    if (r == i.__str__()):
                                                        find = True
                                                if (find == False):
                                                    gendiverse.append(i.__str__())
                                                t["children"].append(copy.copy(stringhe))
                                                lhspresente = True
                                                break

                                        if (lhspresente != True):
                                            # print("sono nell'else perchè in confronto è falso")
                                            stringhe = {
                                                "name": object,
                                                "value": 0
                                            }
                                            LHSoriginali = {
                                                "name": object,
                                                "children": []
                                            }
                                            LHSoriginali["name"] = str(j.stampaLHS)
                                            stringhe["name"] = i.__str__()
                                            find = False
                                            for r in gendiverse:
                                                if (r == i.__str__()):
                                                    find = True
                                            if (find == False):
                                                gendiverse.append(i.__str__())
                                            LHSoriginali["children"].append(copy.copy(stringhe))
                                            z["children"].append(copy.copy(LHSoriginali))
                                            # print("[T children]"+t["children"])
                                if flagtrovato == False:
                                    # print("non ho trovato RHS che cercavo, allora non esiste e devo crearlo")

                                    stringhe = {
                                        "name": object,
                                        "value": 0
                                    }

                                    RHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }

                                    LHSoriginali = {
                                        "name": object,
                                        "children": []
                                    }
                                    RHSoriginali["name"] = str(j.stampaRHS)
                                    LHSoriginali["name"] = str(j.stampaLHS)
                                    stringhe["name"] = i.__str__()
                                    find = False
                                    for r in gendiverse:
                                        if (r == i.__str__()):
                                            find = True
                                    if (find == False):
                                        gendiverse.append(i.__str__())
                                    LHSoriginali["children"].append(copy.copy(stringhe))
                                    RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                    genMap["children"].append(copy.copy(RHSoriginali))
                            else:
                                # print("questa è la prima volta")

                                stringhe = {
                                    "name": object,
                                    "value": 0
                                }

                                RHSoriginali = {
                                    "name": object,
                                    "children": []
                                }
                                LHSoriginali = {
                                    "name": object,
                                    "children": []
                                }
                                RHSoriginali["name"] = str(j.stampaRHS)
                                LHSoriginali["name"] = str(j.stampaLHS)
                                stringhe["name"] = i.__str__()
                                find = False
                                for r in gendiverse:
                                    if (r == i.__str__()):
                                        find = True
                                if (find == False):
                                    gendiverse.append(i.__str__())
                                LHSoriginali["children"].append(copy.copy(stringhe))
                                RHSoriginali["children"].append(copy.copy(LHSoriginali))
                                genMap["children"].append(copy.copy(RHSoriginali))
                            # print(genMap)

    for k in RFDsfullDS:
        if not k.found:
            l2 = list(k.stampaLHS)
            tmp = {"RHS": k.stampaRHS, "LHS": l2}
            RFDnontrovate.append(tmp)
            countnonTrovate += 1
            arrayTmp = notFoundMap["children"]
            flagtrovato = False
            if len(arrayTmp) != 0:
                for z in arrayTmp:
                    if z["name"] == str(k.stampaRHS):
                        #print("ho trovato RHS: " + str(k.RHS))
                        flagtrovato = True

                        stringhe = {
                            "name": object,
                            "value": 0
                        }

                        LHSoriginali = {
                            "name": object,
                            "children": []
                        }
                        LHSoriginali["name"] = str(k.stampaLHS)
                        stringhe["name"] = k.__str__()
                        LHSoriginali["children"].append(copy.copy(stringhe))
                        z["children"].append(copy.copy(LHSoriginali))
                        break

                if flagtrovato == False:
                    #print("non ho trovato RHS che cercavo, allora non esiste e devo crearlo")

                    stringhe = {
                        "name": object,
                        "value": 0
                    }

                    RHSoriginali = {
                        "name": object,
                        "children": []
                    }

                    LHSoriginali = {
                        "name": object,
                        "children": []
                    }
                    RHSoriginali["name"] = str(k.stampaRHS)
                    LHSoriginali["name"] = str(k.stampaLHS)
                    stringhe["name"] = k.__str__()
                    LHSoriginali["children"].append(copy.copy(stringhe))
                    RHSoriginali["children"].append(copy.copy(LHSoriginali))
                    notFoundMap["children"].append(copy.copy(RHSoriginali))
            else:
                #print("questa è la prima volta")

                stringhe = {
                    "name": object,
                    "value": 0
                }

                RHSoriginali = {
                    "name": object,
                    "children": []
                }
                LHSoriginali = {
                    "name": object,
                    "children": []
                }
                RHSoriginali["name"] = str(k.stampaRHS)
                LHSoriginali["name"] = str(k.stampaLHS)
                stringhe["name"] = k.__str__()
                LHSoriginali["children"].append(copy.copy(stringhe))
                RHSoriginali["children"].append(copy.copy(LHSoriginali))
                notFoundMap["children"].append(copy.copy(RHSoriginali))
                #print(notFoundMap)

    for k in RFDstoTest:
        if not k.found:
            l2 = list(k.stampaLHS)
            tmp = {"RHS": k.stampaRHS, "LHS": l2}
            RFDnuove.append(tmp)
            countnuove += 1
            arrayTmp = newRFDMap["children"]
            flagtrovato = False
            if len(arrayTmp) != 0:
                for z in arrayTmp:
                    if z["name"] == str(k.stampaRHS):
                        #print("ho trovato RHS: " + str(k.RHS))
                        flagtrovato = True

                        stringhe = {
                            "name": object,
                            "value": 0
                        }

                        LHSoriginali = {
                            "name": object,
                            "children": []
                        }
                        LHSoriginali["name"] = str(k.stampaLHS)
                        stringhe["name"] = k.__str__()
                        LHSoriginali["children"].append(copy.copy(stringhe))
                        z["children"].append(copy.copy(LHSoriginali))
                        break

                if flagtrovato == False:
                    #print("non ho trovato RHS che cercavo, allora non esiste e devo crearlo")

                    stringhe = {
                        "name": object,
                        "value": 0
                    }

                    RHSoriginali = {
                        "name": object,
                        "children": []
                    }

                    LHSoriginali = {
                        "name": object,
                        "children": []
                    }
                    RHSoriginali["name"] = str(k.stampaRHS)
                    LHSoriginali["name"] = str(k.stampaLHS)
                    stringhe["name"] = k.__str__()
                    LHSoriginali["children"].append(copy.copy(stringhe))
                    RHSoriginali["children"].append(copy.copy(LHSoriginali))
                    newRFDMap["children"].append(copy.copy(RHSoriginali))
            else:
                #print("questa è la prima volta")

                stringhe = {
                    "name": object,
                    "value": 0
                }

                RHSoriginali = {
                    "name": object,
                    "children": []
                }
                LHSoriginali = {
                    "name": object,
                    "children": []
                }
                RHSoriginali["name"] = str(k.stampaRHS)
                LHSoriginali["name"] = str(k.stampaLHS)
                stringhe["name"] = k.__str__()
                LHSoriginali["children"].append(copy.copy(stringhe))
                RHSoriginali["children"].append(copy.copy(LHSoriginali))
                newRFDMap["children"].append(copy.copy(RHSoriginali))
            #print#(newRFDMap)

    dictionary ={
        "RFD trovate" : RFDtrovate,
        "specializzazioni" : RFDspec,
        "generalizzazioni" : RFDgen,
        "RFD nuove" : RFDnuove,
        "RFD non trovate" : RFDnontrovate,
    }


    #with open(f"./ris_{tipologia}/{nomedataset}/jsonForChart_{nomedataset}_{versione}_{iteration}.json", "w") as outfile:
    #    json.dump(RFDMap, outfile)

    specMap2 = {
        "name": "specializations",
        "children": []
    }
    genMap2 = {
        "name": "generalizations",
        "children": []
    }
    newRFDMap2 = {
        "name": "new RFDs",
        "children": []
    }
    RFDfoundMap2 = {
        "name": "RFD found",
        "children": []
    }
    notFoundMap2 = {
        "name": "RFD not found",
        "children": []
    }

    #print("originali trovate: "+str(originaliTrovate))
    print("specializzate trovate: "+str(len(specdiverse)))
    print("specializzate trovate: " + str(specdiverse))
    print("generalizzate trovate: "+str(len(gendiverse)))
    countspec=0
    for i in specMap["children"]:
        for j in i["children"]:
            countspec += 1
    #print(str(countspec))

    coutngen=0
    for z in genMap["children"]:
        for zt in z["children"]:
            coutngen += 1
    #print(str(coutngen))

    #print("rfd non trovate "+str(countnonTrovate))
    #print("rfd nuove "+str(countnuove))
    #print("GRANDEZZA FILE fullds: " + str(len(RFDsfullDS)))
    #print("GRANDEZZA FILE dstotest " + str(len(RFDstoTest))+"\n")

    lenFull = len(RFDsfullDS)
    lenResult = len(RFDstoTest)

    #print('\033[1m'+nullDatasetName+": "+str(len(RFDstoTest))+" dipendenze"'\033[0m')

    countcompleto = 0
    finaletrovate = 0
    percentualitrovate = []
    alldep = 0
    specMap2 = specMap
    rhstrovate = specMap2["children"]
    for z in rhstrovate:
        figlidiz =z["children"]
        for tk in figlidiz:
            countcompleto += 1
            numero = len(tk["children"])
            alldep = alldep + len(tk["children"])
            finaletrovate = finaletrovate +1
        percent = (finaletrovate *100)/countspec
        percent = round(percent,2)
        percentrhs = percent
        nometemp = z["name"]
        z["name"] = nometemp+": "+str(percent)+"%"
        percentualitrovate.append(percent)
        percent = 0
        finaletrovate = 0
        for tk in figlidiz:
            percent = (len(tk["children"]) *100)/alldep
            percent = round(percent, 2)
            tk.pop("children")
            tk["size"]=percent
            nometemp = tk["name"]
            tk["name"] = nometemp + ": " + str(percent) + "%"
            percentualitrovate.append(percent)
        alldep=0
    if(lenResult == 0):
        percent = 0.00
    else:
        percent = (countcompleto *100)/lenFull
        percent = round(percent, 2)
        #print(percent)
    parola = specMap2["name"]
    parolafinale = parola+": "+str(percent)
    specMap2["name"]=parolafinale
    #print("\n",'\033[1m'+str(specMap2["name"])+"% ("+str(countspec)+" dipendenze)"'\033[0m')
    #for nf in specMap2["children"]:
        #print("---- ",str(nf["name"])," ("+str(len(nf["children"])),"dipendenze)")


    countcompleto = 0
    finaletrovate = 0
    percentualitrovate = []
    alldep = 0
    genMap2 = genMap
    rhstrovate = genMap2["children"]
    for z in rhstrovate:
        #print("z: -- ",str(z))
        figlidiz = z["children"]
        for tk in figlidiz:
            #print("tk: -- ", str(tk))
            countcompleto += 1
            numero = len(tk["children"])
            #print("numero: ",numero)
            alldep = alldep + len(tk["children"])
            #print("alldep: ",alldep)
            finaletrovate = finaletrovate + numero
            #print("finaletrovate: ", finaletrovate)
        percent = (len(z["children"]) *100)/coutngen
        percent = round(percent,2)
        percentrhs = percent
        nometemp = z["name"]
        z["name"] = nometemp+": "+str(percent)+"%"
        percentualitrovate.append(percent)
        percent = 0
        finaletrovate = 0
        for tk in figlidiz:
            #print("len tk children: ",len(tk["children"]))
            #print("percentrhs: ",percentrhs)
            percent = (len(tk["children"]) * percentrhs) / alldep
            percent = round(percent, 2)
            tk.pop("children")
            tk["size"]=percent
            nometemp = tk["name"]
            tk["name"] = nometemp + ": " + str(percent) + "%"
            percentualitrovate.append(percent)
        alldep=0
    if(lenResult == 0):
        percent = 0.00
    else:
        percent = (countcompleto *100)/lenResult
        percent = round(percent, 2)
        #print(percent)
    parola = genMap2["name"]
    parolafinale = parola+": "+str(percent)
    genMap2["name"]=parolafinale
    #print("\n",'\033[1m'+str(genMap2["name"])+"% ("+str(coutngen)+" dipendenze)"'\033[0m')
    #for nf in genMap2["children"]:
        #print("---- ",str(nf["name"])," ("+str(len(nf["children"])),"dipendenze)")
    #print("countcompleto ",countcompleto)

    countcompleto = 0
    finaletrovate = 0
    percentualitrovate = []
    alldep = 0
    newRFDMap2 = newRFDMap
    rhstrovate = newRFDMap2["children"]
    for z in rhstrovate:
        figlidiz =z["children"]
        for tk in figlidiz:
            countcompleto += 1
            numero = len(tk["children"])
            alldep = alldep + len(tk["children"])
            finaletrovate = finaletrovate + numero
        percent = (finaletrovate *100)/countnuove
        percent = round(percent,2)
        percentrhs = percent
        nometemp = z["name"]
        z["name"] = nometemp+": "+str(percent)+"%"
        percentualitrovate.append(percent)
        finaletrovate = 0
        for tk in figlidiz:
            percent = (len(tk["children"]) *percentrhs)/alldep
            percent = round(percent, 2)
            tk.pop("children")
            tk["size"]=percent
            nometemp = tk["name"]
            tk["name"] = nometemp + ": " + str(percent) + "%"
            percentualitrovate.append(percent)
        alldep=0
    print(lenResult)
    if(lenResult == 0):
        percent = 0.00
        stampe_per_plot.update({"new": percent})
        stampe_per_metriche.update({"new": countcompleto})

    else:
        percent = (countcompleto *100)/lenResult
        percent = round(percent, 2)
        stampe_per_plot.update({"new": percent})
        stampe_per_metriche.update({"new": countcompleto})

        #print(percent)
    parola = newRFDMap2["name"]
    parolafinale = parola+": "+str(percent)
    newRFDMap2["name"]=parolafinale
    #print("\n",'\033[1m'+str(newRFDMap2["name"])+"% ("+str(countnuove)+" dipendenze)"'\033[0m')
    #for nf in newRFDMap2["children"]:
        #print("---- ",str(nf["name"])," ("+str(len(nf["children"])),"dipendenze)")
    #print(originaliTrovate)
    #percent = (originaliTrovate *100)/len(RFDstoTest)
    #percent = round(percent, 2)
    #print('\033[1m'+"\nrfd trovate: "+str(percent)+"% ("+str(originaliTrovate)+" dipendenze)"'\033[0m')

    #print('\033[1m'+"\nRISULTATI ORACOLO: "+str(len(RFDsfullDS))+" dipendenze"'\033[0m')

    countcompleto = 0
    finaletrovate = 0
    percent = 0
    percentualitrovate = []
    alldep = 0
    RFDfoundMap2 = RFDfoundMap
    rhstrovate = RFDfoundMap2["children"]
    for z in rhstrovate:
        figlidiz =z["children"]
        for tk in figlidiz:
            countcompleto += 1
            numero = len(tk["children"])
            alldep = alldep + len(tk["children"])
            finaletrovate = finaletrovate + numero
        percent = (finaletrovate *100)/originaliTrovate
        percent = round(percent,2)
        percentrhs = percent
        nometemp = z["name"]
        z["name"] = nometemp+": "+str(percent)+"%"
        percentualitrovate.append(percent)
        percent = 0
        finaletrovate = 0
        for tk in figlidiz:
            percent = (len(tk["children"]) * percentrhs) / alldep
            percent = round(percent, 2)
            tk.pop("children")
            tk["size"]=percent
            nometemp = tk["name"]
            tk["name"] = nometemp + ": " + str(percent) + "%"
            percentualitrovate.append(percent)
        alldep=0
    #print(countcompleto)
    percent = (countcompleto *100)/lenFull
    percent = round(percent, 2)
    stampe_per_plot.update({"Found": percent})
    stampe_per_metriche.update({"Found": countcompleto})

    #print(percent)
    parola = RFDfoundMap2["name"]
    parolafinale = parola+": "+str(percent)
    RFDfoundMap2["name"]=parolafinale
    #print("\n",'\033[1m'+str(RFDfoundMap2["name"])+"% ("+str(originaliTrovate)+" dipendenze)"'\033[0m')
    #for nf in RFDfoundMap2["children"]:
        #print("---- ",str(nf["name"])," ("+str(len(nf["children"])),"dipendenze)")


    countcompleto = 0
    finaletrovate = 0
    percentualitrovate = []
    alldep = 0
    notFoundMap2 = notFoundMap
    rhstrovate = notFoundMap2["children"]
    for z in rhstrovate:
        figlidiz =z["children"]
        for tk in figlidiz:
            countcompleto += 1
            numero = len(tk["children"])
            alldep = alldep + len(tk["children"])
            finaletrovate = finaletrovate + numero
        percent = (finaletrovate *100)/countnonTrovate
        percent = round(percent,2)
        percentrhs = percent
        nometemp = z["name"]
        z["name"] = nometemp+": "+str(percent)+"%"
        percentualitrovate.append(percent)
        percent = 0
        finaletrovate = 0
        for tk in figlidiz:
            percent = (len(tk["children"]) * percentrhs) / alldep
            percent = round(percent, 2)
            tk.pop("children")
            tk["size"]=percent
            nometemp = tk["name"]
            tk["name"] = nometemp + ": " + str(percent) + "%"
            percentualitrovate.append(percent)
        alldep=0
    #print(countcompleto)
    percent = (countcompleto *100)/lenFull
    percent = round(percent, 2)
    stampe_per_plot.update({"notFound": percent})
    stampe_per_metriche.update({"notFound": countcompleto})

    #print(percent)
    parola = notFoundMap2["name"]
    parolafinale = parola+": "+str(percent)
    notFoundMap2["name"]=parolafinale
    #print("\n",'\033[1m'+str(notFoundMap2["name"])+"% ("+str(countnonTrovate)+" dipendenze)"'\033[0m')
    #for nf in notFoundMap2["children"]:
        #print("---- ",str(nf["name"])," ("+str(len(nf["children"])),"dipendenze)")

    percent = (len(gendiverse) *100)/lenFull
    percent = round(percent, 2)
    #print('\033[1m'+"\nrfd generalizzate: "+str(percent)+"% ("+str(len(gendiverse))+" dipendenze)"'\033[0m')
    stampe_per_plot.update({"generalized": percent})
    stampe_per_metriche.update({"generalized": len(gendiverse)})

    percent = (len(specdiverse) *100)/lenFull
    percent = round(percent, 2)
    #print('\033[1m'+"\nrfd specializzate: "+str(percent)+"% ("+str(len(specdiverse))+" dipendenze)"'\033[0m')
    stampe_per_plot.update({"specialized": percent})
    stampe_per_metriche.update({"specialized": len(specdiverse)})

    type2 = [specMap2,genMap2,newRFDMap2,RFDfoundMap2,notFoundMap2]

    RFDMap2 ={
        "name": "RFDs",
        "children": type2
    }
    #print(str(RFDMap2))

    #with open(f"./ris_{tipologia}/{nomedataset}/percentages_{nomedataset}_{versione}_{iteration}.json", "w") as outfile:
    #    json.dump(RFDMap2, outfile)

    with open(f"./ris_{tipologia}/{nomedataset}/analisi_{nomedataset}_{versione}_{iteration}.json", "w") as outfile:
        json.dump(stampe_per_plot, outfile)

    stampe_per_metriche.update({"oracolo": lenFull})
    stampe_per_metriche.update({"test": lenResult})
    print(stampe_per_metriche)
    with open(f"./ris_{tipologia}/{nomedataset}/count_{nomedataset}_{versione}_{iteration}.json", "w") as outfile:
        json.dump(stampe_per_metriche, outfile)

tipologia = "incremental"

#datasets = ["actorfilms_4000","Boeing_1485","EV_Vehicles_4000","F1_REBUILT_5000","Med_Ch_2500","MotoGP_REBUILT_3000","NBA_3200","superstore_4500","US_Presidents_3754"]

datasets = {"actorfilms_4000":["280","560","840","1120","1400","2800","5600","8400","11200","14000"],
            "Boeing_898":["90","180","269","359","449","898","1796","2694","3592","4490"],
            "EV_Vehicles_4000":["400","800","1200","1600","2000","4000","8000","12000","16000","20000"],
            "F1_REBUILT_5000":["350","700","1050","1400","1750","3500","7000","10500","14000","17500"],
            "Med_Ch_2500":["300","600","900","1200","1500","3000","6000","9000","12000","15000"],
            "MotoGP_REBUILT_3000":["360","720","1080","1440","1800","3600","7200","10800","14400","18000"],
            "NBA_3200":["384","768","1152","1536","1920","3840","7680","11520","15360","19200"],
            "superstore_4500":["495","990","1485","1980","2475","4950","9900","14850","19800","24750"],
            "US_Presidents_3754":["375","751","1126","1502","1877","3754","7508","11262","15016","18770"],
            "cars":["37","73","110","146","183","365","731","1096","1462","1827"],
            "police":["198","397","595","793","992","1984","3967","5951","7934","9918"],
            "restaurant":["52","104","156","207","259","518","1037","1555","2074","2592"],
            "IoT_Telemetry3000":["240","480","720","960","1200","2400","4800","7200","9600","12000"],
            "Air_9000":["1170","2340","3510","4680","5850","11700","23400","35100","46800","58500"],
            "Cats_1071":["107","214","321","428","536","1071","2142","3213","4284","5355"]}

'''
datasets = {"Boeing_898_MNAR":["90","180","269","359","449","898","1796","2694","3592","4490"],
            "cars_MNAR":["37","73","110","146","183","365","731","1096","1462","1827"],
            "police_MNAR":["198","397","595","793","992","1984","3967","5951","7934","9918"],
            "restaurant_MNAR":["52","104","156","207","259","518","1037","1555","2074","2592"]
            }

datasets = {"Boeing_898_MBUV":["90","180","269","359","449","898","1796","2694","3592","4490"],
            "cars_MBUV":["37","73","110","146","183","365","731","1096","1462","1827"],
            "police_MBUV":["198","397","595","793","992","1984","3967","5951","7934","9918"],
            "restaurant_MBUV":["52","104","156","207","259","518","1037","1555","2074","2592"]
            }


datasets = {"Boeing_898_FD":["90","180","269","359","449","898","1796","2694","3592","4490"],
            "cars_FD":["37","73","110","146","183","365","731","1096","1462","1827"],
            "police_FD":["198","397","595","793","992","1984","3967","5951","7934","9918"],
            "restaurant_FD":["52","104","156","207","259","518","1037","1555","2074","2592"]
            }
'''


for dataset in datasets.keys():
    nomedataset = dataset
    oracolo = f"./oracolo/{nomedataset}.csv"
    for versione in datasets[nomedataset]:
        for i in range(1,6):
            nuovirisultati = f"./{tipologia}/{nomedataset}/{nomedataset}_{versione}_{i}.csv"
            create_json(oracolo, nuovirisultati, nomedataset,versione,i, tipologia)

