fruit_upper = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruit_lower = [fruit.lower() for fruit in fruit_upper]
fruit_copy = list(fruit_lower)
for fruit in fruit_lower:
    while True:
        fruit_v = input(f'do you like {fruit}: ')
        if fruit_v.lower() == 'yes':
            break
        elif fruit_v.lower() == 'no':
            fruit_copy.remove(fruit)
            break
        else:
           print(f'please say yes or no do you like {fruit}: ')
print(fruit_copy)
