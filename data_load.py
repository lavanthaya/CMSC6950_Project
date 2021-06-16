from argopy import DataFetcher as ArgoDataFetcher
import pandas as pd
import numpy as np
import sys

def load_argodata(Lon_min=-75, Lon_Max=-45, Lat_min=20, Lat_max=30, 
                                depth_min=0, depth_max=70, yr_start='2011', yr_end='2012',source='argovis'):
    
    # Can choose 'argovis' or 'erddap' as source
    ds = ArgoDataFetcher(src=source).region([Lon_min, Lon_Max, Lat_min, Lat_max, 
                                depth_min, depth_max, yr_start, yr_end]).to_xarray()

    # Converting xarray to dataframe
    dr = ds.to_dataframe()

    # Cleaning the data 
    dr.replace("", np.nan, inplace=True)
    dr.dropna()

    # Adding new column ""Year" and "MONTH" from data extracted from "TIME column" 
    dr['MONTH'] = pd.DatetimeIndex(dr['TIME']).month
    dr['YEAR'] = pd.DatetimeIndex(dr['TIME']).year
    dr['TIME'] = pd.to_datetime(dr.TIME, format='%Y-%m-%d %H:%M:%S')
    dr['MONTH-YEAR'] = dr['TIME'].dt.strftime('%b %Y')

    # Filtering only the required data
    dr_filter =dr[['LATITUDE','LONGITUDE','TIME','MONTH','YEAR','MONTH-YEAR','PRES','PSAL','TEMP']]

    # Renaming the column name
    dr_col_rename = dr_filter.rename(columns={'PRES': 'PRESURE (db)', 'PSAL': 'PRACTICAL SALINITY (psu)','TEMP':'TEMPERATURE (C)'})

    # Save it to a csv file in local datastore
    dr_col_rename.to_csv('argo_data.csv',index=False)
    print("argo_data.csv data file created..!")

if len(sys.argv) == 10:
   a = sys.argv
   load_argodata(float(a[1]), float(a[2]), float(a[3]), float(a[4]), 
                            float(a[5]), float(a[6]), a[7], a[8], a[9])
else:
   load_argodata()

