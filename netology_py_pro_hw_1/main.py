from datetime import datetime
from colorama import Fore, Back, Style
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    print(datetime.now())

    payment_hours = calculate_salary(60000)

    print(f'Оплата в час: {payment_hours}')

    result = get_employees()
    print(Fore.RED, result)
    print(Back.GREEN, result)
    print(Style.RESET_ALL)