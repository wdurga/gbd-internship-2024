# You have a sequence of items, and you’d like to determine the most frequently occurring items
# in the sequence

# utilizes counter class from collection module: designed for counting hashable objects
from collections import Counter

def most_frequent_items(sequence):
    # Create a Counter object to count the occurrences of each item in the sequence
    counter = Counter(sequence)
    
    # Find the most common items
    most_common_items = counter.most_common()
    # most_common()::: This method returns a list of tuples, where each 
    # tuple contains an item and its count, sorted in descending order by count
    
    return most_common_items

# Example usage:
sequence = [3, 1, 2, 3, 5, 1, 4, 2, 3, 2, 1, 1, 1]
most_frequent = most_frequent_items(sequence)
print("Most frequently occurring items:", most_frequent)



# Internally, Counter uses a dictionary-like structure to store the counts,
# which allows for fast lookup and updating of counts.

# The time complexity is O(n + k log k), where n is the number of items
# in the sequence and k is the number of unique items. This is because 
# creating the Counter object takes O(n) time, and finding the most
# common items takes O(k log k) time due to sorting.

# If multiple items have the same count, they are 
# sorted by their order of appearance in the sequence.