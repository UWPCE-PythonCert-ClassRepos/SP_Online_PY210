#!/usr/bin/env python3

def task_one(): 
    """
        uses format() function to display formatted string
    """
    a_tuple = (2, 123.4567, 10000, 12345.67 ) 
    print( "file_{0:03d} : {1:.2f}, {2:.2e}, {3:.2e}".format(*a_tuple) ) 

def task_two(): 
    """
        uses f-strings to display formatted string
    """
    a_tuple = (2, 123.4567, 10000, 12345.67 ) 
    print( f"file_{a_tuple[0]:03d} : {a_tuple[1]:.2f}, {a_tuple[2]:.2e}, {a_tuple[3]:.2e}" )

def task_three(): 
    """
        demonstrates re-write of: "the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)" 
        to take an arbitrary number of values
    """
    a_tuple = (1, 2, 3)
    print("the 3 numbers are: {:d}, {:d}, {:d}".format(*a_tuple))

def task_four(): 
    a_tuple = (4, 30, 2017, 2, 27)
    print(f"{a_tuple[-2]} {a_tuple[-1]} {a_tuple[-3]} {a_tuple[0]:02} {a_tuple[1]}")

def task_five(): 
    """
        demonstrates the uses of f-strings and run time computation
    """
    a_list = ['oranges', 1.3, 'lemons', 1.1]
    print(f"the weight of an {a_list[0].upper():.6} is {a_list[1]} and the weight of a {a_list[2].upper():.5} is {a_list[3]}")

def task_six(): 
    """
        demonstrates the use of format specifiers
        
        Function uses a list of list of salaries, calculating the size 
        of each element, and using the size as a specification 
        for the output format width.
    """
    salaries = [
            ['john smith', 40, 10000], 
            ['erick smith', 30,  500], 
            ['ed barrow', 20, 100000]
        ]
    
    # track the largest of each element
    # size is used as a format specifier
    longest_name = 0 
    biggest_age  = 0 
    biggest_salary = 0

    for salary in salaries: 
        if  len(salary[0]) > longest_name: 
            longest_name = len(salary[0])
        if  len(str(salary[1])) >  biggest_age: 
            biggest_age = len(str(salary[1]))
        if  len(str(salary[2])) > biggest_salary: 
            biggest_salary = len(str(salary[2]))

    for salary in salaries: 
        print(f"{salary[0]:{longest_name}} {salary[1]:{biggest_age}} {salary[2]:{biggest_salary}}")


if __name__ == '__main__': 
    print("[+] task_one() output")
    task_one()
    print() 
    print("[+] task_two() output")
    task_two()
    print() 
    print("[+] task_three output")
    task_three()
    print() 
    print("[+] task_four output")
    task_four()
    print() 
    print("[+] task_five output")
    task_five()
    print() 
    print("[+] task_six output")
    task_six()

