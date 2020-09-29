#!/usr/bin/env python3

#Series 1
#Create and do modifications on list
#including pop, append, +,insert
#

print("--------Series 1 started--------")
fruit_list=["Apples","Pears","Oranges","Peaches"]
print("The fruits mentioned in fruit list are:", fruit_list)

new_fruit=input("Name the new fruit want to add in list : ")
fruit_list.append(new_fruit.title())
print("The fruits list is: ",fruit_list)

print()
fruit_num=int(input("Provide the number to see fruit from the list on that number "))
print(fruit_list[fruit_num-1])

print()
new_flist=input("Provide new fruit name for beginning of the list using '+' ")
new_flist=[new_flist.title()]
fruit_list=new_flist+fruit_list
print("The new list is : ", fruit_list)

print()
new_ilist=input("Name the new fruits name to add in beginning using insert ")
fruit_list.insert(0,new_ilist.title())
print("The new list is :", fruit_list)

print
print("Fruits with names starting with P are: ")
for item in fruit_list:
    if item[0]=="P":
        print(item,end=" ")
print()

#
#Series 2
#Modify first series fruits list
#

print()
print("--------Series 2 started--------")
print("The final list from first series is:",fruit_list)
print(fruit_list.pop())
print("List after removing last fruit from list:",fruit_list)

dfruit=input("Name the fruit want to delete: ")

for item in fruit_list:
    if item == dfruit.title():
        fruit_list.remove(item)
        print("Final list after deleting "+ dfruit.title()+ " is",fruit_list)
        break
else:
    print(dfruit.title(), "can not be deleted as it's not in list")

#
#
#series 3
#deleting values from using while loop
#
print()
print("--------Series 3 started--------")
i=0
f_list=fruit_list[:]
length=(len(fruit_list))
while i < length:
    resp=input("Do you like " + f_list[i].lower()+"?")
    if resp == "no":
        fruit_list.remove(f_list[i])
        i=i+1
    elif resp == "yes":
        i=i+1
    else:
        print("Please enter yes or no")
print(fruit_list)

#
#
#Series 4
#copying and removing the items from list along with reversing the list values
#
print()
print("--------Series 4 started--------")
reverse_list=[]

for item in fruit_list:
    reverse_list.append(item[::-1])

print(reverse_list)

copy_list=fruit_list

print("Fruit removed form list using pop method is:",fruit_list.pop())
print("Original List is:", fruit_list)
print("Copied List is :", copy_list)
