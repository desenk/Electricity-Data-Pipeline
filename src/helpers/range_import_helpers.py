import datetime as dt
from src.helpers.BMRS_helpers import *
import pandas as pd

def iter_data_extract(func_name = temperature, start_date = '2020-03-24', end_date =  '2020-03-25', weekly = False):
    '''Iterates through the given range of dates, day by day, to avoid time out and max import problems'''
    format_str = '%Y-%m-%d'
    delta = dt.timedelta(days=1)
    start_date_dt = dt.datetime.strptime(start_date, format_str)
    rel_start_date = start_date_dt
    df = pd.DataFrame()
    if weekly == False:
        end_date_dt = dt.datetime.strptime(end_date, format_str)
    else:
        end_date_dt = start_date_dt+(6*delta)
    while rel_start_date <= end_date_dt:
        rel_end_date = rel_start_date + delta
        for x in [func_name]: 
            df1 = x(rel_start_date.strftime(format_str), rel_end_date.strftime(format_str))
        df = pd.concat([df, df1], ignore_index=True)
        rel_start_date = rel_start_date+delta
    return df
 
def extract_data_range(func_name = temperature, start_date = '2020-03-24', end_date =  '2020-04-24', save_to_csv = False):
    '''Extracts data for long timeframes.Inputs: function name, start_date, end_date, save_to_csv. Without the timeout and max row limitations'''
    df = iter_data_extract(func_name, start_date, end_date)
    df = df.drop_duplicates().reset_index(drop=True)
    if save_to_csv == True:
        df.to_csv(func_name.__name__+'_'+start_date+'_'+end_date+'.csv')
    return df

def extract_data_weekly(func_name = demand, start_date = '2020-03-24', save_to_csv = False):
    '''Extracts data for a week from the start_date. Inputs: function name, start_date, save_to_csv. Note: NO end_date '''
    df = iter_data_extract(func_name, start_date, weekly=True)
    df = df.drop_duplicates().reset_index(drop=True)
    if save_to_csv == True:
        df.to_csv(func_name.__name__+'_week_starting_'+start_date+'.csv')
    return df

def iter_data_extract_without_helper(report_name = 'TEMP', start_date = '2020-03-24', end_date =  '2020-03-25', weekly = False):
    '''Iterates through the given range of dates, day by day, for BMRS reports without a helper'''
    format_str = '%Y-%m-%d'
    delta = dt.timedelta(days=1)
    start_date_dt = dt.datetime.strptime(start_date, format_str)
    rel_start_date = start_date_dt
    df = pd.DataFrame()
    if weekly == False:
        end_date_dt = dt.datetime.strptime(end_date, format_str)
    else:
        end_date_dt = start_date_dt+(7*delta)
    while rel_start_date <= end_date_dt:
        rel_end_date = rel_start_date + delta
        for x in [extract_data]: 
            df1 = x(report_name, rel_start_date.strftime(format_str), rel_end_date.strftime(format_str))
        df = pd.concat([df, df1], ignore_index=True)
        rel_start_date = rel_start_date+delta
    return df

def extract_data_range_with_BMRS_label(report_name = 'TEMP', start_date = '2020-03-24', end_date =  '2020-03-25', save_to_csv = False):
    '''Extracts data using the BMRS labels. Inputs: BMRS label, start_date, end_date, save_to_csv'''
    df = iter_data_extract_without_helper(report_name, start_date, end_date)
    df = df.drop_duplicates().reset_index(drop=True)
    if save_to_csv == True:
        df.to_csv(report_name+'_'+start_date+'_'+end_date+'.csv')
    return df