
# coding: utf-8

# # Semi-major axis
# This notebook analise the time evolution of the semi-major axis for each planet. 

# In[1]:


#get_ipython().run_line_magic('matplotlib', 'inline')
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import platform


# In[2]:


#Matplotlib configure
plt.style.use('ggplot')
font = {'size'   :  16}
matplotlib.rc('font', **font)


# In[3]:


def create_columns(simulations):
    """Create a list of columns for dataframe"""
    return ['time'] + ['ss_{}'.format(simulation) for simulation in simulations]


def init_df(planet, simulations):
    """Initialize an empty dataframe"""
    columns = create_columns(simulations)
    df = pd.DataFrame(columns=columns)
    df['time']= np.genfromtxt('{}0/{}.txt'.format(prefix_simulation,planet))[:,0]
    return df


def read_orbital_element(planet, orbital_element, simulations):
    """Read the orbital elements for each planet for all simulations"""
    df = init_df(planet, simulations)
    for simulation in simulations:
        os.chdir('{}{}'.format(prefix_simulation, simulation))
        df['ss_{}'.format(simulation)] = np.genfromtxt('{}.txt'.format(planet))[:,orbital_element]
        os.chdir('..')
    return df


def create_data_planet(planet, orbital_element, simulations):
    """Create data frame for all planets together by each orbital element"""
    oe = {'time':0, 'a':1, 'e':2, 'inc':3, 'capom':4, 'omega':5, 'capm':6, 'peri':7, 'apo':8, 'obar':9}
    list_df_planets = [read_orbital_element(planet, oe[orbital_element], simulations) for planet in planets]
    data_planets = pd.concat(list_df_planets, keys=planets)
    return data_planets


# In[11]:


# Paths configuration
if platform.system() == 'Darwin': 
    # Mac
    path_proj = '/Users/sandro/Documents/Projetos/MVS_SS_Circ_Invar4'
    follow_path = '/Users/sandro/Programas/swift/tools'
else:
    # Linux
    path_proj = '/home/sandro/Documentos/Projetos/MVS_SS_Circ_Invar4'
    follow_path = '/home/sandro/Programas/swift/tools'


path_ss_data = 'data/ss'
prefix_simulation = 'ss-'
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


# In[13]:


os.chdir(path_proj)
os.chdir(path_ss_data)
planet = 'Mercury' # for time reference
orbital_element = 'a'
n_lines = 96
simulations = np.arange(n_lines)


# In[14]:


data_planet = create_data_planet('Mercury', 'a', simulations)


# In[15]:


data_planet


# In[17]:


mercury = data_planet.loc['Mercury']


# In[18]:


mercury


# ## Evolution of the Mercury's semi-major axis

# In[28]:


mercury.set_index('time').plot.line(legend=False, figsize=(14,10))


# In[33]:


time = data_planet.loc['Mercury']['time']
venus = data_planet.loc['Venus']
earth = data_planet.loc['Earth']
mars = data_planet.loc['Mars']


# In[44]:


ax = plt.gca()
inners = planets[0:4]
for planet in inners:
    data_planet.loc[planet].set_index('time').plot(ax = ax, legend=False, figsize=(14,10))


# In[47]:


ax = plt.gca()
giants = planets[4:8]
for planet in giants:
    data_planet.loc[planet].set_index('time').plot(ax = ax, legend=False, figsize=(14,10))

