class SimpleClass:
    def __init__(self):
        self.name = "SimpleClass"

    def method_one(self):
        print("SimpleClass: Method One")

    def method_two(self):
        print("SimpleClass: Method Two")

class Decorator:
    def __init__(self, original_object):
        self._original_object = original_object

    def method_one(self):
        print("Decorator: Decorated Method One Start")
        self._original_object.method_one()
        print("Decorator: Decorated Method One End")

    def method_two(self):
        print("Decorator: Decorated Method Two Start")
        self._original_object.method_two()
        print("Decorator: Decorated Method Two End")

    def additional_method_one(self):
        print("Decorator: Additional Method One")

    def additional_method_two(self):
        print("Decorator: Additional Method Two")

simple_object = SimpleClass()
print("Calling methods on the undecorated object:")
simple_object.method_one()
simple_object.method_two()

decorated_object = Decorator(simple_object)
print("\nCalling methods on the decorated object:")
decorated_object.method_one()
decorated_object.method_two()
decorated_object.additional_method_one()
decorated_object.additional_method_two()
