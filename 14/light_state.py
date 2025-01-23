from abc import ABC, abstractmethod

class LightState:
    def __init__(self, name:str) -> None:
        self.__name = name

    @property
    def name(self)->str:
        return self.__name
    
    def turn_on(self,light_switch):
        raise ValueError(f"Cannot turn on in {self.__name} state")
    
    def turn_off(self, light_switch):
        raise ValueError(f"Cannot turn off in {self.__name} state")
    
    def dim(self, light_switch):
        raise ValueError(f"Cannot dim in {self.__name} state")
    
class OnState(LightState):
    def __init__(self) -> None:
        super().__init__("ON")

    def turn_off(self, light_switch):
        light_switch.state = OffState()
        print("Light is on now!")
    def dim(self, light_switch):
        light_switch.state = DimState()
        print("Light is dimed now!")


class OffState(LightState):
    def __init__(self) -> None:
        super().__init__("ON")

    def turn_off(self, light_switch):
        light_switch.state = OffState()
        print("Light is off now!")
    def dim(self, light_switch):
        light_switch.state = DimState()
        print("Light is dimed now!")
    
class DimState(LightState):
    def __init__(self) -> None:
        super().__init__("DIM")
    
    def turn_on(self, light_switch):
        light_switch.state = OnState()
        print("Light is On now!")

class LightSwitch:
    def __init__(self) -> None:
        self.__state = OffState()

    @property
    def state(self) -> LightState:
        return self.__state
    
    @state.setter
    def state(self, state:LightState)->None:
        self.__state = state

    def turn_on(self):
        self.__state.turn_on(self)
    def turn_off(self):
        self.__state.turn_off(self)
    def dim(self):
        self.__state.dim(self)

def show_menu():
    print("===========MENU=========")
    print("1. Turn on")
    print("2. Turn off")
    print("3. Dim")
    print("4. Exit")

def main():
    switch = LightSwitch()
    while True:
        show_menu()
        try:
            option = int(input("Enter your choice: "))
            if option == 1:
                switch.turn_on()
            elif option == 2:
                switch.turn_off()
            elif option == 3:
                switch.dim()
            else:
                break
        except ValueError as err:
            print(err)

if __name__ == "__main__":
    main()