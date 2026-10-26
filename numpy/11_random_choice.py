import numpy as np

rng = np.random.default_rng()
fruits = np.array(["apple", "banana", "cherry", "date"])

random_fruit = rng.choice(fruits)
print("Random fruit:", random_fruit)
