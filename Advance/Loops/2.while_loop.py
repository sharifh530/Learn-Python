# While loop

i = 0
while i < 50:
    print(i)
    i += 1
else:
  print("Done")


my_list = [1, 2, 3, 4, 5]
j = 0
while j < len(my_list):
    print(my_list[j])
    j += 1
else:
  print("Done")


# break , continue, pass
k = 0
while k < len(my_list):
    print(my_list[k])
    k += 1
    continue
    print("It will not print")
