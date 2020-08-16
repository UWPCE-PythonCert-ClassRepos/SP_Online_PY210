#!/user/bin/env python3

fruit = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruit)
fruit.append(input("Add another fruit> "))
print(fruit)
num = int(input("Give me a number between 1 and 5> "))
print(f"{num}: {fruit[num-1]}")
response = input("Add a fruit again> ")
fruit = [response] + fruit
print(fruit)
fruit.insert(0, input("Add yet another fruit> "))
print(fruit)