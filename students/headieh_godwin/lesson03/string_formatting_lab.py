#!/usr/bin/env python3
#TASK 1
#Write a format string that will take the following four element tuple:
t = ( 2, 123.4567, 10000, 12345.67)
# and produce: 'file_002 :   123.46, 1.00e+04, 1.23e+04'
new = "file_%.03d :   %.2f, %.2e, %.2e" % t
match = 'file_002 :   123.46, 1.00e+04, 1.23e+04'
assert new == match

#TASK 2
#Using your results from Task One, 
#repeat the exercise, but this time using an alternate type of format string 
#(hint: think about alternative ways to use .format() (keywords anyone?), 
# and also consider f-strings if you've not used them already).
new1 = "file_{:03d} :   {:.2f}, {:.2e}, {:.2e}".format(*t)
new2 = f'file_{t[0]:03} :   {t[1]:.2f}, {t[2]:.2e}, {t[3]:.2e}'
assert new1 == match
assert new2 == match

#TASK 3
#Rewrite: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)
#to take an arbitrary number of values.
t2= (2,3,5)
t1= (2,3,5,7,9)

def formatter(in_tuple):
    l = len(in_tuple)
    return ('the {} numbers are: '+ ', '.join(['{}']*l)).format(l, *in_tuple)
    
assert formatter(t2) == 'the 3 numbers are: 2, 3, 5'

#TASK 4
#take tuple and reorder and reformat
##start with: ( 4, 30, 2017, 2, 27)
##end with '02 27 2017 04 30'
def neworder(in_tuple):
    temp =  ', '.join(['{:02d}']*5).format(*in_tuple) 
    temp = temp.split(", ")
    last = temp[-2:]
    first = temp[:2]
    temp[-2:]=first
    temp[:2]=last
    return ' '.join(temp)

t = ( 4, 30, 2017, 2, 27)
assert neworder(t) == '02 27 2017 04 30'

#TASK 5

#Here's a task for you: Given the following four element list:
li = ['oranges', 1.3, 'lemons', 1.1]
#Write an f-string that will display:
#The weight of an orange is 1.3 and the weight of a lemon is 1.1
string1 = f'The weight of an {li[0][:-1]} is {li[1]} and the weight of a {li[2][:-1]} is {li[3]}'
assert string1 == 'The weight of an orange is 1.3 and the weight of a lemon is 1.1'
#Now see if you can change the f-string so that it displays the names of the fruit 
#in upper case, and the weight 20% higher (that is 1.2 times higher).
string2 = f'The weight of an {li[0][:-1].title()} is {li[1]*1.2} and the weight of a {li[2][:-1].title()} is {li[3]*1.2}'
print(string2)

#TASK 6

#Write some Python code to print a table of several rows, 
#each with a name, an age and a cost.
#Make sure some of the costs are in the hundreds and thousands to test your alignment specifiers.
r0=["Name","Age","Cost"]
r1=["Al", 100, 1000.9]
r2=["Alex", 1, 100.8]
r3=["Alexander", 10, 100.14]
print(f"{r0[0]:<10}{r0[1]:<10}{r0[2]:>9}")
print(f"{r1[0]:<10}{r1[1]:<10}{r1[2]:9.2f}")
print(f"{r2[0]:<10}{r2[1]:<10}{r2[2]:9.2f}")
print(f"{r3[0]:<10}{r3[1]:<10}{r3[2]:9.2f}")

#given a tuple with 10 consecutive numbers,
#can you work how to quickly print the tuple in columns that are 5 charaters wide? 
#It can be done on one short line!
t = (10000,2000,3,4,50,600,7,80,9,10)
def five_wide(in_tuple):
    temp =  ('{:5}'*10).format(*in_tuple) 
    return(temp)
print(five_wide(t))
