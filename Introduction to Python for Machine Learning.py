#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


df = pd.read_csv('FoodBalanceSheets_E_Africa_NOFLAG.csv', encoding='latin-1')


# In[4]:


df.info()


# In[5]:


df.head()


# In[14]:


df_item = df.groupby('Item')


# In[16]:


df_item.sum()


# In[19]:


df.describe()


# In[21]:


percent_missing = df['Y2016'].isnull().sum() * 100 / len(df)


# In[22]:


percent_missing


# In[25]:


data_missing = df['Y2016'].isnull().sum()


# In[26]:


data_missing


# In[27]:


df.corr().abs()


# In[28]:


df.head()


# In[34]:


df_element = df.groupby('Element')


# In[35]:


df_element.sum()


# In[39]:


df['Area'].nunique()


# In[51]:


df[df['Area'] == 'Algeria']


# In[70]:


df_algeria = df.groupby(['Area', 'Element']).sum()


# In[73]:


df_algeria


# In[68]:


x = df_algeria.iloc(0)


# In[69]:


x


# In[ ]:
