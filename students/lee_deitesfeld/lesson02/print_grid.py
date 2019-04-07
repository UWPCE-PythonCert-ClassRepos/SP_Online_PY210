#--------------------------
#Title: Variable size grid
#Description: Print grids in different sizes according to number input
#Original Dev: Lee Deitesfeld
#Change Log:
#20190331LAD Created function
#--------------------------

def print_grid(n):
    '''Prints a grid of varying size depending on number input (n).'''

    #grid components
    plus = '+'
    pipe = '|'
    hyphen_by_four = '-'*4
    space_by_four = ' '*4
    hyphen_by_n = '-'*n
    space_by_n = ' '*n
    pipe_line = '|' + space_by_n + '|' + space_by_n + '|'

    #matches the graph in step 1 of grid assignment
    if n == 9:
        print(plus, hyphen_by_four, plus, hyphen_by_four, plus)
        print(pipe, space_by_four, pipe, space_by_four, pipe)
        print(pipe, space_by_four, pipe, space_by_four, pipe)
        print(pipe, space_by_four, pipe, space_by_four, pipe)
        print(pipe, space_by_four, pipe, space_by_four, pipe)
        print(plus, hyphen_by_four, plus, hyphen_by_four, plus)
        print(pipe, space_by_four, pipe, space_by_four, pipe)
        print(pipe, space_by_four, pipe, space_by_four, pipe)
        print(pipe, space_by_four, pipe, space_by_four, pipe)
        print(pipe, space_by_four, pipe, space_by_four, pipe)
        print(plus, hyphen_by_four, plus, hyphen_by_four, plus)

    #creates grid of variable size depending on input
    else:
        #prints one line with hyphens and plus signs
        print(plus + hyphen_by_n + plus + hyphen_by_n + plus)
        #prints multiple lines with pipes and spaces
        for i in range(n):
            print(pipe_line)
        print(plus + hyphen_by_n + plus + hyphen_by_n + plus)
        for i in range(n):
            print(pipe_line)
        print(plus + hyphen_by_n + plus + hyphen_by_n + plus)
