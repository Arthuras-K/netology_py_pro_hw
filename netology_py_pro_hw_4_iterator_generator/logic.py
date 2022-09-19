class FlatIterator:
    '''
    Класс итератор для вывода элементов 2D списка
    '''    
    def __init__(self, nested_list: list):
        self.nested_list = nested_list

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        # Сглаживание вложенного списка с использованием понимания списка
        flat_list = [el for item in self.nested_list for el in item]

        self.index += 1
        if self.index >= len(flat_list):
            raise StopIteration

        return flat_list[self.index]


# Функции генератор для вывода элементов 2D списка
def flat_generator(nested_list: list) -> list:
    flat_list = [el for item in nested_list for el in item]
    index = 0
    while index < len(flat_list):
        yield flat_list[index]
        index += 1


class DeepIterator:
    '''
    Класс итератор для вывода элементов списка с любым уровнем вложенности
    '''       
    def __init__(self, deep_list: list):
        self.deep_list = deep_list

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        def diving(sea_list):
            if isinstance(sea_list[0], list) and sea_list[0]:
                sea_list = sea_list[0]
                return diving(sea_list)
            else:
                return sea_list.pop(0)

        while True:    
            if self.deep_list:    
                result = diving(self.deep_list)
                if result != []:
                    return result
            else:
                raise StopIteration

    
# Функции генератор для вывода элементов списка с любым уровнем вложенности
def deep_generator(deep_list: list) -> list:
    def diving(sea_list):
        if isinstance(sea_list[0], list) and sea_list[0]:
            sea_list = sea_list[0]
            return diving(sea_list)
        else:
            return sea_list.pop(0)

    while True:    
        if deep_list:    
            result = diving(deep_list)
            if result != []:
                yield result
