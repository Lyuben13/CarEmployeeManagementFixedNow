from unittest.mock import mock_open, patch
from operations import list_employees, EMPLOYEE_DB_PATH


# Тест за функцията list_employees, когато базата данни е празна
def test_list_employees_empty_db():
    # Симулирайте отварянето на файл с празно съдържание
    with patch('builtins.open', mock_open(read_data='')) as mock_file: # noqa
        # Симулирайте функцията os.path.exists
        with patch('os.path.exists') as mock_exists:
            mock_exists.return_value = True  # Файлът съществува
            employees = list_employees()  # Извикване на функцията
            assert employees == []  # Проверка дали върнатата стойност е празен списък
            mock_file.assert_called_once_with(EMPLOYEE_DB_PATH, mode='r')  # Проверка дали файлът е отворен правилно


# Тест за функцията list_employees, когато файлът не съществува
def test_list_employees_nonexistent_file():
    # Симулирайте функцията os.path.exists
    with patch('os.path.exists') as mock_exists:
        mock_exists.return_value = False  # Файлът не съществува
        employees = list_employees()  # Извикване на функцията
        assert employees == []  # Проверка дали върнатата стойност е празен списък


# Тест за функцията list_employees с неправилно форматирани данни
def test_list_employees_malformed_data():
    # Неправилно форматирани CSV данни
    mock_csv_data = """full_name,job_position,contact_number,email
John Doe,Manager,1234567890,john.doe@example.com
Jane Smith,Salesperson
"""
    # Симулирайте отварянето на файл с неправилно форматирано съдържание
    with patch('builtins.open', mock_open(read_data=mock_csv_data)):
        # Симулирайте функцията os.path.exists
        with patch('os.path.exists') as mock_exists:
            mock_exists.return_value = True  # Файлът съществува
            employees = list_employees()  # Извикване на функцията

            # Проверка дали служителят "John Doe" е в списъка на върнатите служители
            assert any(emp.full_name == "John Doe" for emp in employees)
