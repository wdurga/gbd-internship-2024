#  You need to convert or output integers represented by binary, octal, or hexadecimal digits.

# converting from Binary, Octal, Hexadecimal to decimal
# Binary to Decimal : use the int() function with base 2 to convert binary strings to integers.
binary_number = '1010'
decimal_number = int(binary_number, 2)
print(decimal_number)

# Octal to Decimal:  use the int() function with base 8 to convert octal strings to integers.
octal_number = '12'
decimal_number = int(octal_number, 8)
print(decimal_number)

# Hexadecimal to Decimal:: use int() fxn with base 16
hexadecimal_number = 'A'
decimal_number = int(hexadecimal_number, 16)
print(decimal_number)


# converting from Decimal to Binary, Octal or Hexadecimal
decimal_number = 10

binary_string = bin(decimal_number)
print(binary_string)

octal_string = oct(decimal_number)
print(octal_string)

hexadecimal_string =hex(decimal_number)
print(hexadecimal_string)



# leading zeros in integer literals indicate the number is in octal(base 8) notation.
# 01 is not valid octal number as octal digits only range from 0 to 7.
# Error is : SyntaxError
a = 01
print(a)