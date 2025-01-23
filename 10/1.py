from abc import ABC, abstractmethod
from typing import List, Optional


class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass


class House(Displayable):
    def __init__(self, address: str, square_feet: int, num_rooms: int, price: int, city: str) -> None:
        self.__address = address
        self.__square_feet = square_feet
        self.__num_rooms = num_rooms
        self.__price = price
        self.__city = city

    @property
    def address(self) -> str:
        return self.__address

    @property
    def price(self) -> int:
        return self.__price

    @price.setter
    def price(self, new_price: int) -> None:
        self.__price = new_price

    def __eq__(self, value: object) -> bool:
        if isinstance(value, House):
            return self.__address == value.address
        return False

    def __str__(self) -> str:
        return (f"Address = {self.__address}, Square Feet = {self.__square_feet}, "
                f"Number of Rooms = {self.__num_rooms}, Price = {self.__price}")

    def display(self) -> None:
        print(self.__str__())


class Contact(Displayable):
    def __init__(self, firstname: str, lastname: str, phone_number: str, email: str) -> None:
        self.__lastname = lastname
        self.__firstname = firstname
        self.__email = email
        self.__phone_number = phone_number

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Contact):
            return self.__firstname == value.__firstname and self.__lastname == value.__lastname
        return False

    def __str__(self) -> str:
        return (f"Last Name = {self.__lastname}, First Name = {self.__firstname}, "
                f"Phone Number = {self.__phone_number}, Email = {self.__email}")

    def display(self) -> None:
        print(self.__str__())


class Owner(Contact):
    def __init__(self, firstname: str, lastname: str, phone_number: str, email: str) -> None:
        super().__init__(firstname, lastname, phone_number, email)
        self.__houses: List[House] = []

    def add_house(self, house: House) -> None:
        self.__houses.append(house)

    def __str__(self) -> str:
        output = super().__str__() + "\nOwns the following houses:\n"
        for house in self.__houses:
            output += str(house) + "\n"
        return output

    def display(self) -> None:
        print(self.__str__())


class Buyer(Contact):
    def __init__(self, firstname: str, lastname: str, phone_number: str, email: str) -> None:
        super().__init__(firstname, lastname, phone_number, email)
        self.__watch_list: List[House] = []

    def save_to_watchlist(self, house: House) -> None:
        if house not in self.__watch_list:
            self.__watch_list.append(house)

    def remove_from_watchlist(self, house: House) -> None:
        if house in self.__watch_list:
            self.__watch_list.remove(house)

    def __str__(self) -> str:
        output = super().__str__() + "\nWatching the following houses:\n"
        for house in self.__watch_list:
            output += str(house) + "\n"
        return output

    def display(self) -> None:
        print(self.__str__())


class Company(Displayable):
    def __init__(self, company_name: str) -> None:
        self.__company_name = company_name
        self.__owners: List[Owner] = []
        self.__buyers: List[Buyer] = []
        self.__agents: List['Agent'] = []
        self.__houses: List[House] = []

    def add_owner(self, owner: Owner) -> None:
        if owner not in self.__owners:
            self.__owners.append(owner)

    def add_buyer(self, buyer: Buyer) -> None:
        if buyer not in self.__buyers:
            self.__buyers.append(buyer)

    def add_agent(self, agent: 'Agent') -> None:
        if agent not in self.__agents:
            self.__agents.append(agent)

    def add_house_to_listing(self, house: House) -> None:
        if house not in self.__houses:
            self.__houses.append(house)

    def get_house_by_address(self, address: str) -> Optional[House]:
        for house in self.__houses:
            if house.address == address:
                return house
        return None

    def remove_house_from_listing(self, house: House) -> None:
        if house in self.__houses:
            self.__houses.remove(house)

    def remove_house_from_watchlist(self, house: House) -> None:
        for buyer in self.__buyers:
            buyer.remove_from_watchlist(house)

    def display(self) -> None:
        print(f"Company Name = {self.__company_name}")
        print("=========================== The list of agents: ==============================")
        for agent in self.__agents:
            agent.display()

        print("=========================== The house listing: ===============================")
        for house in self.__houses:
            house.display()

        print("=========================== The list of owners: ==============================")
        for owner in self.__owners:
            owner.display()

        print("=========================== The list of buyers: ==============================")
        for buyer in self.__buyers:
            buyer.display()

    def __str__(self) -> str:
        output = f"Company Name = {self.__company_name}\n"
        output += "=========================== The list of agents: ==============================\n"
        for agent in self.__agents:
            output += str(agent) + "\n"
        output += "=========================== The house listing: ===============================\n"
        for house in self.__houses:
            output += str(house) + "\n"
        output += "=========================== The list of owners: ==============================\n"
        for owner in self.__owners:
            output += str(owner) + "\n"
        output += "=========================== The list of buyers: ==============================\n"
        for buyer in self.__buyers:
            output += str(buyer) + "\n"
        return output


