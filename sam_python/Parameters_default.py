import pathlib
import  os,sys
import cartopy.crs as ccrs
from pathlib import Path
MODEL='SAM'

plotdef='2d'

#Latex width 
wf=0.50
hf=1.0
cmmais=0.0

extend='both'

egeon='/pesq'

UTC=-4

# default. assumes that data is in the current directory. 
# You can change this to any other path where your data is located.
# @todo: if path not specified, use the current working directory
path=Path("./Rar_data") 

# Out figure folder
out_fig=path.joinpath('sam_figures')

#out python nc files
out_files= path.joinpath('python_nc')


# Check if the directory exists
os.makedirs(out_fig, exist_ok=True)
# Check if the directory exists
os.makedirs(out_files, exist_ok=True)
