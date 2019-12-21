#!/usr/bin/env python3

#Series 1 lists
print("Series 1\n")
list1 = ["Apples", "Pears", "Oranges", "Peaches"]
print(list1)

add1 = input("\nPlease give another fruit: \n")
list1.append(add1)
print(list1)

index = int(input("\nGive me a number from 1 to " + str(len(list1)) + ".\n"))
print(index, " = ", list1[index-1],"\n")

list1 = ["Bananas"] + list1
print(list1)

list1.insert(0, "Watermelons")
print(list1)

for item in list1:
    if item[0] == "P":
    print(item)


#Series 2 lists
print("\nSeries 2\n")
list2 = list1[:]
print(list2)
del list2[-1]
print(list2)

#delete a fruit
item = input("\nWhich fruit to delete?\n")

list2a = [i for i in list2 if i != item]
print(list2a)

#Series 3 lists
print("\nSeries 3\n")
list3 = list1[:]

for item in list3:
    while True:
    ans = input("\nDo you like " + item.lower() + "?\n")
    if ans != "yes" and ans != "no":
    print("\nyes or no please!\n")
    elif ans == "no":
    list3a = [i for i in list3 if i != item]
    break

    else:
    break

print(list3a)


#Series 4 lists
print("\nSeries 4\n")
list4 = list1[:]

for i, item in enumerate(list4):
    list4[i]=item[::-1]

print(list1[:-1])
print(list4)
