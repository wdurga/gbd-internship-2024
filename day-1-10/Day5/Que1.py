# . write a Python program that takes user input and appends it to a text file.
# Also write a program that overwrites the existing content of a file with new data.


def append_to_file(filename):
    # Take user input
    user_input = input("Enter the text you want to append to the file: ")
    
    # Open the file in append mode and write the input to the file
    with open(filename, 'a') as file:
        file.write(user_input + '\n')
    
    print("The text has been appended to the file.")


filename = "example.txt"
append_to_file(filename)

def overwrite_file(filename):
    user_input = input("Enter the file content to overwrite the file text:")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
        
    print("The file has been overwritten with the new content.")
    
filename = "example.txt"
overwrite_file(filename)

