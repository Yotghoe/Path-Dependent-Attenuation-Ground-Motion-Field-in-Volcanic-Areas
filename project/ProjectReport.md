
## EMSC4033 - Project Report

### Path-Dependent Attenuation Ground Motion Field in Volcanic Areas

### Instructions

- __Data source.__ The information of any earthquake can be found on USGS website: https://earthquake.usgs.gov/earthquakes/search. The volcanic position shape file can be found at this link: https://github.com/Yotghoe/Path-Dependent-Attenuation-Ground-Motion-Field-in-Volcanic-Areas/tree/main/notebook/assets
- ~~OpenQuake calculation~~ (__This step can be ignored in this project since the data are provided, required data can be found at this link: https://github.com/Yotghoe/Path-Dependent-Attenuation-Ground-Motion-Field-in-Volcanic-Areas/tree/main/notebook/assets__). ~~This project requires ground motion fields data produced by OpenQuake engine, the engine should be installed (Details at https://docs.openquake.org/oq-engine/master/manual/getting-started/installation-instructions/index.html#installing-the-long-term-support-lts-version) and calculation should be run (Tutorial at https://youtu.be/nbYBBT8r3N0).~~  
```
#Open the terminal or command prompt on your computer.  
cd /.../directory #Can be replaced by any location you want
#Clone the repository
git clone https://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@github.com/Yotghoe/Path-Dependent-Attenuation-Ground-Motion-Field-in-Volcanic-Areas.git
```
- __Create and activate the environment__
```
cd Path-Dependent-Attenuation-Ground-Motion-Field-in-Volcanic-Areas
conda env create -f environment.yml
conda activate myproject
#Open Jupyter lab
jupyter-lab
```
- __Open notebook.__ Open'notebook/notebook.ipynb', Run the code.


### List of dependencies + short description


- **pandas**: Data manipulation and analysis library for handling tabular data. In this project, it is used to read, clean, and merge site coordinates and GMF data.
- **geopandas**: Extension of pandas for geospatial data manipulation. In this project, it is used to read and manipulate shapefiles, create and analyse geospatial data, and handle coordinate transformations.
- **shapely**: Library for creating and manipulating geometric shapes. In this project, it is used to create geometric objects like points and line strings, and perform spatial operations such as buffering.
- **matplotlib**: Library for creating visualizations and plots. In this project, it is used to visualise the original and combined ground motion field data.
- **jupyterlab**: Interactive development environment for notebooks, code, and data. JupyterLab can easily create an independent environment.
- **notebook**: Web-based interactive environment for creating Jupyter notebooks. Jupyter notebook can save the unfinished code easily, terminal can not.


### Testing

- **Tests**: In each small step, there are tests in the form of `print()` and `assert`. `print()` helps verify that each step of the process is producing the expected results. `assert` checks that the data is not empty and that necessary columns are present.
- **Validation**: The project visualised the original and combined GMF data, earthquake source, and volcanic buffers. Comparing the visuals, it is clear that the combination of oringinal ground motion fields is based on whether the path to each site crosses buffers that delimit volcanic areas. The combination performed correctly.


### Limitations

- It will not work with h5py files because of h5py package is not included in this environment/project.
- It is only applicable to the fusion of one high attenuation GMF and one low attenuation GMF, and is not suitable for the fusion of additional GMFs.
- The volcanic areas ploygons(buffers) are rough.



### Future Improvements	

- Install and import package h5py, make the code availabale for h5py files.
- Combine multiple GMFs depending on how long their path form source to site intersects the volcanic areas.
- Gather information (e.g. satallite imagery) to draw better volcanic areas.
