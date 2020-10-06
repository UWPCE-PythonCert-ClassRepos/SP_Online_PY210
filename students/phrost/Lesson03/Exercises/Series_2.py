fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)
del fruit[-1]
print(fruit)
fruit_d = input('Please select a fruit to delete: ')
fruit_d = int(fruit_d)
for value, response in enumerate(fruit, start=1):
    if value == fruit_d:
        fruit.remove(response)
print(fruit)
