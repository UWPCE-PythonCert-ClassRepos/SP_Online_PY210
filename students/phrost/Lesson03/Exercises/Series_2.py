fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)
del fruit[-1]
print(fruit)
fruit_2 = fruit[:] + fruit[:]
print(fruit_2)
polling_active = True
while polling_active:
    fruit_d = input('Please select a fruit to delete: ')
    if fruit_d in fruit_2:
        fruit_2.remove(fruit_d)
    if fruit_d in fruit_2:
        fruit_2.remove(fruit_d)
        polling_active = False
print(fruit_2)
