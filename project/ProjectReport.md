
## EMSC4033 - Project Report

### Path-Dependent Attenuation Ground Motion Field in Volcanic Areas

### Instructions

- __Data source.__ The information of any earthquake can be found on USGS website: https://earthquake.usgs.gov/earthquakes/search. The volcanic position shape file can be found at this link: https://github.com/Yotghoe/Path-Dependent-Attenuation-Ground-Motion-Field-in-Volcanic-Areas/tree/main/notebook/assets
- ~~OpenQuake calculation (~~__This step can be ignored in this project since the data are provided, required data can be found at this link: https://github.com/Yotghoe/Path-Dependent-Attenuation-Ground-Motion-Field-in-Volcanic-Areas/tree/main/notebook/assets__~~). This project requires ground motion fields data produced by OpenQuake engine, the engine should be installed (Details at https://docs.openquake.org/oq-engine/master/manual/getting-started/installation-instructions/index.html#installing-the-long-term-support-lts-version) and calculation should be run (Tutorial at https://youtu.be/nbYBBT8r3N0).~~  
```
#Open the terminal or command prompt on your computer.  
cd /.../directory #Can be replaced by any location you want
#Clone the repository
git clone https://github.com/Yotghoe/Path-Dependent-Attenuation-Ground-Motion-Field-in-Volcanic-Areas.git new_directory_name
```
- __Create and activate the environment__
```
conda env create -f environment.yml
conda activate myproject
#Open Jupyter lab
jupyter-lab
```
- 


Add here instructions for what the user need to do to use your code. List any dependencies and/or input files that might be needed or include instructrions for how the user can use, e.g., a custom conda environment that you may have included with your code.

### List of dependencies + short description

(for example)

- **numpy**: a package to create and manipulate n-dimensional arrays
- **package_blah_blah*: ...

Ideally there will be something like an environment.yml file (conda) or a requirements.txt (pip) in the repository

You should also discuss why you need specific dependencies and we would always take a minimslist view: only add what you need.




### Testing

Give a short description of the tests and input validations you have included in your code.

Remember: tests are checks to see that you have not added bugs to your code since it was last run whereas validation means that you check the input data to make sure it is consistent with the expectations. Generally you need both.



### Limitations

Describes the limitations of your code. E.g., it only works with netCDF files because of this package that is used cannot read anything else. Any other limitations also in what users cannot do with this code. Or other things that you feel you could have done better?



### Future Improvements	

Talk a bit about how you or somebody could take this code to the next level. How is the code generalizable to solve more general problems?
