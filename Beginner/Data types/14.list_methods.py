# List Methods

basket = [1, 2, 3, 4, 5, 6, 7, 8]

print(basket)

# append

basket.append(9)
new_basket = basket

print(new_basket)

# insert

basket.insert(5, 66)
new_basket = basket

print(new_basket)

# extend

basket.extend([10, 11, 12])

new_basket = basket
print(new_basket)

# Remove

# pop
basket.pop()
basket.pop(11)
print(basket)

# remove
basket.remove(66)
print(basket)

# basket.clear()
# print(basket)

# Index

print(basket.index(4))

print(3 in basket)
print(16 in basket)
print(basket.count(2))

# reverse

basket.reverse()
print(basket)

# Sort
basket.sort()
print(basket)
print(sorted(basket))

# Range

print(list(range(101)))

# Join

sentence = " "

print(sentence.join(["is", "everything", "fine?"]))

# List unpacking

a, b, c = [1, 2, 3]

print(a)
print(b)
print(c)

d, e, f, *g, h = [4, 5, 6, 7, 8, 9, 10]

print(d)
print(e)
print(f)
print(g)
print(h)
