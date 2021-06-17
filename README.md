# CMSC6950_Project
CMSC6950_Project | ARGOPY | Lavan [201990251]

## Installation instruction
### Create a conda environment
 $ conda create -n env_name python=3.8.5

### Activate the conda environment
 $ conda activate my_env
 
### clone the project
 $ git clone <https://github.com/lavanthaya/CMSC6950_Project.git>
 
### Run below command to install the dependencies
 $ make install

### To check the argopy installation run below command in Python shell
 >> from argopy import DataFetcher as ArgoDataFetcher

### ArgoPy fetch data from "Argovis" or "Erddap" you can check those server status below 

![Erddap status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/euroargodev/argopy-status/master/argopy_api_status_erddap.json) ![Argovis status](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/euroargodev/argopy-status/master/argopy_api_status_argovis.json)

### Run make file to execute the project
  $ make

### You can pass below set of arguments(optional) while running make file (given below are default values)
  Lon_min=-75, Lon_Max=-45, Lat_min=20, Lat_max=30, depth_min=0, depth_max=70, year_start=2011, year_end=2012, source=argovis
  
  Example:
  
  $ make source=erddap depth_max=100

### Final output can be accessed via below urls (Ctrl + C to stop the server)

   http://local-ip:8080/OceanTemp.gif
   
   http://local-ip:8080/Ocean_Sspeed_Temp.gif
   
   http://local-ip:8080/Ocean_Sspeed_Sal.gif
   
### Output Visualization:

#### Task-01 Visualization 

Ocean Temperature Plot on Geo Coordinates, Monthly Visualization

![task1_viz1](https://github.com/lavanthaya/CMSC6950_Project/blob/main/OceanTemp.gif)

#### Task-02 Visuaization

Sound Speed Vs Depth Plot With Temperature, Monthly Visualization

![task2_viz1](https://github.com/lavanthaya/CMSC6950_Project/blob/main/Ocean_Sspeed_Temp.gif)

Sound Speed Vs Depth Plot With Salinity, Monthly Visualization


![task2_viz2](https://github.com/lavanthaya/CMSC6950_Project/blob/main/Ocean_Sspeed_Sal.gif)

### Finally, run below command to clean
   $ make clean
   
