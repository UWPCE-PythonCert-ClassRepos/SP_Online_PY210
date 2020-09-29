# Lesson 3 List Lab Exercise

##Series 1
l1 = ["Apples","Pears","Oranges","Peaches"]
print (l1)

fruit_input = input("Add another fruit to the end of the list")
l1.append(fruit_input)
print (l1)

number_input = input ("Identify a fruit using number")
print (l1[int(number_input)-1])

l1 = ["grapes"] +l1
print(l1)

l1.insert(0,'cherries')
print(l1)

for i in l1:
    if i[0] == 'P':
        print(i)

##Series 2
l2 = l1

print (l2)

l2 = l2[:-1]

print (l2)

user_delete = input("Pick a fruit to delete")
for i, item in enumerate(l2):
    if item == user_delete:
        l2.pop(i)

print(l2)

##Series 3
l3 = l1

index_to_remove = []
for i, fruit in enumerate(l3):
    fruit = fruit.lower()
    likeness = input["Do you like {}?".format(l3.lower)]
    while likeness.lower() != 'yes' and likeness.lower() != 'no':
        likeness = input('only answer yes or no')
        if likeness.lower() == 'yes':
            pass
        elif likeness.lower() == 'no':
            index_to_remove.append(i)

index_to_remove.reverse()
for i in index_to_remove:
    l3.pop(i)
print(l3)

##Series 4
l4 = l1

for i, fruits in enumerate(l4):
    reverse = fruits[::-1]
    l4[i] = reverse

l1.pop()
print(l1)
print(l4)