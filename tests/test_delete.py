import os
import unittest
from unittest.mock import patch, mock_open, MagicMock

from operations import delete_employee


class TestDeleteEmployee(unittest.TestCase):
    # Декориране на метода с patch за симулиране на отваряне на файл
    @patch('operations.open', new_callable=mock_open,
           read_data="full_name,job_position,contact_number,email\nJohn Doe,Manager,123456789,"
                     "johndoe@example.com\nJane Smith,Engineer,987654321,janesmith@example.com")
    @patch('operations.os.path.exists', return_value=True)  # Симулирайте, че файлът съществува
    @patch('operations.csv.DictWriter')  # Симулирайте DictWriter от CSV
    @patch('operations.list_employees')  # Симулирайте функцията list_employees
    def test_delete_employee(self, mock_list_employees, mock_dict_writer, mock_exists, mock_open):  # noqa
        # Симулирайте list_employees, за да върне списък с служители
        mock_list_employees.return_value = [
            MagicMock(full_name="John Doe", job_position="Manager", contact_number="123456789",
                      email="johndoe@example.com"),
            MagicMock(full_name="Jane Smith", job_position="Engineer", contact_number="987654321",
                      email="janesmith@example.com")
        ]

        # Извикване на функцията с името на служителя, който трябва да бъде изтрит
        delete_employee("John Doe")

        # Проверка дали е извикана функцията list_employees
        mock_list_employees.assert_called_once()

        # Проверка дали методът open е извикан за запис на новите данни след изтриването
        mock_open.assert_called_with(os.path.join('db', 'employees.csv'), mode='w', newline='')

        # Получаване на mock обекта на writer
        writer = mock_dict_writer.return_value

        # Проверка дали методът writeheader на DictWriter е извикан веднъж
        writer.writeheader.assert_called_once()

        # Проверка дали методът writerow на DictWriter е извикан с данните на оставащия служител
        writer.writerow.assert_called_once_with({
            'full_name': 'Jane Smith',
            'job_position': 'Engineer',
            'contact_number': '987654321',
            'email': 'janesmith@example.com'
        })


if __name__ == '__main__':
    unittest.main()  # Изпълнение на тестовете
