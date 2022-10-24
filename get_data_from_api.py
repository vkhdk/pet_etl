#everything related to connecting to the API

#importing public libraries
import requests
import json
from datetime import datetime

#importing internal modules
import secrets
import project_files_and_roles

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
            #now I use a simple save in log.txt .
            #then I need to implement via getLogger.
            error_content = json.loads(res.content)
            status_code_content = res.status_code
            error_server_time_content = datetime.now()
            full_error_content = f'there is a bug, but there is also content - '\
                                 f'time:{error_server_time_content} - '\
                                 f'code:{status_code_content} - '\
                                 f'error content:{error_content}'
            with open(project_files_and_roles.errors_log, 'w', encoding='utf-8') as outfile:
                json.dump(full_error_content, outfile, ensure_ascii=False, indent=4)
        except Exception as error_text:
            status_code_content = res.status_code
            error_server_time_content = datetime.now()
            full_error_content = f'no content. only a bug - '\
                                 f'time:{error_server_time_content} - '\
                                 f'code:{status_code_content} - '\
                                 f'error text:{error_text}'
            with open(project_files_and_roles.errors_log, 'w', encoding='utf-8') as outfile:
                json.dump(full_error_content, outfile, ensure_ascii=False, indent=4)
    else:
        content = res.content
        with open(project_files_and_roles.content, 'w', encoding='utf-8') as outfile:
            json.dump(full_error_content, outfile, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    api_url = secrets.api_url
    params = secrets.params
    headers = secrets.headers
    api_request(api_url, params, headers)
