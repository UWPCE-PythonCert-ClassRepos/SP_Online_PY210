#series 1
#fruit list
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits, '\n')

# Adding respondent input to list
response = input('What fruit do you want to add? ')
fruits.append(response.capitalize())
print(fruits, '\n')

# returning number and fruit in list
fruitlen = len(fruits)
response2 = input('PLease pick a number from 1 to {}: '.format(fruitlen))
print('{} is item {} on the fruit list'.format(fruits[int(response2)-1], response2), '\n')

# adding 2 fruits to the list
print('Adding Mangos and Blueberries:')
fruits = ['Mangos'] + fruits
print(fruits, '\n')
fruits.insert(0, 'Blueberries')
print(fruits, '\n')

# printing all fruits that start with p
print('They start with p:')
for fruit in fruits:
    lcaseI = fruit.lower()
    if lcaseI.startswith('p'):
        print(fruit)
print('\n')


#series2
print('removing the last fruit:')
print(fruits)
fruits.pop(-1)
print(fruits, '\n')

# asking what they want to remmove, checking if it is in the list then removing if it is there
lowerfruits = [lfruit.lower() for lfruit in fruits]
response2 = input('What fruit would you like to delete? ')
print('\n')
while response2.lower() not in lowerfruits:
    print(fruits)
    response2 = input('What fruit would you like to delete? Please pick one from the list above. ')
else:
    for fruit in fruits:
        if fruit.lower() == response2.lower():
            fruits.remove(fruit)
print(fruits, '\n')


#series3
# going through the fruit list and deleting any fruits they dont like
ans = ['yes', 'no']
for fruit in fruits[::-1]:
    response3 = input('Do you like {}? '.format(fruit))
    while response3.lower() not in ans:
        response3 = input('Do you like {}? Please type yes or no. '.format(fruit))
    if response3.lower() == 'no':
        fruits.remove(fruit)
print(fruits, '\n')

#series4
print('new list and original', '\n')
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
newlist  = [fruit[::-1] for fruit in fruits]
print(newlist)
fruits.pop()
print(fruits)
