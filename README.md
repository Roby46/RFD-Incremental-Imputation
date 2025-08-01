
# RFD-based imputation: an empirical study

This repository contains all useful tools for replicating the empirical study concering metadata-driven incremental imputation. Our study focuses on the evaluation of the benefits derived from the cooperation between incremental discovery algorithms and metadata-driven imputation algorithms. To this aim, we devised two different pipelines: the Imputation Pipeline poses an incremental discovery algorithm to support imputation, while the Discovery pipeline poses imputation processes to support metadata discovery.
This repository contains a python project that provides all the necessary tools to prepare data and to perform an evaluation of the results. The scripts for plotting the latters is also here provided. 

## Project overview

The repository is divided into two main folders (i.e.,  RFD-Incremental Imputation Utils and RFD-Incremental Imputation Exe).


The folder contains the following Java Executables:


### 1 - RFD-Incremental Imputation Utils

This folder contains a python project which provides all the necessary tool to perform data preprocessing and evaluate the results of imputation. This project is divided into 3 main subfolders (i.e., Datasets, Preprocessing, Evaluation).

### 2.1 Datasets

This folder is divided into 3 subfolders: ‘Original Datasets’ contains the original datasets, ‘Preprocessed Datasets’ contains the filtered and cleaned datasets, and ‘Missing Datasets’ contains the data with injected missing values. In the following table we report the basic characteristics of the datasets we employed in our experiments. Specifically, the table reports the name and the number of rows and columns of the datasets (in their preprocessed version) along with the link to the original dataset. Finally, for each dataset we also report the parameters used for the experiments: the size of the sliding window (i.e., 2% for the pipeline executions, 15% and 20% for the baseline executions).


| Dataset Name  | Rows  | Columns | WindowSize (2%,20%) | Thresholds                                                   | Source                                                                                                                 |
|---------------|-------|---------|---------------------|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Cars          | 406   | 9       | 8,80                | [5.0,4.18,0.82,16,10.0,11.3,1.37,1.84,1.0]                   | https://github.com/DastLab/TestDataset                                                                                 |
| Restaurant    | 864   | 6       | 18,180              | [2.0,8.5,8.5,1.0,1.0,3.5]                                    | https://www.kaggle.com/datasets/adrianevensen/restaurants-entity-resolution                                            |
| Boeing        | 898   | 10      | 17,170              | [1, 3, 3, 1, 2, 1, 3, 2, 2, 2]                               | https://www.kaggle.com/datasets/nurielreuven/boeing-historical-airplane-orders-deliveries                              |
| Cats          | 1071  | 10      | 21,210              | [ 0.5,0.5,2,0,3,0.5,0,0,0,0]                                 | https://www.kaggle.com/datasets/joannanplkrk/its-raining-cats                                                          |
| Police        | 2204  | 9       | 44,440              | [3.5,3.5,3.5,3.5,1,3.5,3.5,3.5,3.5]                          | https://data.world/stevenburnett/police-shootings-2015-2016                                                            |
| Telemetry     | 3000  | 8       | 60,600              | [1.5,0.001,2.5,0.5,0.001,0.5,0.003,2]                        | https://www.kaggle.com/datasets/garystafford/environmental-sensor-data-132k                                            |
| Actors        | 4000  | 7       | 80,800              | [1, 0, 3, 2, 100, 1.5,0]                                     | https://www.kaggle.com/datasets/darinhawley/imdb-films-by-actor-for-10k-actors                                         |
| Med_Ch        | 2500  | 12      | 50,500              | [0.5,1,2,1,0.5,1,3,500,500,500,0.5,2]                        | https://www.openml.org/search?type=data&status=active&qualities.NumberOfInstances=between_1000_10000&id=42130&sort=runs |
| F1            | 5000  | 7       | 100,1000            | [0.5,2,0.5,0.5,0.5,0.5,0.5]                                  | https://www.kaggle.com/datasets/lakshayjain611/f1-races-results-dataset-1950-to-2024                                   |
| MotoGP        | 3000  | 12      | 60,600              | [2,0,1,3,2,5,6,4,2,5,0,0]                                    | https://www.kaggle.com/datasets/amalsalilan/motogpresultdataset                                                        |
| US_Presidents | 3754  | 10      | 75,750              | [1,1,1,1,2,2,1,250,250,1]                                    | https://www.kaggle.com/datasets/tunguz/us-elections-dataset                                                            |
| NBA 3200      | 3200  | 12      | 64,640              | [2,2,2,2,2,5,2,3,10,2,2,2]                                   | https://www.kaggle.com/datasets/jacobbaruch/basketball-players-stats-per-season-49-leagues                             |
| EV_Vehicles   | 4000  | 10      | 80,800              | [2.5,2.5,1,2,2,3,3,3,20,10]                                  | https://www.kaggle.com/datasets/utkarshx27/electric-vehicle-population-data                                            |
| Superstore    | 4500  | 11      | 90,900              | [1, 0, 2, 1,1, 1, 3, 0, 3, 10]                               | https://www.kaggle.com/datasets/rohitsahoo/sales-forecasting                                                           |
| Air           | 9000  | 13      | 180,1800            | [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5] | https://www.kaggle.com/datasets/fedesoriano/air-quality-data-set                                                       |

### 2.2 Preprocessing

