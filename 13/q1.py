from abc import ABC, abstractmethod
# Receivers
class Light:
    def turn_on(self)->None:
        print('Turning on the light.')

    def turn_off(self)->None:
        print('Turning off the light.')

class Fan:
    def start(self)-> None:
        print('Starting the fan.')
    
    def stop(self)-> None:
        print('Stopping the fan.')

# Command classes
class Command(ABC):
    @abstractmethod
    def execute(self)-> None:
        pass

class LightOnCommand(Command):
    def __init__(self,obj:Light) -> None:
        self.__obj = obj

    def execute(self) -> None:
        self.__obj.turn_on()

class LightOffCommand(Command):
    def __init__(self,obj:Light) -> None:
        self.__obj = obj

    def execute(self) -> None:
        self.__obj.turn_off()

class FanStartCommand(Command):
    pass

class FanStopCommand(Command):
    pass

# Invoker
class RemoteControl:
    def __init__(self) -> None:
        self.__lightOnCommand:LightOnCommand
        self.__lightOffCommand:LightOffCommand
        self.__fanStartCommand: FanStartCommand
        self.__fanStopCommand: FanStopCommand

    def setCommand(self, command:Command)->None:
        if isinstance(command,LightOnCommand):
            self.__lightOnCommand = command
        elif isinstance(command,LightOffCommand):
            self.__lightOffCommand = command
        pass

    def lightOnButtonPressed(self)->None:
        self.__lightOnCommand.execute()

    def lightOffButtonPressed(self)->None:
        pass

    def fanStartButtonPressed(self)->None:
        pass

    def fanStopButtonPressed(self)->None:
        pass

def main():
    light = Light()
    fan = Fan()
    control = RemoteControl()

    control.setCommand(LightOnCommand(light))
    control.setCommand(LightOffCommand(light))
    control.setCommand(FanStartCommand(fan))
    control.setCommand(FanStopCommand(fan))

    control.lightOnButtonPressed()
    control.lightOffButtonPressed()
    control.fanStartButtonPressed()
    control.fanStopButtonPressed()

if __name__ == '__main__':
    main()


