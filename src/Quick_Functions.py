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

# `Electricity-Data-Pipeline` Example 1

# Import the `Electricity-Data-Pipeline` modules
from src.helpers.BMRS_helpers import *
from src.helpers.range_import_helpers import *
import matplotlib.pyplot as plt

# Import raw data using quick BMRS helper function (See Table 1 in the README.md).
# Please note that these functions are subject to capping and time-out limits imposed by the data provider. 
# Please look at the range import functions to overcome this (See Table 2).
# Demand example with default dates
demand = demand()
print(demand.head())
# Plot demand example
plt.style.use('seaborn')
plt.plot(demand['fuelTypeGeneration'])

# Generation example with custom dates & save_to_csv option enabled
generation_default = generation() #default dates 
print(generation_default.head())
#function(start_date = '2020-03-28', end_date = '2020-03-31, save_to_csv = True)
generation_custom = generation(start_date = '2020-03-28', end_date = '2020-03-31', save_to_csv = True)
print(generation_custom)
# Here is the rest of the functions, for you to try out:
# 
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
# 
# Use case:
# To see how Electricity-Data-Pipeline was employed for assesing the impact of the March 2020 COVID-19 lockdown on the electricity system, please visit our publication below:
# > Kirli, Desen; Parzen, Maximilian; Kiprakis, Aristides. 2021. "Impact of the COVID-19 Lockdown on the Electricity System of Great Britain: A Study on Energy Demand, Generation, Pricing and Grid Stability" Energies 14, no. 3: 635.
# >(https://doi.org/10.3390/en14030635)
# 
# All data used in this paper lives here:
# > Kirli, Desen; Kiprakis, Aristides; Parzen, Max. (2021). Impact of the COVID-19 Lockdown on the Electricity System of Great Britain: A Study on Energy Demand, Generation, Pricing and Grid Stability, 2019-2020 [dataset]. University of Edinburgh. School of Engineering. Institute for Energy Systems.
# > (https://doi.org/10.7488/ds/2979).




