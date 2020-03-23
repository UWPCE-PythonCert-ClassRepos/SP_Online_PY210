#!/usr/bin/env python3

#SERIES 1
#Create a list that contains "Apples", "Pears", "Oranges" and "Peaches".
fruit = ["Apples", "Pears", "Oranges", "Peaches"]
#Display the list (plain old print() is fine).
print(fruit)
#Ask the user for another fruit and add it to the end of the list.
response0 = input("write another fruit you'd like to add ")
fruit.append(str(response0))
#Display the list.
print(fruit)
#Ask the user for a number and display the number back to the user
#and the fruit corresponding to that number (on a 1-is-first basis).
#Remember that Python uses zero-based indexing, so you will need to correct.
response1 = input("write index value of fruit youd like to select ")
print(response1)
print(fruit[int(response1)-1])
#Add another fruit to the beginning of the list using "+" and display the list.
fruit = ['Mango'] + fruit
print(fruit)
#Add another fruit to the beginning of the list using insert() and display the list.
fruit.insert(0, 'kiwi')
print(fruit)
#Display all the fruits that begin with "P", using a for loop.
for x in fruit:
    if x.startswith('P'):
        print(x)

#SERIES 2

#Using the list created in series 1 above:
#Display the list.
print(fruit)
#Remove the last fruit from the list.
fruit2=fruit[:-1]
#Display the list.
print(fruit2)
#Ask the user for a fruit to delete, find it and delete it.
response2 = input("which fruit would you like to delete?")
fruit2 = [x for x in fruit2 if x != response2]
print(fruit2)
#(Bonus: Multiply the list times two. Keep asking until a match is found.
#Once found, delete all occurrences.)
fruit2=fruit2*2
response3 = input("which fruit would you like to delete?")
if response3 not in fruit2:
    run = True
else:
    run= False
while run:
    print(fruit2)
    response3 = input("which fruit would you like to delete?")
    if response3 not in fruit2:
        run = True
    else:
        fruit2 =[x for x in fruit2 if x != response3]
        print(fruit2)
        run= False
        
#SERIES 3
#Again, using the list from series 1:
print(fruit)
#for each fruit in the list (making the fruit all lowercase).
fruit3 = [item.lower() for item in fruit]

for i in fruit3:
#Ask the user for input displaying a line like "Do you like apples?"
    response4 = input("Do you like {}".format(i))
#For any answer that is not "yes" or "no":
    if response4 not in ['no', 'yes']:
        run=True
#(a while loop is good here)
        while run:
#prompt the user to answer with one of those two values 
            print("please write 'no' or 'yes'")
            response4 = input("Do you like {}".format(i))
            if response4 not in ['no', 'yes']:
                run=True
            else:
                run=False
#For each "no", delete that fruit from the list.
    if response4 == 'no':
        fruit3 =[x for x in fruit3 if x != i]
#Display the list.
print(fruit3)
        
#SERIES 4
#Once more, using the list from series 1:
#Make a new list with the contents of the original,
#but with all the letters in each item reversed.
fruit4 = [item[::-1] for item in fruit]
#Delete the last item of the original list.
fruit4=fruit4[:-1]
#Display the original list
print(fruit)
#and the copy.
print(fruit4)