from datetime import datetime

from operations import list_cars, list_sales


# 6. Функция за продажби по дата
def get_sales_by_date(specific_date):
    sales = list_sales()  # Получаване на списъка с продажби
    sales_on_date = [sale for sale in sales if sale.date_of_sale == specific_date]  # Филтриране по дата
    return sales_on_date  # Връщане на продажбите на конкретната дата


# 7. Функция за продажби по период
def get_sales_by_period(start_date, end_date):
    sales = list_sales()  # Получаване на списъка с продажби
    filtered_sales = []  # Списък за филтрираните продажби
    start = datetime.strptime(start_date, '%Y-%m-%d')  # Конвертиране на началната дата
    end = datetime.strptime(end_date, '%Y-%m-%d')  # Конвертиране на крайната дата

    # Филтриране на продажбите по дати
    for sale in sales:
        sale_date = datetime.strptime(sale.date_of_sale, '%Y-%m-%d')
        if start <= sale_date <= end:
            filtered_sales.append(sale)

    return filtered_sales  # Връщане на филтрираните продажби


# 8. Функция за продажби от служител
def get_sales_by_employee(employee_name):
    sales = list_sales()  # Получаване на списъка с продажби
    employee_sales = [sale for sale in sales if sale.employee == employee_name]  # Филтриране по служител
    return employee_sales  # Връщане на продажбите на конкретния служител


def sales_by_employee(employee_name):
    sales = get_sales_by_employee(employee_name)
    report = f"Sales by {employee_name}:\n"

    if sales:
        for sale in sales:
            report += f"Car: {sale.car}, Date: {sale.date_of_sale}, Price: {sale.actual_selling_price}\n"
    else:
        report += "No sales found for this employee."

    print(report)

    # Запитване за запазване на отчета
    save_choice = input("Do you want to save the report in a text file? (yes/no): ").strip().lower()
    if save_choice == 'yes':
        with open(f"sales_report_by_{employee_name}.txt", mode='w') as file:
            file.write(report)
        print(f"Report saved as 'sales_report_by_{employee_name}.txt'.")

    return sales  # Връщай резултатите, ако е необходимо


# 9. Функция за най-продаваната кола за период

def best_selling_car_for_period(start_date, end_date):
    sales = get_sales_by_period(start_date, end_date)
    car_sales = {}

    for sale in sales:
        if sale.car in car_sales:
            car_sales[sale.car] += 1
        else:
            car_sales[sale.car] = 1

    if car_sales:
        best_car = max(car_sales, key=car_sales.get)
        report = (f"Best selling car for the period from {start_date} to {end_date}: {best_car} "
                  f"(sold {car_sales[best_car]} times)")
    else:
        report = f"No car sales found for the period from {start_date} to {end_date}."

    print(report)

    save_choice = input("Do you want to save the report in a text file? (yes/no): ").strip().lower()

    if save_choice == 'yes':
        with open("best_selling_car_report.txt", mode='w') as file:
            file.write(report)
        print("Report saved as 'best_selling_car_report.txt'.")
    else:
        print("Report not saved.")

    return best_car  # noqa


# 10. Функция за най-добър служител за период
def best_employee_for_period(start_date, end_date):
    sales = get_sales_by_period(start_date, end_date)
    employee_sales = {}

    # Изчисляване на продажбите за всеки служител
    for sale in sales:
        if sale.employee in employee_sales:
            employee_sales[sale.employee] += 1
        else:
            employee_sales[sale.employee] = 1

    # Намиране на служителя с най-много продажби
    if employee_sales:
        best_employee = max(employee_sales, key=employee_sales.get)
        best_employee_sales_count = employee_sales[best_employee]
        report = f"Best employee for the period from {start_date} to {end_date}: {best_employee} (made {best_employee_sales_count} sales)"  # noqa
    else:
        report = f"No sales found for the period from {start_date} to {end_date}."

    print(report)  # Отпечатваме отчета

    # Пита потребителя дали иска да запази отчета в текстов файл
    save_choice = input("Do you want to save the report in a text file? (yes/no): ").strip().lower()

    if save_choice == 'yes':
        with open("best_employee_report.txt", mode='w') as file:
            file.write(report)
        print("Report saved as 'best_employee_report.txt'.")

    # Връщаме най-добрия служител, или None
    return best_employee if employee_sales else None  # noqa


# 11. Функция за изчисляване на чиста печалба за период
def total_profit_for_period(start_date, end_date):
    sales = get_sales_by_period(start_date, end_date)
    total_profit = 0.0
    cars = {car.model: car for car in list_cars()}

    for sale in sales:
        car = cars.get(sale.car)
        if car:
            try:
                selling_price = float(sale.actual_selling_price)
                cost_price = float(car.cost_price)
                profit = selling_price - cost_price
                total_profit += profit
            except (ValueError, TypeError) as e:
                print(f"Error processing sale {sale}: {e}")

    report = f"Total profit for the period from {start_date} to {end_date}: {total_profit:.2f}"
    print(report)

    # Пита потребителя дали иска да запази отчета в текстов файл
    save_choice = input("Do you want to save the report in a text file? (yes/no): ").strip().lower()

    if save_choice == 'yes':
        with open("total_profit_report.txt", mode='w') as file:
            file.write(report)
        print("Report saved as 'total_profit_report.txt'.")

    # Връщаме резултата, за да няма None, ако не се използва
    return total_profit
