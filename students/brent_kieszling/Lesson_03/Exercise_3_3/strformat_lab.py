#-------------------------------------------#
#Tittle: strformat_lab, PYTHON210 - Exercise 3.3
#Desc: String Formatting Lab
#Change Log: (Who, When, What)
#Brent Kieszling, <2020-Nov-7>, created file
#-------------------------------------------#

#DATA---------------------------------------

a_tuple = ( 2, 123.4567, 10000, 12345.67)
tpl_long = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

a_list = ["oranges", 1.3, "lemons", 1.1]
person_1 = ["John", 22, 10.00]
person_2 = ["Jill H. Doe", 23, 100.00]
person_3 = ["Jammie", 24, 1000.00]

lst_group = [person_1, person_2, person_3]


#PROCESS------------------------------------
def display_1(tpl_four):
    """Format and display 4 element tuple
    
    Args:
        tpl_four (tuple): Tuple to be formatted
        
    """
    string = "file_{:03d} :   {:.2f}, {:.2e}, {:.2e}".format(*tpl_four)
    print(string)

def display_2(tpl_four):
    """Format and display 4 element tuple
    
    Args:
        tpl_four (tuple): Tuple to be formatted
        
    """
    f_name, ele_1, ele_2, ele_3 = tpl_four
    #Use 3 spaces, pad empties with 0
    f_name = "{:03d}".format(f_name)
    #Display 2 digits after the decimal rounded
    ele_1 = "{:.2f}".format(ele_1)
    #Display in scientific notation with 2 decimals
    ele_2 = "{:.2e}".format(ele_2)
    #Display in scientific notation with 2 decimals, equivalent to 3 sig figs
    ele_3 = "{:.2e}".format(ele_3)
    
    print(f"file_{f_name} :   {ele_1}, {ele_2}, {ele_3}")

def formatter(in_tuple):
    """Format and display an n element tuple
    
    Args:
        in_tuple (tuple): Tuple to be formatted
        
    Returns:
        sentence (string): Formatted response
    """
    length = len(in_tuple)
    sentence = "The " + str(length) + " numbers are: "
    for item in in_tuple[:length-1]:
        sentence += "{}, "
    sentence += "{}"
    return sentence.format(*in_tuple)

def display_4(tpl_five):
    """Rearrange and display 5 element tuple
    
    Args:
        tpl_four (tuple): Tuple to be rearranged
        
    """
    #In {3:02d} 3 is tpl_five[3], ":" seperates the element
        #call and then allows one to specify formatting "02d".
    format_string ="{3:02d} {4} {2} {0:02d} {1}".format(*tpl_five)
    print(format_string)


def display_5(list_4):
    """Format and display 4 element list
    
    Args:
        lst_four (list): List to be formatted
    """
    fruit_1, weight_1, fruit_2, weight_2 = list_4
    
    #Remove pluralization, capatalize the fruit, increase weight by 20%.
    print(f"The weight of an {fruit_1[:-1].upper()} is {weight_1 * 1.2} and the weight of a {fruit_2[:-1].upper()} is {weight_2 * 1.2}")


def display_list(lst_people):
    """Format a list of lists containing name, age, and cost
    
    Args:
        lst_people (list): List containing a lists of individuals name, age, and overhead costs
    """
    #Align place holder 'name' to the left and pad with 15 spaces.
        #Do the same with 'age' and 'cost' but with 4 and 6 spaces respectively.
    formatted_header = "{name:<15} {age:<4} \t {cost:<6}"
    formatted_row = "{name:<15} {age:<4} \t {cost:<6.2f}"

    print('======= Expense Sheet: =============')
    print(formatted_header.format( name = "Name", age = "Age", cost = "Cost"))
    for item in lst_people:
        print(formatted_row.format(name = item[0], age = item[1], cost = item[2]))
    print('====================================')
    

#PRESENTATION INPUT/OUTPUT------------------


print("Task 1:")
display_1(a_tuple)
print()

print("Task 2:")
display_2(a_tuple)
print()

print("Task 3:")
print(formatter(a_tuple))
print(formatter((1,2,3,4,5,6,7)))
print()

print("Task 4:")
display_4((4, 30, 2017, 2, 27))
print()

print("Task 5:")
display_5(a_list)
print()

print("Task 6:")
display_list(lst_group)
print()

print("Bonus:")

print(("{:5}" * len(tpl_long)).format(*tpl_long))


