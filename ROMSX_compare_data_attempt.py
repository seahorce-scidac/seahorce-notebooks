#!/bin/python

#Activate conda env:
#conda activate seahorce
import xarray
import hvplot.xarray
import xarray
import numpy as np

import hvplot.xarray

import cartopy.crs as ccrs
import cartopy.feature as cfeature
import geoviews as gv

import matplotlib.pyplot as plt
#%matplotlib inline
import cmocean.cm as cmo
import os
home_top_dir=os.environ["HOME"]
ds_roms = xarray.open_dataset(home_top_dir+"/seahorce-scidac/COAWST/roms_his.nc", chunks={"ocean_time": 100})
ds = xarray.open_dataset(home_top_dir+"/seahorce-scidac/ROMSX/Exec/Upwelling/plt_his.nc", chunks={"ocean_time": 100})
for k in np.arange(-1,15):
    for j in np.arange(0,81):
        for i in np.arange(0,40):
            a=(ds.x_velocity.isel(xi_rho=slice(i,i+1), eta_rho=slice(j,j+1),s_rho=slice(1+k,2+k),ocean_time=1)).as_numpy()
            b=(ds_roms.u.isel(xi_u=slice(i+1,i+2), eta_u=slice(j+1,j+2),s_rho=slice(2+k,3+k), ocean_time=1)).as_numpy()
            diff_temp=a-b
            if(diff_temp!=0.0):
                print("-----Difference-----")
                print(diff_temp-0.0)