class Agent(Contact):
    def __init__(self, firstname: str, lastname: str, phone_number: str, email: str, position: str, company: Company) -> None:
        super().__init__(firstname, lastname, phone_number, email)
        self.__position = position
        self.__company = company

    def add_house_to_listing_for_owner(self, owner: Owner, house: House) -> None:
        self.__company.add_owner(owner)
        self.__company.add_house_to_listing(house)

    def help_buyer_to_save_to_watchlist(self, buyer: Buyer, house: House) -> None:
        self.__company.add_buyer(buyer)
        buyer.save_to_watchlist(house)

    def edit_house_price(self, address: str, new_price: int) -> None:
        house = self.__company.get_house_by_address(address)
        if house is not None:
            house.price = new_price

    def sold_house(self, house: House) -> None:
        self.__company.remove_house_from_listing(house)
        self.__company.remove_house_from_watchlist(house)

    def display_potential_buyers(self, house: House) -> None:
        for buyer in self.__company._Company__buyers:
            if house in buyer._Buyer__watch_list:
                buyer.display()

    def display(self) -> None:
        print(super().__str__() + f"Position = {self.__position}")


def main() -> None:
    owner1 = Owner('Peter', 'Li', '510-111-2222', 'peter@yahoo.com')
    owner2 = Owner('Carl', 'Buck', '408-111-2222', 'carl@yahoo.com')

    house1 = House('1111 Mission Blvd', 1000, 2, 1000000, 'Fremont')
    house2 = House('2222 Mission Blvd', 2000, 3, 1200000, 'San Jose')
    house3 = House('3333 Mission Blvd', 3000, 4, 2000000, 'Mountain View')

    owner1.add_house(house1)
    owner2.add_house(house2)
    owner2.add_house(house3)

    buyer1 = Buyer('Tom', 'Buke', '408-555-2222', 'tom@yahoo.com')
    buyer2 = Buyer('Lily', 'Go', '510-222-3333', 'lily@yahoo.com')

    company = Company('Good Future Real Estate')
    agent1 = Agent('Dave', 'Henderson', '408-777-3333', 'dave@yahoo.com', 'Senior Agent', company)
    company.add_agent(agent1)

    agent1.add_house_to_listing_for_owner(owner1, house1)
    agent1.add_house_to_listing_for_owner(owner2, house2)
    agent1.add_house_to_listing_for_owner(owner2, house3)

    agent1.help_buyer_to_save_to_watchlist(buyer1, house1)
    agent1.help_buyer_to_save_to_watchlist(buyer1, house2)
    agent1.help_buyer_to_save_to_watchlist(buyer1, house3)

    agent1.help_buyer_to_save_to_watchlist(buyer2, house2)
    agent1.help_buyer_to_save_to_watchlist(buyer2, house3)

    company.display()
    print('\nAfter one house was sold ..........................')
    agent1.sold_house(house3)
    company.display()
    print('\nDisplaying potential buyers for house 1 ..........................')
    agent1.display_potential_buyers(house1)


if __name__ == "__main__":
    main()
