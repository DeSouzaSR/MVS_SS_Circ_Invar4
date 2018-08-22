
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


# In[39]:


def init_df(planet, simulations):
    columns = ['time'] + ['ss_{}'.format(simulation) for simulation in simulations]
    df = pd.DataFrame(columns=columns)
    df['time']= np.genfromtxt('{}0/{}.txt'.format(prefix_simulation,planet))[:,0]
    return df

def read_semi_major_axis(planet, orbital_element, simulations):
    df = init_df(planet, simulations)
    for simulation in simulations:
        os.chdir('{}{}'.format(prefix_simulation, simulation))
        df['ss_{}'.format(simulation)] = np.genfromtxt('{}.txt'.format(planet))[:,orbital_element]
        os.chdir('..')
    return df


# In[40]:


# Paths configuration
path_proj = '/home/sandro/Documentos/Projetos/MVS_SS_Circ_Invar4'
path_ss_data = '../data/ss'
prefix_simulation = 'ss-'
orbital_elements = ['time', 'a', 'e', 'inc', 'capom', 'omega', 'capm', 'peri', 'apo', 'obar']
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


# In[32]:


a = np.genfromtxt('{}.txt'.format('Mercury'))


# In[36]:


b = np.genfromtxt('Mercury.txt')


# In[38]:


get_ipython().system('pwd')


# In[41]:


os.chdir(path_proj)
os.chdir('data/ss')

planet = 'Mercury'
orbital_element = 1
n_lines = 95
simulations = np.arange(n_lines)

df = read_semi_major_axis(planet, orbital_element, simulations)


# In[42]:


df


# In[25]:


df.head()


# In[17]:


#os.chdir('ss-0')
a = np.genfromtxt('{}.txt'.format('Mercury'))[:,1]
df['ss_0'] = a


# In[19]:


print('ss_{}'.format('1'))


# In[7]:


for simulation in simulations:
    os.chdir('{}{}'.format(prefix_simulation, simulation))
    dataframe['ss_{}'.format(simulation)] = np.genfromtxt('{}.txt'.format(planet))[:,orbital_element]
    os.chdir('..')
    
dataframe.head()


# In[20]:


simulations


# In[ ]:


os.chdir('ss-0')
a = np.genfromtxt('{}.txt'.format('Mercury'))[:,1]
len(a)


# In[ ]:


a[:,1]


# In[ ]:


# Paths configuration
path_proj = '/home/sandro/Documentos/Projetos/MVS_SS_Circ_Invar4'
path_ss_data = '../data/ss'
prefix_simulation = 'ss-'
orbital_elements = ['time', 'a', 'e', 'inc', 'capom', 'omega', 'capm', 'peri', 'apo', 'obar']
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']


# In[ ]:


os.chdir(path_proj)
os.chdir('data/ss')

mercury = read_semi_major_axis(planet = 'Mercury', orbital_element = 1, n_lines = 96)
mercury.head()

# df = [read_semi_major_axis(planet = planet, orbital_element = 1, n_lines = 96) for planet in planets]
# data = pd.concat(df, keys=planets)


# In[ ]:


time = result.loc['Mercury']['time']


# In[ ]:


data.loc['Saturn'].plot(x = 'time', style='-', legend=False, figsize=(16,8), ylim=(9.25, 10.0))


# In[ ]:


os.chdir(prefix_simulation + str(1))
df = []
for planet in planets:
    df.append(read_data_planets(planet))
os.chdir('..')


# In[ ]:


result = pd.concat(df, keys=planets)


# In[ ]:


x = result.loc['Mercury']['time']
y1 = result.loc['Mercury']['a']
y2 = result.loc['Venus']['a']
plt.ylim(0.38, 0.74)
plt.plot(x, y1, x ,y2)


# In[ ]:


raw_data.head()


# In[ ]:


os.chdir(path_proj)
os.chdir('data/MVS_SS_Circ_Invar')


# In[ ]:


mercury = read_semi_major_axis('Mercury', 1, n_lines=96)
mercury.head()


# In[ ]:


plt.figure(figsize=(14,8))
plt.plot(mercury['time'], mercury['s-1'])


# In[ ]:


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

