#!/usr/bin/env python3
"""This is an exercise in which we sort a list of fruit with user input"""
print("Series 1")
fruits=["Apples","Pears","Oranges", "Peaches"]
print("\n",fruits)
new_fruit=input(" \nPlease type the name of a fruit: ")
fruits.append(new_fruit)
print("\n",fruits)
number=int(input(" \nPlease select a number between 1 and {}: ".format(len(fruits))))
print("\n",number,":",fruits[number-1])
fruits=["Pineapple"]+fruits
print("\n",fruits)
fruits.insert(0,"Dragon Fruit")
print("\n",fruits)
for fruit in fruits:
    if fruit[0]=="P":
        print("\n",fruit)

print("\nSeries 2")
s2_fruits=fruits[:]
print("\n",s2_fruits)
del(s2_fruits[len(s2_fruits)-1])
print("\n",s2_fruits)
badfruit=input(" \nSelect a fruit to remove: ")
s2_fruits.remove(badfruit)
s2_fruits=s2_fruits*2
fruitbool=0
while fruitbool==0:
    badfruit=input(" \nSelect another fruit to remove: ")
    if badfruit in s2_fruits:
        while badfruit in s2_fruits:
            s2_fruits.remove(badfruit)
        fruitbool=1
    else:
        print(" \nPlease choose a fruit in the list")

print("\nSeries 3")
s3_fruits=fruits[:]
for fruitz in s3_fruits[:]:
    fruitpref=input(" \nDo you like {choice}?".format(choice=fruitz))
    while fruitpref.lower() not in {"yes","no"}:
        fruitpref=input(" \nPlease enter yes or no.")
    if fruitpref.lower()=="no":
        s3_fruits.remove(fruitz)
print("\n",s3_fruits)
        
print("\nSeries 4")
s4_fruit=[]
for fruit in fruits[:]:
    s4_fruit.append(fruit[::-1])
fruits.remove(fruits[len(fruits)-1])
print("\n",s4_fruit,"\n",fruits)




