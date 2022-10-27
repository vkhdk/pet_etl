#importing internal modules
import project_files_and_roles
import get_data_from_api
import get_weather_from_google_search

if __name__ == '__main__':
    city_names = ['Moscow', 'London']
    output_dict = {}
    for city in city_names:
        question = f'weather {city}'
        soup = get_data_from_api.soup_from_google_search(question)
        output_json = \
        get_weather_from_google_search.google_soup_to_json_weather(soup)
        output_dict[city] = output_json

    ###################
    content = output_dict
    with open(project_files_and_roles.content, 'w', encoding='utf-8') as outfile:
        outfile.write(str(content))
    ###################
