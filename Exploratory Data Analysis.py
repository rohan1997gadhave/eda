#!/usr/bin/env python
# coding: utf-8

# In[26]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)
get_ipython().run_line_magic('matplotlib', 'inline')


# In[32]:


auto = pd.read_csv('automobail.csv')


# In[33]:


auto


# In[34]:


sns.distplot(auto['normalized_losses'])
plt.show()


# In[35]:


sns.distplot(auto['normalized_losses'], kde=False, rug=True)
plt.show()


# In[36]:


sns.jointplot(auto['engine_size'], auto['horsepower'])
plt.show()


# In[37]:


#kind : { "scatter" | "reg" | "resid" | "kde" | "hex" }
sns.jointplot(auto['engine_size'], auto['horsepower'], kind = 'hex')
plt.show()


# In[38]:


sns.pairplot(auto[['normalized_losses', 'engine_size', 'horsepower']])


# In[39]:



sns.stripplot(auto['fuel_type'], auto['horsepower'], jitter = True)


# In[40]:


sns.swarmplot(auto['fuel_type'], auto['horsepower'])


# In[41]:


sns.boxplot(auto['number_of_doors'], auto['horsepower'], hue=auto['fuel_type'])


# In[42]:


sns.barplot(auto['body_style'], auto['horsepower'], hue= auto['engine_location'])


# In[43]:


sns.pointplot(auto['fuel_system'], auto['horsepower'], hue=auto['number_of_doors'])


# In[44]:


sns.lmplot(x='horsepower', y ='peak_rpm', data= auto, hue='fuel_type')


# In[ ]:




