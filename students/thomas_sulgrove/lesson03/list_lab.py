#!/usr/bin/env python3
##SP_Online_PY210 lesson03 list lab https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/list_lab.html


def Series1():
    #Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
    fruits = ["Apples", "Pears", "Oranges", "Peaches"] 
    #Display the list (plain old print() is fine…)
    print(fruits) 
    #Ask the user for another fruit and add it to the end of the list
    response = input("Please list another fruit: ")
    fruits.append(response)
    #Display the list.
    print(fruits)
    #Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis).
    #Remember that Python uses zero-based indexing, so you will need to correct.
    response = int(input("Please a number between 1 and " + str(len(fruits)) + ": "))
    print(fruits[response - 1])
    #Add another fruit to the beginning of the list using “+” and display the list
    fruits = ["Alvocados"] + fruits #didnt know it was a fruit but it is. https://en.wikipedia.org/wiki/Avocado
    print(fruits) 
    #Add another fruit to the beginning of the list using insert() and display the list
    fruits.insert(0,"Blueberries")
    print(fruits)
    #Display all the fruits that begin with “P”, using a for loop.
    for produce in fruits:
        if produce[0] == "P": #check first index of each interation
            print(produce)
    return fruits

#Using the list created in series 1 above
Fruit_List = Series1()

def Series2(Fruit = Fruit_List.copy()): #make a copy of the list so you can make changes and not blow everything up.
    #Display the list.
    print(Fruit)
    #Remove the last fruit from the list.
    Fruit = Fruit[:-1]
    #Display the list.
    print(Fruit)
    #Ask the user for a fruit to delete, find it and delete it.
    response = input("List a fruit to remove: ")
    #(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
    while not(response in Fruit):
        response = input("That fruit is not in the list, please list another: ")
        Fruit *= 2
    Fruit.remove(response) #this removes it.
    return Fruit
        
def Series3(Fruit = Fruit_List.copy()): #Again, using the list from series 1.  This is why its copied.
    #Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
    print(Fruit)
    fruit_length = len(Fruit) - 1 #how many inital iterations to work through
    i = 0 # set iterator
    while i <= fruit_length:
        #pester user for response
        response = input("Do you like " + Fruit[i] + "? ") 
        #check if good answer
        while response not in ["yes", "no"]: 
            #the user is wrong as usual and the question will repease until they get it right
            print("Please answer yes or no") 
            response = input("Do you like " + Fruit[i] + "? ")
        #For each “no”, delete that fruit from the list.
        if response.lower() == "no":
            Fruit.remove(Fruit[i])
            #adjust iterator and fruit length for the deleted fruit
            i -= 1
            fruit_length -= 1
        #iterate
        i += 1
    return Fruit

def Series4(Fruit = Fruit_List.copy()): #useing Series 1 again
    #make a copy
    Fruit_Copy = Fruit.copy()
    #loop through and reverst the letters
    for i in range(len(Fruit_Copy)):
        Fruit_Copy[i] = Fruit_Copy[i][::-1]
    #delete last item from orig
    Fruit = Fruit[:-1]
    #print them.
    print(Fruit)
    print(Fruit_Copy)
    return







