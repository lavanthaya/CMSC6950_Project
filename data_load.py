from argopy import DataFetcher as ArgoDataFetcher
import pandas as pd
import numpy as np


# Can choose 'argovis' or 'erddap' as source
ds = ArgoDataFetcher(src='argovis').region([-75, -45, 20, 30, 0, 70, '2011', '2012']).to_xarray()

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