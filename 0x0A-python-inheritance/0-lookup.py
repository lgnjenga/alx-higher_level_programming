#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (object): The object for which to look up attributes and methods.

    Returns:
        list: A list of attribute and method names.
    """
    # Use the dir() function to get a list of names in the object's namespace
    attributes_and_methods = dir(obj)

    # Filter out names that start with '__' (these are special methods and attributes)
    filtered_names = [name for name in attributes_and_methods if not name.startswith('__')]

    return filtered_names

# Test cases
class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass

print(lookup(MyClass1))
print(lookup(MyClass2))
print(lookup(int))
