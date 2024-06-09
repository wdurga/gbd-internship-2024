# Eg_2 = portfolio = [
# {'name': 'ABC', 'shares': 100, 'price': 91.1},
#  {'name': 'DEF', 'shares': 50, 'price': 543.22},
#  {'name': 'FB', 'shares': 200, 'price': 21.09},
#  {'name': 'ABC', 'shares': 300, 'price': 305}
# ]
# find the largest and smallest three portfolios based on their price. 

import heapq

portfolio = [
    {'name': 'ABC', 'shares': 100, 'price': 91.1},
    {'name': 'DEF', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'ABC', 'shares': 300, 'price': 305}
]

largest_3  = heapq.nlargest(3, portfolio, key=lambda x: x['price'])
print("Largest 3 by price:", largest_3)
    
smallest_3 = heapq.nsmallest(3, portfolio, key=lambda x: x['price'])
print("Smallest 3 by price:", smallest_3)
    
 
    #  3 is now number of elements to retrieve
    # portfolio is the list from which to retrieve the elements
    # lambda fxn extracts the "price" value from each dictionary for comparison.
    
    # heapq.nlargest(n, iterable, key) returns the n largest elements from
# the iterable, ordered by the specified key.

# The key parameter is used to specify a function that extracts a comparison 
# key from each element in the iterable. This determines how the elements are compared.