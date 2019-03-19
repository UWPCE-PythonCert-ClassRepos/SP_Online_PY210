#response = input("a prompt for the user > ")

# Series 1
##################
print('Series 1')
fruit = ['Apples','Pears','Oranges','Peaches']
print(fruit)

#ask user for fruit
add = input('Name a fruit to add to the list ==> ')
fruit.append(add)
print(fruit)

#ask user to pick number for fruit from list
index = input('Name a number between 1 and %d to pick a fruit from the list ==> '%(len(fruit))) 
print(fruit[int(index)-1])

#add a fruit to beginning of list using +
fruit = ['Bananas'] + fruit
print(fruit)

#add a fruit to beginning of list using insert()
fruit.insert(0,'Pineapples')
print(fruit)

#display all fruits that begin with 'P'
pfruit = []
for i in range(len(fruit)):
    if fruit[i][0] == 'P':
        pfruit.append(fruit[i])
    i += 1
print(pfruit)

# Series 2
##################

print('Series 2')
print(fruit)
#delete last fruit
del fruit[-1]
print(fruit)

#ask user for a fruit to delete
delfruit = input('What fruit would you like to remove? ')
for i in range(len(fruit)):
    if delfruit.lower() == fruit[i].lower():
        del fruit[i]
        break
    i += 1
    
print(fruit)


# Series 3
##################

print('Series 3')
for f in fruit:
    q = input('Do you like %s ? ' %f)
    while not (q.lower() == 'yes' or 'no'):
        q = input('Please answer with either "yes" or "no" ')
    if q.lower() == 'no':
        fruit.remove(f)

print(fruit)

# Series 4
##################

print('Series 4')
reverse = []
for f in fruit:
    reverse.append(f[::-1])
print(reverse)
del reverse[-1]
print(reverse)
print(fruit)
