import os

def generate_command_strings(versions, missing_values, dataset, use_true):
    #fixed_params = [";", "?", 10, 80, 2.5, 2.5, 1, 2, 2, 3, 3, 3, 20, 10] #EV_Vehicles
    #fixed_params = [";", "?", 12, 150, 3,0,5,2,8,2,1,4,1,2,2,2] #Olympics
    #fixed_params = [";", "?", 10, 16, 1, 5, 10000, 10,2, 2, 0.5, 4, 32, 3] #Smartphones
    #fixed_params = [";", "?", 7, 240, 5, 0, 5, 2,60, 1.5, 0] #Actors
    #fixed_params = [";", "?", 10, 100, 6, 0, 5, 10, 3, 0, 0, 1, 2, 3] #Chicago
    #fixed_params = [";", "?", 12,157,2,2,2,2,2,5,2,3,10,2,2,2 ]  # NBA
    fixed_params = [";", "?", 12,64,2,2,2,2,2,5,2,3,10,2,2,2 ]  # NBA 3200 64-640
    #fixed_params = [";", "?", 9, 82,2,500,0,0,10,4,20000,1,5]  # Bikes
    #fixed_params = [";", "?", 9, 82, 6, 5000, 6, 6, 5, 8, 10000, 12, 6] # Bikes Updated  82-820
    #fixed_params = [";", "?", 7, 80,1, 0, 3, 2, 100, 1.5,0]  # ActorFilms
    #fixed_params = [";", "?", 11, 90, 1, 0, 2, 1,1, 1, 3, 0, 3, 10,50] #Superstore
    #fixed_params = [";", "?", 12, 177, 2,0,1,3,2,5,6,4,2,5,0,0]  # MotoGP


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

def generate_launch_file(dataset_name, command_string, template, output_dir, reevaluation, algoritmo, heap_size_gb):
    launch_content = template.format(
        dataset_name=dataset_name,
        command_string=command_string,
        heap_size_gb=heap_size_gb
    )
    filename = os.path.join(output_dir, f"{algoritmo}_{heap_size_gb}gb_{dataset_name}_{reevaluation}.launch")
    with open(filename, "w") as f:
        f.write(launch_content)


#dataset = "EV_Vehicles_4000"  # Change dataset name as needed
dataset = "NBA_3200"  # Change dataset name as needed
# Dataset versions
versions = [1, 2, 3, 4, 5]
heap_size_gb=60

#Scelta delle pipeline
algoritmo="Pipeline"
#algoritmo="Baseline"
#algoritmo="RFD_Generator"
reevaluation=False #solo per la pipeline. Per i baseline ed il generator non importa il valore settato

# Number of missing values
#missing_values = [480, 960, 1440, 1920, 2400, 4800, 9600, 14400, 19200, 24000] # Hospital Staff
#missing_values = [400, 800, 1200, 1600, 2000, 4000, 8000, 12000, 16000, 20000] #EV_Vehicles
#missing_values = [900, 1800, 2700, 3600, 4500, 9000, 18000, 27000, 36000, 45000] #Olympics_7500
#missing_values = [82, 165, 247, 329, 412, 823, 1646, 2469, 3292, 4115] #Smartphones
#missing_values = [840, 1680, 2520, 3360, 4200, 8400, 16800, 25200, 33600, 42000] #Actors
#missing_values = [500, 1000, 1500, 2000, 2500, 5000, 10000, 15000, 20000, 25000] #Chicago
#missing_values = [940, 1881, 2821, 3761, 4702, 9403, 18806, 28210, 37613, 47016] #NBA
missing_values = [384, 768, 1152, 1536, 1920, 3840, 7680, 11520, 15360, 19200] #NBA 3200
#missing_values = [369, 738, 1107, 1476, 1845, 3690, 7380, 11070, 14760, 18450] #Bikes
#missing_values = [280,560,840,1120,1400,2800,5600,8400,11200,14000] #Actors
#missing_values=[495,990,1485,1980,2475,4950,9900,14850,19800,24750] #Superstore
#missing_values=[1064,2129,3193,4258,5322,10644,21288,31932,42576,53220] #MotoGP

print(algoritmo)

