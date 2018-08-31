
# coding: utf-8

# # Create Swift input files
# 
# This notebook create directory structure with Swift input files.

# ## Import modules

# In[1]:


# Import modules
import os
import shutil
import numpy as np
import pandas as pd
import yaml
from glob import glob
import tarfile


# ## Setting paths and configuring variables

# In[2]:


# Definitons
path_proj = os.getcwd()
path_ss_data = '../data/ss/'

with open('parameters.yaml', "r") as f:
    parameters = yaml.load(f)
    
n_planets = parameters["n_planets"]
n_clones = parameters["n_clones"]
n_lines = n_planets * n_clones
gm = parameters["gm"]
ialpha = parameters["ialpha"]
m = parameters["mass"]


# ## Read dataframe

# In[3]:


# Read cartesian coordinates
coord = pd.read_csv('../data/xv_invar.csv', dtype=float, delimiter=',')
coord.head()


# In[4]:


# Variables
x  = np.array(coord.x)
y  = np.array(coord.y)
z  = np.array(coord.z)
vx  = np.array(coord.vx)
vy  = np.array(coord.vy)
vz  = np.array(coord.vz)


# ## Configuring Sun's data
# 
# Configuring the Sun data.
# 
# - First line: 9 is the sum of the number of planets and the Sun (8 + 1).
# - Second line: 39.476926421373015 is the parameter gm, considering G = 1.
# - Third line: Position of the Sun in a heliocentric system.
# - Fourth line: Speed of the Sun in a heliocentric system.

# In[5]:


sun_data = """9
39.476926421373015
0.0 0.0 0.0
0.0 0.0 0.0\n"""


# ## Create files

# In[6]:


if os.path.isdir(path_ss_data):
    shutil.rmtree(path_ss_data)
    os.mkdir(path_ss_data)
else:
    os.mkdir(path_ss_data)
in_files = glob('../src/*.in')
k = -1
for i in range(n_clones):
    os.mkdir(path_ss_data + 'ss-' + str(i))
    for file in in_files:
        shutil.copy(file, path_ss_data + 'ss-' + str(i))
    with open(path_ss_data + 'ss-' + str(i) + "/" +'pl.in', 'w') as f:
        f.write(sun_data)
        for j in range(n_planets):
            k = k + 1
            f.write('{0:.15e}\n'.format(m[j]))
            f.write('{0:.15e} {1:.15e} {2:.15e}\n'.format(x[k], y[k], z[k]))
            f.write('{0:.15e} {1:.15e} {2:.15e}\n'.format(vx[k], vy[k], vz[k]))


# ## Verifying results

# ### directories

# In[7]:


print(os.listdir('../data/ss'))


# ### pl.in

# In[8]:


with open(path_ss_data + 'ss-0/pl.in') as f:
    for i in f.readlines():
        print(i)

