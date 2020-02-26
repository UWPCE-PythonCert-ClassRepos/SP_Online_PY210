#!/usr/bin/env python3

original_list = ["Apples", "Pears", "Oranges", "Peaches"]
# Series 1
fruit = original_list[:]
print(fruit)
response = input("What is your favorite fruit? ")
fruit.append(response)
user_number = input("Pick a number from 1 - " + str(len(fruit)) + " ")
print("Your fruit is " + fruit[int(user_number) - 1])
fruit = ["Grapes"] + fruit
print(fruit)
fruit.insert(0, "Blueberries")
for f in fruit:
    if f[0] == 'P':
        print(f)
print(fruit)
# Series 2
fruit = original_list[:]
print(fruit)
fruit.remove(fruit[-1])
print(fruit)
remove_fruit = input("Name your least favorite fruit: ")
if remove_fruit in fruit:
    fruit.remove(remove_fruit)
print(fruit)
# Series 2 Bonus
fruit = original_list[:] * 2
print(fruit)
count = 0
while count == 0:
    remove_fruit = input("Bonus! Name your least favorite fruit: ")
    count = fruit.count(remove_fruit)
for i in range(count):
    fruit.remove(remove_fruit)
print(fruit)
# Series 3
fruit = original_list[:]
for f in fruit[:]:
    like_response = ""
    while like_response.lower() != "yes" and like_response.lower() != "no":
        like_response = input("Do you like " + f.lower() + "(yes/no)? ")
        if like_response.lower() == "no":
            fruit.remove(f)
print(fruit)
# Series 4
fruit = original_list[:]
fruit.reverse()
backward_fruit = []
for f in fruit:
    backward_fruit.append(f[::-1])
fruit.reverse()
fruit.pop()
print(fruit)
print(backward_fruit)
