# 4. Explore f-strings and their use cases. Provided a list of items with
# their prices, create a program that uses f-strings to display the 
# items and their prices in a nicely formatted table.

# formatted String Literal
# use cases:
# 1. Variable Interpolation
name = "Anshika"
age = 90
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

#  2. Expressions inside String
x = 10
y = 5
result = f"The sum of {x} and {y} is {x + y}."
print(result)

# 3. Calling Functions
def greet(name):
    return f"Hello, {name}!"

name = "Anshu"
message = f"{greet(name)} How are you today?"
print(message)

# 4. Formatting Numbers
price = 49.99
discount = 0.2
final_price = price * (1 - discount)
formatted_price = f"Final price after {discount*100}% discount is ${final_price:.2f}."
print(formatted_price)

# 5. Debugging
x = 42
y = 3.14
print(f"x = {x}, y = {y}")

# 6. MUltiline Strings
name = "Sylvie"
age = 90
bio = f"""
Name: {name}
Age: {age}
"""
print(bio)

# 7. Dictionary Keys and Values
user = {'name': 'Lauren', 'age': 40}
message = f"User {user['name']} is {user['age']} years old."
print(message)

# 8. Class Attributes
class Person:
    # self is a reference to the current instance for the person class.
    # Self is used to access the variables that belong to the class.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

person = Person("Eve", 35)
print(f"{person}")


# LIST IN TABLE FORM
# List of items with their prices
items_with_prices = [
    ("Apple", 120.99),
    ("Banana", 100),
    ("Orange", 300.59),
    ("Mango", 400),
    ("Grapes", 180),
    ("Strawberry", 300)
]

# Define the column widths for the table
item_column_width = max(len(item) for item, price in items_with_prices) + 2
price_column_width = 12

# Print table header
print(f"{'Item':<{item_column_width}}{'Price':>{price_column_width}}")

# Print separator
print("-" * (item_column_width + price_column_width))

# Print each item with its price in a formatted manner
for item, price in items_with_prices:
    print(f"{item:<{item_column_width}}${price:>{price_column_width - 1}.2f}")




#  OTHERS....
calculation = f'4 times 11 is equal to {4 * 11}'
print(calculation)

# For n = 1, the formatted string will be "The value is 001".
for n in range(1, 11):
    sentence = f'The value is {n:03}'
    print(sentence)

# for floating point value
pi = 3.14159265
sentence = f'Pi is equal to {pi:.4f}'
print(sentence)

n: int = 100000000
print(f'{n:_}')
print(f'{n:,}')

var: str = 'var'
print(f'{var:_>20}')
print(f'{var:#<20}')
print(f'{var:|^20}')

price1 = 3.1456
print(f"Price 1 is ${price1:.2f}")
