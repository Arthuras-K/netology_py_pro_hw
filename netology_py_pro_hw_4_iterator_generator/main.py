from copy import deepcopy
from logic import FlatIterator
from logic import flat_generator
from logic import DeepIterator
from logic import deep_generator
from data import nested_list
from data import deep_list


if __name__ == '__main__':
    # task 1
    # Написать итератор, который принимает список списков и возвращает их плоское представление
    print('task 1.1:')
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print('\ntask 1.2:\n', flat_list)


    # task 2
    # Написать генератор, который принимает список списков и возвращает их плоское представление
    print('\ntask 2:')
    for item in  flat_generator(nested_list):
        print(item)


    # task 3*
    # Написать итератор, который принимает список c сюбым уровнем вложенности и возвращает их плоское представление
    print('\ntask 3:')
    copy_list = deepcopy(deep_list)
    for item in DeepIterator(copy_list):
        print(item)


    # task 4*
    # Написать генератор, который принимает список с любым уровнем вложенности и возвращает их плоское представление
    print('\ntask 4:')
    copy_list = deepcopy(deep_list)
    for item in  deep_generator(copy_list):
        print(item)        