#!/usr/bin/env python

'''
String Formatting Exercise

Goal:
In this exercise we will reinforce the important 
concepts of string formatting, so that these 
start to become second nature!
'''

# Task 1: format string
a_tuple = (2, 123.4567, 10000, 12345.67)

def file_number():
    # Format index 0 file number
    if a_tuple[0] < 10:
        return ("file_00" + str(a_tuple[0]))
    else:
        return ("file_0" + str(a_tuple[0]))

def round_num():
    # Format index 1, round to 2 decimal places
    return(format(a_tuple[1], '.2f'))    
    
def sci_not():
    # Format index 2, scientific notation
    return(format((a_tuple[2]), '.2e'))

def sci_not_three():
    # Format index 3, scientific notation with 3 significant numbers
    return(format((a_tuple[3]), '.2e'))
    
if __name__ == "__main__" :
    
    # Print task one with formatted numbers.
    print ('{} :   {}, {}, {}'.format(file_number(),round_num(),sci_not(),sci_not_three()))
    
    # Task two, 
    a = "file_00" + str(a_tuple[0])
    b = "{:.2f}".format(a_tuple[1])
    c = "{:.2e}".format(a_tuple[2])
    d = "{:.2e}".format(a_tuple[3])

    print('{} :   {}, {}, {}'.format(a,b,c,d))
    
    # Task 3, re written format string
    form_string = "The three numbers are: {:d}, {:d}, {:d}"
    numb = (1,2,3)
    
    print(form_string.format(*numb))
    
    # Task 4, use string formatiing to display given numbers
    another_tuple = (4, 30, 2017, 2, 27)
    e = format((another_tuple[0]), '0>2d')
    f = another_tuple[1]
    g = another_tuple[2]
    h = format((another_tuple[3]), '0>2d')
    i = another_tuple[4]
    
    print('{} {} {} {} {}'.format(h,i,f,e,g))

    # Task 5, use f-strings
    
    four_elements = ['oranges', 1.3, 'lemons', 1.1]
    j = four_elements[0]
    k = four_elements[1]
    l = four_elements[2]
    m = four_elements[3]
    
    print(f"The weight of an {j} is {k} and the weight of a {l} is {m}")
    
    # Task 6, rite some Python code to print a table of several rows, each with a name, an age and a cost.
    data_one = list()
    data_one.append(["Name 1", 23.0, "$444.00"])
    data_one.append(["Name 2", 1.6, "$44.00"])
    data_one.append(["Name 3", 24, "$444,000.00"])

    print(f"\n\n{'Name':<10}{'Age':<8} {'Cost':<12}")
    print("-" * 9 + " " + "-" * 8 + " " + "-"*11)

    for i in data_one:
        print(f"{i[0]:<10}{i[1]:>8}{i[2]:>12}")

    print(f"\n\n{'5char':<5}{' 5char':<5}")
    print("-" * 5 + " " + "-" * 5)

    # Print the tuple in columns that are 5 charaters wide? It can be done on one short line!
    ten_numb = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print(''.join(map(str, ten_numb[0:5])) + " " + ''.join(map(str, ten_numb[-5:])))
    
    
    