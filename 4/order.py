# Product class definition
class Product:
    def __init__(self, product_id: int, product_name: str, price: float) -> None:
        self.__product_id = product_id
        self.__product_name = product_name
        self.__price = price

    def __str__(self) -> str:
        return (f"\nProduct ID: {self.__product_id}, "
                f"Product Name: {self.__product_name}, Price: ${self.__price:.2f}")

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Product) and self.__product_id == other.__product_id

    @property
    def product_id(self) -> int:
        return self.__product_id

    @property
    def price(self) -> float:
        return self.__price


# Customer class definition
class Customer:
    def __init__(self, name: str, address: str) -> None:
        self.__name = name
        self.__address = address

    def __str__(self) -> str:
        return f"\nCustomer Name: {self.__name}, Address: {self.__address}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Customer) and self.__name == other.__name

    @property
    def name(self) -> str:
        return self.__name

    @property
    def address(self) -> str:
        return self.__address


# OrderItem class definition
class OrderItem:
    def __init__(self, product: Product, quantity: int) -> None:
        self.__product = product
        self.__quantity = quantity

    def __str__(self) -> str:
        return f"\nProduct: {self.__product}, Quantity: {self.__quantity}"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: object) -> bool:
        return isinstance(other, OrderItem) and self.__product == other.__product

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        self.__quantity = quantity

    @property
    def product(self) -> Product:
        return self.__product   

    def get_total_value(self) -> float:
        return self.__product.price * self.__quantity


# Order class definition
class Order:
    def __init__(self, order_id: int, customer: Customer) -> None:
        self.__order_id = order_id
        self.__customer = customer         
        self.__order_items: list[OrderItem] = []

    def __str__(self) -> str:
        return (f"Order ID: {self.__order_id}, "
                f"Customer: {self.__customer}, "
                f"Items: {self.__order_items}")

    def add_item(self, product: Product, quantity: int) -> None:
        for item in self.__order_items:
            if item.product == product:
                item.quantity += quantity
                return
        self.__order_items.append(OrderItem(product, quantity))

    def remove_item(self, product_id: int) -> None:
        self.__order_items = [
            item for item in self.__order_items
            if item.product.product_id != product_id
        ]

    def find_largest_item(self) -> OrderItem:
        return max(self.__order_items, key=lambda item: item.get_total_value(), default=None)

    def get_total(self) -> float:
        return sum(item.get_total_value() for item in self.__order_items)

    def get_discount_value(self, discount_rate: float) -> float:
        return self.get_total() * (1 - discount_rate / 100)

    @property
    def order_id(self) -> int:
        return self.__order_id

    @property
    def customer(self) -> Customer:
        return self.__customer

    @property
    def order_items(self) -> list[OrderItem]:
        return self.__order_items


def main():
    print("\nSimple Order Management System\n")

    products = [
        Product(111, "Hammer", 20.00),
        Product(222, "Screw Driver", 15.00),
        Product(333, "Drill", 43.23)
    ]
    
    customer = Customer("Peter", "1234 Mission Blvd, Fremont, CA, 95678")
    order = Order(123, customer)

    for product in products:
        order.add_item(product, 10)  # Adding an initial quantity of 10 for each product

    print(order)

    order.add_item(products[0], 10)  # Adding more of the Hammer
    print("\nAfter Adding More Hammer:")
    print(order)
    
    order.remove_item(222)  # Removing Screw Driver
    print("\nAfter Removing Screw Driver (ID 222):")
    print(order)

    largest_item = order.find_largest_item()
    print("\nLargest Item:", largest_item)

    print("\nTotal Order Cost:", order.get_total())
    print("Discounted Total (20% off):", order.get_discount_value(20))


if __name__ == "__main__":
    main()