The Preprocessing folder contains all the scripts needed to prepare the data and generate the files required for the imputation algorithm. 
- The ColumnTypes folder contains a csv file showing the column types for each dataset configuration. This file is necessary for the imputation algorithm and is automatically updated each time a new dataset with null values is generated. 
- The Dataset_Preprocessing folder contains scripts for preprocessing datasets. These will load the dataset from the Original_Datasets folder and save the preprocessed version in Preprocessed_Dataset.
- The Header folder contains a csv file that associates each generated dataset with its header. This file is necessary for the imputation algorithm and is automatically updated when a new version of the dataset with null values is generated. 
- The Initial_tuples folder contains, for each dataset with missing values that is generated, information about the location of the injected missing values and the value originally present. This file is used to assess the quality of the imputations made, and is automatically generated during the generation of the dataset with null values. 
- The MissingValue_Injector folder contains the script for injecting null values. The generated dataset versions will be saved in the folder ‘Missing_Datasets’.
- The param_generator folder contains a script to automatically generate the arguments to be given as input to the imputation algorithm. 

### 2.3 Evaluation

This folder contains the files needed to assess the quality of the imputations made and the scripts to generate the plots reported in the paper. 
- The Imputation_Results folder contains the csv files of the results. These files are generated by the imputation algorithm, and are updated incrementally at each step of the algorithm. At the end of the imputation process, this file contains an entry for each missing value originally present, to which it associates either the imputed value or a symbol (in this repository we use ‘?’) to indicate that the value was not imputed. 
- The Imputation_Verifier folder contains the scripts needed to evaluate the quality of the imputation. there is a script for each of the tested datasets. These scripts make use of XML files stored in the ‘XML Files’ folder that contain any similarity rules for the values of the dataset under test. The scripts count the number of correct, incorrect and similar imputations (e.g. ‘ny’ is similar to ‘new york’). XML files contain rules for the attributes where these evaluations need to be made, and contain rules of 3 types (noexpr, delta and expr). NoExpr is used to indicate equivalence classes (like the example of new york mentioned earlier). The delta-type rule, on the other hand, indicates that an imputed value is to be considered similar if it differs by less than a predetermined threshold from the original value. The condition type expr was used to check imputations made on attributes of type telephone. Specifically, it is checked whether the numbers are identical regardless of the separator used for the digits.
- The plots folder contains the scripts needed to replicate the plots shown in the paper. 
- The ALL_Results file is a csv file containing, for each experimental setup, the imputation results obtained. This file is automatically updated during the execution of the imputation verification scripts. 


## How to use

In what follows, we provide an example on how to use the tools in this repository. Specifically, we consider an example regarding the dataset EV_Vehicles. 

### Step 1: Preprocessing
#### 1.1 Dataset preparation
First, the original dataset (in the Original Datasets folder) is preprocessed to remove null values already present, to clean up any imperfections and to remove attributes not of interest in the imputation process (such as IDs). To do this, you can run the Preprocessing EV Vehicles file in the Preprocessing > Dataset_Preprocessing folder.
#### 1.2 Missing value injection
At this point, the dataset is ready to be used to generate data for the experiment. In Preprocessing > MissingValue_Injector there is a file that allows you to automatically generate datasets with various percentages of missing values (which can be specified in the percentages list). it is also possible to specify the number of datasets generated by the script: in our study we generate 5 datasets for each percentage of missing values, then set the iteration list with the version numbers (1,2,3,4,5)
#### 1.3 Parameters generation
After the previous steps have been completed, the imputation can be started. To simplify the start of the script, there is a script in the Preprocessing > Param_Generation folder that automatically generates the argument string to be passed to the java executable. 
### Step 2: Run algorithms

#### 2.1 Configuration

All the Java executables require the following arguments:
- Dataset name: the name of the dataset, including the file extension
- Delimiter: the symbol used as delimiter in the csv file
- Missing value: the symbol used to indicate a missing value
- Number of attributes: number of columns of the dataset
- Window size: the size of the sliding window
- Re-evaluation: a boolean parameter that, if set to True, enables the re-evaluation of older imputations made with invalidated RFDs. When set to false, the algorithms will not re-evaluate previously made imputations 
- Thresholds: a list of float numbers indicating the similarity thresholds defined on each attribute of the dataset

For example, these are the arguments for the execution of a test on the EV_Vehicles_4000 dataset, with 480 missing values and the first configuration:
```
"EV_Vehicles_4000_480_1.csv" ";" "?" 10 80 "True" 2.5 2.5 1 2 2 3 3 3 20 10
```
where 10 is the number of attributes, 80 the size of the sliding window and the remaining values are the threshold for each attribute. 
#### 2.2 Run imputation Pipeline & Baseline approach
#### 2.3 Run discovery Pipeline & Baseline approach

### Step 3: Evaluation

#### 3.1 Evaluate Imputation
#### 3.2 Generate Plots



### 2 - RFD-Incremental Imputation (Exe)
This folder contain the java executables necessary for running the experiments. This section describes the main files stored in this folder, for instructions about how to run the experiments refer to the section "How to Use". 

### 1.1 - Project Files

To run the experiments, the following files are required:
- Dataset
- Initial_tuples
- Headers
- Column_Types

### 1.2 - Project Executables

