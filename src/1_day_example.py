# Demonstation of the BMRS helper functions used for short-term data import from BMRS.
# These functions are defined such that only start_date and end_date (format: 'YYYY-MM-DD').
#
# Below is a list of all the helper functions defined so far:
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
# Additionally, there is a function called extract_data() that deals directly with the BMRS data labels.
# (e.g. 'ROLSYSDEM' which is programmed into the demand() helper function in this project.)
# Please note that all of these functions are intended for short timeframes.
# Please see the other examples for use in longer timeframes.

from src.helpers.BMRS_helpers import *

demand()
# temperature()
