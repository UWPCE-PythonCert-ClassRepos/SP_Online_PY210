#!/usr/bin/env python

'''
String Formatting Exercise

Goal:
In this exercise we will reinforce the important 
concepts of string formatting, so that these 
start to become second nature!
'''

# task 1: format string
a_tuple = (22, 123.4567, 10000, 12345.67)

def file_number():
    # Format index 0 file number
    if a_tuple[0] < 10:
        
        print ("file_00" + str(a_tuple[0]))
    else:
        print ("file_0" + str(a_tuple[0]))

def round_num():
    # format index 1, round to 2 decimal places
    print('{0:.2f}'.format(a_tuple[1]))

def sci_not():
    # Format index 2, scientific notation
    return("{:.2E}".format(Decimal(a_tuple[2])))

if __name__ == "__main__":
