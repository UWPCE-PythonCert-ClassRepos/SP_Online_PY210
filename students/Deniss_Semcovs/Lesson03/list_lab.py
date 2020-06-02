#!/usr/bin/env python3
list01 = ['Apples', 'Pears', 'Oranges', 'Peaches']
print("Original list:")
for i in list01:    #Display the list
    print(i)
response = input("Please enter a fruit: ")
list01.append(response) #add it to the end of the list
print("Adding new item to the end of the list")
for i in list01:    
    print(i)
    

v = int(input("Please enter the item number: ")) #This doesn't work- error: 'str' object is not callable
v1=v-1 #Python uses zero-based indexing - fixed
print(v,(list01[v1]))  #display the number back to the user and the fruit corresponding to that number


fruit02 = input("Please enter a new fruit: ")
list02 = [fruit02]+list01 #Add another fruit to the beginning of the list using “+” and display the list
print("Adding new iten to the beginning of the list")
for i in list02:
    print(i)
fruit03 = input("Please enter a new fruit: ")
list02.insert(0, fruit03) #Add another fruit to the beginning of the list using insert() and display the list
print("Adding new iten to the beginning of the list")
for i in list02:
    print(i)
print("Printing items starting with 'P':")
for item in list02: #Display all the fruits that begin with “P”, using a for loop.
    if "P" in item:
        print(item)
print(("_")*15) #Starting Series2
print("Series 2")
for i in (list02):
    print(i)
print("Removing last Item")
for i in (list02[:-1]): #Remove the last fruit from the list.
    print(i)
rem = input("Which item would you like to remove from the list: ")
for i in list02: #Ask the user for a fruit to delete, find it and delete it
    if rem == i:
        continue
    print(i)
print(("_")*15) #Starting Series3
print("Series 3")

for i in list01:
    choice = input(("Do you like {}? yes/no: ").format(i).lower())
    if choice == "no": #For each “no”, delete that fruit from the list
        list01.remove(i) 
print("New list:")
print(list01)

print(("_")*15) #Starting Series4
print("Series 4")
list03 = list01
for i in list03:
    print(i[::-1])  # all letters in each item reversed
print(list03) # copy of original list  
print(list03[:-1]) # last item deleted
