from abc import ABC, abstractmethod

# Abstract Base Classes for Displayable, Flyable, and Movable
class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass

class Movable(ABC):
    @abstractmethod
    def move(self) -> None:
        pass

# Part Class
class Part(Displayable):
    def __init__(self, part_no: int, price: float) -> None:
        self.__part_no = part_no
        self.__price = price

    @property
    def part_no(self) -> int:
        return self.__part_no

    def __str__(self) -> str:
        return f"Part No: {self.__part_no}, Price: ${self.__price:.2f}"

    def display(self) -> None:
        print(self)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Part) and self.__part_no == other.__part_no

# MovablePart Class
class MovablePart(Movable, Part):
    def __init__(self, part_no: int, price: float, part_type: str) -> None:
        super().__init__(part_no, price)
        self.__type = part_type

    def __str__(self) -> str:
        return f"{super().__str__()}, Type: {self.__type}"

    def move(self) -> None:
        print(f"Part No: {self.part_no} is moving fast.")

# Machine Class
class Machine(Displayable):
    def __init__(self, machine_name: str) -> None:
        self.__machine_name = machine_name
        self.__parts = []

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index >= len(self.__parts) - 1:
            raise StopIteration()
        self.__index += 1
        return self.__parts[self.__index]

    def add_part(self, part: Part) -> None:
        self.__parts.append(part)

    def __str__(self) -> str:
        parts_str = "\n".join(str(part) for part in self.__parts)
        return f"Machine Name: {self.__machine_name}\nParts:\n{parts_str}"

    def display(self) -> None:
        print(self)

    @abstractmethod
    def dowork(self) -> None:
        print(f"The {self.__machine_name} is working.")

    @property
    def machine_name(self) -> str:
        return self.__machine_name

    def find_duplicated_parts(self) -> dict[int, int]:
        part_freq = {}
        for part in self.__parts:
            part_freq[part.part_no] = part_freq.get(part.part_no, 0) + 1
        return {part_no: count for part_no, count in part_freq.items() if count > 1}

    def remove_part(self, part_no: int) -> None:
        # self.__parts = [part for part in self.__parts if part.part_no != part_no]
        updated_parts = []
        for part in self.__parts:
            if part.part_no != part_no:
                updated_parts.append(part)
        self.__parts = updated_parts

        for part in updated_parts:
            self.__parts.remove(part)
        # return None


    def get_movable_parts(self) -> list[MovablePart]:
        # return [part for part in self.__parts if isinstance(part, MovablePart)]
        moveable_parts = []
        for part in self:
            if isinstance(part, MovablePart):
                moveable_parts.append(part)
        return moveable_parts
        

# JetFighter Class
class JetFighter(Displayable, Flyable):
    def __init__(self, model: str, speed: int) -> None:
        self.__model = model
        self.__speed = speed

    def __str__(self) -> str:
        return f"Model: {self.__model}, Speed: {self.__speed}"

    def display(self) -> None:
        print(self)

    def fly(self) -> None:
        print(f"The JetFighter {self.__model} is flying!")

# Robot Class
class Robot(Machine, JetFighter):
    def __init__(self, machine_name: str, cpu: str, model: str, speed: int) -> None:
        Machine.__init__(self, machine_name)
        JetFighter.__init__(self, model, speed)
        self.__cpu = cpu

    def __str__(self) -> str:
        return f"Processor: {self.__cpu}\n{Machine.__str__(self)}\n{JetFighter.__str__(self)}"

    def display(self) -> None:
        print(self)

    def dowork(self) -> None:
        print(f"The Robot {self.machine_name} is assembling a big truck.")

    def fly(self) -> None:
        super().fly()
        print(f"The Robot {self.machine_name} is flying over the ocean!")

    def get_expensive_parts(self, price_limit: float) -> list[Part]:
        return [part for part in self._Machine__parts if part._Part__price >= price_limit]

    def get_movable_parts_by_type(self) -> dict[str, list[MovablePart]]:
        movable_parts_by_type = {}
        for part in self:
            if isinstance(part, MovablePart):
                movable_parts_by_type.setdefault(part._MovablePart__type, []).append(part)
        return movable_parts_by_type

def main():
    robo = Robot('MTX', 'M1X', 'F-16', 10000)
    robo.add_part(Part(111, 100))
    robo.add_part(Part(222, 200))
    robo.add_part(Part(333, 300))
    robo.add_part(Part(222, 300))
    robo.add_part(MovablePart(555, 300, "TypeA"))
    robo.add_part(Part(111, 100))
    robo.add_part(Part(111, 100))
    robo.add_part(MovablePart(777, 300, "TypeB"))
    robo.add_part(MovablePart(655, 300, "TypeA"))
    robo.add_part(MovablePart(755, 300, "TypeA"))
    robo.add_part(MovablePart(977, 300, "TypeB"))
    
    robo.display()

    print("\nRobot Test Flight:")
    robo.fly()

    print("\nRobot Dowork Test:")
    robo.dowork()

    print("\nDuplicated Part List:")
    part_freq = robo.find_duplicated_parts()
    for part_no, occurrences in part_freq.items():
        print(f"Part No: {part_no} => {occurrences} times")

    print("\nExpensive Part List:")
    expensive_parts = robo.get_expensive_parts(200)
    for part in expensive_parts:
        part.display()

    print("\nMovable Part List:")
    movable_parts = robo.get_movable_parts_by_type()
    for part_type, parts in movable_parts.items():
        print(f"Type: {part_type}")
        for part in parts:
            part.display()

    print("\nAsk Movable Parts to Move:")
    for part in robo.get_movable_parts():
        part.move()

    print("\nTest Remove Part:")
    robo.remove_part(333)
    if any(part.part_no == 333 for part in robo):
        print('Found part No. 333')
    else:
        print('Part No. 333 removed successfully.')

if __name__ == "__main__":
    main()
