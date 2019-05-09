#!/usr/bin/env python3

# Series 1

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)
received_fruit = input("Another fruit, please. ---> ")
fruit.append(received_fruit)
print(fruit)
received_number = input("What number fruit would you like to know? ---> ")
print("Fruit number {} is ".format(received_number) +
      fruit[int(received_number)-1])
fruit = ["Durian"] + fruit
print(fruit)
fruit.insert(1, "Cantaloupe")
print(fruit)
for i in fruit:
    if i[0].upper() == 'P':
        print(i)
