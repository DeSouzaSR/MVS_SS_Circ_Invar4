
# coding: utf-8

# # Semi-major axis
# This notebook analise the time evolution of the semi-major axis for each planet. 

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd


# In[2]:


#Matplotlib configure
plt.style.use('ggplot')
font = {'size'   :  16}
matplotlib.rc('font', **font)


# In[20]:


def read_semi_major_axis(planet, orbital_element, n_lines):
    """planet: string
       orbital_element: integer  
    """
    columns = ['time'] + ['s_' + str(i) for i in np.arange(1, n_lines + 1)]
    dataframe = pd.DataFrame(columns=columns)
    dataframe['time']= np.genfromtxt(prefix_simulation + '1' + '/' + planet + '.txt')[:,0]
    for simulation in np.arange(1, n_lines + 1):
        os.chdir(prefix_simulation + str(simulation))
        dataframe['s_' + str(simulation)]= np.genfromtxt(planet + '.txt')[:,orbital_element]
        os.chdir('..')
    return dataframe


# In[21]:


# Paths configuration
path_proj = '/Users/sandro/Documents/Projetos/MVS_SS_Circ_Invar4'
path_ss_data = '../data/MVS_SS_Circ_Invar'
prefix_simulation = 'MVS_SS_Circ_Invar-'


# In[22]:


os.chdir(path_proj)
os.chdir('data/MVS_SS_Circ_Invar')


# In[23]:


mercury = read_semi_major_axis('Mercury', 1, n_lines=96)
mercury.head()


# In[ ]:


plt.figure(figsize=(14,8))
plt.plot(mercury['time'], mercury['s-1'])


# In[25]:


venus = read_semi_major_axis('Venus', 1, n_lines=96)
venus.head()


# In[ ]:


plt.figure()
mercury.plot(x = 'time', kind='line', legend=False, figsize=(14,8), ylim=(0.3,0.5))
venus.plot(x = 'time', kind='line', legend=False, figsize=(14,8), ylim=(0.6,0.8))


# In[ ]:


def plot(planet):
    plt.plot(planet.time, planet.s-1)

plt.figure(figsize=(14,8))
plt.ylim(0.3, 0.75)
planets = ['mercury', 'venus']
for planet in planets:
    plot(planet)


# In[ ]:


pd.

