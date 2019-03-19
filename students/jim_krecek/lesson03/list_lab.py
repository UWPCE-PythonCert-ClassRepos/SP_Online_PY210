#response = input("a prompt for the user > ")

# Series 1
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
for i in range(0,len(fruit)):
	if fruit[i][0] == 'P':
		pfruit.append(fruit[i])
	i += 1
print(pfruit)

# Series 2

