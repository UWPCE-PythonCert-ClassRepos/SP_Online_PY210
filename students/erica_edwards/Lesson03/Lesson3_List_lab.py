#!/usr/bin/env python3

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print(fruits)

response = input("Please enter a new fruit. ")
fruits.append(response)
print(fruits)

response = int(input("Please enter a number. "))
number = response - 1
#print(number)
print(f'{response}  {fruits[number]}')

fruits = ['Bananas'] + fruits
print(fruits)

fruits.insert(0, 'Cherries')
print(fruits)

for fruit in fruits:
    #print(fruit)
    if fruit[0].upper() == 'P':
        print(fruit)

print('='*40)
print(f'{" "*14}Begin Series 2')
print('='*40)

print(fruits)

del fruits[-1]
print(fruits)

fruits = fruits * 2
print (fruits)
done = False 
while not done:
    response = input("Please enter a fruit to delete. ")
    if response in fruits:
        print('found it')
        # the_fruit = fruits.index(response)
        # del fruits[the_fruit]
        while response in fruits:
            fruits.remove(response)
        done = True
print(fruits)    

print('='*40)
print(f'{" "*14}Begin Series 3')
print('='*40)       
print(fruits)

for fruit in fruits[:]:
    done = False
    while not done:
        response = input(f"Do you like {fruit.lower()}? ")
        # print(response.upper())
        if response.upper() == 'NO': 
            fruits.remove(fruit)
            done = True
        elif response.upper() == 'YES':
            done = True
        else: 
            print('Please answer with a yes or no.')
print(fruits)

print('='*40)
print(f'{" "*14}Begin Series 4')
print('='*40)    

fruits = ["Apples", "Pears", "Oranges", "Peaches"]
fruits1 = [fruit[::-1] for fruit in fruits]
del fruits[-1]
print(fruits)
print(fruits1)


