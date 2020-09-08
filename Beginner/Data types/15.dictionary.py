# Dictionary

dictionary = {
    "item": ["pencil", "pen"],
    "available": True,
    "quantity": 5
}

print(dictionary["item"])
print(dictionary["item"][1])

my_list = [
    {
        "item": ["pencil", "pen"],
        "available": True,
        "quantity": 5
    },
    {
        "item": ["mouse", "rubber"],
        "available": True,
        "quantity": 5
    },
    {
        "item": ["mask", "wire"],
        "available": True,
        "quantity": 5
    }
]

print(my_list[1]["item"][0])
print(my_list[1]["available"])

# pop

print(my_list[0].pop("quantity"))
print(my_list)

# update

print(my_list[1].update({"available": False}))
print(my_list)
