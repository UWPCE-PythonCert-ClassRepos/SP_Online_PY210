#!/usr/bin/env python3

# Series 1
print("Series 1 ---------------")
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

fruit.append(input("Plese enter a fruit: ").title())
print(fruit)

prompt = "Choose a number (between 1 and " + str(len(fruit)) + "): "
user_choice = int(input(prompt))
print("You selected: ", user_choice, "--", fruit[user_choice-1])

fruit = ["Mangos"] + fruit
print(fruit)

fruit.insert(0, "Grapes")
print(fruit)

for name in fruit:
    if (name[0] == "P"):
        print(name)

# Series 2
print()
print("Series 2 ---------------")
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

fruit.pop()
print(fruit)

user_choice = input("Which one to delete: ").title()
if user_choice in fruit:
    fruit.remove(user_choice)

print(fruit)

# Series 3
print()
print("Series 3 ---------------")
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

for name in fruit[:]:
    while True:
        user_choice = input("Do you like " + name.lower() + "?")
        if (user_choice.lower() == "no"):
            fruit.remove(name)
            break
        if (user_choice.lower() == "yes"):
            break
print(fruit)

# Series 4
print()
print("Series 4 ---------------")
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)

fruit_name_reversed = []
for name in fruit:
    fruit_name_reversed.append(name[::-1])

del fruit[-1]

print(fruit)
print(fruit_name_reversed)

