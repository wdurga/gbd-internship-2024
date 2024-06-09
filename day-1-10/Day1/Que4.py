# 4. Eliminate duplicate from the sequence preserving the order of the items. 

def remove_duplicates(seq):
    # Initialize an empty dictionary to store unique items
    seen = {}
    
    # Iterate through the sequence
    result = []
    for item in seq:
        # If the item is not in the dictionary, add it to the result list and mark it as seen
        if item not in seen:   
            seen[item] = True
            result.append(item)
        print(seen)
        print(result)
    return result


# Example usage:
sequence = [3, 1, 2, 3, 5, 1, 4, 2]
unique_sequence = remove_duplicates(sequence)
print("Sequence with duplicates removed while preserving order:", unique_sequence)



# seen = {} initializes an empty dictionary named seen. This dictionary 
# is used to keep track of items that have already been encountered.

# result = [] initializes an empty list named result that will store
# the unique items in the original order.

# Efficiency: Using a dictionary to track seen items allows for 
# efficient checking of duplicates with an average time complexity of O(1) for each lookup.

# Using a list for tracking seen items would result in O(n) time 
# complexity for each membership test because checking if an item
# is in the list requires scanning through the list.


# Lists in Python maintain the order of elements as they are inserted. By appending items
# to the result list, we ensure that the order of first appearance is preserved.

# Lists are designed for storing sequences of items, making 
# them ideal for the final result where order matters.

# Appending to a list (result.append(item)) is an O(1) operation, which is efficient and 
# complements the fast lookup of the dictionary.