#importing public libraries
import datetime as dt
from datetime import datetime
import logging
import pandas as pd
import json
import os.path
from sqlalchemy.types import BigInteger, Time, Date, Float, Integer, Boolean, Text, TIMESTAMP

#importing internal modules
import folder_files_and_roles
import get_data_from_api
import get_weather_from_google_search
import ETL_utilities
import db_connection

if __name__ == '__main__':
    #logging setup
    logging.basicConfig(filename=folder_files_and_roles.manual_run_log,
                        format=f'%(asctime)s'
                               f' - %(name)s'
                               f' - %(levelname)s'
                               f' - %(message)s',
                        filemode='a', # add filemode="w" to overwrite
                        level=logging.INFO)
    logging.getLogger('googleapiclient.discovery_cache').setLevel(logging.ERROR)
    logger = logging.getLogger(__name__)

    #just debug
    city_names = ['Moscow', 'London']
    columns = ['weather_id',
               'date',
               'time',
               'city_name',
               'temp_c',
               'temp_f']
    db_df = pd.DataFrame(columns=columns)

    #take a city
    for city in city_names:
        #put city in question
        question = f'weather {city}'
        logger.info(f'...make soup for "{city}"')
        #make soup with question
        soup = get_data_from_api.soup_from_google_search(question)
        logger.info(f'...make json for "{city}"')
        #make json from soup
        output_json = \
        get_weather_from_google_search.google_soup_to_json_weather(soup)
        #create a dictionary to save the results
        data_dict = {
                     #create unique id
                     'weather_id': ETL_utilities.create_unique_id_from_date(),
                     #create date feature
                     'date': datetime.now().date(),
                     'time': datetime.now().time(),
                     #data from json
                     #load string json as dict and write in data dict
                     'city_name': city,
                     'temp_c': json.loads(output_json)['temperature_c'],
                     'temp_f': json.loads(output_json)['temperature_f']
                     }
        #convert dictionary to df for concat
        data_dict_df = pd.DataFrame([data_dict])
        db_df = pd.concat([db_df,data_dict_df])

    
    ############
    #debug with write to csv
    ############
    #data to write
    content = db_df
    #path to file
    content_path = folder_files_and_roles.content
    #
    if os.path.isfile(content_path):
        #create a file with headers if the file does not exist
        content.to_csv(folder_files_and_roles.content, 
            index=False, 
            sep=';',
            mode='a', 
            header=False)
    else:
        #add data if the file has already been created without headers
        content.to_csv(folder_files_and_roles.content, 
            index=False, 
            sep=';')
    ############

    engine = db_connection.engine
    weather_dtypes = {'time': Time, 
        'date': Date, 
        'temp_c': Float, 
        'temp_f': Float}

    weather_sql_query = '''
    CREATE TABLE IF NOT EXISTS weather_prod(
        weather_id TEXT NOT NULL PRIMARY KEY,
        date DATE NOT NULL,
        time TIME NOT NULL,
        city_name TEXT NOT NULL,
        temp_c FLOAT NOT NULL,
        temp_f FLOAT NOT NULL);
    INSERT INTO weather_prod (weather_id,
        date,
        time,
        city_name,
        temp_c,
        temp_f)
    (SELECT weather_id,
        date,
        time,
        city_name,
        temp_c,
        temp_f
    FROM weather_tmp);
    '''

    db_connection.load_df_to_tpm_table(db_df, 'weather',  weather_dtypes)
    db_connection.load_tmp_table_to_prod_table(weather_sql_query)