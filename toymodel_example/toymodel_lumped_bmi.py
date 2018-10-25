import os
import toymodel_lumped
import bmi


#Use CSDMS standard variable names
class toy_bmi(bmi.Bmi):

    """
    BMI Base functionality
    """

    def initialize(self, filename):
        """Perform startup tasks for the model.
        Perform all tasks that take place before entering the model's time
        loop, including opening files and initializing the model state. Model
        inputs are read from a text-based configuration file, specified by
        `filename`.
        """
        self.filename = filename
        self.datadir = os.path.dirname(filename)
        inifile = os.path.basename(filename)

        self.toym = toymodel_lumped.mytoymodel(inifile)
        self.toym.read_config()


    def update(self):
        """Advance model state by one time step.
        Perform all tasks that take place within one pass through the model's
        time loop. This typically includes incrementing all of the model's
        state variables. If the model's state variables don't change in time,
        then they can be computed by the :func:`initialize` method and this
        method can return with no action.
        """
        self.toym.dt +=1

        return self.toym.model_run()


    def update_until(self, time):
        """Advance model state until the given time."""
        self.time = time
        self.toym.dt = self.time

        return self.toym.model_run()


    def update_frac(self, time_frac):
        """Advance model state by a fraction of a time step."""
        log = 'No fraction of timestep available'

        return log


    def finalize(self):
        """Perform tear-down tasks for the model."""

        return 'finalized'


    """
    BMI info functionality
    """

    def get_component_name(self):
        """Name of the component."""
        log = 'Toymodel Lumped Edition'

        return log


    def get_input_var_names(self):
        """List of a model's input variables.
        Input variable names must be CSDMS Standard Names, also known
        as *long variable names*.
        """

        return self.toym.var_in


    def get_output_var_names(self):
        """List of a model's output variables.
        Output variable names must be CSDMS Standard Names, also known
        as *long variable names*.
        """

        return self.toym.var_out


    """
    BMI time functionality
    """

    def get_start_time(self):
        """
        Returns model start time
        Input:  -
        Output: time as datetime (YYYY,MM,DD)
        """

        return self.toym.tstart


    def get_current_time(self):
        """Current time of the model.
        """

        return self.toym.tstep_nmbr


    def get_end_time(self):
        """End time of the model.
        """

        return self.toym.tend


    def get_time_step(self):
        """Current time step of the model.
        The model time step should be of type float. The default time
        step is 1.0.
        """

        return self.toym.tstep


    def get_time_units(self):
        """Time units of the model.
        """

        return self.toym.tunit


    """
    BMI grid functionality
    """

    def get_grid_rank(self, grid_id):
        """Get number of dimensions of the computational grid.
        """
        log = 'No get_grid_rank, get_grid_size, get_grid_type implemented'

        return log


    def get_grid_size(self, grid_id):
        """Get the total number of elements in the computational grid.
        """
        log = 'No get_grid_rank, get_grid_size, get_grid_type implemented'

        return log


    def get_grid_type(self, grid_id):
        """Get the grid type as a string.
        """
        log = 'No get_grid_rank, get_grid_size, get_grid_type implemented'

        return log


    def get_grid_shape(self):
        """Get dimensions of the computational grid.
        """

        return self.toym.grid_shape


    def get_grid_x(self):
        """Get coordinates of grid nodes in the streamwise direction.
        """

        return self.toym.grid_x


    def get_grid_y(self):
        """Get coordinates of grid nodes in the transverse direction.
        """

        return self.toym.grid_y


    def get_grid_z(self):
        """Get coordinates of grid nodes in the normal direction.
        """

        return self.toym.grid_z

    """
    BMI variable functionality
    """

    def get_var_type(self, var_name):
        """Get data type of the given variable.
        """
        self.var_name = var_name

        return self.toym.var_type[var_name]


    def get_var_units(self, var_name):
        """Get units of the given variable.
        Standard unit names, in lower case, should be used, such as
        ``meters`` or ``seconds``. Standard abbreviations, like ``m`` for
        meters, are also supported. For variables with compound units,
        each unit name is separated by a single space, with exponents
        other than 1 placed immediately after the name, as in ``m s-1``
        for velocity, ``W m-2`` for an energy flux, or ``km2`` for an
        area.
        """
        self.var_name = var_name
        #gettattribute, setattribute function can avoid hardcoding.

        return self.toym.var_units[var_name]


    def get_var_itemsize(self, var_name):
        """Get memory use for each array element in bytes.
        """
        self.var_name = var_name

        return self.toym.var_size[var_name]


    def get_var_nbytes(self, var_name):
        """Get size, in bytes, of the given variable.
        """
        self.var_name = var_name

        return self.toym.var_size[var_name]


    def get_var_grid(self, var_name):
        """Get grid identifier for the given variable.
        """
        log = 'No grid identifiers available'

        return log


    """
    BMI getter functionality
    """

    def get_value(self, var_name):
        """Get a copy of values of the given variable.
        This is a getter for the model, used to access the model's
        current state. It returns a *copy* of a model variable, with
        the return type, size and rank dependent on the variable.
        """
        self.var_name = var_name

        if self.var_name == 'Area':
            return self.toym.Area

        if self.var_name == 'prec':
            return self.toym.prec

        if self.var_name == 'Q':
            return self.toym.Q


    def get_value_ref(self, var_name):
        """Get a reference to values of the given variable.
        """
        log = 'Not implemented'

        return log


    def get_value_at_indices(self, var_name, indices):
        """Get values at particular indices.
        """
        log = 'No indices in lumped model'

        return log


    """
    BMI setter functionality
    """

    def set_value(self, var_name, src):
        """Specify a new value for a model variable.
        This is the setter for the model, used to change the model's
        current state. It accepts, through *src*, a new value for a
        model variable, with the type, size and rank of *src*
        dependent on the variable.
        """
        self.var_name = var_name
        self.src = src

        #Hardcoded for each variable, better to refer to dict and then update the variables.
        if self.var_name == 'Area':
            self.toym.Area = self.src
            print('Variable Area Set')

        if self.var_name == 'prec':
            self.toym.prec = self.src
            print('Variable prec Set')


    def set_value_at_indices(self, var_name, indices, src):
        """Specify a new value for a model variable at particular indices.
        """
        log = 'No indices in lumped model'

        return log