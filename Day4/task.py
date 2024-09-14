import random
import my_module


random_integer = random.randint(1,10)
print(random_integer)

print(my_module.my_favourite_number)     # Example of using our own created module

random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1,10)
print(random_float)