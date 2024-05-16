#Create an environment with python 3.10
conda create -n myproject python=3.10
conda activate myproject
#Install packages
pip install pandas geopandas shapely
#Test of python version
python3
#Test of whether pandas and geopandas are installed: If there are no errors, and the interpreter returns to the next line without any messages, it means that both pandas and geopandas have been successfully installed and are accessible in the environment.You don't have to type ">>>" if they already exist.
>>> import pandas
>>> import geopandas
>>> import shapely

#Install OpenQuake Engine
#Step 1
pip install numpy scipy matplotlib lxml uncertainties sqlalchemy lxml cherrypy networkx

git clone https://github.com/gem/oq-engine.git
cd oq-engine
python setup.py install

pip install numba #This will install the 'numba' module in the environment, resolving the dependency issue for OpenQuake.
