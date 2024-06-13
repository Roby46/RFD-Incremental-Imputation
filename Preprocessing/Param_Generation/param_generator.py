#Script to generate the args for the imputation algorithm

def generate_command_strings(versions, missing_values,dataset):
    #params=delimiter,missing_value,num_attributes,window_size,thresholds (one for each attribute)
    #fixed_params = [";", "?", 10, 80, 2.5, 2.5, 1, 2, 2, 3, 3, 3, 20, 10]
    fixed_params = [";", "?", 10, 80, 2.5, 2.5, 1, 2, 2, 3, 3, 3, 20, 10]
    command_strings = []

    for bool_param in [True, False]:
        for version in versions:
            for missing_value in missing_values:
                dataset_name = f"{dataset}_{missing_value}_{version}.csv"
                bool_str = str(bool_param)
                command_string = f'"{dataset_name}" "{fixed_params[0]}" "{fixed_params[1]}" {fixed_params[2]} {fixed_params[3]} "{bool_str}"'
                for param in fixed_params[4:]:
                    command_string += f" {param}"
                command_strings.append(command_string)

    return command_strings

# Hospital Staff 120
# EV_Vehicles 80
dataset="EV_Vehicles_4000"
# Dataset version
versions = [1,2,3,4,5]

#Number of missing values
#missing_values = [400, 800, 1200, 1600, 2000, 4000, 8000, 12000, 16000, 20000] #EV_Vehicles
#missing_values = [480, 960, 1440, 1920, 2400, 4800, 9600, 14400, 19200, 24000] #Hospital Staff
# Genera le stringhe di comando
commands = generate_command_strings(versions, missing_values,dataset)

# Stampa le stringhe di comando generate
for command in commands:
    print(command)
