#--------------------------
#Title: Specified size grid
#Description: Print grids according to user's specifications
#Original Dev: Lee Deitesfeld
#Change Log:
#20190331LAD Created function
#--------------------------

def print_grid2(x, y):
    '''Prints grid according to user's size specifications (LxW).'''
    pipe = '|'
    spaces = ' '*y
    plus = '+'
    hyphens = '-'*y

    mult_hyphens = (plus + hyphens)*x
    mult_spaces = (pipe + spaces)*x

    #prints one line with hyphens and plus signs
    print(mult_hyphens + plus)

    #prints rest of grid
    for i in range(x):
        #prints multiple lines with pipes and spaces
        for i in range(y):
            print(mult_spaces + pipe)

        print(mult_hyphens + plus)
