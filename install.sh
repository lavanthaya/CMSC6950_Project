#!/bin/sh

echo "Installing Conda packages...!"
conda install -c conda-forge cartopy

echo "Installing pip packages...!"
pip install seaborn tqdm netCDF4 Pillow==6.2.2 matplotlib

echo "Installing ArgoPy"
pip install git+http://github.com/euroargodev/argopy.git@master
