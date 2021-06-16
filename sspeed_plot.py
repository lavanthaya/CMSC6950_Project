from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os.path
from os import path
import glob
from PIL import Image

DataFile = "SSpeed_data.csv"

def plot_sspeed_temp(data, month):
    fig, ax = plt.subplots(figsize=(18, 10))
    img = ax.scatter(data['SSPEED'], data.index, s=200, c=data['TEMPERATURE (C)'], cmap='YlOrRd', label = data['TEMPERATURE (C)'])
    ax.set_xlabel('SSPEED (m/s)')
    ax.set_ylabel('DEPTH (m)')
    ax.set_title('Sound of Speed in Ocean with Temperature - %s' % month)
    plt.colorbar(img, label='Temperature (*c)')
    plt.grid(True)
    plt.savefig('sspeed_temp_'+month+'.png')
    print('sspeed_temp_'+month+'.png '+"File created")
    plt.close(fig)


def plot_sspeed_salinity(data, month):
    fig, ax = plt.subplots(figsize=(18, 10))
    img = ax.scatter(data['SSPEED'], data.index, s=200, c=data['PRACTICAL SALINITY (psu)'], cmap='YlGn', label = data['PRACTICAL SALINITY (psu)'])
    ax.set_xlabel('SSPEED (m/s)')
    ax.set_ylabel('DEPTH (m)')
    ax.set_title('Sound of Speed in Ocean with Salinity - %s' % month)
    plt.colorbar(img, label='Salinity (psu)')
    plt.grid(True)
    plt.savefig('sspeed_sal_'+month+'.png')
    print('sspeed_sal_'+month+'.png '+"File created")
    plt.close(fig)

def make_gif(file_in, file_out):
    ss_files = glob.glob(file_in)
    gif_file = file_out

    ss_files.sort(key=os.path.getmtime) #sorting files by timestamp
    
    img, *imgs = [Image.open(f) for f in ss_files]
    img.save(fp=gif_file, format='GIF', append_images=imgs,
             save_all=True, duration=1200, loop=0)
    
    img.close()


if path.exists(DataFile):
    data = pd.read_csv(DataFile) 
    months = data["MONTH-YEAR"].unique()

    for m in months:
        ds_month = data.loc[data['MONTH-YEAR']==m]
        ds_month = ds_month.groupby(['DEPTH (m)']).mean()
        month_name = m.replace(' ' , '_')

        plot_sspeed_temp(ds_month, month_name)
        plot_sspeed_salinity(ds_month, month_name)

    make_gif("sspeed_temp_*.png", "Ocean_Sspeed_Temp.gif")
    make_gif("sspeed_sal_*.png", "Ocean_Sspeed_Sal.gif")

else:
    print("The file Doesn't exist...!")