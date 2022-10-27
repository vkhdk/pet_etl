#importing public libraries
from bs4 import BeautifulSoup
import json

#importing internal modules
import secrets
import project_files_and_roles

#converting a BeautifulSoup object to JSON
def google_soup_to_json_weather(soup, city_name):
    #parsing temperature in celsius and fahrenheit based on id
    temperature_f = soup.select_one("#wob_tm").text
    temperature_c = soup.select_one("#wob_ttm").text
    #parsing temperature in celsius and fahrenheit based on id

    output_dict = {}
    output_dict[city_name] = {'temperature_f' :temperature_f,
                              'temperature_c': temperature_c
                              }
    output_json = json.dumps(output_dict)
    
    ###################
    content = output_json
    with open(project_files_and_roles.content, 'w', encoding='utf-8') as outfile:
        outfile.write(str(content))
    ###################
