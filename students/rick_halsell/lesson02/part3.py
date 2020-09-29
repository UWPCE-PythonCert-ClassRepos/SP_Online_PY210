# part 2
# Printing a Grid with size options
# function to print the top line of the box
print('Part 3')
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
    def pipespacefunc():
        pipesymbol = [print('|', end=' ') for pipesymbol in range(1)]
        spacesymbol = [print(' ' * ((size * 2)-1) , end=' ') for spacesymbol in range(1)]
        pipesymbol = [print('|', end=' ') for pipesymbol in range(1)]
        spacesymbol = [print(' ' * ((size * 2)-1) , end=' ') for spacesymbol in range(1)]
        pipesymbol = [print('|', end=' ') for pipesymbol in range(1)]
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
        pipespacefunc()
    plusfunc() # insert plus symbol
    for i in range(size): # insert dash symbol
        tabfunc()
    plusfunc() # insert plus symbol
    for i in range(size): # insert dash symbol
        tabfunc()
    plusfunc() # insert plus symbol
    print()
    for i in range(size): # instert pipe symbol
        pipespacefunc()
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
box_size_func(4)
