import pandas as pd

def metric1(spec, gen, nw, nf, oracle, coeff):
    numerator = nf + coeff * spec + coeff * gen + nw
    denominator = oracle + nw
    if denominator == 0:
        return 0
    value = numerator / denominator
    return min(value, 1)

def metric2(spec, gen, nf, oracle, coeff):
    numerator = nf + coeff * spec + coeff * gen
    denominator = oracle
    if denominator == 0:
        return 0
    value = numerator / denominator
    return min(value, 1)

def compute_metrics(spec, gen, new, not_found, found):
    #Numero di RFD dell'oracolop
    num_rfd_oracle=spec+gen+found+not_found

    #Coefficiente per spec e gen (peso dimezzato)
    spec_gen_coeff=0.5

    print(metric1(spec, gen, new, not_found, num_rfd_oracle, spec_gen_coeff))
    print(metric2(spec, gen, not_found, num_rfd_oracle, spec_gen_coeff))


specialized=5
generalized=1
new=2
not_found=3
found=1

compute_metrics(specialized, generalized, new, not_found, found)
