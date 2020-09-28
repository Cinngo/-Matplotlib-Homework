#!/usr/bin/env python
# coding: utf-8

# In[100]:


import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as st
import numpy as np


# In[117]:


mouse_metadata_path = "Matplotlib/Mouse_metadata.csv.csv"
study_results_path = "Matplotlib/Study_results.csv.csv"

mouse_metadata = pd.read_csv(mouse_metadata_path)
study_results = pd.read_csv(study_results_path)


# In[118]:


single_dataset = pd.merge(mouse_metadata,study_results,how="left", on=["Mouse ID", "Mouse ID"])


# In[110]:


single_dataset.head()


# In[119]:


single_dataset['Mouse ID'].value_counts()


# In[112]:


single_dataset['Mouse ID'].value_counts().head()
 


# In[120]:


Numberofmice = single_dataset.set_index('Mouse ID')

Numberofmice


# In[126]:


Numberofmice.count()


# In[127]:


clean_Numberofmice = Numberofmice.drop(index = 'g989')

clean_Numberofmice
clean_Numberofmice.count()


# In[128]:


cleanindex_Numberofmice = clean_Numberofmice.reset_index()

cleanindex_Numberofmice
cleanindex_Numberofmice.head()


# In[129]:


capomulin2 = cleanindex_Numberofmice.loc[cleanindex_Numberofmice["Drug Regimen"] == "Capomulin"]
capomulin2 = capomulin2.reset_index()
singlecapomulin = capomulin2.loc[capomulin2["Mouse ID"] == "b128"]
singlecapomulin = singlecapomulin.loc[:, ["Timepoint", "Tumor Volume (mm3)"]]
singlecapomulin = singlecapomulin.reset_index(drop=True)
# Generate a line plot of time point versus tumor volume for a mouse treated with Capomulin
singlecapomulin.set_index('Timepoint').plot(figsize=(10, 8))


# In[131]:


redcapomulin = capomulin2.loc[:, ["Mouse ID", "Weight (g)", "Tumor Volume (mm3)"]]
avecap = pd.DataFrame(redcapomulin.groupby(["Mouse ID", "Weight (g)"])["Tumor Volume (mm3)"].mean()).reset_index()
avecap = avecap.rename(columns={"Tumor Volume (mm3)": "Average Volume"})
avecap = avecap.set_index('Mouse ID')
avecap.plot(kind="scatter", x="Weight (g)", y="Average Volume",
              title="Weight Vs. Average Tumor Volume")

