"""
RANDOM MODÜLÜ
"""

import random

# ------------------------------
# random() -> 0 ile 1 arasında
# ------------------------------
print(random.random())

# ------------------------------
# randint() -> Dahil
# ------------------------------
print(random.randint(1, 10))

# ------------------------------
# randrange() -> Son dahil değil
# ------------------------------
print(random.randrange(1, 10))

# ------------------------------
# choice()
# ------------------------------
myList = ["black", "white", "orange"]
print(random.choice(myList))

# ------------------------------
# choices() -> Ağırlıklı seçim
# ------------------------------
myList = ["cherry", "strawberry", "grape", "banana"]
print(random.choices(myList, weights=[10,1,1,1], k=5))

# ------------------------------
# shuffle() -> Listeyi değiştirir
# ------------------------------
myList = ["harley", "bmw", "honda"]
random.shuffle(myList)
print(myList)

# ------------------------------
# sample() -> Listeyi bozmaz
# ------------------------------
print(random.sample(myList, k=2))

# ------------------------------
# uniform()
# ------------------------------
print(random.uniform(30, 70))

# ------------------------------
# triangular()
# ------------------------------
print(random.triangular(30, 70, 33))

# ------------------------------
# getrandbits()
# ------------------------------
print(random.getrandbits(8))
