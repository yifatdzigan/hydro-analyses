## Running the notebook in Windows:

RUN 
```conda create --name ewatercycle python=2.7```
OR
```conda create --name ewatercycle python=3.6```

RUN 
```conda activate ewatercycle```

RUN 
```conda install xarray dask netCDF4 bottleneck```
OR 
```conda install -c conda-forge xarray cartopy pynio pseudonetcdf``` 
currntly pynio not available

RUN 
```conda install -c conda-forge cartopy```

RUN 
```conda install -c ioam holoviews bokeh```

RUN ```conda install -c pyviz geoviews```

RUN 
```pip install hydrostats```
RUN 
```pip install rank-histogram```
