from customer import Customer
import csv

class CustomerRepository:
    def read_customers(self) -> list[Customer]:
        customers = []
        try:
            with open("customers.csv", "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    # Ensure that each row has exactly 4 elements by filling missing ones
                    first_name = row[0] if len(row) > 0 else ""
                    last_name = row[1] if len(row) > 1 else ""
                    account_number = row[2] if len(row) > 2 else ""
                    balance = float(row[3]) if len(row) > 3 else 0.0
                    customer = Customer(first_name, last_name, account_number, balance)
                    customers.append(customer)
        except FileNotFoundError:
            pass  # File will be created when the first customer is added
        return customers

    def save_customers(self, customers: list[Customer]) -> None:
        with open("customers.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)
            for customer in customers:
                writer.writerow(customer.tolist())

    def add_customer(self, customer: Customer) -> None:
        with open("customers.csv", "a", newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(customer.tolist())
