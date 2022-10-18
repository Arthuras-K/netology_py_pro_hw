class Stack:
    '''Класс создает аналог стека.
    Стек - абстрактный тип данных, представляющий собой список элементов, 
    организованных по принципу LIFO 
    (англ. last in — first out, «последним пришёл — первым вышел»).'''    
    def __init__(self):
        self.elements = []

    def is_empty(self):
        'Проверка стека на пустоту. Метод возвращает True или False.'
        if self.elements:
            return True        
        else:
            return False

    def push(self, element):
        'Добавляет новый элемент на вершину стека. Метод ничего не возвращает.'
        self.elements.append(element)

    def pop(self):
        'Удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека'
        return self.elements.pop()

    def peek(self):
        'Возвращает верхний элемент стека, но не удаляет его. Стек не меняется.'
        return self.elements[-1]

    def size(self):
        'Возвращает количество элементов в стеке.'
        return len(self.elements)



