
# coding: utf-8

# # Extract data of the planets
# 
# The output of Swift program is a binary file. This Notebook extract the planets' data and convert it in a text file, separated each planet.

# ## Import modules, configuring variables and settings paths

# In[8]:


import os
import subprocess
import shutil
from glob import glob
import yaml
import platform


# In[21]:


# Definitons
if platform.system() == 'Darwin': 
    # Mac
    path_proj = '/Users/sandro/Documents/Projetos/MVS_SS_Circ_Invar4'
    follow_path = '/Users/sandro/Programas/swift/tools'
else:
    # Linux
    path_proj = '/home/sandro/Documentos/Projetos/MVS_SS_Circ_Invar4'
    follow_path = '/home/sandro/Programas/swift/tools'

os.chdir(path_proj)

path_ss_data = path_proj + '/data/ss'
prefix_simulation = 'ss-'
# Follow program path
 # Linux
 # Mac

with open(path_proj + '/src/parameters.yaml', "r") as f:
    parameters = yaml.load(f)
    
n_planets = parameters["n_planets"]
n_clones = parameters["n_clones"]
n_lines = n_planets * n_clones


# In[22]:


# Code planets used by follow_swift program
planets = {"Mercury":-2, "Venus":-3, "Earth":-4, "Mars":-5,           "Jupiter":-6, "Saturn":-7, "Uranus":-8, "Neptune":-9}


# ## Extrating planets

# In[23]:


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

