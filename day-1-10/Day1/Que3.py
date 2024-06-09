# 3. Perform calculations i.e (minimum, max, sorting etc) on a dictionary of data. 

import heapq

data = {
    'Anshika': 88,
    'Durga': 98,
    'Anshu': 77,
    'Sylvie': 87,
    'Lauren': 86 
}

#minimum value
min_key = min(data, key = data.get)
min_value = data[min_key]
print(f"Minimum value: {min_value}, key: {min_key}")

# maximum  value
max_key = max(data, key = data.get)
max_value = data[max_key]
print(f"Maximun value : {max_value}, key: {max_key}")

# sorting by keys
sorted_by_keys = dict(sorted(data.items()))
print("Sorted by keys", sorted_by_keys)

#sorting by values
sorted_by_values = dict(sorted(data.items(), key=lambda item: item[1]))
print("sorted by values:", sorted_by_values)

# top N elements by value
N = 2
top_n = heapq.nlargest(N, data.items(), key=lambda item: item[1])
top_n_dict = dict(top_n)
print(f"Top {N} elements by value:", top_n_dict)

######*****#####
list1 = [100, 3, 4, 12, 1]
# index() returns the index for 4 in list1
print(list1.index(4))

# If the element is not found, the index() method raises a ValueError.

# data.items() returns a view object that displays 
# a list of the dictionary's key-value pairs as tuple.
# convert sorted list of tuples back into dictionary.

# Square brackets ([]) are used to access values in a dictionary by their keys.
# Parentheses (()) are used for function calls and grouping expressions.
# Curly braces ({}) are used to define dictionaries and sets, not for accessing elements.

# In the context of a key-value pair tuple, item[0] represents the key,
# and item[1] represents the value.
# Therefore, item[1] extracts the value from the key-value pair.
