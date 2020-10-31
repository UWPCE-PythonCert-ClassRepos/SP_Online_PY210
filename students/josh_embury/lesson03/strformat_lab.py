#--------------------------------------------------------------#
# Title: Lesson 3, Strings Lab
# Description: Fun with strings
# ChangeLog (Who,When,What):
# JEmbury, 10/5/2020, created new script
#--------------------------------------------------------------#

# TASK 1
tup = (2, 123.4567, 10000, 12345.67)

str1 = 'file_' + f'{tup[0]:03}' + ' :   '
str2 = '%.2f, '% tup[1]
str3 = '%.2e, ' % tup[2]
str4 = '%3.2e' % tup[3]
str_task1 = str1+str2+str3+str4
print(str_task1)

# TASK 2
str_task2 = 'file_{:03d} :   {:.2f}, {:.2e}, {:3.2e}'.format(tup[0],tup[1],tup[2],tup[3])
print(str_task2)

# TASK 3
tup3 = (1,2,3)
str_task3 =('the 3 numbers are '+ (len(tup3)-1)*'{:d}, '+'{:d}').format(*tup3)
print(str_task3)

# TASK 4
tup4 = (4,30,2017,2,27)
str_task4 = f'{tup4[3]:02} {tup4[4]:02} {tup4[2]} {tup4[0]:02} {tup4[1]:02}'
print(str_task4)

# TASK 5
list5 = ['orange', 1.3, 'lemon', 1.1]
str_task5a = f'The weight of an {list5[0]} is {list5[1]} and the weight of a {list5[2]} is {list5[3]}'
print(str_task5a)
str_task5b = f'The weight of an {list5[0].upper()} is {1.2*list5[1]} and the weight of a {list5[2].upper()} is {1.2*list5[3]}'
print(str_task5b)

# TASK 6
def fun_task6(info_list):
    return '{:^6} {:^6} {:^6}'.format(info_list[0],info_list[1],info_list[2])

lst_task6 = [['Name','Age','Cost'],['Nemo',3,'$1027'],['Flappy',5,'$96'],['Oscar',9,'$122']]
#print(fun_task6(['Nemo',3,'$1027']))
for i in lst_task6:
    print(fun_task6(i))

# Task 6b
tup6 = (1,2,3,4,5,6,7,8,9,10)
for i in tup6: print('{:^5}'.format(i))