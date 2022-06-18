import pandas as pd
import numpy as np
import os
from env import host, user, password

# # Acquiring the Zillow Data

# def get_connection(db, user=user, host=host, password=password):
#     '''
#     get_connection uses login info from env.py file to access Codeup db.
#     It takes in a string name of a database as an argument.
#     '''
#     return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# def get_zillow_data():
#     '''
#     zillow_data() gets the zillow (only properties_2017 table) data from Codeup db, then writes it to a csv file,
#     and returns the DF.
#     '''
#     # Creating a SQL query
#     sql_query = '''
#                 SELECT 
#                        bedroomcnt,
#                        bathroomcnt,
#                        calculatedfinishedsquarefeet,
#                        taxvaluedollarcnt,
#                        propertylandusetypeid,
#                        transactiondate
#                 FROM properties_2017
#                 JOIN propertylandusetype USING(propertylandusetypeid)
#                 JOIN predictions_2017 USING(parcelid)
#                 WHERE propertylandusetypeid = '261'
#                 '''
    
#     # Reading in the DataFrame from Codeup db.
#     df = pd.read_sql(sql_query, get_connection('zillow'))
#     return df


def get_local_zillow():
    '''
    get_local_zillow reads in telco data from Codeup database, writes data to
    a csv file if a local file does not exist, and returns a DF.
    '''
    if os.path.isfile('properties_2017.csv'):
        
        # If csv file exists read in data from csv file.
        df = pd.read_csv('properties_2017.csv', index_col=0)
        
    # else:
        
    #     # Read fresh data from db into a DataFrame
    #     df = get_zillow_data()
        
    #     # Cache data
    #     df.to_csv('properties_2017.csv')
        
    return df

#     def get_zillow_data():
#    '''
#    Pulls in data from SQL server. 
#    Only columns without large amounts of nulls where lat and long are not null
#    And where bed and bath count are greater than 0
#    ''' 
#    query = '''
#    SELECT
#       properties_2017.parcelid,
#       bathroomcnt,
#       bedroomcnt,
#       calculatedfinishedsquarefeet,
#       fips,
#       latitude,
#       longitude,  
#       lotsizesquarefeet,
#       yearbuilt, 
#       structuretaxvaluedollarcnt,
#       taxvaluedollarcnt, 
#       landtaxvaluedollarcnt,
#       taxamount,                      
#       predictions_2017.logerror,                       
#       predictions_2017.transactiondate
#    FROM properties_2017
#    JOIN predictions_2017 USING(parcelid)
#    LEFT JOIN airconditioningtype USING(airconditioningtypeid)
#    LEFT JOIN architecturalstyletype USING(architecturalstyletypeid)
#    LEFT JOIN buildingclasstype USING(buildingclasstypeid)
#    LEFT JOIN heatingorsystemtype USING(heatingorsystemtypeid)
#    LEFT JOIN propertylandusetype USING(propertylandusetypeid)
#    LEFT JOIN storytype USING(storytypeid)
#    LEFT JOIN typeconstructiontype USING(typeconstructiontypeid)
#    WHERE
#       latitude IS NOT NULL
#       AND longitude IS NOT NULL
#    AND bathroomcnt > 0
#    AND bedroomcnt > 0
#    '''
#    df = pd.read_sql(query, get_db_url('zillow'))
#    return df