from pprint import pprint
import csv
import re

# читаем адресную книгу в формате CSV в список contacts_list
with open("netology_py_pro_hw_2_reg/phonebook_raw.csv", 'r', encoding='UTF-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


# TODO 1: выполните пункты 1-3 ДЗ
push_list = [contacts_list[0]]

for i in range(1, len(contacts_list)):
    contact = ','.join(contacts_list[i])

    pattern_phone = r'(\+7|8)\W{0,2}(\d{3})\W{0,2}(\d{3})\W?(\d\d)\W?(\d\d)\W{0,2}(доб\.)?\W{0,2}(\d{4})?\)?'
    standard_phone = r'+7(\2)\3-\4-\5 \6\7'
    contact_fix = re.sub(pattern_phone, standard_phone, contact)    

    pattern = r"^(\w+)[ ,](\w+)[ ,](\w*),+(\w*),+(.*[^,])?,+(.*),+(.*)"
    result = list(re.findall(pattern, contact_fix)[0])

    pprint(result)

    flag = True

    for pl in push_list:        
        if pl[0] == result[0] and pl[1] == result[1]:
            flag = False 
            break

    if flag:
        push_list.append(result)
    else:
        for j in range(2,7): 
            if  pl[j] == '':
                pl[j] = result[j]


# TODO 2: сохраните получившиеся данные в другой файл

# код для записи файла в формате CSV
with open("netology_py_pro_hw_2_reg/phonebook.csv", "w", encoding='UTF-8') as f:
    datawriter = csv.writer(f, delimiter=',', lineterminator='\n')
    datawriter.writerows(push_list)