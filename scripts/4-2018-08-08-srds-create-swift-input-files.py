# # Create Swift input files
# 
# This notebook create directory structure with Swift input files.

# Import modules
import os
import shutil
import numpy as np
import pandas as pd
import yaml
from glob import glob
import tarfile

# Define paths and parameters
path_ss_data = '../data/raw_data/ss_in/'

with open('../parameters.yaml', "r") as f:
    parameters = yaml.load(f)
    
n_planets = parameters["n_planets"]
n_clones = parameters["n_clones"]
n_lines = n_planets * n_clones
gm = parameters["gm"]
ialpha = parameters["ialpha"]
m = parameters["mass"]

# Read cartesian coordinates
coord = pd.read_csv('../data/xv_invar.csv', dtype=float, delimiter=',')

# Variables
x  = np.array(coord.x)
y  = np.array(coord.y)
z  = np.array(coord.z)
vx  = np.array(coord.vx)
vy  = np.array(coord.vy)
vz  = np.array(coord.vz)

# Configuring the Sun data.
# 
# - First line: 9 is the sum of the number of planets and the Sun (8 + 1).
# - Second line: 39.476926421373015 is the parameter gm, considering G = 1.
# - Third line: Position of the Sun in a heliocentric system.
# - Fourth line: Speed of the Sun in a heliocentric system.

sun_data = "9\n39.476926421373015\n0.0 0.0 0.0\n0.0 0.0 0.0\n"

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

print("Verifying directories")
print(os.listdir('../data/raw_data/ss_in'))

print("Verifying pl.in")
with open(path_ss_data + 'ss-0/pl.in') as f:
    for i in f.readlines():
        print(i)

