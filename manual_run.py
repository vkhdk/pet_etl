#importing internal modules
import secrets
import project_files_and_roles
import get_data_from_api
import get_weather_from_google_search

if __name__ == '__main__':
    city_name = 'Бишкек'
    question = f'weather {city_name}'
    soup = get_data_from_api.soup_from_google_search(question)
    get_weather_from_google_search.google_soup_to_json_weather(soup, city_name)
