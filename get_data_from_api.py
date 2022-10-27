#everything related to connecting to the API

#importing public libraries
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

#get soup from google search
def soup_from_google_search(question):
    #url to search
    google_url = f'https://www.google.com/search'
    #basic agent parameters
    headers = {
       'user-agent':
       f'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
       f'AppleWebKit/537.36 (KHTML, like Gecko) '
       f'Chrome/103.0.5060.134 Safari/537.36'
       }
    #basic parameters for data output in english
    params = {
        'hl': 'en',
        'gl': 'us',
        'lr': 'lang_en'
        }
    #add question in params
    params['q'] = question

    # requests.get(url) returns a response that is saved
    # in a response object called page
    page = requests.get(google_url, headers=headers, params=params)
    # page.text gives us access to the web data in text
    # format, we pass it as an argument to BeautifulSoup
    # along with the html.parser which will create a
    # parsed tree in soup
    soup = BeautifulSoup(page.text, "html.parser")
    return(soup)
