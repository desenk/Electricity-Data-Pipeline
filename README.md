# Welcome to the Electricity-Data-Pipeline 👋
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


## Prerequisites

Before you begin, ensure you have met the following requirements:
<!--- These are just example requirements. Add, duplicate or remove as required --->
* You have installed `python` 3 and followed the instructions to download the required packages
* Your working directory is set to `your_machine\Electricity-Data-Pipeline`
* You obtained an API key and pasted it in `api_key.txt` (lives in `your_machine\Electricity-Data-Pipeline`)
* You have read the `examples`.

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
$ conda create --name <env> --file <this file>
```
or just using pip
```
$ pip install requirements.txt
```
## Using Electricity-Data-Pipeline

To use Electricity-Data-Pipeline, follow these steps:

(1) Please check the Prerequisites section above
(2) Obtain an API key from Elexon
(3) Save this API key in api_key.txt
(4) Follow the examples to access the Great Britain electricity system data


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
