from class_stack import Stack


def check_balance(collection: str)-> str:
    stack = Stack()
    len_col = len(collection)
    if len_col % 2 == 0:
        for i in range(len_col):
            if stack.size():
                up_stack = stack.peek()
                if up_stack == "(" and collection[i] == ")":
                    stack.pop()
                elif up_stack == "[" and collection[i] == "]":
                    stack.pop()
                elif up_stack == "{" and collection[i] == "}":
                    stack.pop()
                else:
                    stack.push(collection[i])
            else:
                stack.push(collection[i])
        if not stack.size():
            return 'Сбалансированно'
    return 'Несбалансированно'


if __name__ == '__main__':
    # task_1  
    print('-'*10, 'task_1', '-'*10) 
    object = Stack()
    print(object.is_empty())
    object.push('one')
    object.push('two')
    object.push('three')
    print(object.is_empty())
    print(object.pop())
    print(object.peek())
    print(object.size())


    # task_2
    print('\n', '-'*10, 'task_2', '-'*10) 
    example = '[([])](){()}'
    print(check_balance(example))
