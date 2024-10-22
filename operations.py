from app_config import EMPLOYEE_DB_PATH, CAR_DB_PATH, SALE_DB_PATH
import os
import csv
from models.specifics import Sale, Employee, Car


# Функции за управление на служителите
def add_employee(employee):
    # Проверка дали файлът съществува
    file_exists = os.path.exists(EMPLOYEE_DB_PATH)
    # Отваряне на файла в режим на добавяне
    with open(EMPLOYEE_DB_PATH, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['full_name', 'job_position', 'contact_number', 'email'])
        if not file_exists:
            writer.writeheader()  # Записване на заглавията, ако файлът е нов
        writer.writerow(employee.to_dict())  # Записване на данните за служителя


def list_employees():
    employees = []  # Списък за служителите
    # Проверка дали файлът съществува
    if os.path.exists(EMPLOYEE_DB_PATH):
        # Отваряне на файла в режим на четене
        with open(EMPLOYEE_DB_PATH, mode='r') as file:
            reader = csv.DictReader(file)  # Четене на данните в CSV формат
            for row in reader:
                if isinstance(row, dict):  # Проверка дали row наистина е речник
                    employee = Employee(  # Създаване на обект Employee и добавяне в списъка
                        full_name=row['full_name'],
                        job_position=row['job_position'],
                        contact_number=row['contact_number'],
                        email=row['email']
                    )
                employees.append(employee)
    return employees  # Връщане на списъка с служители


def delete_employee(full_name):
    employees = list_employees()  # Получаване на списъка със служители

    # Проверка дали служителят съществува
    employee_exists = any(e.full_name == full_name for e in employees)
    if not employee_exists:
        print(f"Employee {full_name} not found.")  # Служителят не е намерен
        return

    # Филтриране на служителите, за да се изключи избраният
    employees = [e for e in employees if e.full_name != full_name]

    # Записване на новия списък със служители в CSV файла
    with open(EMPLOYEE_DB_PATH, mode='w', newline='') as file:
        fieldnames = ['full_name', 'job_position', 'contact_number', 'email']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()  # Записване на заглавията

        for employee in employees:
            writer.writerow({
                'full_name': employee.full_name,
                'job_position': employee.job_position,
                'contact_number': employee.contact_number,
                'email': employee.email
            })

    print(f"Employee {full_name} deleted successfully.")  # Успешно изтриване


# Функции за управление на автомобилите
def add_car(car):
    # Проверка дали файлът съществува
    file_exists = os.path.exists(CAR_DB_PATH)
    # Отваряне на файла в режим на добавяне
    with open(CAR_DB_PATH, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['manufacturer', 'year', 'model', 'cost_price', 'sale_price'])
        if not file_exists:
            writer.writeheader()  # Записване на заглавията, ако файлът е нов
        writer.writerow(car.to_dict())  # Записване на данните за колата


def list_cars():
    cars = []  # Списък за автомобилите

    # Проверка дали файлът съществува и дали е празен
    if os.path.exists(CAR_DB_PATH):
        if os.stat(CAR_DB_PATH).st_size == 0:  # Проверка дали файлът е празен
            print("The car database is empty.")
            return cars

        # Отваряне на файла в режим на четене с добавен newline=''
        with open(CAR_DB_PATH, mode='r', newline='') as file:
            reader = csv.DictReader(file)

            # Създаване на обекти Car и добавяне в списъка
            for row in reader:
                # Проверка дали редът съдържа всички необходими полета
                if isinstance(row, dict):  # Проверка дали row наистина е речник
                    if all(key in row for key in ['manufacturer', 'year', 'model', 'cost_price', 'sale_price']):
                        cars.append(Car(
                            row['manufacturer'],
                            row['year'],
                            row['model'],
                            row['cost_price'],
                            row['sale_price']
                        ))
                    else:
                        print(f"Missing data in row: {row}")  # Логване на липсващи данни
    else:
        print(f"File {CAR_DB_PATH} does not exist.")  # Файлът не съществува

    return cars  # Връщане на списъка с автомобили


def delete_car(model):
    cars = list_cars()  # Получаване на списъка с автомобили

    # Проверка дали колата съществува
    car_exists = any(c.model == model for c in cars)
    if not car_exists:
        print(f"No car found with model {model}.")  # Колата не е намерена
        return

    # Филтриране на автомобилите, за да се изключи избраната кола
    cars = [c for c in cars if c.model != model]

    # Записване на новия списък с автомобили в CSV файла
    with open(CAR_DB_PATH, mode='w', newline='') as file:
        fieldnames = ['manufacturer', 'year', 'model', 'cost_price', 'sale_price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()  # Записване на заглавията

        for car in cars:
            writer.writerow({
                'manufacturer': car.manufacturer,
                'year': car.year,
                'model': car.model,
                'cost_price': car.cost_price,
                'sale_price': car.sale_price
            })

    print(f"Car with model {model} deleted successfully.")  # Успешно изтриване


# Функции за управление на продажбите
def add_sale(sale):
    # Проверка дали файлът съществува
    file_exists = os.path.exists(SALE_DB_PATH)
    # Отваряне на файла в режим на добавяне
    with open(SALE_DB_PATH, mode='a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['employee', 'car', 'date_of_sale', 'actual_selling_price'])
        if not file_exists:
            writer.writeheader()  # Записване на заглавията, ако файлът е нов
        writer.writerow(sale.to_dict())  # Записване на данните за продажбата


def list_sales():
    sales = []  # Списък за продажбите
    try:
        # Отваряне на файла в режим на четене
        with open(SALE_DB_PATH, mode='r') as file:
            reader = csv.DictReader(file)  # Четене на данните в CSV формат
            for row in reader:
                if isinstance(row, dict):  # Проверка дали row наистина е речник
                    sale = Sale(  # Създаване на обект Sale и добавяне в списъка
                        employee=row['employee'],
                        car=row['car'],
                        date_of_sale=row['date_of_sale'],
                        actual_selling_price=row['actual_selling_price']
                    )
                sales.append(sale)

    except FileNotFoundError:
        print("Sales file not found.")  # Файлът за продажби не е намерен
    except Exception as e:
        print(f"An error occurred: {e}")  # Обработка на други грешки
    return sales  # Връщане на списъка с продажби


def delete_sale(employee_name, car_model):
    sales = list_sales()  # Получаване на списъка с продажби

    # Проверка дали продажбата съществува
    sale_exists = any(s.employee == employee_name and s.car == car_model for s in sales)
    if not sale_exists:
        print(f"No sale found for employee {employee_name} and car {car_model}.")  # Продажбата не е намерена
        return

    # Филтриране на продажбите, за да се изключи избраната
    sales = [s for s in sales if not (s.employee == employee_name and s.car == car_model)]

    # Записване на новия списък с продажби в CSV файла
    with open(SALE_DB_PATH, mode='w', newline='') as file:
        fieldnames = ['employee', 'car', 'date_of_sale', 'actual_selling_price']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()  # Записване на заглавията

        for sale in sales:
            writer.writerow({
                'employee': sale.employee,
                'car': sale.car,
                'date_of_sale': sale.date_of_sale,
                'actual_selling_price': sale.actual_selling_price
            })

    print(f"Sale for employee {employee_name} and car {car_model} deleted successfully.")  # Успешно изтриване
