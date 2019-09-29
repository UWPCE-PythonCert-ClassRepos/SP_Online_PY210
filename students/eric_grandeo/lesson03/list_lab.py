#!/usr/bin/env python3

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

response = input("Please enter in a new fruit > ")
fruits.append(response)

print(fruits)

num = int(input("Please enter a number > "))
print("You selected number {}, which is {}".format(num, fruits[num-1]))





    