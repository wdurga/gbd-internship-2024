# 1. create a custom class representing a complex number. Implement special
# methods like __add__, __sub__, and __str__ to enable arithmetic 
# operations and custom string representation

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)
        return NotImplemented

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

# Usage Example
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, -2)

# Addition
c3 = c1 + c2
print("Addition:", c3)

# Subtraction
c4 = c1 - c2
print("Subtraction:", c4)
