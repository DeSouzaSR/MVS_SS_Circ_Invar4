#' # Convert orbital elements in cartesian coordinates and velocities
#' This notebook transforms cartesian positions and velocities to the \
#' invariable plane. 
#' 
#' The input is a table with the [positions and velocities](../data/xv.csv)

#' Import modules
import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import yaml

#' Setting Matplotlib
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
m = parameters["mass"]

#' Read cartesian coordinates
coord = pd.read_csv('../data/xv.csv', dtype=float, delimiter=',')

#' Variables
x  = np.array(coord.x)
y  = np.array(coord.y)
z  = np.array(coord.z)
vx  = np.array(coord.vx)
vy  = np.array(coord.vy)
vz  = np.array(coord.vz)

#'Computes angular momentum of the system
amx = 0.0
amy = 0.0
amz = 0.0

for i in range(n_planets):
    amx = amx + m[i]*y[i]*vz[i] - m[i]*z[i]*vy[i]
    amy = amy + m[i]*z[i]*vx[i] - m[i]*x[i]*vz[i]
    amz = amz + m[i]*x[i]*vy[i] - m[i]*y[i]*vx[i]
    
#' Angular momentum module
am = np.sqrt(amx*amx + amy*amy + amz*amz)

#' Amgular momentum inclination
aminc = np.arccos(amz/am)

#' Angular momentum long. node
amcapom = np.arctan2(amx,-amy)

#' Rotation to the invariable plane
for i in range(5):
    xp  =  x[i]*np.cos(amcapom)+y[i]*np.sin(amcapom)
    yp  = -x[i]*np.sin(amcapom)+y[i]*np.cos(amcapom)
    vxp =  vx[i]*np.cos(amcapom)+vy[i]*np.sin(amcapom)
    vyp = -vx[i]*np.sin(amcapom)+vy[i]*np.cos(amcapom)
    x[i] = xp
    y[i] = yp
    vx[i] = vxp
    vy[i] = vyp
    yp  =  y[i]*np.cos(aminc)+z[i]*np.sin(aminc)
    zp  = -y[i]*np.sin(aminc)+z[i]*np.cos(aminc)
    vyp =  vy[i]*np.cos(aminc)+vz[i]*np.sin(aminc)
    vzp = -vy[i]*np.sin(aminc)+vz[i]*np.cos(aminc)
    y[i] = yp
    z[i] = zp
    vy[i] = vyp
    vz[i] = vzp

#' Crate data frame
{'x':x, 'y':y, 'z':z, 'vx':vx, 'vy':vy, 'vz':vz}
coord = pd.DataFrame({'x':x, 'y':y, 'z':z, 'vx':vx, 'vy':vy, 'vz':vz},\
                    columns=['x', 'y', 'z', 'vx', 'vy', 'vz'])

#' Save data
# coord.to_csv("../data/xv_invar.csv", index=False)

#' Verifying distribution of positions and velocities
plt.figure(figsize = (8,8))
plt.axis('equal')
plt.xlim(-1.62,1.62)
plt.ylim(-1.62,1.62)
plt.title("Inner Solar System: Distribution of clones")
plt.xlabel("x axis [au]")
plt.ylabel("y axis [au]")
plt.plot(coord['x'], coord['y'], '.')
plt.show()

plt.figure(figsize = (8,8))
plt.axis('equal')
plt.xlim(-32.0,32.0)
plt.ylim(-32.0,32.0)
plt.title("Giants Solar System: Distribution of clones")
plt.xlabel("x axis [au]")
plt.ylabel("y axis [au]")
plt.plot(coord['x'], coord['y'], '.')
plt.show()
