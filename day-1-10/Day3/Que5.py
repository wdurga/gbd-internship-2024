# You want to pick random items out of a sequence or generate
# random numbers., shuffle them, use seed .

import random

# Generate a random integer between 0 and 10
random_int = random.randint(0, 10)

# Generate a random float between 0 and 1
random_float = random.uniform(0, 1)

# Choose a random element from a sequence
sequence = ['apple', 'banana', 'cherry', 'date']
random_element = random.choice(sequence)

# Shuffle a sequence
random.shuffle(sequence)

# Control randomness with seeds
random.seed(50)
random_number_1 = random.randint(0, 100)
random.seed(50)
same_random_number_1 = random.randint(0, 100)

# Print the results
print("Random Integer:", random_int)
print("Random Float:", random_float)
print("Random Element:", random_element)
print("Shuffled Sequence:", sequence)
print("Random Number with Seed:", random_number_1)
print("Same Random Number with Seed:", same_random_number_1)


import random

# Set the seed value
random.seed(42)

# Generate random numbers
random_number_1 = random.randint(0, 100)
random_number_2 = random.uniform(0, 1)
random_element = random.choice(['apple', 'banana', 'cherry'])

# Print the results
print("Random Number 1:", random_number_1)
print("Random Number 2:", random_number_2)
print("Random Element:", random_element)


import random
random.seed(50)

def print_random():
    for i in range (5):
        print(random.randint(0, 100), end =' ')
print_random()

import numpy as np
np.random.seed(1)
x = np.random.randint(1, 7, size = 2)
print(x)
