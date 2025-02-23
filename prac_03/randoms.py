import random

# Line 1: Generates a random integer between 5 and 20 (inclusive)
print(random.randint(5, 20))  # Smallest: 5, Largest: 20

# Line 2: Generates a random number from the range (3, 10) with a step of 2
print(random.randrange(3, 10, 2))  # Possible values: 3, 5, 7, 9

# Line 3: Generates a random floating-point number between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # Smallest: 2.5, Largest: 5.5

# Random number between 1 and 100 (inclusive)
random_number = random.randint(1, 100)
print(random_number)
