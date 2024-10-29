import os
import sys

from models.specifics import Employee, Car, Sale

from operations import (
    add_employee, add_car, add_sale, list_employees, list_cars, list_sales,
    delete_employee, delete_car, delete_sale)

from reports import (get_sales_by_date, get_sales_by_period, best_selling_car_for_period, best_employee_for_period,
                     get_sales_by_employee, total_profit_for_period)

"""основната директория на проекта към пътя за търсене на Python (sys.path)."""
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


def main():
    while True:
        print("\nChoose an option:")
        print("1. Add Employee")
        print("2. Add Car")
        print("3. Add Sale")
        print("4. List Employees")
        print("5. List Cars")
        print("6. List Sales")
        print("7. Sales by Date")
        print("8. Sales by Period")
        print("9. Sales by Employee")
        print("10. Best-selling Car for Period")
        print("11. Best Employee for Period")
        print("12. Total Profit for Period")
        print("13. Delete Employee")
        print("14. Delete Car")
        print("15. Delete Sale")
        print("16. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            full_name = input("Enter employee full name: ")
            job_position = input("Enter job position: ")
            contact_number = input("Enter contact number: ")
            email = input("Enter email: ")
            add_employee(Employee(full_name, job_position, contact_number, email))

        elif choice == '2':
            manufacturer = input("Enter car manufacturer: ")
            year = input("Enter year of manufacture: ")
            model = input("Enter car model: ")
            cost_price = input("Enter cost price: ")
            sale_price = input("Enter sale price: ")
            add_car(Car(manufacturer, year, model, cost_price, sale_price))

        elif choice == '3':
            employee = input("Enter employee name: ")
            car = input("Enter car model: ")
            date_of_sale = input("Enter date of sale (YYYY-MM-DD): ")
            actual_selling_price = input("Enter actual selling price: ")
            add_sale(Sale(employee, car, date_of_sale, actual_selling_price))

        elif choice == '4':
            employees = list_employees()
            if employees:
                for e in employees:
                    print(e)
                save_choice = input("\nDo you want to save the report in a text file? (yes/no): ").strip().lower()
                if save_choice == 'yes':
                    with open("reports/employees_report.txt", 'w') as file:
                        for e in employees:
                            file.write(f"{e}\n")
                    print("Report saved as 'employees_report.txt'.")
            else:
                print("No employees found.")

        elif choice == '5':
            cars = list_cars()
            if cars:
                for c in cars:
                    print(c)
                save_choice = input("\nDo you want to save the report in a text file? (yes/no): ").strip().lower()
                if save_choice == 'yes':
                    with open("reports/cars_report.txt", 'w') as file:
                        for c in cars:
                            file.write(f"{c}\n")
                    print("Report saved as 'cars_report.txt'.")
            else:
                print("No cars found.")

        elif choice == '6':
            sales = list_sales()
            if sales:
                for s in sales:
                    print(s)
                save_choice = input("\nDo you want to save the report in a text file? (yes/no): ").strip().lower()
                if save_choice == 'yes':
                    with open("reports/sales_report.txt", 'w') as file:
                        for s in sales:
                            file.write(f"{s}\n")
                    print("Report saved as 'sales_report.txt'.")
            else:
                print("No sales found.")

        elif choice == '7':
            specific_date = input("Enter date (YYYY-MM-DD): ")
            sales = get_sales_by_date(specific_date)
            if sales:
                for sale in sales:
                    print(sale)
                save_choice = input("\nDo you want to save the report in a text file? (yes/no): ").strip().lower()
                if save_choice == 'yes':
                    filename = f"reports/sales_{specific_date}.txt"
                    with open(filename, 'w') as file:
                        for sale in sales:
                            file.write(f"{sale}\n")
                    print(f"Report saved as '{filename}'.")
            else:
                print(f"No sales found for {specific_date}.")

        elif choice == '8':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            sales = get_sales_by_period(start_date, end_date)
            if sales:
                for sale in sales:
                    print(sale)
                save_choice = input("\nDo you want to save the report in a text file? (yes/no): ").strip().lower()
                if save_choice == 'yes':
                    filename = f"reports/sales_{start_date}_to_{end_date}.txt"
                    with open(filename, 'w') as file:
                        for sale in sales:
                            file.write(f"{sale}\n")
                    print(f"Report saved as '{filename}'.")
            else:
                print(f"No sales found for the period from {start_date} to {end_date}.")

        elif choice == '9':
            employee_name = input("Enter employee name: ")
            sales = get_sales_by_employee(employee_name)
            if sales:
                for sale in sales:
                    print(sale)
                save_choice = input("Do you want to save the report in a text file? (yes/no): ").strip().lower()
                if save_choice == 'yes':
                    filename = f"reports/{employee_name.replace(' ', '_')}_sales_report.txt"
                    with open(filename, 'w') as file:
                        for sale in sales:
                            file.write(f"{sale}\n")
                    print(f"Report saved as '{filename}'.")
            else:
                print(f"No sales found for {employee_name}.")

        elif choice == '10':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            best_car = best_selling_car_for_period(start_date, end_date)
            print(f"Best-selling car: {best_car}")

        elif choice == '11':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            best_employee = best_employee_for_period(start_date, end_date)
            print(f"Best employee: {best_employee}")

        elif choice == '12':
            start_date = input("Enter start date (YYYY-MM-DD): ")
            end_date = input("Enter end date (YYYY-MM-DD): ")
            profit = total_profit_for_period(start_date, end_date)
            print(f"Total profit: {profit}")

        elif choice == '13':
            employee_name = input("Enter employee name to delete: ")
            delete_employee(employee_name)

        elif choice == '14':
            car_model = input("Enter car model to delete: ")
            delete_car(car_model)

        elif choice == '15':
            employee_name = input("Enter employee name: ")
            car_model = input("Enter car model: ")
            delete_sale(employee_name, car_model)

        elif choice == '16':
            confirm_exit = input("Are you sure you want to exit? (y/n): ").lower()
            if confirm_exit == 'y':
                print("Exiting...")
                break
            else:
                print("Returning to menu...")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print("Lyuben Andreev variant 1(Car dealership app) -> ")
    main()
