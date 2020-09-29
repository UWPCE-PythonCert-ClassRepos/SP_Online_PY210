'''Series 1 actions'''
fruits = ['Apples','Pears','Oranges','Peaches']
print(fruits)
response = input("Please enter another fruit > ")
fruits.append(response)
print(fruits)
response_two = input("Please enter a number > ")
print(response_two)
print(fruits[int(response_two)-1])
fruits = ['Grapes'] + fruits
print(fruits)
fruits.insert(0, 'Kiwi')
print(fruits)
for i in range(len(fruits)):
    if fruits[i][0] == 'P':
        print(fruits[i])
'''Series 2 actions'''
fruits_2 = fruits.copy()
print(fruits_2)
fruits_2.pop()
print(fruits_2)
response_three = input("Please remove a fruit > ")
fruits_2.remove(response_three)
'''Series 3 actions'''
fruits_3 = fruits.copy()
response_four = ''
for i in range(len(fruits)):
    response_four = input("Do you like " + fruits[i].lower() + "? > ")
    while response_four != 'no' and response_four != 'yes':
        response_four = input("yes or no > ")
    if response_four == 'no':
        fruits_3.remove(fruits[i])
print(fruits_3)
'''Series 4 actions'''
fruits_4 = fruits.copy()
for i in range(len(fruits_4)):
    fruits_4[i] = fruits_4[i][::-1]
fruits.pop()
print(fruits_4)
print(fruits)