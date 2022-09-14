from pprint import pprint
import csv
import re


# Функция проверяет на наличие контакта в списке и слияние их
def check_repeat(main_list: list, add_list: list) -> bool:
    flag = True
    for ml in main_list:        
        if ml[0] == add_list[0] and ml[1] == add_list[1]:
            flag = False 
            for n in range(2,7): 
                    if  ml[n] == '':
                        ml[n] = result[n]   
    return flag   


if __name__ == '__main__':
    # читаем адресную книгу в формате CSV в список contacts_list
    with open("netology_py_pro_hw_2_reg/phonebook_raw.csv", 'r', encoding='UTF-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    push_list = [contacts_list[0]]

    # используем регулярные выражения, для выборки из текста
    for i in range(1, len(contacts_list)):
        contact = ','.join(contacts_list[i])

        pattern_phone = r'(\+7|8)\W{0,2}(\d{3})\W{0,2}(\d{3})\W?(\d\d)\W?(\d\d)(?:\W{0,2}(доб\.)\W{0,2}(\d{4}))?\)?'
        standard_phone = r'+7(\2)\3-\4-\5 \6\7'
        contact_fix = re.sub(pattern_phone, standard_phone, contact)    
        print(f'Телефонный номер {i} контакта отредактирован')

        pattern = r"^(\w+)[ ,](\w+)[ ,](\w*),+(\w*),+(.*[^,])?,+(.*),+(.*)"
        result = list(re.findall(pattern, contact_fix)[0])

        if check_repeat(push_list, result):
            push_list.append(result)
            print(f'Контакт {i} добавлен')
        else:
            print(f'Контакт {i} объединен')


    # код для записи файла в формате CSV
    with open("netology_py_pro_hw_2_reg/phonebook.csv", "w", encoding='UTF-8') as f:
        datawriter = csv.writer(f, delimiter=',', lineterminator='\n')
        datawriter.writerows(push_list)
        print('\nФайл успешно записан в формате CSV\n')