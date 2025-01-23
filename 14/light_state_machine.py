from state_machine import (State, Event, acts_as_state_machine, after, before, InvalidStateTransition)

@acts_as_state_machine
class LightProcess:
    # define states
    off = State(initial=True)
    on = State()
    dim = State()

    # define transitions
    turn_on = Event(from_states=(off,dim), to_state= on)
    turn_off = Event(from_states=on, to_state= off)
    diming = Event(from_states = on, to_state= dim)
    def __init__(self, light_switch) -> None:
        self._light_switch = light_switch

    @after('turn_on')
    def after_turn_on(self):
        print('Light is on now!')

    @after('turn_off')
    def after_turn_off(self):
        print('Light is off now!')

    @after('diming')
    def after_dim(self):
        print('Light is dim now!')
    
    @after('')
    def after_turn_off(self):
        print('Light is off now!')

class LightSwitch:
    def __init__(self) -> None:
        self.__state = LightProcess(self)

    def turn_on(self):
        self.__state.turn_on()
    def turn_off(self):
        self.__state.turn_off()
    def dim(self):
        self.__state.after_dim()


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