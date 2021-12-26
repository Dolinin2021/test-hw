import json
import requests


class YandexDisk:
    '''
    Класс YandexDisk - используется для работы с Яндекс.Диском.

    Основное применение - работа с файлами на Яндекс.Диске.

    Attributes
    ----------
    token: str
        OAuth - токен


    Methods
    -------
    get_headers()
        возвращает заголовки запроса.

    _error_validator(response: dict)
        обрабатывает возникающие ошибки. Является приватным методом.

    create_directory_yandex_disk(path: str)
        создаёт папку на Яндекс.Диске.


    Exceptions
    ----------
    400	- Некорректные данные.

    401	- Не авторизован.

    403	- API недоступно. Ваши файлы занимают больше места, чем у вас есть.
    Удалите лишнее или увеличьте объём Диска.

    406	- Ресурс не может быть представлен в запрошенном формате.

    429	- Слишком много запросов.

    503	- Сервис временно недоступен.

    507	- Недостаточно свободного места.

    Эти исключения являются общими для используемых методов работы с Яндекс.Диском в данном классе.

    Специальные исключения, которые возникают при работе с конкретным методом,
    можно найти в документации к этим методам.

    '''

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def _error_validator(self, response):
        '''
        Метод для обработки ошибок.
        Возвращает сообщение об ошибке и записывает возникающие ошибки в файл.

        Parameters
        ----------
        response: dict
            ответ сервера.


        В качестве возврата (return) метод использует логическое значение true либо false.

        '''

        if 'error' in response:

            print(f"\nРабота метода была прервана ошибкой. Происходит обработка ошибки, пожалуйста, подождите...\n"
                  f"Название ошибки: \n{response['error']}\n"
                  f"Сообщение об ошибке: \n{response['message']}\n"
                  f"Описание ошибки: \n{response['description']}\n")

            with open('log_yandex.json', 'a', encoding='utf-8') as file_obj:
                print('Данные об ошибке сохранены в лог log_yandex.json')
                json.dump(response, file_obj, ensure_ascii=False, indent=4)
                print()

            return True

        else:
            return False

    def create_directory_yandex_disk(self, path):
        '''
        Метод для создания папки на Яндекс.Диске.

        Parameters
        ----------
        path: str
            путь к создаваемой папке на Яндекс.Диске.


        Exceptions
        ----------
        404	- Не удалось найти запрошенный ресурс.

        409	- Ресурс "{path}" уже существует.

        423	- Ресурс заблокирован. Возможно, над ним выполняется другая операция.

        Данные исключения являются специальными для данного метода.


        В качестве возврата (return) метод использует код статуса запроса.

        '''

        create_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': path}
        response = requests.put(url=create_url, headers=headers, params=params)
        req = response.json()

        if self._error_validator(req) == False:

            print()
            print('Создание папки прошло успешно.')
            print()

        return response.status_code
