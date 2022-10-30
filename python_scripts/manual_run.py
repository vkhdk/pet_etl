#importing public libraries
import datetime as dt
from datetime import datetime
import logging
import tabulate
import pandas as pd

#importing internal modules
import folder_files_and_roles
import get_data_from_api
import get_weather_from_google_search
import utilities

if __name__ == '__main__':
    #logging setup
    logging.basicConfig(filename='manual_run.log',
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

    test_dict = {}

    for city in city_names:
        question = f'weather {city}'
        logger.info(f'...make soup for "{city}"')
        soup = get_data_from_api.soup_from_google_search(question)
        logger.info(f'...make json for "{city}"')
        output_json = \
        get_weather_from_google_search.google_soup_to_json_weather(soup)
        data_dict = {
                     #create unique id
                     'weather_id': utilities.create_unique_id_from_date(),
                     #create date feature
                     'date': datetime.now().date(),
                     'time': datetime.now().time(),
                     #data from json
                     'city_name': city
                     #,
                     #'temp_c': output_json['temperature_c'],
                     #'temp_f': output_json['temperature_f']
                     }
        data_dict_df = pd.DataFrame([data_dict])
        db_df = pd.concat([db_df,data_dict_df])

    ###################
    content = db_df.to_markdown()
    #content = db_df.to_markdown()
    with open(folder_files_and_roles.content, 'w', encoding='utf-8') as outfile:
        outfile.write(content)
    ###################
