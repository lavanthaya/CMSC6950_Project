from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os.path
from os import path
import glob
from PIL import Image

DataFile = "argo_data.csv"

def Plot_temperature(data):
    '''This function is to plot the ocean temperature for given coordinates through out the month'''
    month = data["MONTH-YEAR"].unique()
    
    for m in month:
        temp_monthly = data.loc[data['MONTH-YEAR']==m]
        month_name = m.replace(' ' , '_')
        
        x = temp_monthly['LONGITUDE']
        y = temp_monthly['LATITUDE']
        z = temp_monthly['PRESURE (db)']
        c = temp_monthly['TEMPERATURE (C)']
        
        fig = plt.figure(figsize=(18,10))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.set_zlabel("Depth(m)")
        ax.invert_zaxis()
        img = ax.scatter(x, y, z, c=c, cmap=plt.hot())
        fig.colorbar(img, label='Temperature (*c)')
        plt.title('Ocean Temperature plot for the month of %s' % month_name)
        plt.savefig('oceanTemp_'+month_name+'.png')
        print('oceanTemp_'+month_name+'.png '+"File created")


if path.exists(DataFile):
    data = pd.read_csv(DataFile) 
    Plot_temperature(data)
else:
    print("The file Doesn't exist...!")


# Create a .gif file as final output
file_in = glob.glob("oceanTemp_*.png")
file_in.sort(key=os.path.getmtime) #sorting files by timestamp
file_out = "OceanTemp.gif"

img, *imgs = [Image.open(f) for f in file_in]
img.save(fp=file_out, format='GIF', append_images=imgs,
         save_all=True, duration=1200, loop=0)
