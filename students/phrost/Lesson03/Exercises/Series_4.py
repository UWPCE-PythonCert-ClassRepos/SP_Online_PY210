fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruit_r = [value[::-1] for value in fruits]
del fruits[-1]
print(fruits)
print(fruit_r)
