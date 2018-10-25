import os
from sys import getsizeof
import numpy as np
import ConfigParser
from datetime import datetime
from datetime import timedelta
import xarray as xr


class mytoymodel(object):

    def __init__(self, inifile):

        #Set Path and inifile
        os.path.dirname(os.path.abspath('__file__'))
        self.inifile = inifile


    def read_config(self):
        #Read inifile
        config = ConfigParser.RawConfigParser()
        config.read(self.inifile)

        #Read timestep info
        self.tstart = config.get('run', 'starttime')
        self.tend = config.get('run', 'endtime')
        self.tstep = config.getint('run', 'timestep')

        # Calculate total amount of steps between start en end date
        tstep_nmbr = (datetime.strptime(self.tend, "%Y-%m-%d") - datetime.strptime(self.tstart, "%Y-%m-%d"))
        tstep_nmbr = int(tstep_nmbr.days)
        self.tstep_nmbr = tstep_nmbr
        self.tunit = "days" #Needed for BMI can also be directly read from inifile

        self.current = 0
        self.dt = 0 #Set timestep for loop

        #Read input variables
        Area = config.getfloat('parameters', 'Area')
        self.Area = np.array(Area)

        #Set input and output var names for BMI, can also be directly read from inifile
        self.var_in = ['Area', 'prec']
        self.var_out = ["Q"]

        #Import input datasets (precipitation) calculate 1 value for each timestep (lumped model)
        self.ds = xr.open_dataset('precipitation.nc')

        prec = self.ds['precipitation']
        prec_sum = prec.sum(dim='lat')
        prec_sum = prec_sum.sum(dim='lon')
        prec_sum.reset_coords(drop=True)
        self.prec_sum = prec_sum

        #Create empty array for modelrun
        self.Q = np.zeros(0)
        self.prec = np.array(self.prec_sum.values[0])

        #Set grid shape for BMI
        grid_x = config.getfloat('centroid', 'x')
        grid_x = np.array(grid_x)
        self.grid_x = grid_x

        grid_y = config.getfloat('centroid', 'y')
        grid_y = np.array(grid_y)
        self.grid_y = grid_y

        self.grid_z = 'No elevation taken into account'
        self.grid_shape = self.Q.shape


        #Set variable info for BMI, can also be retrieved from inifile
        self.var_type = {'Area': type(self.Area), 'prec': type(self.prec), 'Q': type(self.Q)}
        self.var_units = {'Area': 'm2', 'prec': 'mm/d', 'Q': 'm3/s'}
        self.var_size = {'Area': getsizeof(self.Area), 'prec': getsizeof(self.prec), 'Q': getsizeof(self.Q)}

        self.var_output = {'Area': self.Area, 'prec': self.prec, 'Q': self.Q}
        
        print "Initialization done"


    def model_run(self):

        while self.current < self.dt:

            #Select current date based on tstart and current timestep
            self.tdate = datetime.strptime(self.tstart, "%Y-%m-%d") + timedelta(days=self.current+1)
            self.tdate = datetime.strftime(self.tdate, "%Y-%m-%d")

            #Retrieve input for current timestep
            self.prec = self.prec_sum.sel(time=self.tdate).values

            #Calculate output for current timestep
            self.Q = (((self.prec / 1000)/ 86400) * self.Area)
            self.Q = np.array(self.Q)

            print 'Timestep:' + " " + str(self.current+1)

            #Get variables with BMI
            self.var_output = {'Area': self.Area, 'prec': self.prec, 'Q': self.Q}

            self.current += 1

