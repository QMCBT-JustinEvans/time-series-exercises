import os
import requests
import numpy as np
import pandas as pd

# Working with Dates & Times
from sklearn.model_selection import TimeSeriesSplit
from datetime import timedelta, datetime

import statsmodels.api as sm

# to evaluate performance using rmse
from sklearn.metrics import mean_squared_error
from math import sqrt 

# for tsa 
import statsmodels.api as sm

# holt's linear trend model. 
from statsmodels.tsa.api import Holt

# Plots, Graphs, & Visualization
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from matplotlib.dates import DateFormatter



def dmy_conversion(df, datetime_column):
    """
    DESCRIPTION:
    This function ensures the datetime_column given as an argument is converted to dtype of datetime64.
    Then adds Day, Month, and Year columns and sets the index to the datetime_column
    ___________________________________
    IMPORTS REQUIRED:
    import pandas as pd
    from datetime import timedelta, datetime
    ___________________________________
    ARGUMENTS:
                 df = DataFrame
    datetime_column = The 'column_name' of the column being used to store Date and Time data as datetime data type.
    """
    
    # Ensure datetime_column is dtype datetime64
    df[datetime_column] = pd.to_datetime(df[datetime_column])
    
    # Convert datetime_column column to Day, Month, Year
    df['day'] = df[datetime_column].dt.day
    df['day_of_week'] = df[datetime_column].dt.day_name()
    df['weekday_number'] = df[datetime_column].dt.day_of_week+1
    df['year'] = df[datetime_column].dt.year
    df['month'] = df[datetime_column].dt.month_name()
    df['month_number'] = df[datetime_column].dt.month
    #df['hour'] = df[datetime_column].dt.hour
    #df['minute'] = df[datetime_column].dt.minute
    #df['second'] = df[datetime_column].dt.second

    # Set index
    df = set_index(df, datetime_column)

    # FUTURE FUNCTIONALITY
    # Use IF statements and D,M,Y,H,Min,Sec arguments to determin layers of conversion
    
    return df

def prep_store_data(df, datetime_column):
    """
    Combine functions needed to prepare store data for use. 
    """
    
    # Convert sale_date column to datetime format; Add Day, Month, Year columns; set Index to sale_date 
    dmy_conversion(df, datetime_column)
    
    # Create Sales Total column from Item Price multiplied by Sales Amount
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df

def set_index(df, datetime_column):
    df = df.set_index(datetime_column).sort_index()
    
    return df

def prep_ops_data(df, datetime_column):
    """
    Combine functions needed to prepare ops data for use. 
    """
    
    # Convert sale_date column to datetime format; Add Day, Month, Year columns; set Index to sale_date 
    dmy_conversion(df, datetime_column)
    
    # Replace all null with 0 and show resulting null count
    df.fillna(0, inplace=True)

    return df