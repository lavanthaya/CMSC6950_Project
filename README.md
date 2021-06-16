# CMSC6950_Project
CMSC6950_Project | ARGOPY

## Installation instruction
### Create a conda environment
 $ conda create -n env_name python=3.8.5

### Activate the conda environment
 $ conda activate my_env
 
### Install dependencies
 $ conda install -c conda-forge cartopy
 $ pip install seaborn, netCDF, Pillow==6.2.2, matplotlib
  
### Install ARGOPY
 $ pip install git+http://github.com/euroargodev/argopy.git@master

### To check the installation run below command in Python shell
 >> from argopy import DataFetcher as ArgoDataFetcher
 
 


