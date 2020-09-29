 # Printing a Grid
# function to print the top line of the box
def full_line_func():
    num_full_line = [ print('+ - - - - + - - - - +') for num_full_line in range(1)]
    return
# function to print the second line of the box
def pipe_space_func():
    num_pipe = [ print('|         |         |', end=' ') for num_pipe in range(1)]
    print()
    return
# function to call the functions to create the box
size = 4
def box_func():
    full_line_func()
    for i in range(4):
        pipe_space_func()
    full_line_func()
    for i in range(4):
        pipe_space_func()
    full_line_func()
    return
# calling the function
box_func()
print()

# part 2
# Printing a Grid with size options
# function to print the top line of the box
print('Part 2')
def plusfunc():
    plussymbol = [print('+', end=' ') for plussymbol in range(1)]
    return
# function to print the second line of the box
def tabfunc():
    tabsymbol = [print('-', end=' ') for tabsymbol in range(1)]
    return
def pipefunc():
    pipesymbol = [print('|', end=' ') for pipesymbol in range(1)]
    return
def spacefunc():
    spacesymbol = [print(' ' * ((size * 2)-1) , end=' ') for spacesymbol in range(1)]
    return
# function to call the functions to create the box
def box_size_func(size):
    # function to print the second line of the box
    def pipe_space_func():
        num_pipe = [ print('|', end=' ') for num_pipe in range(1)]
        num_space = [print(' ' * ((size * 2)-1) , end=' ') for num_space in range(1)]
        num_pipe = [ print('|', end=' ') for num_pipe in range(1)]
        num_space = [print(' ' * ((size * 2)-1), end=' ') for num_space in range(1)]
        num_pipe = [ print('|', end=' ') for num_pipe in range(1)]
        print()
        return
    plusfunc() # insert plus symbol
    for i in range(size): # insert dash symbol
        tabfunc()
    plusfunc() # insert plus symbol
    for i in range(size): # insert dash symbol
        tabfunc()
    plusfunc() # insert plus symbol
    print()
    for i in range(size): # instert pipe symbol
        pipe_space_func()
    plusfunc() # insert plus symbol
    for i in range(size): # insert dash symbol
        tabfunc()
    plusfunc() # insert plus symbol
    for i in range(size): # insert dash symbol
        tabfunc()
    plusfunc() # insert plus symbol
    print()
    for i in range(size): # instert pipe symbol
        pipe_space_func()
    plusfunc() # insert plus symbol
    for i in range(size): # insert dash symbol
        tabfunc()
    plusfunc() # insert plus symbol
    for i in range(size): # insert dash symbol
        tabfunc()
    plusfunc() # insert plus symbol
    print()
    return
# calling the function
box_size_func(7)

# part 3
# Printing a Grid with units options
# function to print the top line of the box
print('Part 3')
# function to call the functions to create the box
# I need some help with trying to use to following function in the while loop to produce the
# grid.
# I'm receiving this error: TypeError: can't multiply sequence by non-int of type 'str'
# I understand what the function is saying, I need to know how to work around this error.

def plusfunc(units,size):
    #plussymbol = [print('+', ((* units * 2)), end=' ') for plussymbol in range(1)]
    #plussymbol = '+ ' + ('- ' * units)
    #print(plussymbol)
    plus = '+ ' + ('- ' * units)
    pipe = '| ' + (' '* (2 * size))
    print(plus * pipe + '+')
    return plus

# function to print the second line of the box
def pipefunc(size):
    #dashsymbol = [print('-', end=' ') for dashsymbol in range(units)]
    #vertical = '| ' + (' '* (2 * size))
    #print(vertical)
    pipe = '| ' + (' '* (2 * size))
    return pipe

def gridprinter3(units, size):
    plusfunc(units)
    pipefunc(size)
    #horizontal = '+ ' + ('- ' * size)
    #vertical = '| ' + (' '*(2*size))
    #print(plusfunc(5) * dashfunc(2) + '+')
    #print(plusfunc(5))# * dashfunc(2)) #+ '+') #for plussymbol in range(units * size))
    print(plusfunc(units) * pipefunc(size) + '+')
    #print(horizontal*square + '+')
    initial = 1
    while initial <= units:
        j = 0
        while j < size:
            print(plusfunc(units) + '|')
            j += 1
        print(pipefunc(size) + '+')
        initial += 1

#gridprinter3(2,2)
#boxrowfunc(8,2)
plusfunc(8,2)
