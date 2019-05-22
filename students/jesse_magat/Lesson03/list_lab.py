
print("**Series1***")
#Series 1
#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”

fruit_list = ['Apples','Pears','Oranges','Peaches']
print(fruit_list)
#Ask user for another fruit_list
user_add_fruit = input("please provide a fruit name: ")
user_add_fruit_a = user_add_fruit.capitalize()
fruit_list.append(user_add_fruit_a)
print(fruit_list)

while True:
	try:
		choose_number = input("please choose a number within the list of fruits above: ")

#subtract 1 to get the right index in the list

		choose_number_1 = int(choose_number) -1
		print(fruit_list[choose_number_1]) #see if the number chosen was on the list
	except:
		print("please choose a number within the number of fruit items")
	else:
		break

#add another fruit and add it in the first value on the list

user_add_fruit2 = input("please select another fruit name: ")
#added list to avoid this error "can only concatenate str (not "list") to str"
#converted the input to a list
user_add_fruit2_a = user_add_fruit2.capitalize()
user_new_fruit = [user_add_fruit2_a] #use brackets to get list result

#put second new item in the front
new_list = user_new_fruit + fruit_list
fruit_list = new_list
print(fruit_list)


user_add_fruit3 = input("please select another fruit name: ")

user_add_fruit3_a = user_add_fruit3.capitalize()
user_add_fruit3 = user_add_fruit3_a

fruit_list.insert(0, user_add_fruit3)
print(fruit_list)


#Display all the fruits that begin with “P”, using a for loop.

print("Fruits that starts with 'P' in the list: ")
for i in fruit_list:
	if i[0] =='P':
		print(i,"\n")
		
#Series 2

print("***Series2*** \n")

print(fruit_list)

#delete last item in the list
fruit_list2 = fruit_list[:len(fruit_list)-1]
print(fruit_list2,"\n")


while True:
	try:
		user_delete = input("please select a fruit on the list to be removed: ")

		user_delete_a = user_delete.capitalize()

		user_delete = user_delete_a

		fruit_list2.remove(user_delete)
		print(fruit_list2,"\n")
		break #added break or else it will keep asking to remove items
	except:
		
		print("please select value that is in the list")
		

print("***Series3***","\n")
		
		
#Series 3

fruit_list3 = fruit_list

for fruit in fruit_list3[:]:
    user_delete2 = input("Do you like {}? (yes/no): ".format(fruit)) #used .format function 
    if user_delete2 not in ("yes","no"): #error handling to only get yes/no answers
        user_delete2 == input("please type yes/no: ")
    else:
        if user_delete2 == "no":
            fruit_list.remove(fruit)
print(fruit_list3, "\n")
        


print("***Series4*** \n")

fruit_list4 = ['Apples','Pears','Oranges','Peaches']

reversed_list = []

for fruit in fruit_list4:
	reversed_list.append(fruit[::-1])
print(reversed_list)

copy = ['Apples','Pears','Oranges','Peaches']
fruit_list4 = fruit_list4[:len(fruit_list4)-1]
print(fruit_list4,"original list with last item removed")
print(copy, "copy of original before deleting the last item")

	






