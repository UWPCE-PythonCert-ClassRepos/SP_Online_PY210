fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)
user_f = input('Please tell me another fav of your fruits: ')
fruit.append(user_f)
print(fruit)
fruit_num = input('Please enter a number between 1 and 5 for your fav fruit in list : ')
fruit_num = int(fruit_num)
for value, response in enumerate(fruit, start=1):
    if value == fruit_num:
        print(value,response)
single_fruit = ['banana']
fruits = single_fruit + fruit
print(fruits)
fruits.insert(0, 'grape_fruit')
print(fruits)
fruit_p = [fruite for fruite in fruit if(fruite[0] =='P')]
print(fruit_p)
