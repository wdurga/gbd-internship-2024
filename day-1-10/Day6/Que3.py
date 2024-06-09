 
# 3. Explore private, public and protected variables. Also explore objectmethod,
# static method and create a questions yourself regarding these.



# public Variable :: can be accessd from anywhere
class PublicExample:
    def __init__(self):
        self.public_var = "I am a public variable"

obj = PublicExample()
print(obj.public_var)  # Accessing the public variable

# Protected VArianble
class ProtectedExample:
    def __init__(self):
        self._protected_var = "I am a protected variable"

obj = ProtectedExample()
print(obj._protected_var)  # It can still be accessed but it's not recommended


# private Variable
class PrivateExample:
    def __init__(self):
        self.__private_var = "I am a private variable"

obj = PrivateExample()
# print(obj.__private_var)  # This would raise an AttributeError
print(obj._PrivateExample__private_var)  # Accessing the private variable via name mangling







# #######################################
# iNstance Methods(Object Methods)
class MyClass:
    def instance_method(self):
        return "This is an instance method"

obj = MyClass()
print(obj.instance_method())


# Class methods
class MyClass:
    class_var = "This is a class variable"

    @classmethod
    def class_method(cls):
        return f"This is a class method accessing {cls.class_var}"

print(MyClass.class_method())


# Static methods
class MyClass:
    @staticmethod
    def static_method():
        return "This is a static method"

print(MyClass.static_method())





























