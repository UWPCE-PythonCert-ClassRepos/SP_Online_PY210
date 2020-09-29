#Series 1

Fruits=["Apples", "Pears", "Oranges", "Peaches"]
print(Fruits)

New_Fruit=input('Please add another fruit to the list: ')
Fruits.append(str(New_Fruit))
print(Fruits)

User_input=int(input('Please choose a fruit by providing a number: '))
if User_input < 1:
    print("Pleasa pick a number greater than zero")
else:
    print("You choose:", User_input, Fruits[User_input-1])

addFruit = "Coconut"
Fruits= [addFruit]+Fruits
print(Fruits)


Fruits.insert(0,'Kiwi')
print(Fruits)

for fruit in Fruits:
    if fruit.startswith('P'):
        print(fruit)

#Series 2
print(Fruits)
del Fruits[-1]
print(Fruits)


a =input('Which fruit do you want to delete: ')
if a in Fruits:
    Fruits.remove(a)
else:
    print(a,"cannot be deleted because it is not on the list")
print(Fruits)

#Series 3
def user_input_list():
    index = 0
    while index <= len(Fruits):
        #for i in range(len(Fruits)):
     #while True:
        for i, fruits in enumerate(Fruits):
        #for i in Fruits:
            fruitchoice = input('Do you like ' + Fruits[i]+'? yes/no  ')
            if fruitchoice == 'no':
                del Fruits[i]
            elif fruitchoice == 'yes':
                continue
            else:
                print("Please answer yes or no only")
        #break
        #print(Fruits)
user_input_list()
print(Fruits)

#Series 4
New_Fruit= Fruits.copy()
Rev_strings = [x[::-1] for x in New_Fruit][::-1]
print(Rev_strings)
del Fruits[-1]
print(Fruits)
print(New_Fruit)
