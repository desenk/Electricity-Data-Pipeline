#!/usr/bin/env python
# coding: utf-8
"""
...Before we start...
1. Check that you have the required packages
Please ensure you have `Python 3` and the listed items in the `requirements.txt` installed.
2. Get and check your API key
Please ensure that you have an API key from Elexon
1. Register at (https://www.elexonportal.co.uk/registration/newuser?cachebust=3apx5qnzf9) 
> Click on `sign-in`  ->  `register`
2. Follow the instructions at (https://www.elexon.co.uk/documents/training-guidance/bsc-guidance-notes/bmrs-api-and-data-push-user-guide-2/)
> Log-in -> Click on `my profile` -> Copy the `scripting key`
3. Paste the API Key in the `api_key.txt` file
4. Check that your API Key is saved correctly
"""

# `Electricity-Data-Pipeline` Example 2
# Import data for a week or more using Table 2 functions (See README.md).
from pipeline.BMRS_helpers import *
from pipeline.range_import_helpers import *
import matplotlib.pyplot as plt

# Default example using extract_data_weekly()
default_week1 = extract_data_weekly()  # default is demand data
print(default_week1.head())
# Plot example
plt.style.use("seaborn")
plt.plot(default_week1["fuelTypeGeneration"])
# Custom example using extract_data_weekly()
# extract_data_weekly(func_name = function , start_date = 'YYYY-MM-DD', save_to_csv = False)
custom_week1 = extract_data_weekly(demand, "2020-03-02", False)
print(custom_week1)
# plot both
plt.plot(default_week1["fuelTypeGeneration"])
plt.plot(custom_week1["fuelTypeGeneration"])
#
# Import for variable length of time
# Default example using extract_data_range()
# Temperature for a month
default_range = (
    extract_data_range()
)  # Default is temperature for a month starting 24th March 2020
print(default_range)
# Custom example using extract_data_range()
# loss_of_load for 2 months
# **Note:** the first input is the function name from Table 1 in the README.md
# (e.g. demand, generation, etc). It is *not* in quotes but the dates are in single quotes which is consistent in all functions.
# extract_data_range(func_name = function, start_date = '2020-03-28', end_date = '2020-03-31, save_to_csv = False)
custom_range = extract_data_range(
    func_name=loss_of_load,
    start_date="2020-03-28",
    end_date="2020-05-28",
    save_to_csv=True,
)
print(custom_range)

# Import for data that is not in Table 1, using BMRS labels
# using `extract_data_range_with_BMRS_label()
# extract_data_range_with_BMRS_label(report_name = 'report_name', start_date = 'YYYY-MM-DD', end_date = 'YYYY-MM-DD', save_to_csv = False)
extract_data_range_with_BMRS_label("TEMP", "2020-11-01", "2021-02-01")
#
#
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
#
# extract_data_weekly()
# extract_data_range()
# extract_data_range_with_BMRS_label()
#
# Use case:
# To see how Electricity-Data-Pipeline was employed for assesing the impact of the March 2020 COVID-19 lockdown on the electricity system, please visit our publication below:
# > Kirli, Desen; Parzen, Maximilian; Kiprakis, Aristides. 2021. "Impact of the COVID-19 Lockdown on the Electricity System of Great Britain: A Study on Energy Demand, Generation, Pricing and Grid Stability" Energies 14, no. 3: 635.
# >(https://doi.org/10.3390/en14030635)
#
# All data used in this paper lives here:
# > Kirli, Desen; Kiprakis, Aristides; Parzen, Max. (2021). Impact of the COVID-19 Lockdown on the Electricity System of Great Britain: A Study on Energy Demand, Generation, Pricing and Grid Stability, 2019-2020 [dataset]. University of Edinburgh. School of Engineering. Institute for Energy Systems.
# > (https://doi.org/10.7488/ds/2979).
