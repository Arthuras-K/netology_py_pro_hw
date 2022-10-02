import yaml
import requests


# Функция создает папку на яндекс.диске
def create_folder(TOKEN_YD, name_folder):
    url = 'https://cloud-api.yandex.net/v1/disk/'
    files_url = url + 'resources/'
    path_to = f'disk:/{name_folder}/'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'OAuth {}'.format(TOKEN_YD)
        }
    params = {
        'path': path_to
        }

    response = requests.put(files_url, headers=headers, params=params)       
    if response.status_code == 201:
        print(" - Создана папка ")
        return response.status_code

    else:
        print(f' - Ошибка! Код: {response.status_code}')
        return response.status_code    


if __name__ == '__main__':             
    with open('netology_py_pro_hw_6_tests\config.yaml') as f:
        config = yaml.safe_load(f)
        TOKEN_YD = config['token_yd'] # Токен от Яндекс.Диск
    
    name_folder = 'new_folder' # Имя папки 

    create_folder(TOKEN_YD, name_folder)