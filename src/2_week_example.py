# Demonstation of the BMRS helper functions used for long-term data import from BMRS.
# These functions are defined such that they are able to import data without getting caught in time-out and capping (e.g. 4000 rows max) limitations.
# There is (1) WEEKLY extractor and (2) an OPEN RANGE extractor
# (1) data_extract_weekly() requires only the function name (see the list below) and a start_date (format: 'YYYY-MM-DD').
# (2) data_extract_range() requires the same plus an end_date.
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
# Additionally, there is a function called (3) extract_data_with_BMRS_label() that deals directly with the BMRS data labels.
# (e.g. report_name = 'ROLSYSDEM' which is coded as demand using a helper function in this project.)
from src.helpers.range_import_helpers import *


extract_data_weekly()
extract_data_weekly(generation)
extract_data_weekly(temperature)

extract_data_range()
data_extract_range_with_BMRS_label()
data_extract_range_with_BMRS_label('TEMP', '2020-03-24', '2020-04-24')
