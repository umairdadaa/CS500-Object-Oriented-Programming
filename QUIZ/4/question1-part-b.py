from abc import ABC, abstractmethod

class Beverage(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass

class Coffee(Beverage):
    def cost(self) -> float:
        return 2.0

    def description(self) -> str:
        return "Coffee"

class CondimentDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

class Milk(CondimentDecorator):
    def cost(self) -> float:
        return self.beverage.cost() + 0.5

    def description(self) -> str:
        return self.beverage.description() + ", Milk"

class Sugar(CondimentDecorator):
    def cost(self) -> float:
        return self.beverage.cost() + 0.2

    def description(self) -> str:
        return self.beverage.description() + ", Sugar"

class Cream(CondimentDecorator):
    def cost(self) -> float:
        return self.beverage.cost() + 0.7

    def description(self) -> str:
        return self.beverage.description() + ", Cream"

def main():
    coffee = Coffee()
    print(f"Beverage: {coffee.description()}, Cost: ${coffee.cost():.2f}")

    coffee_with_milk = Milk(coffee)
    print(f"Beverage: {coffee_with_milk.description()}, Cost: ${coffee_with_milk.cost():.2f}")

    coffee_with_milk_and_sugar = Sugar(coffee_with_milk)
    print(f"Beverage: {coffee_with_milk_and_sugar.description()}, Cost: ${coffee_with_milk_and_sugar.cost():.2f}")

    coffee_with_all = Cream(coffee_with_milk_and_sugar)
    print(f"Beverage: {coffee_with_all.description()}, Cost: ${coffee_with_all.cost():.2f}")

if __name__ == "__main__":
    main()
