# Author: Brian Minsk

def main():
    """ Call the other functions which do the actual work per
    https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/string_formatting.html
    """
    assert task1(( 2, 123.4567, 10000, 12345.67)) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    
    assert task2(( 2, 123.4567, 10000, 12345.67)) == 'file_002 :   123.46, 1.00e+04, 1.23e+04'

    # Task 3
    assert formatter((1,23,4)) == "the 3 numbers are: 1, 23, 4"
    assert formatter((5, 5, 3, 3, 1)) == "the 5 numbers are: 5, 5, 3, 3, 1"

    assert task4((4, 30, 2017, 2, 27)) == '02 27 2017 04 30'

    assert task5a(['oranges', 1.3, 'lemons', 1.1]) == "The weight of an orange is 1.3 and the weight of a lemon is 1.1"
    assert task5b(['oranges', 1.3, 'lemons', 1.1]) == "The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32"

    task6a((["Dee Zaster", 22, "$319.50"], ["Owen Money", 38, "$1456.00"], ["Shanda Lear", 53, "$999.98"], ["Artie Choke", 103, "$1.95"]))
    task6b((2, 3, 4, 5, 6, 7, 8, 9, 10, 11))

def task1(a_tuple):
    """ For the input ( 2, 123.4567, 10000, 12345.67) return 'file_002 :   123.46, 1.00e+04, 1.23e+04'

    Keyword arguments:
    a_tuple -- a four element tuple
    """
    return "{} :   {:.2f}, {:.2e}, {:.2e}".format(create_file_name(a_tuple[0]), a_tuple[1], a_tuple[2], a_tuple[3])

def task2(a_tuple):
    """ For the input ( 2, 123.4567, 10000, 12345.67) return 'file_002 :   123.46, 1.00e+04, 1.23e+04'

    Keyword arguments:
    a_tuple -- a four element tuple
    """
    float_rounded = "{:.2f}".format(a_tuple[1])
    int_sci_notation = "{:.2e}".format(a_tuple[2])
    float_sci_notation = "{:.2e}".format(a_tuple[3])

    return f"{create_file_name(a_tuple[0])} :   {float_rounded}, {int_sci_notation}, {float_sci_notation}"

def formatter(a_tuple):
    """ Return the string "the 3 numbers are: 1, 2, 3" for the tuple (1, 2, 3)
    but with an arbitrary number of integers in a tuple.

    Keyword arguments:
    a_tuple -- a tuple of arbitrary size, each element is an integer
    """
    a_string =  "the {:d} numbers are:".format(len(a_tuple))

    temp_string = ""
    
    for i in range(0, len(a_tuple)):
        temp_string += " {:d},"

    temp_string = temp_string[:-1] #remove the extra comma

    form_string = temp_string.format(*a_tuple)

    return f"{a_string}{form_string}"

def task4(a_tuple):
    """ Given a 5 element tuple:
    ( 4, 30, 2017, 2, 27)
    use string formating to print:
    '02 27 2017 04 30'

    Keyword arguments:
    a_tuple: a tuple of 5 integers
    """
    return "{:0>2d} {:d} {:d} {:0>2d} {:d}".format(a_tuple[3], a_tuple[4], a_tuple[2], a_tuple[0], a_tuple[1])

def task5a(a_list):
    """ Given the following four element list:
    ['oranges', 1.3, 'lemons', 1.1]
    return "The weight of an orange is 1.3 and the weight of a lemon is 1.1"

    Keyword arguments:
    a_list -- a list of the form above
    """
    return f"The weight of an {a_list[0][:-1]} is {a_list[1]} and the weight of a {a_list[2][:-1]} is {a_list[3]}"

def task5b(a_list):
    """ Given the following four element list:
    ['oranges', 1.3, 'lemons', 1.1]
    return "The weight of an ORANGE is 1.56 and the weight of a LEMON is 1.32"
    where the weights are 1.2 times the value in the list.

    Keyword arguments:
    a_list -- a list of the form above
    """
    return f"The weight of an {a_list[0].upper()[:-1]} is {1.2 * a_list[1]} and the weight of a {a_list[2].upper()[:-1]} is {1.2 * a_list[3]}"

def create_file_name(file_number):
    if file_number < 10:
        return "file_{:0>3d}".format(file_number)
    elif file_number < 100:
        return "file_0{:0>2d}".format(file_number)
    else:
        return "file_{:d}".format(file_number)

def task6a(a_tuple):
    """ Print a table of several rows, each with a name, an age and a cost. 

    Keyword arguments:
    a_tuple -- a tuple of lists with each list containing a name, age, and cost
    """
    for i,j,k in a_tuple:
        print("{:20}{:>5d}{:>10}".format(i,j,k))

def task6b(a_tuple):
    """ Given a tuple with 10 consecutive numbers quickly print the tuple in columns that are 5 charaters wide
    using one line of code

    Keyword arguments:
    a_tuple -- a tuple of 10 consecutive numbers
    """
    for number in a_tuple: print("{:>5d}".format(number), end = "")

if __name__ == "__main__":
    main()