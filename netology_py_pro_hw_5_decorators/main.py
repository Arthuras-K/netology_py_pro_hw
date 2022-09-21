from logic import logger_dec


# ------- hw_4* ------
@logger_dec(path = "netology_py_pro_hw_5_decorators\logger.json")
def flat_generator(nested_list: list) -> list:
    flat_list = [el for item in nested_list for el in item]
    index = 0
    return flat_list

nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
    ]
# -------------------


if __name__ == '__main__':
    flat_generator(nested_list)
    

  

