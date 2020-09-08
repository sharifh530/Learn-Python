# List slicing is also work as a string slicing

li = ["work", 5, "dinner", True]

print(li)
# Reverse
print(li[::-1])

# String is immutable but list is not immutable we can change the values of list

li[0] = "sleep"

print(li)

# Copy list

li1 = li[:]

li1[1] = "work"

print(li)
print(li1)

# modify list

li1 = li

li1[3] = False

print(li)
print(li1)
