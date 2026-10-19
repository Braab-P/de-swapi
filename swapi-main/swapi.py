import requests
import os
import json

# Создаем базовый класс
class APIRequester:
    def __init__(self, base_url):
        self.base_url = base_url

   # Проверяем на ошибки
    def get(self, url):
        try:
            response = requests.get(f'{self.base_url}{url}')
            response.raise_for_status()
            return response
        except requests.ConnectionError:
            return '<Cетевая ошибка>'
        except requests.HTTPError as e:
            return f'Ошибка: {e.response.status_code}'

# Создаем дочерний класс
class SWRequester(APIRequester):
    def __init__(self, base_url):  
        super().__init__('https://swapi.dev/api/')


    def get_sw_categories(self):
        response=self.get('') 
        categories = response.json() 
        return categories.keys()

    def get_sw_info(self, sw_type):
        response = self.get(sw_type + '/')
        return response.text

    def save_sw_data(self):
        directory = 'data'
        os.makedirs(directory, exist_ok=True)
        categories = self.get_sw_categories()

        for category in categories:
            data = self.get_sw_info(category)
            filename = os.path.join(directory, f'{category}.txt')
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(str(data))

if __name__ == 'saveswdata':
    saveswdata()