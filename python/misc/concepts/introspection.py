import inspect

def introspect_object(obj):
    print(f"Type of object: {type(obj)}")
    print(f"ID of object: {id(obj)}")
    print(f"Attributes of object: {dir(obj)}")

    # Inspect functions and methods
    for name, data in inspect.getmembers(obj):
        if inspect.ismethod(data) or inspect.isfunction(data):
            print(f"Function/method name: {name}")
            print(f"Signature: {inspect.signature(data)}")
            print(f"Docstring: {inspect.getdoc(data)}\n")

# Usage example
class ExampleClass:
    def example_method(self):
        """An example method."""
        pass

example_instance = ExampleClass()
introspect_object(example_instance)
