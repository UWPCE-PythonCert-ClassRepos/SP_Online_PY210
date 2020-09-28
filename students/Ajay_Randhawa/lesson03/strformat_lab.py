def format_string(a,b,c,d):
    #Function for Task1
    #pad the integer with zero for a total of 3 numbers
    #convert the integer into a string to form the output
    A = str(a).zfill(3)
    A = "file_" + A
    print(A)
    #format the float to use only 2 decimal places.
    B = float("{:.2f}".format(b))
    print(B)
    #format the integer to use 2 decimal places with scientific notation
    C = "{:.2e}".format(c)
    print(C)
    #format the integer to use 2 decimal places with scientific notation
    D = "{:.2e}".format(d)
    print(D)

def task_2(a,b,c,d):
    #Task2
    #use f-string to pad integer with 0s
    A = f'{a:03d}'
    print("file_" +A)
    #use f-string to format float to 2 decimal places
    B = f'{b:.2f}'
    print(B)
    #use f-string to change int to scientific notation with 2 decimal places
    C = f'{c:.2e}'
    print(C)
    #use f-string to change int to scientific notation with 2 decimal places
    d = f'{d:.2e}'
    print(d)

def formatter(in_tuple):
    #Task3
    #store the length of the tuple
    a = len(in_tuple)
    #add the lenth of the tuple to the string
    format_string = f'the {a} numbers are:'
    #add place holders for the tuple values
    while a>0:
        if a>1:
            format_string = format_string + " {},"
        else:
            format_string = format_string + " {}"
        a = a-1
    #return string with tuple values
    return format_string.format(*in_tuple)

def task_4(in_tuple):
    #Task4
    #convert tuple to a list to modify it
    list1 = list(in_tuple)
    #modify the 2 values to add zero paddding
    list1[0] = f'{in_tuple[0]:02d}'
    list1[3] = f'{in_tuple[3]:02d}'
    #rearrange the values per the assignemnt in a string
    string1 = "{} {} {} {} {}".format(list1[3], list1[4], list1[2], list1[0], list1[1])
    #print the string
    print(string1)
def task_5():
    #Task 5
    #Create a list
    list1 = ['oranges', 1.3, 'lemons', 1.1]
    #Format string and make the fruits singular
    string1 = f'The weight of an {list1[0][:-1]} is {list1[1]} and the weight of a {list1[2][:-1]} is {list1[3]}'
    print(string1)
    #Format string to captitalize fruits and increase weight by 20%
    string2 = f'The weight of an {list1[0][:-1].upper()} is {list1[1]*1.2} and the weight of a {list1[2][:-1].upper()} is {list1[3]*1.2}'
    print(string2)

def task_6():
    list1 = ['first', '85', '90000.25','second', '55', '8000.75','third', '25', '500.98']
    list1_1 = list1[:3]
    list1_2 = list1[3:6]
    list1_3 = list1[6:]
    print(list1_1)
    string1 = '{:20}{:10}{:>8}'.format(list1_1[0], list1_1[1], list1_1[2])
    print(string1)
    string2= '{:20}{:10}{:>8}'.format(list1_2[0], list1_2[1], list1_2[2])
    print(string2)
    string3 = '{:20}{:10}{:>8}'.format(list1_3[0], list1_3[1], list1_3[2])
    print(string3)

def extra_task():
    #extra Task
    #Create a tuple of 10 consecutive integers
    tup = (1,2,3,4,5,6,7,8,9,10)
    #Format string to create a table of 5 characters wide
    string1 ="{:5}{:5}{:5}{:5}{:5}\n{:5}{:5}{:5}{:5}{:5}".format(tup[0],tup[1],tup[2],tup[3],tup[4],tup[5],tup[6],tup[7],tup[8],tup[9])
    print(string1)