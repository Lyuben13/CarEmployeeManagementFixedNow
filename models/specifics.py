class Employee:
    def __init__(self, full_name, job_position, contact_number, email):
        self.full_name = full_name
        self.job_position = job_position
        self.contact_number = contact_number
        self.email = email

    def to_dict(self):
        return {
            'full_name': self.full_name,
            'job_position': self.job_position,
            'contact_number': self.contact_number,
            'email': self.email
        }

    def __str__(self):
        return f"{self.full_name}, {self.job_position}, {self.contact_number}, {self.email}"


class Car:
    def __init__(self, manufacturer, year, model, cost_price, sale_price):
        self.manufacturer = manufacturer
        self.year = year
        self.model = model
        self.cost_price = cost_price
        self.sale_price = sale_price

    def to_dict(self):
        return {
            'manufacturer': self.manufacturer,
            'year': self.year,
            'model': self.model,
            'cost_price': self.cost_price,
            'sale_price': self.sale_price
        }

    def __str__(self):
        return f"{self.manufacturer}, {self.year}, {self.model}, Cost: {self.cost_price}, Sale: {self.sale_price}"


class Sale:
    def __init__(self, employee, car, date_of_sale, actual_selling_price):
        self.employee = employee
        self.car = car
        self.date_of_sale = date_of_sale
        self.actual_selling_price = actual_selling_price

    def to_dict(self):
        return {
            'employee': self.employee,
            'car': self.car,
            'date_of_sale': self.date_of_sale,
            'actual_selling_price': self.actual_selling_price
        }

    def __str__(self):
        return f"Employee: {self.employee}, Car: {self.car}, Date: {self.date_of_sale}, Price: {self.actual_selling_price}"
