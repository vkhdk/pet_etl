#importing public libraries
from bs4 import BeautifulSoup
import json

#converting a BeautifulSoup object to JSON
def google_soup_to_json_weather(soup):
    #parsing temperature in celsius and fahrenheit based on id
    temperature_f = float(soup.select_one("#wob_tm").text)
    temperature_c = float(soup.select_one("#wob_ttm").text)
    #write data
    output_dict = {'temperature_f' :temperature_f,
                   'temperature_c': temperature_c
                   }
    #converting dictionary to json
    output_json = json.dumps(output_dict)
    return(output_json)
