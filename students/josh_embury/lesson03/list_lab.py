#--------------------------------------------------------------#
# Title: Lesson 3, List Lab
# Description: Handling a list of fruits
# ChangeLog (Who,When,What):
# JEmbury, 9/19/2020, created new script
#--------------------------------------------------------------#
lst_fruits_original = ['Apples','Pears','Oranges','Peaches']
# Series 1:
series1_lst_fruits = list(lst_fruits_original)
print(series1_lst_fruits)
new_fruit = input('Please enter another fruit >>>')
series1_lst_fruits.append(new_fruit)
print(series1_lst_fruits)
num = int(input('Please input a number {} through {} >>>'.format(1,len(series1_lst_fruits))))
print('The fruit corresponding to {} is {}'.format(num,series1_lst_fruits[num-1]))
series1_lst_fruits  = ['Tomato'] + series1_lst_fruits
print(series1_lst_fruits)
series1_lst_fruits.insert(0,'Mango')
print(series1_lst_fruits)
print('Here are all of the fruits starting with \'P\':')
for i in series1_lst_fruits:
    if i[0].lower() =='p':
        print(i)

# Series 2:
series2_lst_fruits = list(series1_lst_fruits)
print(series2_lst_fruits)
series2_lst_fruits.pop()
print(series2_lst_fruits)
series2_lst_fruits = series2_lst_fruits*2

i = 0
while i < 1:
    item_remove = input('Input an item to remove!! >>> ')
    if item_remove in series1_lst_fruits:
        while item_remove in series2_lst_fruits:
            series2_lst_fruits.remove(item_remove)
        i+=1
    else: print('Item not found in list!!')
print(series2_lst_fruits)

# Series 3:

series3_lst_fruits = list(series1_lst_fruits)
i=0
while i < len(series3_lst_fruits):
    answer = input('Do you like {} ? (yes/no) >>>'.format(series3_lst_fruits[i]))
    if answer=='no':
        removal = series3_lst_fruits[i]
        while removal in series3_lst_fruits:
            series3_lst_fruits.remove(series3_lst_fruits[i])
    elif answer=='yes':
        i+=1
    else:
        print('Please enter yes or no!!!')
print(series3_lst_fruits)

# Series 4:
series4_lst_fruits = list(series1_lst_fruits)
for i in range(0,len(series4_lst_fruits)):
    series4_lst_fruits[i] = series4_lst_fruits[i][::-1]
series4_lst_fruits.pop()
print('Original list:')
print(series1_lst_fruits)
print('Series 4 list:')
print(series4_lst_fruits)