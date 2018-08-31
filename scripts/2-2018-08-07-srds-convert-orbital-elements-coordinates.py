# coding: utf-8

# Convert orbital elements in cartesian coordinates and velocities
# This notebook convert orbital elements in cartesian coordinates and
# velocities.
# 
# The input is a table with the orbital elements (../data/oe.csv)

# Import modules
import os
import sys
sys.path.insert(0, '../src/oe2xv/') # For orbel program
from orbel_mac import orbel_el2xv
#from orbel_linux import orbel_el2xv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import yaml

# Matplotlib config
plt.style.use('ggplot')
font = {'size'   :  16}
matplotlib.rc('font', **font)

with open('../parameters.yaml', "r") as f:
    parameters = yaml.load(f)
    
n_planets = parameters["n_planets"]
n_clones = parameters["n_clones"]
n_lines = n_planets * n_clones
gm = parameters["gm"]
ialpha = parameters["ialpha"]

# Read orbial elements. 
oe = pd.read_csv('../data/oe.csv')

# Applying orbel function and create dataframe xv with postions and velocities
# Note: no need loop
xv = {'v': oe.apply(lambda row: orbel_el2xv(gm, ialpha, row['a'], row['e'],\
                                            row['i'],row['capom'], row['omega'],\
                                            row['capm']), axis=1)}
# Transform Serie into dataframe
xv = pd.DataFrame(xv)

# Splits the tuples column and then removes it
xv = pd.DataFrame(xv['v'].values.tolist(), columns=['x', 'y', 'z', 'vx', 'vy', 'vz'])

# Save data
xv.to_csv('../data/xv.csv', index=False)

# Verifying planets' distribution
# Inners
plt.figure(figsize = (8,8))
plt.axis('equal')
plt.xlim(-1.62,1.62)
plt.ylim(-1.62,1.62)
plt.title("Inner Solar System: Distribution of clones")
plt.xlabel("x axis [au]")
plt.ylabel("y axis [au]")
plt.plot(xv['x'], xv['y'], '.')
plt.show()

# Giants
plt.figure(figsize = (8,8))
plt.axis('equal')
plt.xlim(-32.0,32.0)
plt.ylim(-32.0,32.0)
plt.title("Giants Solar System: Distribution of clones")
plt.xlabel("x axis [au]")
plt.ylabel("y axis [au]")
plt.plot(xv['x'], xv['y'], '.')
plt.show()
