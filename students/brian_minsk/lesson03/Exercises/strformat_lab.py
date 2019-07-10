# Author: Brian Minsk

def main():
    """ Call the other functions which do the actual work per
    https://uwpce-pythoncert.github.io/PythonCertDevel/exercises/string_formatting.html
    """
    formatted_string = task1(( 2, 123.4567, 10000, 12345.67))
    assert formatted_string == 'file_002 :   123.46, 1.00e+04, 1.23e+04'
    
    formatted_string2 = task2(( 2, 123.4567, 10000, 12345.67))
    assert formatted_string2 == 'file_002 :   123.46, 1.00e+04, 1.23e+04'

    # Task 3
    assert formatter((1,23,4)) == "the 3 numbers are: 1, 23, 4"
    assert formatter((5, 5, 3, 3, 1)) == "the 5 numbers are: 5, 5, 3, 3, 1"


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
    a_string =  "The {:d} numbers are:".format(len(a_tuple))

    form_string = ""
    
    for i in range(0, len(a_tuple)):
        form_string += " {:d},"

    form_string = form_string[:-1] #remove the extra comma

    print(form_string)
    print(a_tuple)

    #t = (1, 23, 4)

    form_string.format(*a_tuple)

    print(form_string)

    print(f"{a_string}{form_string}")

    return f"{a_string}{form_string}"

        
def create_file_name(file_number):
    if file_number < 10:
        return "file_{:0>3d}".format(file_number)
    elif file_number < 100:
        return "file_0{:0>2d}".format(file_number)
    else:
        return "file_{:d}".format(file_number)

if __name__ == "__main__":
    main()