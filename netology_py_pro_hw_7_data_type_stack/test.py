import pytest
from main import check_balance


fixture = [
    ('{()[]}', 'Сбалансированно'),
    ('[](([]()){})', 'Сбалансированно'),
    ('(([)])', 'Несбалансированно'),
    ('({}[]))', 'Несбалансированно')
]


@ pytest.mark.parametrize('example, etalon', fixture)
def test_check_balance(example, etalon):        
    result = check_balance(example)
    assert result == etalon


# команда для запуска тестов:  pytest -v test.py