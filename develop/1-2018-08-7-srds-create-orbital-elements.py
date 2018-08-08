
# coding: utf-8

# # Orbital elements
# This notebook generates a table of orbital elements for simulation of the Solar System. The values will be chosen randomly within a range. The semi-major axis are the current values.
# 
# - semi_major_axis: The semi-major axis are the current values
# - eccentr = 0.0 - 0.001: Eccentricity
# - incl = 0.0 - 0.1: Inclination:
# - capom = 0.0 - 360.0 degrees: Longitude of ascending node 
# - omega = 0.0 - 360.0 degrees: Argument of the periastro.
# - capm = 0.0 - 360.0 degrees: Mean anomaly.

# ## Import modules

# In[1]:


# Import modules
import os
import numpy as np
import pandas as pd
import yaml


# ## Settings

# In[2]:


# Definitons
path_proj = os.getcwd()

# Read common parameters
with open('../src/parameters.yaml', "r") as f:
    parameters = yaml.load(f)
    
semi_major_axis = parameters["semi_major_axis"]
n_planets = parameters["n_planets"]
n_clones = parameters["n_clones"]
n_lines = n_planets * n_clones
seed = parameters["seed"] # 24515445, JD for 2000-01-01 00h00, ignoring decimal point.


# ## Generating random orbital elements
# 
# - Semi-major axis: Replicating the semi-major axis throughout the simulation clones, using np.tile method.
# - orbital elements: using $n = (b - a)\cdot \text{random + a}$, where range = [a,b)

# In[3]:


# Using seed
np.random.seed(seed)

# Create a dictionary of orbital elements
planets_dict = {'a'    : np.tile(semi_major_axis, n_clones),
                'e'    : 0.001 * np.random.random_sample(n_lines), 
                'i'    : 0.1   * np.random.random_sample(n_lines), 
                'capom': 361   * np.random.random_sample(n_lines), 
                'omega': 361   * np.random.random_sample(n_lines),  
                'capm' : 361   * np.random.random_sample(n_lines)}


# ## Create a dataframe

# In[4]:


# Create a dataframe of orbital elements.
orbital_elements_name = ['a', 'e', 'i', 'capom', 'omega', 'capm']
planets = pd.DataFrame(planets_dict, columns=orbital_elements_name)
planets[0:10]


# ## Save file

# In[5]:


planets.to_csv('../data/oe.csv', index=False)


# In[6]:


os.listdir('../data')

