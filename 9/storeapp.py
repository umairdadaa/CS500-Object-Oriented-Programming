from customer import Customer
from store import Store

class StoreApp:
    def __init__(self, store_name: str) -> None:
        self.__store = Store(store_name)

    def show_menu(self) -> None:
        print("\nMenu:")
        print("1. Print all customers")
        print("2. Add new customer")
        print("3. Search customer by last name")
        print("4. Search and edit customer information")
        print("5. Delete customer record")
        print("6. Find customer with highest balance")
        print("7. Find customer with lowest balance")
        print("10. Exit")
        print("Please enter your option: ", end="")

    def main(self) -> None:
        while True:
            self.show_menu()
            option = int(input())
            if option == 1:
                self.__store.display_customers()
            elif option == 2:
                firstname = input("Enter customer's first name: ")
                lastname = input("Enter customer's last name: ")
                account_number = input("Enter account number/ID: ")
                balance = float(input("Enter customer's balance: "))
                self.__store.add_customer(firstname, lastname, account_number, balance)
            elif option == 3:
                lastname = input("Enter last name to search: ")
                self.__store.search_customer_by_last_name(lastname)
            elif option == 4:
                account_number = input("Enter account number to edit: ")
                self.__store.edit_customer(account_number)
            elif option == 5:
                account_number = input("Enter account number to delete: ")
                self.__store.delete_customer(account_number)
            elif option == 6:
                self.__store.find_highest_balance()
            elif option == 7:
                self.__store.find_lowest_balance()
            elif option == 10:
                break

if __name__ == "__main__":
    app = StoreApp("SFBU Store")
    app.main()
