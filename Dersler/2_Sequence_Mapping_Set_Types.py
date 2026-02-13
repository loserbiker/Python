"""
SEQUENCE TYPES
(list, tuple, range)
"""

# ------------------------------
# List (Değiştirilebilir)
# ------------------------------

myList = ["Apple", "Grape", "Cherry"]

# ------------------------------
# Tuple (Değiştirilemez)
# ------------------------------

myTuple = ("Red", "Blue", "White")

# ------------------------------
# Range
# ------------------------------

myRange = range(7)

print(*myRange)

# ------------------------------
# Dictionary (Mapping Type)
# ------------------------------

myDict = {"name": "Can", "yas": 27}
print(myDict)

# ------------------------------
# Set Types
# ------------------------------

mySet = {"Apple", "Grape", "Cherry"}

myFrozen = frozenset({"Apple", "Grape", "Cherry"})

# ------------------------------
# Boolean ve None
# ------------------------------

myBool = True
myNone = None

print(type(myBool))
print(type(myNone))
