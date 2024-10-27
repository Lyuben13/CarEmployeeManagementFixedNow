import pytest # noqa
from unittest.mock import patch, MagicMock
from reports import (get_sales_by_date, get_sales_by_period, get_sales_by_employee,
                     sales_by_employee, best_selling_car_for_period, best_employee_for_period,
                     total_profit_for_period, save_report) # noqa
from datetime import datetime # noqa

# Примерни фиктивни данни за продажби и автомобили
sample_sales = [
    MagicMock(car="Toyota", date_of_sale="2023-10-10", actual_selling_price="15000", employee="John"),
    MagicMock(car="Honda", date_of_sale="2023-10-11", actual_selling_price="12000", employee="Alice"),
    MagicMock(car="Toyota", date_of_sale="2023-10-10", actual_selling_price="16000", employee="John"),
]

sample_cars = [
    MagicMock(model="Toyota", cost_price="10000"),
    MagicMock(model="Honda", cost_price="8000")
]

# Тест за get_sales_by_date
@patch('reports.list_sales', return_value=sample_sales)
def test_get_sales_by_date(mock_list_sales):
    specific_date = "2023-10-10"
    result = get_sales_by_date(specific_date)
    assert len(result) == 2
    assert all(sale.date_of_sale == specific_date for sale in result)

# Тест за get_sales_by_period
@patch('reports.list_sales', return_value=sample_sales)
def test_get_sales_by_period(mock_list_sales):
    start_date = "2023-10-10"
    end_date = "2023-10-11"
    result = get_sales_by_period(start_date, end_date)
    assert len(result) == 3

# Тест за get_sales_by_employee
@patch('reports.list_sales', return_value=sample_sales)
def test_get_sales_by_employee(mock_list_sales):
    employee_name = "John"
    result = get_sales_by_employee(employee_name)
    assert len(result) == 2
    assert all(sale.employee == employee_name for sale in result)

# Тест за best_selling_car_for_period
@patch('reports.list_sales', return_value=sample_sales)
def test_best_selling_car_for_period(mock_list_sales):
    start_date = "2023-10-10"
    end_date = "2023-10-11"
    result = best_selling_car_for_period(start_date, end_date, save_to_file=False)
    assert result == "Toyota"  # Toyota е най-продаваният автомобил

# Тест за best_employee_for_period
@patch('reports.list_sales', return_value=sample_sales)
def test_best_employee_for_period(mock_list_sales):
    start_date = "2023-10-10"
    end_date = "2023-10-11"
    result = best_employee_for_period(start_date, end_date, save_to_file=False)
    assert result == "John"  # John е с най-много продажби

# Тест за total_profit_for_period
@patch('reports.list_sales', return_value=sample_sales)
@patch('reports.list_cars', return_value=sample_cars)
def test_total_profit_for_period(mock_list_sales, mock_list_cars):
    start_date = "2023-10-10"
    end_date = "2023-10-11"
    result = total_profit_for_period(start_date, end_date, save_to_file=False)
    expected_profit = (15000 - 10000) + (12000 - 8000) + (16000 - 10000)
    assert result == expected_profit  # Проверяваме дали печалбата е изчислена правилно

# Тест за sales_by_employee с опция за записване
@patch('reports.get_sales_by_employee', return_value=sample_sales)
@patch('reports.prompt_save_report')
def test_sales_by_employee(mock_prompt_save_report, mock_get_sales_by_employee):
    employee_name = "John"
    sales_by_employee(employee_name, save_to_file=True)
    mock_prompt_save_report.assert_called_once()
