from copy import deepcopy
from def_hw_4 import FlatIterator
from def_hw_4 import flat_generator
from def_hw_4 import DeepIterator
from def_hw_4 import deep_generator


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]

deep_list = [
    ['start', 's',['t', ['a'], 'r'], 't'],
	['a', 'b', 'c', [1, [[[[2]]]], 3]],
    [4],
	[False, 'or', None],
    [['finish']]
]



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

