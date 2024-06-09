# 3. Your code for interacting with the latest web authentication scheme has encountered a
# singularity and your only solution is to go around it in the complex plane. Or maybe
# you just need to perform some calculations using complex numbers. like conjugate,
# exploring real parts and imaginary parts, addition, subtraction, and converting into polar form.

# 1.  Conjugate of a Complex Number
# "a+bi" is "a-bi" :: here 'a' is real part and 'i' is an imaginary part

# define complex number
z = 3 + 4j
#  calculate the conjugate
conjugate_z = z.conjugate()
print("Conjugate of ", z, "is",conjugate_z)

# 2.  Real and Imaginary Parts
# the real part of a complex number is the coefficient of the real unit 1.
# the imaginary part is the coefficient of the imaginary unit i.

# define a complex number
z = 3 + 4J
#  extract real and imaginary parts
real_part = z.real
imaginary_part = z.imag

print("Real part of ", z, "is", real_part)
print("The imaginary part of", z, "is", imaginary_part)

#  3. Addition and Substraction of complex numbers

# define complex number
z1 = 3 + 4j
z2 = 1 + 2j

#  Addition
addition_result = z1 + z2
# SUbstraction
substraction_result = z1-z2

print("Additin result:", addition_result)
print("substraction Reault:", substraction_result)

# 4. Converting into Polar form
import cmath
import math
# define a complex number
z = 3 + 4j
#  calculate the modulus and argument
modulus = abs(z)
argument = cmath.phase(z)

print("Modulus of", z, "is", modulus)
print("Argument of", z, "is", argument, "radians")
print("Argument of", z, "is", math.degrees(argument), "degrees")


# cmath: This module provides mathematical functions for complex numbers.
# math: This module provides standard mathematical functions, including
# functions to convert angles between degrees and radians.


