#!/usr/bin/env python3

# series 1
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']

print(fruits)

fruitprompt = ''
while not fruitprompt:
    fruitprompt = input('Name a fruit, any fruit! ')
fruits.append(fruitprompt)

print(fruits)

fruitprompt = input('Ok, now pick a number! ')

if int(fruitprompt) < 1: # this will technically /work/ but it's not in the spirit of the problem :)
    print("I don't have a fruit number {}".format(fruitprompt))
else:
    try:
        print("Fruit number {} is {}".format(fruitprompt, fruits[int(fruitprompt)-1]))
    except:
        # catch all manner of bad input, including not numbers and bad indicies
        print("I don't have a fruit number {} :()".format(fruitprompt))

newfruit = 'Kiwi'
fruits = [newfruit] + fruits
print(fruits)

fruits.insert(0, 'Dragonfruit')
print(fruits)

print("All the fruits that start with the letter of the day .. 'P'!")
for fruit in fruits:
    if fruit.startswith('P'):
        print(fruit)

# series 2
fruits2 = fruits[:]

print(fruits2)

fruits2.remove(fruits2[-1])

print(fruits2)

fruits2 = fruits2*2
while True:
    fruitprompt = input('What fruit are we deleting? ')
    if fruitprompt in fruits2:
        break

while fruitprompt in fruits2:
    fruits2.remove(fruitprompt)
