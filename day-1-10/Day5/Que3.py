
# 3. create a program that can merge multiple text files into one file and 
# another program to split a large file into smaller files based on a 
# specified file size or line count.


#  function definition
# Opening Output File
# Iterating over input files
# Opening each input files
# Writing content to output file
# call the defined function


# merge multiole text files
def merge_text_files(output_file, *input_files):
    with open(output_file, 'w') as outfile:
        for input_file in input_files:
            with open(input_file, 'r') as infile:
                outfile.write(infile.read())

merge_text_files("merged_output.txt", "input1.txt", "input2.txt")
print("The file is merged successfully.")



# split large file into smaller files
import os

def split_large_file(input_file, output_dir, max_size=None, max_lines=None):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    def write_chunk(output_dir, file_index, lines):
        output_file = os.path.join(output_dir, f"chunk_{file_index}.txt")
        with open(output_file, 'w') as outfile:
            outfile.writelines(lines)

    file_index = 1
    current_chunk = []
    current_size = 0
    current_lines = 0

    with open(input_file, 'r') as infile:
        for line in infile:
            current_chunk.append(line)
            current_size += len(line)
            current_lines += 1

            if (max_size and current_size >= max_size) or (max_lines and current_lines >= max_lines):
                write_chunk(output_dir, file_index, current_chunk)
                file_index += 1
                current_chunk = []
                current_size = 0
                current_lines = 0

        # Write any remaining lines to a new chunk
        if current_chunk:
            write_chunk(output_dir, file_index, current_chunk)

split_large_file("large_input.txt", "output_directory", max_size=1024 * 1024)  # Split into 1MB chunks
