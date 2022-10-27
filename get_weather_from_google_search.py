#importing public libraries
from bs4 import BeautifulSoup
import json

#converting a BeautifulSoup object to JSON
def google_soup_to_json_weather(soup, city_name):
    #parsing temperature in celsius and fahrenheit based on id
    temperature_f = soup.select_one("#wob_tm").text
    temperature_c = soup.select_one("#wob_ttm").text
    #create an empty dictionary for data output
    output_dict = {}
    #write data
    output_dict[city_name] = {'temperature_f' :temperature_f,
                              'temperature_c': temperature_c
                              }
    #converting dictionary to json
    output_json = json.dumps(output_dict)
    return(output_json)
