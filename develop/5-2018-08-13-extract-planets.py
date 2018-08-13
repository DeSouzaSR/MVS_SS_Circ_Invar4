
# coding: utf-8

# # Analysis of the semi-major axis
# 
# Analysis of the semi-major axis of the MVS_SS_Circ_Invar Simulation.

# ## Import modules, configuring variables and settings paths

# In[1]:


import os
import subprocess
import shutil
from glob import glob
import yaml


# In[2]:


# Definitons
path_proj = os.getcwd()
path_ss_data = '../data/ss'
prefix_simulation = 'ss-'
# Follow program path
follow_path = '/home/sandro/Programas/swift/tools' # Linux

with open(path_proj + '/parameters.yaml', "r") as f:
    parameters = yaml.load(f)
    
n_planets = parameters["n_planets"]
n_clones = parameters["n_clones"]
n_lines = n_planets * n_clones


# In[3]:


# Code planets used by follow_swift program
planets = {"Mercury":-2, "Venus":-3, "Earth":-4, "Mars":-5,           "Jupiter":-6, "Saturn":-7, "Uranus":-8, "Neptune":-9}


# ## Extrating planets

# In[4]:


os.chdir(path_ss_data)
for clone in range(n_clones):
    os.chdir(prefix_simulation + '{}'.format(clone))
    shutil.copy(follow_path + "/follow_swift.x", ".")
    for planet in planets:
        with open("input_follow.txt", "w") as f:
            f.write(str(planets[planet]) + "\n1")
        subprocess.run("./follow_swift.x < input_follow.txt", shell = True)
        os.rename("follow.out", planet + ".txt")
        os.remove("input_follow.txt")
    os.remove("follow_swift.x")
    os.chdir("..")
os.chdir(path_proj)

