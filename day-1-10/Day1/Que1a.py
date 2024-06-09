# Q.1. Make a list of the largest or smallest N items in a collection.
# Eg:
# Nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
# To print largest_three =
# largest_3 = [42,37, 23]
# smallest_3 = [-4,1,2]


import heapq
# heapq module provides an implementaion of the heap queue algo.
# also known as priority queue algo.

Nums = [1,8,2,23,7,-4,18,23,42,37,2]

largest_3 = heapq.nlargest(3,Nums)
print("The largest 3 numbers:", largest_3)

smallest_3 = heapq.nsmallest(3,Nums)
print("The smallest 3 numbers:", smallest_3)


# Heap Structure: A heap is a specialized tree-based data structure
# that satisfies the heap property. In a min-heap, the key at
# a parent node is less than or equal to the keys of its children,
# and the smallest element is at the root. Conversely, in a max-heap,
# the key at a parent node is greater than or equal to the keys of its children.

# Heaps are efficient for operations that involve finding and 
# extracting the smallest or largest elements. The insertion and extraction
# operations have a time complexity of O(logn).

# Product n log n :: Combining these two terms, 
# O(nlogn) means that the algorithm's runtime increases almost linearly with 
# n, but with an additional logarithmic factor. This is generally more 
# efficient than O(n2) but less efficient than O(n).


# The heapq module provides an implementation of the heap queue algorithm, 
# also known as the priority queue algorithm. It is used for efficiently
# finding the smallest or largest elements in a collection.



