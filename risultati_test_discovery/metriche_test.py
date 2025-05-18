import json

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

def compute_metrics(spec, gen, new, not_found, found):
    #Numero di RFD dell'oracolo
    num_rfd_oracle=spec+gen+found+not_found

    #Coefficiente per spec e gen (peso dimezzato)
    spec_gen_coeff=0.5

    print(metric1(spec, gen, new, not_found, num_rfd_oracle, spec_gen_coeff))
    print(metric2(spec, gen, not_found, num_rfd_oracle, spec_gen_coeff),"\n")


#specialized=5
#generalized=1
#new=6
#not_found=3
#found=6

with open(f"./ris_incremental/metrics_medie_incremental.json", "r") as outfile2:
    dict_finale = json.load(outfile2)
    #print(dict_finale)

with open(f"./ris_baseline/medie_metrics_baseline.json", "r") as outfile3:
    dict_finale2 = json.load(outfile3)

for ds in range (0,13):
    print("ds:",ds)
    for mr in dict_finale.keys():
        #print("dataset:",ds)
        #print(mr)
        print("incremental:",dict_finale[mr][ds])
        compute_metrics(dict_finale[mr][ds][3],dict_finale[mr][ds][2],dict_finale[mr][ds][4],dict_finale[mr][ds][1],dict_finale[mr][ds][0])
        print("baseline:", dict_finale2[mr][ds])
        compute_metrics(dict_finale2[mr][ds][3], dict_finale2[mr][ds][2], dict_finale2[mr][ds][4], dict_finale2[mr][ds][1],dict_finale2[mr][ds][0])