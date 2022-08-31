def calculate_salary(salary_month: int, day: int =20, hours_day: int =8) -> int:
    payment_hours  = round((salary_month / day) / hours_day, 2)
    return payment_hours 