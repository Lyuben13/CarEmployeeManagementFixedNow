import os

DB_FOLDER = 'db'
EMPLOYEE_DB_PATH = os.path.join(DB_FOLDER, 'employees.csv')
CAR_DB_PATH = os.path.join(DB_FOLDER, 'cars.csv')
SALE_DB_PATH = os.path.join(DB_FOLDER, 'sales.csv')

REPORTS_FOLDER = 'reports'
EMPLOYEES_REPORT_PATH = os.path.join(REPORTS_FOLDER, 'employees_report.txt')
CARS_REPORT_PATH = os.path.join(REPORTS_FOLDER, 'cars_report.txt')
SALES_REPORT_PATH = os.path.join(REPORTS_FOLDER, 'sales_report.txt')
SALES_BY_DATE_REPORT_PATH = os.path.join(REPORTS_FOLDER, 'sales_by_date_report.txt')
SALES_BY_PERIOD_REPORT_PATH = os.path.join(REPORTS_FOLDER, 'sales_by_period_report.txt')
SALES_BY_EMPLOYEE_REPORT_PATH = os.path.join(REPORTS_FOLDER, 'sales_by_employee_report.txt')
BEST_SELLING_CAR_REPORT_PATH = os.path.join(REPORTS_FOLDER, 'best_selling_car_report.txt')
BEST_EMPLOYEE_REPORT_PATH = os.path.join(REPORTS_FOLDER, 'best_employee_report.txt')
TOTAL_PROFIT_REPORT_PATH = os.path.join(REPORTS_FOLDER, 'total_profit_report.txt')
