# Television class definition
class Television:
    def __init__(self, screen_type: str, screen_size: int, resolution: str, price: float) -> None:
        self.__screen_type = screen_type
        self.__screen_size = screen_size
        self.__resolution = resolution
        self.__price = price

    def __str__(self) -> str:
        return (f"\nScreen Type: {self.__screen_type}, "
                f"Screen Size: {self.__screen_size} inches, "
                f"Resolution: {self.__resolution}, Price: ${self.__price:.2f}")

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def screen_type(self) -> str:
        return self.__screen_type
    
    @property
    def screen_size(self) -> int:
        return self.__screen_size

    @property
    def resolution(self) -> str:
        return self.__resolution

    @property
    def price(self) -> float:
        return self.__price

# Garage class definition
class Garage:
    def __init__(self, garage_type: str, size: int, door_type: str) -> None:
        self.__garage_type = garage_type
        self.__size = size
        self.__door_type = door_type

    def __str__(self) -> str:
        return (f"\nGarage Type: {self.__garage_type}, "
                f"Size: {self.__size} sq ft, Door Type: {self.__door_type}")

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def garage_type(self) -> str:
        return self.__garage_type
    
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, new_size: int) -> None:
        self.__size = new_size

    @property
    def door_type(self) -> str:
        return self.__door_type

# Room class definition
class Room:
    def __init__(self, room_type: str, size: int) -> None:
        self.__room_type = room_type
        self.__size = size

    def __str__(self) -> str:
        return f"\nRoom Name: {self.__room_type}, Size: {self.__size} sq ft"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def room_type(self) -> str:
        return self.__room_type

    @property
    def size(self) -> int:
        return self.__size

# House class definition
class House:
    def __init__(self, address: str, square_feet: int, garage: Garage) -> None:
        self.__address = address
        self.__square_feet = square_feet
        self.__rooms: list[Room] = []
        self.__garage = garage
        self.__televisions: list[Television] = []

    def __str__(self) -> str:
        return (f"\nHouse Address: {self.__address}, "
                f"Square Feet: {self.__square_feet}, "
                f"Garage: {self.__garage}, "
                f"Rooms: {self.__rooms}, "
                f"Televisions: {self.__televisions}")

    def __repr__(self) -> str:
        return self.__str__()

    def add_television(self, tv: Television) -> None:
        self.__televisions.append(tv)

    def remove_television(self, tv: Television) -> None:
        self.__televisions.remove(tv)
    
    def add_room(self, room: Room) -> None:
        self.__rooms.append(room)

    def remove_room(self, room: Room) -> None:
        self.__rooms.remove(room)

    def change_garage_size(self, new_size: int) -> None:
        self.__garage.size = new_size

    def get_biggest_room(self) -> Room:
        return max(self.__rooms, key=lambda room: room.size, default=None)

    def get_oled_televisions(self) -> list[Television]:
        return [tv for tv in self.__televisions if tv.screen_type.lower() == "oled"]
    
    def is_similar_house(self, other_house) -> bool:
        return (self.__square_feet == other_house.__square_feet and 
                len(self.__rooms) == len(other_house.__rooms))

    @property
    def address(self) -> str:
        return self.__address
    
    @property
    def square_feet(self) -> int:
        return self.__square_feet
        
    @property
    def rooms(self) -> list[Room]:
        return self.__rooms
    
    @property
    def televisions(self) -> list[Television]:
        return self.__televisions
    
    @property
    def garage(self) -> Garage:
        return self.__garage

    @garage.setter
    def garage(self, garage: Garage) -> None:
        self.__garage = garage

# Main function to create objects and demonstrate functionality
def main():
    print("\nSimple House Management System")

    garage = Garage("Single", 250, "Manual")
    house1 = House("2222 S Rock Rd, Wichita, KS, 67207", 1400, garage)

    rooms = [
        Room("Master Bedroom", 400),
        Room("Bedroom", 300),
        Room("Kitchen", 150),
        Room("Living Room", 200)
    ]

    for room in rooms:
        house1.add_room(room)

    televisions = [
        Television("LED", 55, "1080p", 499.99),
        Television("OLED", 60, "4K", 999.99),
        Television("OLED", 75, "4K", 1499.99)
    ]

    for tv in televisions:
        house1.add_television(tv)

    print("\n", house1)

    house1.change_garage_size(500)
    print("\nUpdated Garage Size:", house1.garage.size)

    largest_room = house1.get_biggest_room()
    print("\nBiggest Room:", largest_room)

    oled_tv = house1.get_oled_televisions()
    print("\nOLED Televisions:", oled_tv)

    garage2 = Garage("Double", 400, "Automatic")
    house2 = House("1111 Corpley Ave, San Jose, CA, 95132", 1400, garage2)

    for room in rooms:
        house2.add_room(room)

    print("\nAre these two houses similar?", house1.is_similar_house(house2))

if __name__ == "__main__":
    main()
