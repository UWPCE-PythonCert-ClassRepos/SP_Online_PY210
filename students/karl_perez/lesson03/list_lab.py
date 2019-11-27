#!/usr/bin/env python3

"""Series 1"""
#Create a list that contains “Apples”, “Pears”, “Oranges” and “Peaches”.
list_original = ['Apples', 'Pears', 'Oranges', 'Peaches']
series1 = list_original[:]
#Display the list (plain old print() is fine…).
print(series1)
#Ask the user for another fruit and add it to the end of the list.
user = input('Add another fruit please:\n')
series1.append(user)
#Display the list.
print(series1)
#Ask the user for a number and display the number back to the user and the fruit corresponding to that number (on a 1-is-first basis). Remember that Python uses zero-based indexing, so you will need to correct.
num = input('Please give a number. ')
integ_num = int(num)
print(integ_num, series1[integ_num-1])
#Add another fruit to the beginning of the list using “+” and display the list.
series1 = ['Grapes'] + series1
print(series1)
#Add another fruit to the beginning of the list using insert() and display the list.
series1.insert(0,'Bananas')
print(series1)
#Display all the fruits that begin with “P”, using a for loop.
fruits_p = []
for i in series1:
    if i[0] == 'P':
        fruits_p.append(i)
    print("Display all the fruits that begin with 'P': {}".format(fruits_p))

"""Series 2"""
#Display the list.
print(list_original)
series2 = list_original[:]
#Remove the last fruit from the list.
series2.pop()
#Display the list.
print(series2)
#Ask the user for a fruit to delete, find it and delete it.
user_1 = input("Pick a fruit to remove please: ")
if user_1 not in series2:
    print("Please choose a fruit from the list.") 
else:
    series2.remove(user_1)
    print(series2)
#(Bonus: Multiply the list times two. Keep asking until a match is found. Once found, delete all occurrences.)
series2 = series2 * 2
print("multipling the list by 2:")
print(series2)
user_2 = input("Enter another fruit to remove please: ")
while user_2 in series2:
	series2.remove(user_2)
print(series2)

# """Series 3"""
series3 = list_original[:]
#Ask the user for input displaying a line like “Do you like apples?” for each fruit in the list (making the fruit all lowercase).
for fruits in series3[:]:
    user_3 = input("Do you like" + " " + fruits + "?\n")
#For each “no”, delete that fruit from the list.
    if user_3 == 'no':
        series3.remove(fruits)
    elif user_3 == 'yes':
         continue
#For any answer that is not “yes” or “no”, prompt the user to answer with one of those two values
    else:
         print("Please answer with either 'yes' or 'no'")
#Display the list.
print(series3)

"""Series 4"""
series4 = list_original[:]
new_series_list = []
#Make a new list with the contents of the original, but with all the letters in each item reversed.
for fruit in series4:
    new_series_list.append(fruit[::-1])
print(new_series_list)
#Delete the last item of the original list.
del list_original[-1]
#Display the original list and the copy.
print(list_original)
























