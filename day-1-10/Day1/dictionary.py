# Creating a dictionary
student = {
    "name": "Anshika",
    "age": 20,
    "major": "Computer Science",
    "grades": [85, 90, 92]
}

# Accessing values
print(student["name"])   
print(student.get("age")) 

# Modifying values
student["age"] = 16
student["grades"].append(95)

# Adding new key-value pairs
student["gender"] = "Female"

# Removing key-value pairs
del student["major"]



# dictionaries
my_dict = {'name': 'Durga', 'age':23, 'city': 'ktm'}

#accessing values
print(my_dict['name'])

#setting value
my_dict['age'] = 20
print(my_dict)

#adding new key-vlaue pairs
my_dict['job'] = 'NUrse'
print(my_dict)

#deleting key-value pair
del my_dict['city']
print(my_dict)

# Iterating over keys
for key in student:
    print(key, ":", student[key])

# Iterating over key-value pairs
for key, value in student.items():
    print(key, ":", value)



# student[key] is used to access the value associated with a
# specific key in the dictionary student.

