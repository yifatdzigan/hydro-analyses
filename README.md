# hydro-analyses
Repository for data analyses

1. Model validation analysis
2. Model calibration analysis
3. Model forecast and ensemble analysis

Each of these subsections require different types of outputdata and benefit from certain metrics and plots. The aim is to collect all plots, metrics, and functions used in the analysis to create a library that is publicly available.

Short description of the subsection/ what to expect as of now.

1. Model validation:
The model validation can be performed in many shapes and forms, however for the time being the focus will be on stream flow (discharge) validation of the model outputs. The main dataset for validation will be the GRDC river discharge dataset. This dataset possess many problems; the discharge station locations do not always coincide with the river locations of the model outputs, multiple discharge stations can coincide within one model pixel/grid cell, and inconsistent data quality (data gaps).
To do:

Build station filter that selects stations that match the choice of model (resolution) with the aim to enhance data consistency and quality.
Exclude multiple stations in one grid cell or solve the problem in a different manner.
Figure out how to match river and station locations.

2. Model calibration:
To be determined.

3. Model forecast and ensemble:
Again a lot of different types of analyses can be performed. An overview of the different options is given in the following links:

- https://www.ecmwf.int/sites/default/files/elibrary/2017/17626-ensemble-verification-metrics.pdf
- https://www.esrl.noaa.gov/psd/people/tom.hamill/MSMM_vizverif_hamill.pdf
- http://www.nws.noaa.gov/oh/rfcdev/docs/HHartmann_ensemble_verification_refresher_RFCworkshop_Nov08_Part3.pdf
- https://oss.deltares.nl/c/document_library/get_file?uuid=8be6e178-f3d3-4c46-a40f-5ae851cbe8c8&groupId=145641
