# Tuples - its more like list and its immutable

my_tuple = (1, 2, 3, 4, 5, 6)

print(my_tuple)
print(my_tuple[2])
print(5 in my_tuple)

# Tuples in dictonary

user = {
    ("id", "value"): [5, 150],  # use tuple of immutability
    "name": "Sazzad",
    "contact": 4523424
}

print(user[("id", "value")])

# Tuple unpacking

x, y, z, *other = (1, 2, 3, 4, 5, 6, 7, 8)

print(x)
print(y)
print(z)
print(other)

print(other.count(4))
print(other.index(6))
print(len(other))
