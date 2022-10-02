import unittest
import app


class  TestFunction(unittest.TestCase):
    # # Методы setUp() и tearDown() (в данном простом случае не нужны) позволяют определять инструкции, выполняемые перед и после каждого теста, соответственно.
    # def setUp(self) -> None:
    #     print("SetUp==>")

    # def tearDown(self) -> None:
    #     print("tearDown")

    # Проверка функции на наличие документа
    def test_check_doc_exist(self):
        result = app.check_document_existance("2207 876234")
        self.assertTrue(result)

    # Проверка функции на получение имени по номеру
    def test_get_doc_name(self):
        etalon = "Василий Гупкин"
        result = app.get_doc_owner_name("2207 876234")
        self.assertEqual(result, etalon)

    # Проверка функции на получение всех имен
    def test_get_all_doc_names(self):
        etalon = {"Василий Гупкин", "Геннадий Покемонов", "Аристарх Павлов"}
        result = app.get_all_doc_owners_names()
        self.assertEqual(result, etalon)

    # Проверка функции на удаление документа
    def test_remove_doc_from_shelf(self):
        app.directories['1'] += ['test_doc']
        app.remove_doc_from_shelf('test_doc')
        self.assertFalse('test_doc' in app.directories['1'])
        if 'test_doc' in app.directories['1']:
            app.directories['1'].remove('test_doc')

    # Проверка функции на добавление полки
    def test_add_new_shelf(self):
        app.add_new_shelf('test_shelf')
        self.assertTrue('test_shelf' in app.directories)
        if 'test_shelf' in app.directories:
            app.directories.pop('test_shelf')

    # Проверка функции на добавление дока на полку
    def test_append_doc_to_shelf(self):
        app.append_doc_to_shelf('test_doc', '1')
        self.assertTrue('test_doc' in app.directories['1'])
        if 'test_doc' in app.directories['1']:
            app.directories['1'].remove('test_doc')      

    # Проверка функции на удаление документа
    def test_delete_doc(self):
        app.directories['1'] += ['test_doc']
        app.documents.append({"type": "test", "number": 'test_doc', "name": "test test"})
        app.delete_doc('test_doc')
        self.assertTrue('test_doc' not in app.directories['1'] and 'test_doc' != app.documents[-1]["number"])
        if 'test_doc' in app.directories['1']:
            app.directories['1'].remove('test_doc')
        if 'test_doc' == app.documents[-1]["number"]:
            app.documents.pop(-1)

    # Проверка функции нахождения номера полки
    def test_get_doc_shelf(self):
        etalon = "1"
        result = app.get_doc_shelf("2207 876234")
        self.assertEqual(result, etalon)

    # Проверка функции перемещения дока с полки на полку
    def test_move_doc_to_shelf(self):
        app.directories['1'] += ['test_doc']
        app.move_doc_to_shelf('test_doc', '2')
        self.assertTrue('test_doc' in app.directories['2'])
        if 'test_doc' in app.directories['1']:
            app.directories['1'].remove('test_doc')     
        if 'test_doc' in app.directories['2']:
            app.directories['2'].remove('test_doc')       

    # Проверка функции добавления документа
    def test_add_new_doc(self):
        app.add_new_doc('test_doc', "test", "test test", '1')
        # self.assertTrue('test_doc' in app.directories['1'] and 'test_doc' == app.documents[-1]["number"])
        if 'test_doc' in app.directories['1']:
            app.directories['1'].remove('test_doc')
        if 'test_doc' == app.documents[-1]["number"]:
            app.documents.pop(-1)


if __name__ == "__main__":
    unittest.main()