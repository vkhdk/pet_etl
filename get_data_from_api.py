#everything related to connecting to the API

#importing public libraries
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

#importing internal modules
import secrets
import project_files_and_roles

def data_from_google_search(question, google_url, headers, params):
    #add question in params
    params = params
    params['q'] = question


    # requests.get(url) returns a response that is saved
    # in a response object called page
    page = requests.get(google_url, headers=headers, params=params)
    # page.text gives us access to the web data in text
    # format, we pass it as an argument to BeautifulSoup
    # along with the html.parser which will create a
    # parsed tree in soup

    soup = BeautifulSoup(page.text, "html.parser")
    temp = soup.find('div', attrs={'class': 'vk_bk TylWce SGNhVe'})
    #hz = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    ###################
    content = temp
    with open(project_files_and_roles.content, 'w', encoding='utf-8') as outfile:
        outfile.write(str(content))
    ###################



def api_request(api_url, params, headers):
    """
    getting requests from the REST API
    :api_url: API url from secrets.py
    :params: REST API params from secrets.py
    :headers: headerы for the GET request
    """
    res = requests.get(api_url, params=params, headers=headers)
    if res.status_code != 200:
        try:
            #now I use a simple store in log.txt.
            #then I need to implement via getLogger.

            #generating data for error
            error_content = json.loads(res.content)
            status_code_content = res.status_code
            error_server_time_content = datetime.now()
            full_error_content = f'there is a bug, but there is also content - '\
                                 f'time:{error_server_time_content} - '\
                                 f'code:{status_code_content} - '\
                                 f'error content:{error_content}'

            #store error in log.txt.
            with open(project_files_and_roles.errors_log, 'w', encoding='utf-8') as outfile:
                json.dump(full_error_content, outfile, ensure_ascii=False, indent=4)

        except Exception as error_text:
            #if it is impossible to get the content
            #store the error text
            status_code_content = res.status_code
            error_server_time_content = datetime.now()
            full_error_content = f'no content. only a bug - '\
                                 f'time:{error_server_time_content} - '\
                                 f'code:{status_code_content} - '\
                                 f'error text:{error_text}'
            #store error in log.txt.
            with open(project_files_and_roles.errors_log, 'w', encoding='utf-8') as outfile:
                json.dump(full_error_content, outfile, ensure_ascii=False, indent=4)
    else:
        content = res.content
        with open(project_files_and_roles.content, 'w', encoding='utf-8') as outfile:
            json.dump(full_error_content, outfile, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    question = f'weather lucknow'
    google_url = secrets.google_url
    headers = secrets.headers
    params = secrets.params
    data_from_google_search(question, google_url, headers, params)
