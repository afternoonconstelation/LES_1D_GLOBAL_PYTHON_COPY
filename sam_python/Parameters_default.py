import  os,sys
import cartopy.crs as ccrs
MODEL='SAM'

plotdef='2d'

#Latex width 
wf=0.50
hf=1.0
cmmais=0.0

extend='both'

egeon='/pesq'

UTC=-4

path ="./" 

# Out figure folder
out_fig=path

#out python nc files
out_files= path+'/python_nc'


# Check if the directory exists
if not os.path.exists(out_fig):
    # If it doesn't exist, create it
    os.makedirs(out_fig)

# Check if the directory exists
if not os.path.exists(out_files):
    # If it doesn't exist, create it
    os.makedirs(out_files)
