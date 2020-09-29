#!/usr/bin/env python3

# Series 1 Section
seed_list = ["Apples", "Pears", "Oranges", "Peaches"]

print(seed_list)
response = input("Please suggest an additional fruit: ")

new_list = seed_list[:]

new_list.append(response)
print(new_list)

response2 = int(input("Please suggest a number: "))
print(response2, new_list[response2 - 1])

new_list = (["Cherries"] + new_list)
print(new_list)
new_list.insert(0, "Lemons")
print(new_list)

for fruit in new_list:
    if fruit[0].upper() == "P":
        print(fruit)

# Series 2 Section
print(new_list)
new_list.pop(-1)
print(new_list)
double_list = new_list[:] * 2
print(double_list)
def get_input(seq):
    worst_fruit = (input("Which fruit would you like to remove? "))
    if worst_fruit.capitalize() in seq:
        for item in seq:
            if item == worst_fruit:
                seq.remove(item)
    else:
        print("Yeah, it has to be in the list to remove it...")
        get_input(seq)

get_input(double_list)
print(double_list)

# Series 3 Section
print(new_list)
print(len(new_list))

hated_fruits = []

for fruit in new_list:
    dislike = ""
    while dislike.lower() != "yes" and dislike.lower() != "no":
        dislike = input("Are you a fan of {}? >".format(fruit.lower()))
    if dislike.lower() == "no":
        hated_fruits.append(fruit)

for hated in hated_fruits:
    new_list.remove(hated)
print(new_list)

# Series 4 Section
crazy_fruits = []
for fruit in seed_list:
    crazy_fruits.append(fruit[::-1])

seed_list.pop(-1)
print(seed_list)
print(crazy_fruits)
