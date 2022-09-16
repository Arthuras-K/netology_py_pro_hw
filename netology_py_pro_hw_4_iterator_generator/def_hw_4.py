class FlatIterator:
    
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

def flat_generator(nested_list: list) -> list:
    flat_list = [el for item in nested_list for el in item]
    index = 0
    while index < len(flat_list):
        yield flat_list[index]
        index += 1