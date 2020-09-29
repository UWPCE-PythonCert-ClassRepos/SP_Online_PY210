
def line_style_1():

    """This function return line style for the
     first, middle and last section of the 4 blocks grid """

    return("+ - - - - + - - - - +")

def line_style_2():

    """This function returns line style /"|         |         |/" """

    return("|         |         |")

def print_two_blocks():

    "This function print two blocks without the last line of the block"

    print (line_style_1())
    for i in range(0,4):
        print(line_style_2())


def print_error():
    print('Number of rows can not be zero')


def print_result(n):

    """This function prints the final result
    it will take n as number of rows and will
    print rows of 2 block grid"""
    if n == 0:
        return print_error()
    for i in range(0, n):
        print_two_blocks()
    print(line_style_1())

print_result(2)


