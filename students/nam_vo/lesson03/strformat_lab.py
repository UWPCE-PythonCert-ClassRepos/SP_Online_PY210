def task_one(a_tuple):
    """Write a format string that will take the following four element tuple:
    ( 2, 123.4567, 10000, 12345.67)
    and produce:
    'file_002 :   123.46, 1.00e+04, 1.23e+04'
    """

    formattedStr = "file_{:03d} :{:9.2f},{:9.2e},{:9.2e}".format(a_tuple[0], a_tuple[1], a_tuple[2], a_tuple[3])

    return formattedStr

def task_two(a_tuple):
    """Write a format string that will take the following four element tuple:
    ( 2, 123.4567, 10000, 12345.67)
    and produce:
    'file_002 :   123.46, 1.00e+04, 1.23e+04'
    """

    formattedStr = 'file_{0:03d} :{1:{width}.{precision}f},{2:{width}.{precision}e},{3:{width}.{precision}e}'.format(*a_tuple, width=9, precision=2)

    return formattedStr

def formatter(in_tuple):
    """Return a formatted string contains all numbers in any arbitrary tuple"""
    fstring = (', '.join(['{}']*len(in_tuple))).format(*in_tuple)

    print(f'the {len(in_tuple)} numbers are: {fstring}')

def task_four(in_tuple):
    """Use string formating to print 5 element tuple ( 4, 30, 2017, 2, 27) to '02 27 2017 04 30'"""
    fstring = '{3:0{width}} {4:0{width}} {2:0{width}} {0:0{width}} {1:0{width}}'.format(*in_tuple, width=2)

    print(fstring)

def task_five():
    l = ['oranges', 1.3, 'lemons', 1.1]

    fstring = f'The weight of an {l[0][:-1]} is {l[1]} and the weight of a {l[2][:-1]} is {l[3]}'
    print(fstring)

    fstring = f'The weight of an {l[0][:-1].upper()} is {l[1] * 1.2} and the weight of a {l[2][:-1].upper()} is {l[3] * 1.2}'
    print(fstring)

def task_six(a_tuple):
    fstring = '{0:<20}{1:<10}{2:<20}'
    for row in a_tuple:
        print(fstring.format(*row))

def extra_task(a_tuple):
    """Print a tuple of 10 consecutive numbers in columns that are 5 charaters wide"""
    print(('{:<5}'*len(a_tuple)).format(*a_tuple))

if __name__ == "__main__":
    """
    fileInfo = task_one((2, 123.4567, 10000, 12345.67))
    print(fileInfo)
    
    fileInfo = task_two((2, 123.4567, 10000, 12345.67))
    print(fileInfo)
    
    formatter((2,3,5))
    formatter((2,3,5,7,9))

    task_four(( 4, 30, 2017, 2, 27))

    task_five()

    test_tuple = (
        ('Name', 'Age', 'Cost'),
        ('This is a long name', '1000', '$123.56'),
        ('Short name', '999', '$1234567890.123456789'),
    )
    task_six(test_tuple)
    """

    extra_task(tuple(range(10)))
