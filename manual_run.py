#importing internal modules
import secrets
import project_files_and_roles
import get_data_from_api


if __name__ == '__main__':
    question = f'weather Токсово'
    get_data_from_api.data_from_google_search(question)
