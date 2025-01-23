class Person:
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self):
        return self.__name

    def walk(self):
        print(f"{self.name} is walking slowly...")

    def sleep(self):
        print(f"{self.name} does not sleep well...")

    def __str__(self) -> str:
        return f"name={self.__name}"


class SkillAdapter(Person):
    def __init__(self, person: Person) -> None:
        self._person = person

    @property
    def name(self):
        return self._person.name

    def walk(self):
        self._person.walk()

    def sleep(self):
        self._person.sleep()


class WalkBooster(SkillAdapter):
    def __init__(self, person: Person) -> None:
        super().__init__(person)

    def walk(self):
        self._person.walk()
        print(f"{self.name} is walking faster...")


class ScooterAdapter(SkillAdapter):
    def __init__(self, person: Person) -> None:
        super().__init__(person)

    def walk(self):
        self._person.walk()
        print(f"{self.name} is scooting...")


class SleepAid(SkillAdapter):
    def __init__(self, person: Person) -> None:
        super().__init__(person)

    def sleep(self):
        self._person.sleep()
        print(f"{self.name} is having enough sleep...")


def main() -> None:
    p1 = Person("Peter")
    p1.walk()
    p1.sleep()
    print("==========================================")
    p1 = WalkBooster(p1)
    p1.walk()
    print("==========================================")
    p1 = ScooterAdapter(p1)
    p1.walk()
    print("==========================================")
    p1 = SleepAid(p1)
    p1.sleep()
    print("==========================================")
    p1 = ScooterAdapter(WalkBooster(p1))
    p1 = SleepAid(p1)
    p1.walk()
    p1.sleep()


if __name__ == "__main__":
    main()
