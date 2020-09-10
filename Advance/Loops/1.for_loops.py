# For loops

items = [1, 2, 3, 4, 5, 6]

for item in items:
    print(item)


# Iterable

user = {
    "name": "Harry potter",
    "age": 15,
    "Muggle": False
}

for user in user:
    print(user)


# Count array numbers

li = [1, 2, 3, 4, 5, 6, 7, 9]

counter = 0

for item in li:
    counter += item

print(counter)

# Range

print(range(0, 10))

for number in range(0, 10):
    print(number)

for _ in range(11, 20, 2):
    print(_)


for x in range(30, 21, -1):
    print(x)
