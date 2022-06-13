import pandas as pd
import numpy as np
import os
from env import host, user, password

# Acquiring the Zillow Data

def get_connection(db, user=user, host=host, password=password):
    '''
    get_connection uses login info from env.py file to access Codeup db.
    It takes in a string name of a database as an argument.
    '''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


def get_zillow_data():
    '''
    zillow_data() gets the zillow (only properties_2017 table) data from Codeup db, then writes it to a csv file,
    and returns the DF.
    '''
    # Creating a SQL query
    sql_query = '''
                SELECT 
                       bedroomcnt,
                       bathroomcnt,
                       calculatedfinishedsquarefeet,
                       taxvaluedollarcnt,
                       propertylandusetypeid,
                       transactiondate
                FROM properties_2017
                JOIN propertylandusetype USING(propertylandusetypeid)
                JOIN predictions_2017 USING(parcelid)
                WHERE propertylandusetypeid = '261'
                '''
    
    # Reading in the DataFrame from Codeup db.
    df = pd.read_sql(sql_query, get_connection('zillow'))
    return df


def get_local_zillow():
    '''
    get_local_zillow reads in telco data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a DF.
    '''
    if os.path.isfile('properties_2017.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('properties_2017.csv', index_col=0)
        
    else:
        
        # Read fresh data from db into a DataFrame
        df = get_zillow_data()
        
        # Cache data
        df.to_csv('properties_2017.csv')
        
    return df