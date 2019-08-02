#!/usr/bin/env python3
##SP_Online_PY210 lesson03 list lab https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/string_formatting.html

def Task_1(numbers):
    #Pad file name number with zeros
    file_name = 'file_' + str('%03d' % numbers[0])
    #2 decimil places
    first_num = str(round(numbers[1],2))
    #Scientific notation w/ 2 decimil places
    second_num = str('{:.2e}'.format(numbers[2])) 
    #Scientific notation w/ 3 decimil places
    third_num = str('{:.3e}'.format(numbers[3])) 
    #glue all together
    return file_name + ' :   '  + first_num + ', ' + second_num + ', ' + third_num

def Task_2(numbers):
    #Task1 trimmed down to one line using F strings 
    return F"file_'{'%03d' % numbers[0]} :   {round(numbers[1])}, {'{:.2e}'.format(numbers[2])}, {'{:.3e}'.format(numbers[3])}"
    
def Task_3(t):
    #str(len(t)) changes based on length of touple.
    #(len(t) - 1) indexes start at 0 so len needs -1 to match up.
    string = 'the ' + str(len(t)) + ' numbers are: {:d}' + ', {:d}'  * (len(t) - 1)
    #*t inserts all variables into format.
    return string.format(*t)

#t = ( 4, 30, 2017, 2, 27)
#return '02 27 2017 04 30'
def Task_4(t):
    #{index number:{fill value}{width of fill}}
    string = "{3:{fill}{width}}, {4:{fill}{width}}, {2:{fill}{width}}, {0:{fill}{width}}, {1:{fill}{width}}"
    return string.format(*t, fill = '0', width = 2)


#lst = ['oranges', 1.3, 'lemons', 1.1]
def Task_5(lst):
    #use upper to change to uppercase and mulitply the numeric values by 1.2 to raise 20%
    return F"The weight of an {lst[0].upper()} is {lst[1] * 1.2} and the weight of a {lst[2].upper()} is {lst[3] * 1.2}"


#tuple with 10 consecutinve numbers.  print the tuple in columns that are 5 char wide.
t = (1, 5 ,10, 50, 100, 500, 1000, 5000, 10000, 50000)
def Task_6(t):
    #build the string :{fill value}{width of fill}}, length number of times
    string = '{:{fill}{width}}' * (len(t))
    return string.format(*t, fill = ' ', width = 5)

