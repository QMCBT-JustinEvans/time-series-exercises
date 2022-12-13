import pandas as pd



def dmy_conversion(df, datetime_column):
    """
    This function ensures the datetime_column given as an argument is converted to dtype of datetime64.
    Then adds Day, Month, and Year columns and sets the index to the datetime_column

    Imports Required:
    import pandas as pd

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