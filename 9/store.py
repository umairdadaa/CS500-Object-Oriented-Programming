from customer import Customer
from customer_repository import CustomerRepository

class Store:
    def __init__(self, store_name: str) -> None:
        self._store_name = store_name
        self._repository = CustomerRepository()
        self._customers = self._repository.read_customers()

    def display_customers(self) -> None:
        for customer in self._customers:
            print(customer)

    def add_customer(self, firstname: str, lastname: str, account_number: str, balance: float) -> None:
        new_customer = Customer(firstname, lastname, account_number, balance)
        self._customers.append(new_customer)
        self._repository.add_customer(new_customer)
        print(f"Customer {firstname} {lastname} added successfully!")

    def search_customer_by_last_name(self, lastname: str) -> None:
        found = [customer for customer in self._customers if customer.last_name == lastname]
        for customer in found:
            print(customer)

    def edit_customer(self, account_number: str) -> None:
        for customer in self._customers:
            if customer.account_number == account_number:
                customer.first_name = input("Enter new first name: ")
                customer.last_name = input("Enter new last name: ")
                customer.balance = float(input("Enter new balance: "))
                self._repository.save_customers(self._customers)
                print("Customer information updated successfully!")
                return
        print("Customer not found.")

    def delete_customer(self, account_number: str) -> None:
        self._customers = [c for c in self._customers if c.account_number != account_number]
        self._repository.save_customers(self._customers)
        print("Customer deleted successfully.")

    def find_highest_balance(self) -> None:
        highest = max(self._customers, key=lambda c: c.balance, default=None)
        print(f"Customer with highest balance: {highest}")

    def find_lowest_balance(self) -> None:
        lowest = min(self._customers, key=lambda c: c.balance, default=None)
        print(f"Customer with lowest balance: {lowest}")
