# -*- coding: utf-8 -*-

"""
This code contains the answers to 6 different string-related tasks. 
"""

"""
Lesson03 :: String Lab
Exercise 3.3
@author: Chuck Stevens :: CCSt130
Created on Sat Jun  1 18:53:03 2019
"""

""" Menu """

import random

if __name__ == "__main__":

    def main():
        """ Main contains the Menu and if/elif/else block. """
        # List below used for Tasks 1, 2, 3
        my_list = (2, 123.4567, 10000, 12345.67)
        
        usr_input = ""
        
        #while (usr_input != 'Q'):
        while True:
            # Displaying menu header
            print()
            print(48 * '*')
            print()
            print(17 * '*', "Menu Options", 17 * '*')
            print()

            # Display menu options
            print(" 1. Task 1: Demo .format syntax")
            print(" 2. Task 2: Demo f string syntax")
            print(" 3. Task 2: Use formatted string as a name")
            
            print(" 4. Task 3: Print a dynamic list")
            print(" 5. Task 3: Print a dynamic list using PRNG")
            print(" 6. Task 4: Print a reordered Tuple")
            
            print(" 7. Task 5: Demo f string syntax with math")
            print(" 8. Task 6: Print a Table with aligned columns")
            print()
            print(" Enter 'Q' to Quit")        
            
            print()
            print(48 * '*')
            # Prompt user for input
            input_msg = "Please choose a Menu Option [1-8]: "
            # Capture user choice 
            usr_input = str(input(input_msg))
                
            if usr_input == '1':
                dot_format_tsk_1(my_list)
            
            elif usr_input == '2':
                f_string_tsk_2(my_list)
            
            elif usr_input == '3':
                my_formatter(my_list)

            elif usr_input == '4':
                prn_dynamic_list()
            
            elif usr_input == '5':
                prn_dynamic_list_prng()
            
            elif usr_input == '6':
                prn_reordered_tuple()
            
            elif usr_input == '7':
                math_prn_f_string()

            elif usr_input == '8':
                prn_align_columns()

            elif usr_input == 'Q':
                break
            # Error handling
            elif usr_input == 'q':
                break            

            else: 
                print()
                print("Invalid entry--try again!")
                print()

        print()
        print("### Program Exit ###")

""" Task 1 """

def dot_format_tsk_1(a_list):
    """ Prints a string using the '.format' syntax. """

    print()
    print("Here's the list to interpolate: ")
    print(a_list)

    print()
    print("Here's the list printed using the '.format' syntax:")

    # print("file_{:03} : {:06.2f}, {:.2e}, {:.2e}".format(*a_list))
    # Was the objective for the above to actually rename the value (file) in the list?
    
    # Assign new format to another tuple
    # Colon becomes an element in tuple, not sure if we want that.
    reformat_e = ("file_{:03} : {:06.2f}, {:.2e}, {:.2e}".format(*a_list))
    # Print new tuple
    print(reformat_e)

""" Task 2 """

def f_string_tsk_2(a_list):
    """ Prints a string using the 'f string' syntax. """
    print()
    print("Here's the list printed using the 'f string' syntax:")
    print(f'file_{a_list[0]:03} : {a_list[1]:06.2f}, {a_list[2]:.2e}, {a_list[3]:.2e}')

def my_formatter(a_list):
    """ Function demonstrates formatted str as a name """
    
    my_formatted_str = "file_{:03} : {:06.2f}, {:.2e}, {:.2e}"
    
    print()
    print("Now using '.format' syntax in a function:")
    # print(my_formatted_str.format(*a_list))
    
    # Assign new format to another tuple        
    reformat_e = (my_formatted_str.format(*a_list))
    # Print reformatted tuple
    print(reformat_e)    

""" Task 3 """

def prn_dynamic_list():
    """ Prints a list of dynamic length. """
    
    dynamic_list = (22, 14, 3, 7, 11, 19, 15, 101)

    # Find length of list
    list_len = len(dynamic_list)

    print()
    print("Dynamic list: ")

    print(("This list contains {} elements: " + ", ".join(["{}"] * list_len)).format(list_len, *dynamic_list))
    # print(", ".join(["{}"] * list_len).format(*dynamic_list))

""" Task 3.5 """

# Uses PRNG for really dynamic list
def prn_dynamic_list_prng():
    """ Uses PRNG for list length and list contents. """
    
    dyn_list_len = random.randint(12, 24)
    
    dyn_prng_list = []
    
    dyn_counter = 0
    
    while(dyn_list_len >= dyn_counter):
        
        dyn_prng_item = random.randint(1, 240)
        
        dyn_prng_list.append(dyn_prng_item)
        
        dyn_counter+=1
    
    print()   
    print("Dynamic List using PRNG:")
    # print(dyn_prng_list)
    print(("This list contains {} elements: " + ", ".join(["{}"] * dyn_list_len)).format(dyn_list_len, *dyn_prng_list))

