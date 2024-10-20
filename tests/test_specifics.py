import unittest
from unittest.mock import patch, MagicMock # noqa
from models.specifics import Employee, Car, Sale


class TestEmployee(unittest.TestCase):
    @patch('models.specifics.Employee.to_dict', return_value={'full_name': 'Mocked Name'})
    def test_employee(self, mock_to_dict):
        """Тест за класа Employee с mock"""
        full_name = 'L.A.'
        job_position = 'Developer'
        contact_number = '08981234567'
        email = 'LA@example.com'

        employee = Employee(full_name, job_position, contact_number, email)

        # Проверка дали е извикан метода to_dict
        employee_dict = employee.to_dict()
        mock_to_dict.assert_called_once()  # Проверяваме дали to_dict е извикан веднъж

        # Проверка на резултата от mock
        expected_dict = {'full_name': 'Mocked Name'}
        self.assertEqual(employee_dict, expected_dict)


class TestCar(unittest.TestCase):
    @patch('models.specifics.Car.to_dict', return_value={'manufacturer': 'Mocked Manufacturer'})
    def test_car(self, mock_to_dict):
        """Тест за класа Car с mock"""
        manufacturer = 'Nissan'
        year = 1997
        model = 'Premiera'
        cost_price = 1700
        sale_price = 2100

        car = Car(manufacturer, year, model, cost_price, sale_price)

        # Проверка дали е извикан метода to_dict
        car_dict = car.to_dict()
        mock_to_dict.assert_called_once()  # Проверяваме дали to_dict е извикан веднъж

        # Проверка на резултата от mock
        expected_dict = {'manufacturer': 'Mocked Manufacturer'}
        self.assertEqual(car_dict, expected_dict)


class TestSale(unittest.TestCase):
    @patch('models.specifics.Sale.to_dict', return_value={'employee': 'Mocked Employee'})
    def test_sale(self, mock_to_dict):
        """Тест за класа Sale с mock"""
        employee = Employee("Lyuben Andreev", "Manager", "08881234567", "lyuben@example.com")
        car = Car("Premiera", 2024, "Premiera", 1800, 2100)
        date_of_sale = "2024-01-03"
        actual_selling_price = 2100

        sale = Sale(employee, car, date_of_sale, actual_selling_price)

        # Проверка дали е извикан метода to_dict
        sale_dict = sale.to_dict()
        mock_to_dict.assert_called_once()  # Проверяваме дали to_dict е извикан веднъж

        # Проверка на резултата от mock
        expected_dict = {'employee': 'Mocked Employee'}
        self.assertEqual(sale_dict, expected_dict)


if __name__ == '__main__':
    unittest.main()
