#!/usr/bin/env python3

# series 1
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
fruitprompt = ''

print(fruits)

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
