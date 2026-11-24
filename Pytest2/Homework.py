from unittest.mock import Mock, MagicMock

import pytest
import os
from pathlib import Path
import pytest_mock
from app import process_files, read_config, generate_password

#1.1 Простая фикстура с данными
@pytest.fixture(scope="function", autouse=True)
def book_data():
    return {"title": "1984", "author": "George Orwell", "pages": 328}

def test_book_pages(book_data):
    assert book_data["pages"] > 300


#1.2 Жизненный цикл (Setup / Teardown)
@pytest.fixture(scope="function", autouse=True)
def temp_list():
    temp = [1, 2, 3]
    yield temp
    temp.clear()

def test_temp_list(temp_list):
    temp_list.append(4)
    assert len(temp_list) == 4


#1.3 Вызов через @pytest.mark.usefixtures
@pytest.mark.usefixtures("env_setup")
def test_app_mode():
    assert os.environ["APP_MODE"] == "testing"

#1.4 Цепочка зависимостей
@pytest.fixture(scope="function", autouse=True)
def base_url():
    return "https://example.com"

@pytest.fixture(scope="function", autouse=True)
def users_endpoint(base_url):
    return f"{base_url}/users"

def test_users_endpoint(users_endpoint):
    assert users_endpoint == "https://example.com/users"

#Задание 1.5. Параметризация фикстуры (params)
def test_is_even(number):
    assert number % 2 == 0

#Задание 1.6. Встроенная фикстура tmp_path
def test_create_file(tmp_path):
    with open(f"{tmp_path}/hello.txt", "w", encoding="UTF-8") as f:
        f.writelines("Pytest is awesome")
    assert Path(f"{tmp_path}/hello.txt").is_file()

    with open(f"{tmp_path}/hello.txt", "r", encoding="UTF-8") as r:
        string = r.read()
    assert string == "Pytest is awesome"

#Задание 2.1 Мок времени (time.sleep)

def test_process_files(mocker):
    mock = mocker.patch('app.time.sleep')

    result = process_files()
    assert result == "processed"

    mock.assert_called_once_with(3)

#Задание 2.2: Мок чтения файла (open)
def test_read_config(mocker):
    mock_open = mocker.patch('app.open')

    mock_file = MagicMock()
    mock_file.read.return_value = "host=localhost"

    mock_file.__enter__.return_value = mock_file
    mock_open.return_value = mock_file

    result = read_config('config.txt')

    assert result == "host=localhost"
    mock_open.assert_called_once_with('config.txt', 'r')


#Задание 2.3: Мок случайных чисел (random)
def test_generate_password(mocker):
    mock_get = mocker.patch('app.random.choice', side_effect = ["a", "a", "a", "a", "b", "b", "b", "b"])
    result = generate_password()

    assert result == "aaaabbbb"
    assert mock_get.call_count == 8
