import random

from Day4.task import random_integer

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
#Method 1
random_index = random.randint(0,4)
print(friends[random_index])

#Method 2
print(random.choice(friends))