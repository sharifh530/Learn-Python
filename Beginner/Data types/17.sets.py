# Set - set is an unordered collections of unique objects

my_set = {1, 2, 3, 4, 5, 6, 7, 8, 67, 3, 3}
your_set = {24, 36, 7, 7, 2, 9, 3, 7, 1, 79}
my_set.add(12)
my_set.add(5)  # will not be added beacause its already on set

print(my_set)

# Check item

print(5 in my_set)

# diffrence
print(my_set)
print(your_set)
print(my_set.difference(your_set))

# discard
print(my_set.discard(5))
print(my_set)


# intersection

print(my_set.intersection(your_set))
print(my_set)


# isdisjoint
print(my_set.isdisjoint(your_set))

# union
print(my_set.union(your_set))

# issubset
print(my_set.issubset(your_set))

# issuperset
print(my_set.issuperset(your_set))

# diffrence update
print(my_set.difference_update(your_set))
print(my_set)
