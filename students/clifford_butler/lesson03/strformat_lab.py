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


if __name__ == "__main__":
    print(sci_not_three())