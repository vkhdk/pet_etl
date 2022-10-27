#importing internal modules
import project_files_and_roles
import get_data_from_api
import get_weather_from_google_search

if __name__ == '__main__':
    city_name = 'Moscow'
    question = f'weather {city_name}'
    soup = get_data_from_api.soup_from_google_search(question)
    content = \
        get_weather_from_google_search.google_soup_to_json_weather(soup,
                                                                   city_name)

    ###################
    content = content
    with open(project_files_and_roles.content, 'w', encoding='utf-8') as outfile:
        outfile.write(str(content))
    ###################
