#!/usr/bin/env python3
#The list lab exercise created by Niels Skvarch
#"""
# series 1
#create a list and display it
fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruits)

#prompt user for a new fruit and add it to the list
new_fruit = input("What is your favorite fruit?: ")
fruits.append(new_fruit)

print(fruits)

n = int(input("Pick a number between 1 and {}:" .format(len(fruits))))
print("The number {} is the fruit {} in this list.".format(n, fruits[n-1]))

#add another fruit to the beginning of the list and display the list
fruits = ["Mangoes"] + fruits
print(fruits)

#add yet another fruit to the beginning of the list and display the list
fruits.insert(0, "Pomegranate")
print(fruits)

#display the list of fruits that begin with the letter "p"
for i in fruits:
    if i.startswith("P"):
        print(i)

#"""
#series 2
#copy the list
fruits2 = fruits[:]
print(fruits2)

#remove the last item from the list and display the list
fruits2.remove(fruits2[-1])
print(fruits2)

#multiply the list by 2
fruits2a = fruits2*2

#prompt for a fruit to be removed and then remove both instances of that fruit then display the list
del_a_fruit = input("What fruit sould be removed from the list?: ")
fruits2a.remove(del_a_fruit)
fruits2a.remove(del_a_fruit)
print(fruits2a)


#series 3
#copy the list from series 1 and display it
fruits3 = fruits[:]
print(fruits3)

#Step through each fruit asking for input to remove the fruit or not
for i in fruits:
    del_fruit = input('Do you like {}? yes or no: '.format(i.lower()))
    while(del_fruit.lower() != "yes" and del_fruit.lower() != "no"):
        del_fruit = input("\nDo you like {}? (Please give a 'Yes' or 'No' answer.) ".format(i.lower()))
    if(del_fruit.lower() == 'no'):
        fruits3.remove(i)
print(fruits3)


#"""
#series 4
#reverse the order of each item in the list then display the list
fruits4 = []
for fruit in fruits:
    fruits4 += [fruit[::-1]]
print(fruits4)

#remove the last item from the original list then display the list with the reversed list
fruits.remove(fruits[-1])
print(fruits + fruits4)




