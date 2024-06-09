# You have a byte string and you need to unpack it into an integer value. 
# Alternatively, you need to convert a large integer back into a byte string.

# To unpack a byte string into an integer value and convert a large integer back 
# into a byte string in Python, you can use the int.from_bytes() and int.to_bytes() methods
# b indicates byte string:: which are used to handle binary data.



# UNPACKING a Byte String into an Integer
byte_string = b'\x00\x10'

# unpacking the byte string into an integer (big-endian)
integer_value = int.from_bytes(byte_string, byteorder='big')
print(integer_value)

# unpacking the byte string into an integer (little-endian)
integer_value_le = int.from_bytes(byte_string, byteorder='little')
print(integer_value_le)


# PACKING an Integer into a Byte string
integer_value = 16
#  integer_value 16 requires 5 bits as its representation is "10000".
# to  determine the number of bytes needed we add 7 to the bit length then perform integer division by 8.
# this ensures any extra bits are rounded up to the next full byte.
num_bytes = (integer_value.bit_length() + 7) // 8
# num_bytes = (5 + 7)//8  is equal to 1: so we need one byte to represent '16

# packing the integer into a byte string(big-endian)
byte_string = integer_value.to_bytes(num_bytes, byteorder='big')
print(byte_string)

byte_string_le = integer_value.to_bytes(num_bytes, byteorder='little')
print(byte_string_le)