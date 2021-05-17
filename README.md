# Welcome to the Electricity-Data-Pipeline 👋                        
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/desenk/Electricity-Data-Pipeline/blob/master)

Electricity-Data-Pipeline is a tool that allows people in the field of energy systems to extract the Great Britain electricity market (a.k.a. balancing mechanism) data. The origin of the data is Balancing Mechanism Reporting Service [BMRS](https://www.bmreports.com/).

This tool was developed as a means of easier data extraction for our paper on the impact of the first COVID-19 lockdown on the electricity system [here](https://doi.org/10.3390/en14030635).

The dataset used in this publication is also made available on DataShare. Hence, if you are interested in the same datasets, please click [here](https://doi.org/10.7488/ds/2979
).

## Publications
### Paper
[link to paper](https://doi.org/10.3390/en14030635)
```
Kirli, Desen; Parzen, Maximilian; Kiprakis, Aristides. 2021. "Impact of the COVID-19 Lockdown on the Electricity System of Great Britain: A Study on Energy Demand, Generation, Pricing and Grid Stability" Energies 14, no. 3: 635. https://doi.org/10.3390/en14030635
```
### Dataset
[link to dataset](https://doi.org/10.7488/ds/2979)
```
Kirli, Desen; Kiprakis, Aristides; Parzen, Max. (2021). Impact of the COVID-19 Lockdown on the Electricity System of Great Britain: A Study on Energy Demand, Generation, Pricing and Grid Stability, 2019-2020 [dataset]. University of Edinburgh. School of Engineering. Institute for Energy Systems. https://doi.org/10.7488/ds/2979.
```

## Using Electricity-Data-Pipeline

There are multiple ways to use the Electricity-Data-Pipeline:
1. Google Colab: Click [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/desenk/Electricity-Data-Pipeline/blob/master) to open our example notebooks.

2. Please check the Prerequisites section below and proceed with your chosen interpreter.


## Highlights
The `<Electricity-Data-Pipeline>` offers ready-to-use functions to import different sets of electricity data.
Below is a list of all functions defined so far:

_**Table 1:** List of the quick BMRS helper functions_

`Electricity-Data-Pipeline` Quick Functions | Description | Resolution | Inputs 
------------ | ------------- | ------------ | ------------
**`demand()`** | Rolling System Demand | 5 min | demand(start_date = 'YYYY-MM-DD', end_date = 'YYYY-MM-DD', save_to_csv = False)
**`temperature()`** | Average Daily Temperature in Britain | Daily  | "
**`generation()`** | Half-hourly Generation by Fuel Type | Halfhourly (30 min) | "
**`frequency()`** | System Frequency | 15 sec | "
**`initial_demand_national()`** | Initial National Demand Out-turn | Halfhourly (30 min) | "
**`initial_demand_transmission()`** | Initial Transmission System Demand Out-turn | Halfhourly (30 min) | "
**`demand_forecast_national()`** | National Demand Forecast | Halfhourly (30 min) | "
**`demand_forecast_transmission()`** | Transmission System Demand Forecast | Halfhourly (30 min) | "
**`imbalance_volume()`** | Imbalance Volume | Halfhourly (30 min) | "
**`loss_of_load()`** | Loss of Load and De-rated Margin | Halfhourly (30 min) | "
**`imbalance_price()`** | Imbalance Price | Halfhourly (30 min) | "
**`derived_system_data()`** | Derived System Data | Halfhourly (30 min) | "
**`extract_data()`** | Uses BMRS data label and tries different methods | depends on dataset of choice | extract_data(report_name = 'TEMP', start_date = 'YYYY-MM-DD', end_date = 'YYYY-MM-DD', save_to_csv = True)

_______________________________________________


_**Table 2:** List of the data extractions functions for a week or longer periods._

`Electricity-Data-Pipeline` Function for Weekly/Long-term Imports | Description | Range | Inputs 
------------ | ------------- | ------------ | ------------
**`extract_data_weekly()`** | Extracts data for a week from the start_date using the function names from the table above| Fixed - Weekly | extract_data_weekly(func_name = demand , start_date = 'YYYY-MM-DD', save_to_csv = True)
**`extract_data_range()`** | Extracts data for long timeframes | Variable  | extract_data_range(func_name = temperature, start_date = 'YYYY-MM-DD', end_date =  'YYYY-MM-DD', save_to_csv = False)
**`extract_data_range_with_BMRS_label()`** | Same as above but using BMRS report names rather than the function names from the table above | Variable | data_extract_range_with_BMRS_label(report_name = 'TEMP', start_date = 'YYYY-MM-DD', end_date =  'YYYY-MM-DD', save_to_csv = False)

## Prerequisites

Before you begin, ensure you have met the following requirements:
<!--- These are just example requirements. Add, duplicate or remove as required --->
* You have installed `python 3` and followed the instructions to download the required packages
* Your working directory is set to `your_machine\Electricity-Data-Pipeline`
* You obtained an API key and pasted it in `api_key.txt` (lives in `your_machine\Electricity-Data-Pipeline`)
1. Register on Elexon's website a new user - [here](https://www.elexonportal.co.uk/registration/newuser?cachebust=3apx5qnzf9) 
> Click on `sign-in`  ->  `register`
2. Follow the instructions [here](https://www.elexon.co.uk/documents/training-guidance/bsc-guidance-notes/bmrs-api-and-data-push-user-guide-2/)
> Log-in -> Click on `my profile` -> Copy the `scripting key`
3. Paste the API Key in the `api_key.txt` file
4. Check that your API Key is saved correctly

* Please check the example notebooks for more detailed information.


## Installing <Electricity-Data-Pipeline>

To install <Electricity-Data-Pipeline>, follow these steps:

```
Download as zipped folder from top RHS
```
or
```
git clone https://github.com/desenk/Electricity-Data-Pipeline.git
```

then if using Anaconda

```
$ conda create --name <env name> --file requirements.txt
```
or just using pip
```
$ pip install -r requirements.txt
```
## More info about datasets and BMRS
For more info about the BMRS and its user guide - [here](https://www.elexon.co.uk/documents/training-guidance/bsc-guidance-notes/bmrs-api-and-data-push-user-guide-2/)

## Contact

If you want to contact me you can reach me at <desen.kirli@ed.ac.uk>.

## License
Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg

## Acknowledgement
Contains BMRS data © Elexon Limited copyright and database right [2021] [license link] (https://www.elexon.co.uk/operations-settlement/bsc-central-services/balancing-mechanism-reporting-agent/copyright-licence-bmrs-data/)
