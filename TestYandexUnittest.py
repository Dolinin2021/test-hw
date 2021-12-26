import unittest
from yandex_class import YandexDisk
from parameterized import parameterized


with open('ya_token.txt', 'r', encoding='utf-8') as yandex_file:
    yandex_token = yandex_file.read().strip()

yandex_disk = YandexDisk(yandex_token)


class TestYandexUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass method')

    def setUp(self) -> None:
        print('setUp method')


    @parameterized.expand([[
        'Netology',
         201
    ]])
    def test_status_code_created(self, path, result):
        status_code = yandex_disk.create_directory_yandex_disk(path)
        self.assertEqual(status_code, result)

    @parameterized.expand([[
        'Netology',
        409
    ]])
    def test_status_code_conflict(self, path, result):
        status_code = yandex_disk.create_directory_yandex_disk(path)
        self.assertEqual(status_code, result)

    @parameterized.expand([[
        '.',
        404
    ]])
    def test_status_code_not_found(self, path, result):
        status_code = yandex_disk.create_directory_yandex_disk(path)
        self.assertEqual(status_code, result)

    @parameterized.expand([[
        'Netology',
        401
    ]])
    def test_status_code_unauthorized(self, path, result):
        status_code = yandex_disk.create_directory_yandex_disk(path)
        self.assertEqual(status_code, result)


    def tearDown(self) -> None:
        print('tearDown method')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass method')


if __name__ == '__main__':
    unittest.main()