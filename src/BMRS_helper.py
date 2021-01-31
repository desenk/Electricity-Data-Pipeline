import urllib.request
import pandas as pd
import numpy as np
from lxml import objectify
import matplotlib.pyplot as plt
import datetime

def get_APIKey(filename='api_key.txt'):
    '''Reads the user API from the api_key.txt file'''
    try:
        with open(filename, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        print("<api_key.txt> file not found! Please create a txt file called <api_key.txt> and paste your API key in there.")

def import_data(**kwargs):
    '''Imports data from the BMRS API. Report name and API Key are essential, all other keywords (mentioned in the BMRS API Guide) are optional'''
    API_key = get_APIKey()
    url = 'https://api.bmreports.com/BMRS/{report}/v1?APIKey={APIkey}&ServiceType=xml'.format(APIkey = API_key, **kwargs)

    for key, value in kwargs.items():
        if key not in ['report']:
            additional = "&%s=%s" % (key, value)
            url = url + additional
    xml = objectify.parse(urllib.request.urlopen(url))
    return xml

def make_dataframe(**kwargs):
    '''Returns a pandas dataframe using the BMRS XML output'''
    headers = []
    for entry in import_data(**kwargs).findall("./responseBody/responseList/item/"):
        headers.append(entry.tag)
    header_dict = dict.fromkeys(headers)
    body = []
    for entry in import_data(**kwargs).findall("./responseBody/responseList/item"):
        data = entry.getchildren()
        body.append(data)
    try:
        df = pd.DataFrame(body, columns=header_dict)
    except:
        df = pd.DataFrame(body, columns=list(header_dict)[:len(body[0])])
    return df 

def extract_data1(report_name, start_date, end_date):
    '''v1:extracts data from BMRS using report_name, start_date and end_Date'''
    df = make_dataframe(report=report_name, FromDate=start_date, ToDate=end_date)
    return df

def extract_data2(report_name, start_date, end_date):
    '''v2:extracts data from BMRS using report_name, start_date and end_Date'''
    df = make_dataframe(report=report_name, FromSettlementDate=start_date, ToSettlementDate=end_date)
    return df

def extract_data3(report_name, start_date, end_date):
    '''v3:extracts data from BMRS using report_name, start_date and end_Date'''
    df = make_dataframe(report=report_name, FromDatetime=start_date+'%2000:00:00', ToDatetime=end_date+'%2000:00:00')
    return df

def extract_data4(report_name, start_date, end_date):
    '''v3:extracts data from BMRS using report_name, start_date and end_Date'''
    df = make_dataframe(report=report_name, SettlementDate=start_date, Period='1')
    return df

def extract_data(report_name, start_date, end_date):
    '''Extracts BMRS data regardless of the date formats. report_name follows the BMRS API guide.'''
    for func in [extract_data3, extract_data2, extract_data1, extract_data4]:
        try:   
            df = func(report_name, start_date, end_date)
            break
        except Exception as err:
            print (err)
        continue
    return df

def demand(start_date='2020-03-24', end_date='2020-03-25', save_to_csv=False):
    '''System demand data, inputs are start_date and end_date. Option to save as CSV'''
    report_name = 'ROLSYSDEM'
    df = make_dataframe(report=report_name, FromDateTime=(start_date+'%2000:00:00'), ToDateTime=(end_date+'%2000:00:00'))
    if save_to_csv == True:
        df.to_csv(report_name+'_'+start_date+'_'+end_date+'.csv')
    return df

def temperature(start_date='2020-03-24', end_date='2020-03-25', save_to_csv=False):
    '''Daily average tempature in Britain, inputs are start_date and end_date. Option to save as CSV'''
    report_name = 'TEMP'
    df = make_dataframe(report=report_name, FromDate=start_date, ToDate=end_date)
    if save_to_csv == True:
        df.to_csv(report_name+'_'+start_date+'_'+end_date+'.csv')
    return df

def generation(start_date='2020-03-24', end_date='2020-03-25', save_to_csv=False):
    '''Generation data by fuel type, inputs are start_date and end_date. Option to save as CSV'''
    report_name = 'FUELHH'
    df = make_dataframe(report=report_name, FromDate=start_date, ToDate=end_date)
    if save_to_csv == True:
        df.to_csv(report_name+'_'+start_date+'_'+end_date+'.csv')
    return df

def loss_of_load(start_date='2020-03-24', end_date='2020-03-25', save_to_csv=False):
    '''Loss of Load data, inputs are start_date and end_date. Option to save as CSV'''
    report_name = 'LOLPDRM'
    df = make_dataframe(report=report_name, FromSettlementDate=start_date, ToSettlementDate=end_date, recordType='LOLP')
    df = df[df['recordType'] =='LOLP']
    if save_to_csv == True:
        df.to_csv(report_name+'_'+start_date+'_'+end_date+'.csv')
    return df


def initial_demand_national(start_date='2020-03-24', end_date='2020-03-25', save_to_csv=False):
    '''Initial demand data on transmission and national level, inputs are start_date and end_date. Option to save as CSV'''
    report_name = 'INDOITSDO'
    df = make_dataframe(report=report_name, FromSettlementDate=start_date, ToSettlementDate=end_date)
    df = df[df['recordType'] =='INDO']
    if save_to_csv == True:
        
            df.to_csv(report_name+'_'+start_date+'_'+end_date+'.csv')
    return df

def initial_demand_transmission(start_date='2020-03-24', end_date='2020-03-25', save_to_csv=False):
    '''Initial demand data on transmission and national level, inputs are start_date and end_date. Option to save as CSV'''
    report_name = 'INDOITSDO'
    df = make_dataframe(report=report_name, FromSettlementDate=start_date, ToSettlementDate=end_date)
    df = df[df['recordType'] =='ITSDO']
    if save_to_csv == True:
        df.to_csv(report_name+'_'+start_date+'_'+end_date+'.csv')
    return df

def frequency(start_date='2020-03-24', end_date='2020-03-24', save_to_csv=False):
    '''System frequency data, inputs are start_date and end_date. Option to save as CSV'''
    report_name = 'FREQ'
    df = make_dataframe(report=report_name, FromDateTime=(start_date+'%2000:00:00'), ToDateTime=(end_date+'%2000:00:00'))
    if save_to_csv == True:
        df.to_csv(report_name+'_'+start_date+'_'+end_date+'.csv')
    return df

def demand_forecast_national(start_date='2020-03-24', end_date='2020-03-25', save_to_csv=False):
    '''National day-ahead demand forecast data, inputs are start_date and end_date. Option to save as CSV'''
    report_name = 'FORDAYDEM'
    df = make_dataframe(report=report_name, FromDate=(start_date), ToDate=(end_date))
    df = df[df['recordType'] == 'DANF']
    if save_to_csv == True:
        df.to_csv(report_name+'_'+start_date+'_'+end_date+'.csv')
    return df

def demand_forecast_transmission(start_date='2020-03-24', end_date='2020-03-25', save_to_csv=False):
    '''National day-ahead demand forecast data, inputs are start_date and end_date. Option to save as CSV'''
    report_name = 'FORDAYDEM'
    df = make_dataframe(report=report_name, FromDate=(start_date), ToDate=(end_date))
    df = df[df['recordType'] == 'DATF']
    if save_to_csv == True:
        df.to_csv(report_name+'_'+start_date+'_'+end_date+'.csv')
    return df


def imbalance_volume(start_date='2020-03-24', period='1', save_to_csv=False):
    '''Imbalance volume data from BMRS using report_name, start_date and period'''
    report_name = 'B1780'
    df = make_dataframe(report=report_name, SettlementDate=start_date, Period=period)
    if save_to_csv == True:
        df.to_csv(report_name+'_'+start_date+'.csv')
    return df

def imbalance_price(start_date='2020-03-24', period='1', save_to_csv=False):
    '''Imbalance volume data from BMRS using report_name, start_date and period'''
    report_name = 'B1770'
    df = make_dataframe(report=report_name, SettlementDate=start_date, Period=period)
    if save_to_csv == True:
        df.to_csv(report_name+'_'+start_date+'.csv')
    return df
