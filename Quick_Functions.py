#!/usr/bin/env python
# coding: utf-8

# __________________________
# #### _...Before we start..._
# ##### _1. Check that you have the required packages_
# Please ensure you have `Python 3` and the listed items in the `requirements.txt` installed.
# ##### _2. Get and check your API key_
# Please ensure that you have an API key from Elexon
# 1. Register [here](https://www.elexonportal.co.uk/registration/newuser?cachebust=3apx5qnzf9) 
# > Click on `sign-in`  ->  `register`
# 2. Follow the instructions [here](https://www.elexon.co.uk/documents/training-guidance/bsc-guidance-notes/bmrs-api-and-data-push-user-guide-2/)
# > Log-in -> Click on `my profile` -> Copy the `scripting key`
# 3. Paste the API Key in the `api_key.txt` file
# 4. Check that your API Key is saved correctly
# __________________________

# # `Electricity-Data-Pipeline` Examples

# ## 1. Import the `Electricity-Data-Pipeline` functions

# In[1]:


from src.helpers.BMRS_helpers import *
from src.helpers.range_import_helpers import *
import matplotlib.pyplot as plt


# Below is a list of all the `<Electricity-Data-Pipeline>` functions defined so far:
# 
# _**Table 1:** List of the quick BMRS helper functions_
# 
# `Electricity-Data-Pipeline` Quick Functions | Description | Resolution | Inputs 
# ------------ | ------------- | ------------ | ------------
# **`demand()`** | Rolling System Demand | 5 min | demand(start_date = 'YYYY-MM-DD', end_date = 'YYYY-MM-DD', save_to_csv = False)
# **`temperature()`** | Average Daily Temperature in Britain | Daily  | "
# **`generation()`** | Half-hourly Generation by Fuel Type | Halfhourly (30 min) | "
# **`frequency()`** | System Frequency | 15 sec | "
# **`initial_demand_national()`** | Initial National Demand Out-turn | Halfhourly (30 min) | "
# **`initial_demand_transmission()`** | Initial Transmission System Demand Out-turn | Halfhourly (30 min) | "
# **`demand_forecast_national()`** | National Demand Forecast | Halfhourly (30 min) | "
# **`demand_forecast_transmission()`** | Transmission System Demand Forecast | Halfhourly (30 min) | "
# **`imbalance_volume()`** | Imbalance Volume | Halfhourly (30 min) | "
# **`loss_of_load()`** | Loss of Load and De-rated Margin | Halfhourly (30 min) | "
# **`imbalance_price()`** | Imbalance Price | Halfhourly (30 min) | "
# **`extract_data()`** | Uses BMRS data label and tries different methods | depends on dataset of choice | extract_data(report_name = 'TEMP', start_date = 'YYYY-MM-DD', end_date = 'YYYY-MM-DD', save_to_csv = True)
# 
# _______________________________________________
# 
# 
# _**Table 2:** List of the data extractions functions for a week or longer periods._
# 
# `Electricity-Data-Pipeline` Function for Weekly/Long-term Imports | Description | Range | Inputs 
# ------------ | ------------- | ------------ | ------------
# **`extract_data_weekly()`** | Extracts data for a week from the start_date using the function names from the table above| Fixed - Weekly | extract_data_weekly(func_name = demand , start_date = 'YYYY-MM-DD', save_to_csv = True)
# **`extract_data_range()`** | Extracts data for long timeframes | Variable  | extract_data_range(func_name = temperature, start_date = 'YYYY-MM-DD', end_date =  'YYYY-MM-DD', save_to_csv = False)
# **`data_extract_range_with_BMRS_label()`** | Same as above but using BMRS report names rather than the function names from the table above | Variable | data_extract_range_with_BMRS_label(report_name = 'TEMP', start_date = 'YYYY-MM-DD', end_date =  'YYYY-MM-DD', save_to_csv = False)

# ## 2. Import raw data using quick BMRS helper function

# Here, we demonstrate the quick functions used for short-term data import (See Table 1).
# Please note that these functions are subject to capping and time-out limits imposed by the data provider. Please look at the range import functions to overcome this (See Table 2).

# ### Demand example with default dates

# In[2]:


demand = demand()
demand


# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('seaborn')
plt.plot(demand['fuelTypeGeneration'])


# ### Generation example with custom dates & save_to_csv option enabled

# In[4]:


generation_default = generation() #default dates 
generation_default.head()


# In[5]:


#function(start_date = '2020-03-28', end_date = '2020-03-31, save_to_csv = True)
generation_custom = generation(start_date = '2020-03-28', end_date = '2020-03-31', save_to_csv = True)
generation_custom


# ### Here is the rest of the functions, for you to try out:
# 
# ```
# demand()
# temperature()
# generation()
# frequency()
# loss_of_load()
# initial_demand_national()
# initial_demand_transmission()
# demand_forecast_national()
# demand_forecast_transmission()
# imbalance_volume()
# imbalance_price()
# ```

# ### Use case:
# To see how ```Electricity-Data-Pipeline``` was employed for assesing the impact of the March 2020 COVID-19 lockdown on the electricity system, please visit our publication below:
# > Kirli, Desen; Parzen, Maximilian; Kiprakis, Aristides. 2021. "Impact of the COVID-19 Lockdown on the Electricity System of Great Britain: A Study on Energy Demand, Generation, Pricing and Grid Stability" Energies 14, no. 3: 635. [https://doi.org/10.3390/en14030635](https://doi.org/10.3390/en14030635)
# 
# All data used in this paper lives here:
# > Kirli, Desen; Kiprakis, Aristides; Parzen, Max. (2021). Impact of the COVID-19 Lockdown on the Electricity System of Great Britain: A Study on Energy Demand, Generation, Pricing and Grid Stability, 2019-2020 [dataset]. University of Edinburgh. School of Engineering. Institute for Energy Systems. [https://doi.org/10.7488/ds/2979](https://doi.org/10.7488/ds/2979).

# In[ ]:




