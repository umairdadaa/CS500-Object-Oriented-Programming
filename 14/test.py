from state_machine import (
    State, Event, acts_as_state_machine, after, InvalidStateTransition
)

@acts_as_state_machine
class VendingProcess:
    # States
    idle = State(initial=True)
    coin_inserted = State()
    product_selected = State()
    product_dispensed = State()

    # Events
    insert_coin = Event(from_states=idle, to_state=coin_inserted)
    return_coin = Event(from_states=coin_inserted, to_state=idle)
    select_product = Event(from_states=coin_inserted, to_state=product_selected)
    dispense_product = Event(from_states=product_selected, to_state=product_dispensed)
    finish_transaction = Event(from_states=product_dispensed, to_state=idle)

    # State transitions
    @after('insert_coin')
    def after_insert_coin(self):
        print("Coins accepted. Please select your product.")

    @after('return_coin')
    def after_return_coin(self):
        print("Returning your coins. Resetting to idle.")

    @after('select_product')
    def after_select_product(self):
        print("Product selected. Preparing to dispense...")

    @after('dispense_product')
    def after_dispense_product(self):
        print("Product dispensed. Please take your item.")

    @after('finish_transaction')
    def after_finish_transaction(self):
        print("Transaction complete. Ready for the next customer.")

class VendingMachine:
    def __init__(self):  # Fixed constructor
        self.process = VendingProcess()
        self.balance = 0
        self.products = {
            "soda": 125,
            "chips": 100,
            "candy": 75,
        }

    def insert_coin(self, amount):
        if amount not in [5, 10, 25, 50]:
            print("Invalid coin. Please use 5, 10, 25, or 50 cents.")
            return

        self.balance += amount
        print(f"You added {amount} cents. Total balance: {self.balance} cents.")

        if self.process.current_state == self.process.idle:
            try:
                self.process.insert_coin()
            except InvalidStateTransition:
                print("Error: Unable to switch to 'coin inserted' state.")

    def return_coin(self):
        if self.process.current_state != self.process.coin_inserted:
            print("Coins can’t be returned at this stage.")
            return

        try:
            self.process.return_coin()
            print(f"Coins returned: {self.balance} cents.")
            self.balance = 0
        except InvalidStateTransition:
            print("Error: Unable to switch to 'idle' state.")

    def select_product(self, product_name):
        if product_name not in self.products:
            print("Invalid product. Please choose soda, chips, or candy.")
            return

        product_cost = self.products[product_name]
        if self.balance < product_cost:
            print(f"Insufficient balance. {product_name.capitalize()} costs {product_cost} cents.")
            return

        confirmation = input(f"Confirm purchase of {product_name.capitalize()}? (yes/no): ").strip().lower()
        if confirmation != "yes":
            print("Selection canceled.")
            return

        try:
            self.process.select_product()
            self.balance -= product_cost
            print(f"{product_name.capitalize()} selected. Remaining balance: {self.balance} cents.")
        except InvalidStateTransition:
            print("Error: Unable to switch to 'product selected' state.")

    def dispense_product(self):
        try:
            self.process.dispense_product()
            self.process.finish_transaction()
        except InvalidStateTransition:
            print("Error: Unable to dispense product at this stage.")

    def show_current_balance(self):
        print(f"Current balance: {self.balance} cents.")

    def get_current_state(self):
        return self.process.current_state

def show_menu():
    menu = """
    VENDING MACHINE MENU
    1. Insert Coin
    2. Select Product
    3. Dispense Product
    4. Return Coin
    5. Check Balance
    6. Quit
    """
    print(menu)

def main():
    vending_machine = VendingMachine()

    while True:
        show_menu()
        choice = input("Please select an option: ").strip()

        if choice == "1":
            try:
                coin = int(input("Enter coin amount (5, 10, 25, 50): "))
                vending_machine.insert_coin(coin)
            except ValueError:
                print("Invalid input. Please enter a valid coin value.")
        elif choice == "2":
            vending_machine.show_current_balance()
            product = input("Choose a product (soda [$1.25], chips [$1.00], candy [$0.75]): ").lower()
            vending_machine.select_product(product)
        elif choice == "3":
            vending_machine.dispense_product()
        elif choice == "4":
            vending_machine.return_coin()
        elif choice == "5":
            vending_machine.show_current_balance()
        elif choice == "6":
            print("Exiting the vending machine. Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option (1-6).")

if __name__ == "__main__":
    main()