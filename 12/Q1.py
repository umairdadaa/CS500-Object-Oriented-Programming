class FirstSystem:
    def foo(self, value:int)-> str:
        return str(value)

class SecondSystem:
    def bar(self, value:str)-> int:
        return int(value)

class Adapter(FirstSystem):
    def __init__(self, obj: SecondSystem) -> None:
        self.__obj = obj

    def foo(self,value:int):
        return str(self.__obj.bar(str(value)))

class Factory:
    @staticmethod
    def get_system() -> FirstSystem:
        return Adapter(SecondSystem())
    
def main():
    system = Factory.get_system()
    print(system.foo(1234))

if __name__ == "__main__":
    main()


