import os

def generate_command_strings(versions, missing_values, dataset, use_true):
    #fixed_params = [";", "?", 10, 80, 2.5, 2.5, 1, 2, 2, 3, 3, 3, 20, 10] #EV_Vehicles
    #fixed_params = [";", "?", 12, 150, 3,0,5,2,8,2,1,4,1,2,2,2] #Olympics
    #fixed_params = [";", "?", 10, 16, 1, 5, 10000, 10,2, 2, 0.5, 4, 32, 3] #Smartphones
    fixed_params = [";", "?", 7, 240, 5, 0, 5, 2,60, 1.5, 0] #Actors

    command_strings = []

    bool_param = use_true  # Usa il parametro di input per determinare True o False
    for version in versions:
        for missing_value in missing_values:
            dataset_name = f"{dataset}_{missing_value}_{version}.csv"
            bool_str = str(bool_param)
            command_string = f'"{dataset_name}" "{fixed_params[0]}" "{fixed_params[1]}" {fixed_params[2]} {fixed_params[3]} "{bool_str}"'
            for param in fixed_params[4:]:
                command_string += f" {param}"
            # Replace quotes with XML entity references
            command_string = command_string.replace('"', '&quot;')
            command_strings.append((dataset_name, command_string))

    return command_strings

def generate_launch_file(dataset_name, command_string, template, output_dir):
    launch_content = template.format(
        dataset_name=dataset_name,
        command_string=command_string
    )
    filename = os.path.join(output_dir, f"{dataset_name}.launch")
    with open(filename, "w") as f:
        f.write(launch_content)

# Template for the launch file
launch_template = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<launchConfiguration type="org.eclipse.jdt.launching.localJavaApplication">
    <listAttribute key="org.eclipse.debug.core.MAPPED_RESOURCE_PATHS">
        <listEntry value="/RFD-Incremental-Imputation/src/main/java/incremental_Imputation_v2/IncrementalImputationv2Alternative_ARGS.java"/>
    </listAttribute>
    <listAttribute key="org.eclipse.debug.core.MAPPED_RESOURCE_TYPES">
        <listEntry value="1"/>
    </listAttribute>
    <booleanAttribute key="org.eclipse.jdt.launching.ATTR_ATTR_USE_ARGFILE" value="false"/>
    <booleanAttribute key="org.eclipse.jdt.launching.ATTR_EXCLUDE_TEST_CODE" value="true"/>
    <booleanAttribute key="org.eclipse.jdt.launching.ATTR_USE_CLASSPATH_ONLY_JAR" value="false"/>
    <booleanAttribute key="org.eclipse.jdt.launching.ATTR_USE_START_ON_FIRST_THREAD" value="true"/>
    <stringAttribute key="org.eclipse.jdt.launching.CLASSPATH_PROVIDER" value="org.eclipse.m2e.launchconfig.classpathProvider"/>
    <stringAttribute key="org.eclipse.jdt.launching.MAIN_TYPE" value="incremental_Imputation_v2.IncrementalImputationv2Alternative_ARGS"/>
    <stringAttribute key="org.eclipse.jdt.launching.MODULE_NAME" value="RFD-Incremental-Imputation"/>
    <stringAttribute key="org.eclipse.jdt.launching.PROGRAM_ARGUMENTS" value="{command_string}"/>
    <stringAttribute key="org.eclipse.jdt.launching.PROJECT_ATTR" value="RFD-Incremental-Imputation"/>
    <stringAttribute key="org.eclipse.jdt.launching.SOURCE_PATH_PROVIDER" value="org.eclipse.m2e.launchconfig.sourcepathProvider"/>
    <stringAttribute key="org.eclipse.jdt.launching.VM_ARGUMENTS" value="-Xmx30G"/>
</launchConfiguration>
"""

#dataset = "EV_Vehicles_4000"  # Change dataset name as needed
dataset = "smartphones_823"  # Change dataset name as needed
# Dataset versions
versions = [1, 2, 3, 4, 5]
reevaluation=True
# Number of missing values
#missing_values = [480, 960, 1440, 1920, 2400, 4800, 9600, 14400, 19200, 24000] # Hospital Staff
#missing_values = [400, 800, 1200, 1600, 2000, 4000, 8000, 12000, 16000, 20000] #EV_Vehicles
#missing_values = [900, 1800, 2700, 3600, 4500, 9000, 18000, 27000, 36000, 45000] #Olympics_7500
#missing_values = [82, 165, 247, 329, 412, 823, 1646, 2469, 3292, 4115] #smartphones
missing_values = [840, 1680, 2520, 3360, 4200, 8400, 16800, 25200, 33600, 42000] #actors

# Generate the command strings
commands = generate_command_strings(versions, missing_values, dataset,reevaluation)

# Directory to save the .launch files
output_dir = f"./Launch_Files/{reevaluation}_{dataset}"
os.makedirs(output_dir, exist_ok=True)

# Generate the .launch files
for dataset_name, command_string in commands:
    generate_launch_file(dataset_name, command_string, launch_template, output_dir)

print(f"Generated {len(commands)} launch files in '{output_dir}'")





