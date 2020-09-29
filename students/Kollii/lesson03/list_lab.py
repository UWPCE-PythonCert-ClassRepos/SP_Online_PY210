# Series 1
print("### Series 1 ###")

#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
fruit_list = ["Apples","Pears","Oranges","Peaches"]

#Display the list
print (fruit_list)

#Ask the user for another fruit and add it to the end of the list.
add_fruit = input("Name a fruit to add at the end of the above fruit list  ")
fruit_list.append(add_fruit)

#Display the list.
print (fruit_list)

#Ask the user for a number and display the number back to the user and the fruit corresponding to that number 
input_no = input ("Enter a  number and display the fruit corresponding to that number ")
print (fruit_list[int(input_no )-1])

#Add another fruit to the beginning of the list using “+” and display the list.
fruit_list = ["Mangoes"] +fruit_list
print("Another fruit added to the fruit list at the beginning", fruit_list)

#Add another fruit to the beginning of the list using insert() and display the list.
fruit_list.insert(0,'Kiwi')
print("Another fruit added", fruit_list)


#Display all the fruits that begin with “P”, using a for loop.
print("Display all the fruits that begin with “P”")
for x in fruit_list:
    if x[0] == 'P':
        print(x)


# Series 2

print("### Series 2 ###")
#Display the list created in series 1
print ("Fruits list created in Series 1", fruit_list)

fruit_list.pop()

print("Fruit list with the last fruit removed ", fruit_list)
delete_fruit = input("Enter Fruit name to delete from the list ")

for x, fruit in enumerate(fruit_list):
    if fruit.lower() == delete_fruit.lower():
        fruit_list.pop(x)

print("New List ", fruit_list)

# Series 3
print("### Series 3 ###")

#Display the list created in series 1
print ("Fruits list created in Series 1", fruit_list)

for fruit in fruit_list:
        prompt = input("Do you like " + fruit.lower() + "?")
        while  prompt.lower() not in ("yes", "no"):
            print("Please enter  Yes/No")
            prompt = input("Do you like " + fruit.lower() + " yes/no ?")
        if  prompt.lower() == "no":
            fruit_list.remove(fruit)
        
print(fruit_list)

# Series 4
print("### Series 4 ###")

#Display the list created in series 1
print ("Fruits list created in Series 1", fruit_list)

new_fruitlist = fruit_list[:]

print("new list with the contents of the original, with all the letters in each item reversed")

reversed_fruitslist = [fruit[::-1] for fruit in new_fruitlist[:]]
print(reversed_fruitslist)

print("Delete the last item of the original list")
fruit_list.pop()
print(fruit_list)

