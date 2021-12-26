import unittest
import functions as hw
from parameterized import parameterized


class TestFunctionsUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setUpClass method')

    def setUp(self) -> None:
        print('setUp method')


    @parameterized.expand([
        ['2207 876234', True],
        ['11-2', True],
        ['10006', True]
    ])
    def test_check_document_existance(self, number, result):
        self.assertEqual(hw.check_document_existance(number), result)


    @parameterized.expand([
        ['2207 876234', 'Василий Гупкин'],
        ['11-2', 'Геннадий Покемонов'],
        ['10006', 'Аристарх Павлов'],
        ['1111', None]
    ])
    def test_get_doc_owner_name(self, number, result):
        self.assertEqual(hw.get_doc_owner_name(number), result)


    @parameterized.expand([[
        {'Аристарх Павлов',
         'Василий Гупкин',
         'Геннадий Покемонов'},
        {'Аристарх Павлов',
         'Василий Гупкин',
         'Геннадий Покемонов'}
    ]])
    def test_get_all_doc_owners_names(self, set_users_name, result):
        self.assertEqual(hw.get_all_doc_owners_names(set_users_name), result)


    @parameterized.expand([[
        [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
            {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
        ],

        '10006',

        [
            {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
            {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        ]

    ]])
    def test_delete_doc(self, documents, user_doc_number, result):
        self.assertEqual(hw.delete_doc(documents, user_doc_number), result)


    @parameterized.expand([[
        {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3': []
        },

        '4',

        {
            '1': ['2207 876234', '11-2', '5455 028765'],
            '2': ['10006'],
            '3':[],
            '4':[]
        }
    ]])
    def test_add_new_shelf(self, directories, shelf_number, result):
        res = hw.add_new_shelf(directories, shelf_number)
        self.assertEqual(res, result)


    def tearDown(self) -> None:
        print('tearDown method')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass method')


if __name__ == '__main__':
    unittest.main()