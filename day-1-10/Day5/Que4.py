# . write a program that compresses a file using a compression algorithm 
# (e.g., zlib) and then another program to decompress it.

# compresssion program
import zlib

def compress_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        data = f_in.read()
        compressed_data = zlib.compress(data)
        with open(output_file, 'wb') as f_out:
            f_out.write(compressed_data)
    print(f"Compressed {input_file} to {output_file}")


compress_file('example.txt', 'example.txt.zlib')


# Decompresion program
import zlib

def decompress_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        compressed_data = f_in.read()
        decompressed_data = zlib.decompress(compressed_data)
        with open(output_file, 'wb') as f_out:
            f_out.write(decompressed_data)
    print(f"Decompressed {input_file} to {output_file}")


decompress_file('example.txt.zlib', 'example_decompressed.txt')
