
# Series 1
fruits = ['Apples','Pears','Oranges','Peaches']
print(fruits)
user_fruit = [input('Please name another fruit.  ')]
fruits = fruits + user_fruit
print(fruits)
num = int(input('Please give a number. '))
print(num, fruits[num-1])
fruits = ['Bananas']+fruits
print(fruits)
fruits.insert(0,'Strawberrys')
print(fruits)

for i in fruits:
	if 'P' in i:
		print(i)

# Series 2
fruits2 = fruits.copy()
print(fruits2)
del fruits2[-1:]
print(fruits2)
user_del_fruit = input("Name a fruit to be deleted. ")
fruits2.remove(user_del_fruit)

# Series 3
fruits3 = fruits.copy()
for i in fruits3[:]:
	print('Do you like ', i.lower()+'?')
	question = input('')
	while question != 'yes' and question != 'no':
		print('Please enter yes or no.')
		question = input("")
	if question == 'yes':
		continue
	elif question == 'no':
		fruits3.remove(i)

print(fruits3)

# Series 4
fruits4 = fruits.copy()
newlist = []
for i in fruits4:
	newlist = newlist + [i[::-1]]
del fruits[-1:]
print(newlist)
print(fruits)
print(fruits4)


