#!/usr/bin/env python3
#https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/string_formatting.html
#https://startlearning.uw.edu/courses/course-v1:UW+PYTHON210+2019_Winter/courseware/ff548d5d7b4c460fa2a9cca69f3c0332/28904f1864f84c62bc2a3443f5ae5da6/

def task0(input):
  theList = list(input)

  fileName = "file_" + str(input[0]). zfill(3)
  field1 = str(round(input[1],2))
  field2 = "{:.2e}".format(input[2])
  field3 = "{:.2e}".format(input[3])

  output0 = fileName + " :  " + field1 + ", " + field2  + ", " + field3  
  return output0

def task1(input):
  theList = list(input)

  fileName = str(input[0]). zfill(3)
  field1 = str(round(input[1],2))
  field2 = "{:.2e}".format(input[2])
  field3 = "{:.2e}".format(input[3])

  txt = "file_{0}  :  {1}, {2}, {3}"
  formattedString = txt.format(fileName,field1,field2,field3)
  return formattedString

def task1b(input):
  theList = list(input)

  txt = "file_{fn}  :  {f1}, {f2}, {f3}"
  formattedString = txt.format(fn=str(input[0]). zfill(3),f1=str(round(input[1],2)),f2="{:.2e}".format(input[2]),f3="{:.2e}".format(input[3]))
  return formattedString

def task2(input):
  print("task2")
  theList = list(input)

  fileName = str(input[0]). zfill(3)
  field1 = str(round(input[1],2))
  field2 = "{:.2e}".format(input[2])
  field3 = "{:.2e}".format(input[3])

  return f"file_{fileName}  :  {field1}, {field2}, {field3}"

def formatter_task3(*in_tuple):
  
  form_string = "the {:d} numbers are: ".format(len(in_tuple))+ "{:d}, "  * (len(in_tuple)-1) +  "{:d}"
  formattedStr=((form_string).format(*in_tuple))
  
  return formattedStr

def task4(input):
  print("task4: ", input)
  
  return "{:02d} {:d} {:d} {:02d} {:d}".format(input[3],input[4],input[2],input[0],input[1])

def task5a(input):
  fruit1 = input[0] 
  fruit2 = input[2] 
  return f'The weight of an {fruit1[:-1]} is {input[1]} and the weight of a {fruit2[:-1]} is {input[3]}'

def task5b(input):
  fruit1 = input[0] 
  fruit2 = input[2] 
  return f'The weight of an {(fruit1[:-1]).upper()} is {(input[1]*1.2)} and the weight of a {(fruit2[:-1].upper())} is {(input[3]*1.2)}'

def task6a(input):
    return '{:20}{:10}{:20}{:8}'.format('First', '$99.01', 'Second', '$88.09')

def task6b(input):
  name = input[0]
  age = input[1]
  cost = input[2]
  return '{:15}{:5}{:8}'.format(name, age, cost)

def task6c(input):
  field1 = input[0]
  field2 = input[1]
  field3 = input[2]
  return field1

#print(task6b(['bob jones', 15, 1.1]))
print(task6c([('bob jones', 15, 1.1), 'bob jones', 15, 1.1, 'anthony peterson', 33, 1004003, 'jane jphnson', 45, 10425.5]))



def task6xxx(input):
#    return '{:<30}'.format('left aligned')
#    return '{:>30}'.format('right aligned')
#    return '{:^30}'.format('centered')
#    return '{:*^30}'.format('centered')
#    return '{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
     return '{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
#    return '{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
#    return '{:,}'.format(1234567890) #  Using the comma as a thousands separator
#    return 'Correct answers: {:.2%}'.format(points/total) # Expressing a percentage
#    return xx
#    return xx

    
 #'02 27 2017 04 30'
#input = ( 2, 123.4567, 10000, 12345.67)
#output1 = task1(input)
#print((output1))

#output1b = task1b(input)
#print((output1b))

#output2 = task2(input)
#print((output2))

#print(formatter_task3(2,3,5))
#print(formatter_task3(2,3,5,7,9))

#task4_input = ( 4, 30, 2017, 2, 27)
#print(task4(task4_input))
#print(task4((4, 30, 2017, 2, 27)))

#print(task5a(['oranges', 1.3, 'lemons', 1.1]))
#print(task5b(['oranges', 1.3, 'lemons', 1.1]))

#print(task6a(['oranges', 1.3, 'lemons', 1.1]))
