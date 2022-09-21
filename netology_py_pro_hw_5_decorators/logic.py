import json
import datetime as dt
import pathlib


# task 1
# Функция декоратор с параметром
def logger_dec(path:str = 'logger.json'):
    def logger(old_finction):
        def new_function(*args, **kwargs):
            key = str(dt.datetime.now())

            result = old_finction(*args, **kwargs)       
            
            log = {
                'name_function': old_finction.__name__,
                'arguments': [args, kwargs],
                'result': result
            } 

            # Проверка на наличие файла и если нет,то создание его            
            if not pathlib.Path(path).is_file():
                with open(path, 'w') as file:
                    json.dump({}, file)     

            # Открываем файл в режиме чтения и возможности записи («r+»)
            with open(path, 'r+', encoding='utf-8') as file:
                # Считываем имеющееся в нем содержимое и преобразуем его в словарь    
                data = json.load(file)
                # Добавляем новую запись в словарь с ключом key
                data[key] = log
                # Создать словарь с ключом key
                data = {key: log}
                file.seek(0)
                # Делаем отступы (indent=4) для удобства чтения, а также отключаем режим «только ASCII», чтобы появилась возможность вставлять кириллицу.
                json.dump(data, file, ensure_ascii=False, indent=4)    

                print(f'Записан вызов функции {old_finction.__name__} по ключу: "{key}"')

            return result
        return new_function
    return logger
