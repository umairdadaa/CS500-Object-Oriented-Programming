from state_machine import (State, Event, acts_as_state_machine, after, before, InvalidStateTransition)

@acts_as_state_machine
class VendingProcess:
    idle = State(initial=True)
    coin_inserted = State()
    product_selected = State()
    product_dispensed = State()

    insert_coin = Event(from_states=idle, to_state=coin_inserted)
    return_coin = Event(from_states=coin_inserted, to_state=idle)
    select_product = Event(from_states=coin_inserted, to_state=product_selected)
    dispense_product = Event(from_states=product_selected, to_state=product_dispensed)
    finish_transaction = Event(from_states=product_dispensed, to_state=idle)

    @after('insert_coin')
    def after_insert_coin(self):
        print("Coins inserted. You can now select a product.")

    @after('return_coin')
    def after_return_coin(self):
        print("Coins returned. Returning to idle state.")

    @after('select_product')
    def after_select_product(self):
        print("Product selected. Dispensing product...")

    @after('dispense_product')
    def after_dispense_product(self):
        print("Product dispensed. Collect your item.")

    @after('finish_transaction')
    def after_finish_transaction(self):
        print("Transaction completed. Returning to idle state.")


class VendingMachine:
    def __init__(self):
        self.process = VendingProcess()
        self.balance = 0
        self.products = {
            "soda": 125,
            "chips": 100,
            "candy": 75,
        }

    def insert_coin(self, amount):
        try:
            if amount not in [5, 10, 25, 50]:
                print("Invalid coin. Use 5, 10, 25 or 50 cents.")
                return

            self.balance += amount
            print(f"Inserted {amount} cents. Current balance: {self.balance} cents.")

            if self.process.current_state == self.process.idle:
                self.process.insert_coin()
        except InvalidStateTransition:
            print("Error in state transition, but coin is still added to balance.")

    def return_coin(self):
        try:
            self.process.return_coin()
            print(f"Returning {self.balance} cents.")
            self.balance = 0
        except InvalidStateTransition:
            print("Cannot return coins now.")

    def select_product(self, product_name):
        try:
            if product_name not in self.products:
                print("Invalid product. Please select a valid product (soda, chips, candy).")
                return

            if self.balance < self.products[product_name]:
                print(f"Insufficient balance. {product_name.capitalize()} costs {self.products[product_name]} cents.")
                return

            confirmation = input(f"Are you sure you want {product_name.capitalize()}? (yes/no): ").strip().lower()
            if confirmation != "yes":
                print("Product selection canceled.")
                return

            self.process.select_product()
            self.balance -= self.products[product_name]
            print(f"{product_name.capitalize()} selected. Remaining balance: {self.balance} cents.")
        except InvalidStateTransition:
            print("Cannot select a product now.")

    def dispense_product(self):
        try:
            self.process.dispense_product()
            self.process.finish_transaction()
        except InvalidStateTransition:
            print("Cannot dispense product now.")

    def show_current_balance(self):
        print(f"Current balance: {self.balance} cents.")

    def get_current_state(self):
        return self.process.current_state

def show_menu():
    print("\n-- MENU -- ")
    print("1. Insert Coin")
    print("2. Select Product")
    print("3. Dispense Product")
    print("4. Return Coin")
    print("5. Check Balance")
    print("6. Quit")


def main():
    vending_machine = VendingMachine()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                coin = int(input("Enter coin amount (5, 10, 25, 50): "))
                vending_machine.insert_coin(coin)
            except ValueError:
                print("Invalid input. Please enter a valid coin amount.")
        elif choice == "2":
            vending_machine.show_current_balance()
            product = input("Enter product name (soda, chips, candy): ").lower()
            vending_machine.select_product(product)
        elif choice == "3":
            vending_machine.dispense_product()
        elif choice == "4":
            vending_machine.return_coin()
        elif choice == "5":
            vending_machine.show_current_balance()
        elif choice == "6":
            print("Exiting the vending machine. Goodbye! (Made by: Umair Dada)")
            break
        else:
            print("Invalid choice. Please select a valid option (1-6).")


if __name__ == "__main__":
    main()
