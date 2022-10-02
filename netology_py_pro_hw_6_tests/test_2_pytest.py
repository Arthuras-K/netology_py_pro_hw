import yaml
import pytest
import cf_yandex


def test_create_folder():        
    with open('netology_py_pro_hw_6_tests\config.yaml') as f:
        config = yaml.safe_load(f)
        TOKEN_YD = config['token_yd'] # Токен от Яндекс.Диск

    etalon = 201
    result = cf_yandex.create_folder(TOKEN_YD, "test_folder777")
    assert result == etalon


# команда для запуска тестов:  pytest -v netology_py_pro_hw_6_tests\test_2_pytest.py