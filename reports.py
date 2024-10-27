from loguru import logger
import os
from datetime import datetime
from app_config import REPORTS_FOLDER
from operations import list_cars, list_sales
import time

# Конфигурация на логовете
logger.remove()
logger.add("app.log", rotation="1 MB", level="INFO", backtrace=True, diagnose=True)

def ensure_folder_exists(folder_path):
    """Проверява дали съществува папката, ако не съществува, я създава.""" # noqa
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        logger.info(f"Created folder: {folder_path}")

def save_report(report_content, report_path):
    """Запазва съдържанието на отчет във файл на посочения път.""" # noqa
    ensure_folder_exists(REPORTS_FOLDER)
    with open(report_path, mode='w') as file:
        file.write(report_content)
    logger.info(f"Report saved as '{report_path}'")
    print("Report successfully saved!\n")

def get_sales_by_date(specific_date):
    """Връща списък от продажби за конкретна дата.""" # noqa
    sales = list_sales()
    specific_sales = [sale for sale in sales if sale.date_of_sale == specific_date]
    logger.info(f"Sales on {specific_date}: {specific_sales}")
    return specific_sales

def get_sales_by_period(start_date, end_date):
    """Връща продажби за даден период от време, след проверка на валидността на датите.""" # noqa
    try:
        sales = list_sales()
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        period_sales = [sale for sale in sales if start <= datetime.strptime(sale.date_of_sale, '%Y-%m-%d') <= end]
        logger.info(f"Sales from {start_date} to {end_date}: {period_sales}")
        return period_sales
    except ValueError:
        # Грешка при невалиден формат на датата
        logger.error(f"Invalid date format for period: {start_date} to {end_date}")
        print("Error: Invalid date format. Please use YYYY-MM-DD.\n")
        return []

def get_sales_by_employee(employee_name):
    """Връща всички продажби, извършени от конкретен служител.""" # noqa
    sales = list_sales()
    employee_sales = [sale for sale in sales if sale.employee == employee_name]
    logger.info(f"Sales by {employee_name}: {employee_sales}")
    return employee_sales

def prompt_save_report(report_content, report_name):
    """Подканва потребителя да избере дали да запази отчета във файл.""" # noqa
    should_save = input("Do you want to save this report? (yes/no): ").strip().lower()
    if should_save == 'yes':
        save_report(report_content, os.path.join(REPORTS_FOLDER, report_name))
    else:
        logger.info("User chose not to save the report.")
        print("Report not saved.\n")

def sales_by_employee(employee_name, save_to_file=False):
    """Генерира отчет за продажбите на конкретен служител и запазва отчета по желание на потребителя.""" # noqa
    sales = get_sales_by_employee(employee_name)
    report = f"Sales by {employee_name}:\n"
    if sales:
        for sale in sales:
            report += f"Car: {sale.car}, Date: {sale.date_of_sale}, Price: {sale.actual_selling_price}\n"
    else:
        report += "No sales found for this employee."
    print(report)
    logger.info(report)
    time.sleep(0.1)

    if save_to_file:
        prompt_save_report(report, f"sales_report_by_{employee_name}.txt")
    return sales

def best_selling_car_for_period(start_date, end_date, save_to_file=True):
    """Намира най-продаваната кола за даден период и запазва отчета, ако е избрано.""" # noqa
    sales = get_sales_by_period(start_date, end_date)
    car_sales = {}
    for sale in sales:
        car_sales[sale.car] = car_sales.get(sale.car, 0) + 1
    if car_sales:
        best_car = max(car_sales, key=car_sales.get)
        report = (f"Best selling car for the period from {start_date} to {end_date}: {best_car} "
                  f"(sold {car_sales[best_car]} times)")
    else:
        report = f"No car sales found for the period from {start_date} to {end_date}."
    print(report)
    logger.info(report)
    time.sleep(0.1)

    if save_to_file:
        prompt_save_report(report, f"best_selling_car_{start_date}_to_{end_date}.txt")
    return best_car if car_sales else None # noqa

def best_employee_for_period(start_date, end_date, save_to_file=True):
    """Намира служителя с най-много продажби за даден период и запазва отчета, ако е избрано.""" # noqa
    sales = get_sales_by_period(start_date, end_date)
    employee_sales = {}
    for sale in sales:
        employee_sales[sale.employee] = employee_sales.get(sale.employee, 0) + 1
    if employee_sales:
        best_employee = max(employee_sales, key=employee_sales.get)
        best_employee_sales_count = employee_sales[best_employee]
        report = f"Best employee for the period from {start_date} to {end_date}: {best_employee} (made {best_employee_sales_count} sales)" # noqa
    else:
        report = f"No sales found for the period from {start_date} to {end_date}."
    print(report)
    logger.info(report)
    time.sleep(0.1)

    if save_to_file:
        prompt_save_report(report, f"best_employee_{start_date}_to_{end_date}.txt")
    return best_employee if employee_sales else None # noqa

def total_profit_for_period(start_date, end_date, save_to_file=True):
    """Изчислява общата печалба за даден период и запазва отчета, ако е избрано.""" # noqa
    sales = get_sales_by_period(start_date, end_date)
    total_profit = 0.0
    cars = {car.model: car for car in list_cars()}
    for sale in sales:
        car = cars.get(sale.car)
        if car:
            try:
                selling_price = float(sale.actual_selling_price)
                cost_price = float(car.cost_price)
                total_profit += (selling_price - cost_price)
            except (ValueError, TypeError) as e:
                # Грешка при конвертиране на цените
                logger.error(f"Error processing sale {sale}: {e}")
    report = f"Total profit for the period from {start_date} to {end_date}: {total_profit:.2f}"
    print(report)
    logger.info(report)
    time.sleep(0.1)

    if save_to_file:
        prompt_save_report(report, f"profit_report_{start_date}_to_{end_date}.txt")
    return total_profit