launch_template=""
if(algoritmo=="Pipeline"):
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
        <stringAttribute key="org.eclipse.jdt.launching.VM_ARGUMENTS" value="-Xmx{heap_size_gb}G"/>
    </launchConfiguration>
    """
elif(algoritmo=="Baseline"):
    # Template for the launch file
    launch_template = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <launchConfiguration type="org.eclipse.jdt.launching.localJavaApplication">
        <listAttribute key="org.eclipse.debug.core.MAPPED_RESOURCE_PATHS">
            <listEntry value="/RFD-Incremental-Imputation/src/main/java/incremental_Imputation_v2/IncrementalImputationv2_Comparison_ARGS.java"/>
        </listAttribute>
        <listAttribute key="org.eclipse.debug.core.MAPPED_RESOURCE_TYPES">
            <listEntry value="1"/>
        </listAttribute>
        <booleanAttribute key="org.eclipse.jdt.launching.ATTR_ATTR_USE_ARGFILE" value="false"/>
        <booleanAttribute key="org.eclipse.jdt.launching.ATTR_EXCLUDE_TEST_CODE" value="true"/>
        <booleanAttribute key="org.eclipse.jdt.launching.ATTR_USE_CLASSPATH_ONLY_JAR" value="false"/>
        <booleanAttribute key="org.eclipse.jdt.launching.ATTR_USE_START_ON_FIRST_THREAD" value="true"/>
        <stringAttribute key="org.eclipse.jdt.launching.CLASSPATH_PROVIDER" value="org.eclipse.m2e.launchconfig.classpathProvider"/>
        <stringAttribute key="org.eclipse.jdt.launching.MAIN_TYPE" value="incremental_Imputation_v2.IncrementalImputationv2_Comparison_ARGS"/>
        <stringAttribute key="org.eclipse.jdt.launching.MODULE_NAME" value="RFD-Incremental-Imputation"/>
        <stringAttribute key="org.eclipse.jdt.launching.PROGRAM_ARGUMENTS" value="{command_string}"/>
        <stringAttribute key="org.eclipse.jdt.launching.PROJECT_ATTR" value="RFD-Incremental-Imputation"/>
        <stringAttribute key="org.eclipse.jdt.launching.SOURCE_PATH_PROVIDER" value="org.eclipse.m2e.launchconfig.sourcepathProvider"/>
        <stringAttribute key="org.eclipse.jdt.launching.VM_ARGUMENTS" value="-Xmx{heap_size_gb}G"/>
    </launchConfiguration>
    """
elif(algoritmo=="RFD_Generator"):
    # Template for the launch file
    launch_template = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
    <launchConfiguration type="org.eclipse.jdt.launching.localJavaApplication">
        <listAttribute key="org.eclipse.debug.core.MAPPED_RESOURCE_PATHS">
            <listEntry value="/RFD-Incremental-Imputation/src/main/java/incremental_Imputation_v2/IncrementalImputationv2_RFDGenerator_ARGS.java"/>
        </listAttribute>
        <listAttribute key="org.eclipse.debug.core.MAPPED_RESOURCE_TYPES">
            <listEntry value="1"/>
        </listAttribute>
        <booleanAttribute key="org.eclipse.jdt.launching.ATTR_ATTR_USE_ARGFILE" value="false"/>
        <booleanAttribute key="org.eclipse.jdt.launching.ATTR_EXCLUDE_TEST_CODE" value="true"/>
        <booleanAttribute key="org.eclipse.jdt.launching.ATTR_USE_CLASSPATH_ONLY_JAR" value="false"/>
        <booleanAttribute key="org.eclipse.jdt.launching.ATTR_USE_START_ON_FIRST_THREAD" value="true"/>
        <stringAttribute key="org.eclipse.jdt.launching.CLASSPATH_PROVIDER" value="org.eclipse.m2e.launchconfig.classpathProvider"/>
        <stringAttribute key="org.eclipse.jdt.launching.MAIN_TYPE" value="incremental_Imputation_v2.IncrementalImputationv2_RFDGenerator_ARGS"/>
        <stringAttribute key="org.eclipse.jdt.launching.MODULE_NAME" value="RFD-Incremental-Imputation"/>
        <stringAttribute key="org.eclipse.jdt.launching.PROGRAM_ARGUMENTS" value="{command_string}"/>
        <stringAttribute key="org.eclipse.jdt.launching.PROJECT_ATTR" value="RFD-Incremental-Imputation"/>
        <stringAttribute key="org.eclipse.jdt.launching.SOURCE_PATH_PROVIDER" value="org.eclipse.m2e.launchconfig.sourcepathProvider"/>
        <stringAttribute key="org.eclipse.jdt.launching.VM_ARGUMENTS" value="-Xmx{heap_size_gb}G"/>
    </launchConfiguration>
    """

# Generate the command strings
commands = generate_command_strings(versions, missing_values, dataset,reevaluation)

# Directory to save the .launch files
output_dir = f"./Launch_Files/{algoritmo}_{heap_size_gb}gb_{reevaluation}_{dataset}"
os.makedirs(output_dir, exist_ok=True)

# Generate the .launch files
for dataset_name, command_string in commands:
    generate_launch_file(dataset_name, command_string, launch_template, output_dir, reevaluation, algoritmo, heap_size_gb)

print(f"Generated {len(commands)} launch files in '{output_dir}'")





