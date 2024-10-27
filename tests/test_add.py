from pathlib import Path
import unittest
from unittest.mock import patch, mock_open
from operations import add_employee, add_car, add_sale  # Импортиране на функциите.
from models.specifics import Employee, Car, Sale  # Импортиране на класовете.
from loguru import logger

# Конфигуриране на Loguru
logger.add("file.log", rotation="1 MB", level="INFO", backtrace=True, diagnose=True)


class TestOperations(unittest.TestCase):

    @patch('app_config.EMPLOYEE_DB_PATH', new_callable=lambda: Path('db/employees.csv'))  # Път до базата данни
    @patch('builtins.open', new_callable=mock_open)  # Мокване на open() за операции с файлове
    @patch('csv.DictWriter.writerow')  # Мокване на DictWriter
    def test_add_employee(self, mock_writerow, mock_file, mock_db_path):  # noqa
        # Създаване на тестов служител
        employee = Employee("L.A.", "Developer", "08981234567", "LA@example.com")

        logger.info("Testing adding employee...")  # Логване на теста
        # Извикване на функцията за добавяне на служител
        add_employee(employee)

        # Assert: Проверка дали отварянето е извикано с правилния път и режим
        mock_file.assert_called_once_with(str(Path('db/employees.csv')), mode='a', newline='')

        # Assert: Проверка на извикванията на writerow
        expected_employee_data = {
            'full_name': 'L.A.',
            'job_position': 'Developer',
            'contact_number': '08981234567',
            'email': 'LA@example.com'
        }
        mock_writerow.assert_has_calls([unittest.mock.call(expected_employee_data)])

        logger.info("Successfully added employee: {}", employee.full_name)  # Логване на успешното добавяне

    @patch('app_config.CAR_DB_PATH', new_callable=lambda: Path('db/cars.csv'))  # Път до базата данни
    @patch('builtins.open', new_callable=mock_open)  # Мокване на open() за операции с файлове
    @patch('csv.DictWriter.writerow')  # Мокване на DictWriter
    def test_add_car(self, mock_writerow, mock_file, mock_db_path):  # noqa
        # Създаване на тестова кола
        car = Car("Toyota", "2020", "Corolla", "20000", "22000")

        logger.info("Testing adding car...")  # Логване на теста
        # Извикване на функцията за добавяне на кола
        add_car(car)

        # Assert: Проверка дали отварянето е извикано с правилния път и режим
        mock_file.assert_called_once_with(str(Path('db/cars.csv')), mode='a', newline='')

        # Assert: Проверка на извикванията на writerow
        expected_car_data = {
            'manufacturer': 'Toyota',
            'year': '2020',
            'model': 'Corolla',
            'cost_price': '20000',
            'sale_price': '22000'
        }
        mock_writerow.assert_has_calls([unittest.mock.call(expected_car_data)])

        logger.info("Successfully added car: {} {}", car.manufacturer, car.model)  # Логване на успешното добавяне

    @patch('app_config.SALE_DB_PATH', new_callable=lambda: Path('db/sales.csv'))  # Път до базата данни
    @patch('builtins.open', new_callable=mock_open)  # Мокване на open() за операции с файлове
    @patch('csv.DictWriter.writerow')  # Мокване на DictWriter
    def test_add_sale(self, mock_writerow, mock_file, mock_db_path):  # noqa
        # Създаване на тестова продажба
        sale = Sale("Lyuben Andreev", "Premiera", "2024-01-03", "2100")

        logger.info("Testing adding sale...")  # Логване на теста
        # Извикване на функцията за добавяне на продажба
        add_sale(sale)

        # Assert: Проверка дали отварянето е извикано с правилния път и режим
        mock_file.assert_called_once_with(str(Path('db/sales.csv')), mode='a', newline='')

        # Assert: Проверка на извикванията на writerow
        expected_sale_data = {
            'employee': 'Lyuben Andreev',
            'car': 'Premiera',
            'date_of_sale': '2024-01-03',
            'actual_selling_price': '2100'
        }
        mock_writerow.assert_has_calls([unittest.mock.call(expected_sale_data)])

        logger.info("Successfully added sale: {}, for car: {}", sale.employee, sale.car)  # Логване на успешното
        # добавяне


if __name__ == '__main__':
    unittest.main()