""" Task 4 """

def prn_reordered_tuple():
    """ Prints a tuple in a different order. """

    """
    Given a 5 element tuple: (4, 30, 2017, 2, 27)
    Use string formating to print: '02 27 2017 04 30'
    """
    my_tuple = [4, 30, 2017, 2, 27]

    print()
    print("Print 5 element tuple in a different order: ")
    print(f'{my_tuple[3]:02}, {my_tuple[4]}, {my_tuple[2]}, {my_tuple[0]:02}, {my_tuple[1]}')

""" Task 5 """

def math_prn_f_string():
    """ Prints a tuple in a formatted string with calculations. """
    
    """
    Here’s a task for you: Given the following four element list:
        ['oranges', 1.3, 'lemons', 1.1]
    Write an f-string that will display:
        The weight of an orange is 1.3 and the weight of a lemon is 1.1
    """
    fruit_list = ['orange', 1.3, 'lemon', 1.1]

    print()
    print("f string that displays four element tuple: ")
    print(f'"The weight of an {fruit_list[0]} is {fruit_list[1]} and the weight of a {fruit_list[2]} is {fruit_list[3]}"')

    print()
    print("String with math: ")
    print(f'"The weight of an {fruit_list[0]} is {fruit_list[1] * 1.2} and the weight of a {fruit_list[2]} is {fruit_list[3] * 1.2}"')

""" Task 6 """

"""
Write some Python code to print a table of several rows, each with a name, an \
age and a cost. Make sure some of the costs are in the hundreds and thousands \
to test your alignment specifiers. And for an extra task, given a tuple with \
10 consecutive numbers, can you work how to quickly print the tuple in columns \
that are 5 charaters wide? It can be done on one short line!
"""

def prn_align_columns():
    """ Prints a list of lists with formatted columns. """
    
    expensive_wheels = [[1962, 'Ferrari', '250 GTO', 38110000.00], [1954, 'Mercedes-Benz', 'W196', 38000000.00], \
                    [1967, 'Ferrari', '275GTS/4 N.A.R.T. Spider', 27500000.00], [1964, 'Ferrari', '275 GTB/C Speciale', 26400000.00], \
                    [1954, 'Ferrari', '375-Plus Spider Competizione', 18400000.00], [1957, 'Ferrari', '250 Testa Rossa', 16400000.00], \
                    [1964, 'Ferrari', '250 LM', 14000000.00], [1953, 'Ferrari', '340/375 MM Berlinetta Competizione', 13000000.00], \
                    [1957, 'Ferrari', '250 Testa Rossa', 12000000.00], [1936, 'Mercedes-Benz', '540K Special Roadster', 11770000.00], \
                    [2016, 'Hot Wheels', 'Camaro SS', 10.99], [2012, 'Matchbox', 'VW Beetle', 7.49], [2011, 'Chevrolet', 'Impala', 3999.99], \
                    [2012, 'Nissan', 'Titan', 12200.00], [2016, 'Acura', 'MDX', 34777.77], [2018, 'Koenigsegg', 'Regera', 1890000.00], \
                    [2019, 'McLaren', 'Senna', 958966.00]]

    # Sort based on first element
    expensive_wheels.sort()
    # Find length of list
    wheels_len = len(expensive_wheels)
    # Column labels
    header = ['Year', 'Make', 'Model', 'Auction Price', 'Age']

    print()
    print("Expensive wheels:") 
    print()
    # Print header
    print('{:<6} {:<15} {:<35} {:>13} {:>5}'.format(*header))
    print()
   
    w = 0 # While loop counter and index
    current_year = 2019 # Constant used to determine age 
    
    while(w < wheels_len):    
   
        # age = (current_year - (int(expensive_wheels[wheel][0])))
        # Above not needed when using f string syntax
        # For an array, especially a 2D array, the .format syntax seems easier to implement
        # print('{:<6} {:<15} {:<35} ${:>13,.2f} {:>4}'.format(*expensive_wheels[wheel], age))
    
        # Wrapping f string such as this can make the column alignment an impossible mess--whitespace is not ignored
        print(f'{expensive_wheels[w][0]:<6} {expensive_wheels[w][1]:<15} {expensive_wheels[w][2]:<35} \
${expensive_wheels[w][3]:>13,.2f} {(current_year - expensive_wheels[w][0]):>4}')
    
        w+=1 # Increment counter

### Program Entry Point ###
main()














    
    
    
    
    
    
    
    
    
    
    