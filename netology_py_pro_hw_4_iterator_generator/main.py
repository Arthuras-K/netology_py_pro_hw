from def_hw_4 import FlatIterator
from def_hw_4 import flat_generator


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

if __name__ == '__main__':
    # task 1
    # Написать итератор, который принимает список списков, и возвращает их плоское представление

    print('task 1.1:')
    for item in FlatIterator(nested_list):
        print(item)

    flat_list = [item for item in FlatIterator(nested_list)]
    print('\ntask 1.2:\n', flat_list)

    # task 2
    # Написать генератор, который принимает список списков, и возвращает их плоское представление
    print('\ntask 2:')
    for item in  flat_generator(nested_list):
        print(item)